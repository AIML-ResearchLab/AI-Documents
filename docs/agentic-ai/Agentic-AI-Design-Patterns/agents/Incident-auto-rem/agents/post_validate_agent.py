import json
from datetime import datetime
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage
from state import IncidentState, HealthStatus
from tools import POST_VALIDATE_TOOLS
from utils import log, audit

LLM = ChatOpenAI(model="gpt-4o", temperature=0)

_incident_start_time = {}  # track MTTR

async def post_validate_node(state: IncidentState) -> dict:
    """
    Stage 7 — Post-Validation Agent
    Re-polls metrics, runs health checks, compares pre/post snapshots.
    Determines: resolved / degraded / failed.
    """
    event     = state["incident_event"]
    diagnosis = state["diagnosis_report"]
    log("POST-VALIDATE", f"Running health checks for {event.affected_svc}")

    prompt = ChatPromptTemplate.from_messages([
        ("system", f"""You are a health validation agent.
Service: {event.affected_svc} | Namespace: {event.namespace}

Pre-incident metrics: {json.dumps(diagnosis.metric_snapshot)}

Run comprehensive health checks:
1. run_health_check to verify service is responding
2. fetch_pod_metrics to compare with pre-incident snapshot
3. fetch_application_logs to check for remaining errors

Determine if the incident is RESOLVED, DEGRADED, or STILL_FAILING."""),
        MessagesPlaceholder("chat_history", optional=True),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ])

    agent    = create_openai_tools_agent(LLM, POST_VALIDATE_TOOLS, prompt)
    executor = AgentExecutor(agent=agent, tools=POST_VALIDATE_TOOLS, verbose=False, max_iterations=6)
    result   = executor.invoke({"input": "Run all health checks and validate service recovery"})

    # ── Parse health status ───────────────────────────────────────────────────
    parse_prompt = f"""
From this health check output:
{result["output"]}

Extract JSON:
{{
  "resolved": bool,
  "slo_restored": bool,
  "checks_passed": ["list"],
  "checks_failed": ["list"],
  "metrics_recovered": {{"cpu": float, "memory": float, "error_rate": float}},
  "status": "resolved|degraded|failed"
}}
Respond ONLY with JSON.
"""
    parse_resp = LLM.invoke([HumanMessage(content=parse_prompt)])
    health_data = json.loads(parse_resp.content.strip().strip("```json").strip("```"))

    # Estimate MTTR
    mttr = 420  # ~7 min default simulation

    health = HealthStatus(
        resolved           = health_data["resolved"],
        metrics_recovered  = health_data.get("metrics_recovered", {}),
        checks_passed      = health_data.get("checks_passed", []),
        checks_failed      = health_data.get("checks_failed", []),
        slo_restored       = health_data.get("slo_restored", False),
        mttr_seconds       = mttr,
    )

    icon = "✅" if health.resolved else "⚠️ "
    log("POST-VALIDATE", f"{icon} Status: {health_data['status'].upper()} | SLO: {'✓' if health.slo_restored else '✗'} | MTTR: {mttr}s")
    audit(state, "post_validate", f"resolved={health.resolved}, status={health_data['status']}")

    return {"health_status": health}
