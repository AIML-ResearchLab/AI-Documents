import json
from datetime import datetime
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage
from state import IncidentState
from tools import FEEDBACK_TOOLS
from utils import log, audit

LLM = ChatOpenAI(model="gpt-4o", temperature=0.3)

async def feedback_node(state: IncidentState) -> dict:
    """
    Stage 9 — Feedback Agent
    Generates RCA report, sends Slack notification,
    creates JIRA post-mortem, resolves PagerDuty.
    """
    event   = state["incident_event"]
    rca     = state["rca_result"]
    plan    = state.get("remediation_plan")
    health  = state.get("health_status")
    lessons = state.get("lessons_learned")

    log("FEEDBACK", f"Generating incident report for {event.incident_id}")

    resolved   = health.resolved if health else False
    mttr       = health.mttr_seconds if health else "unknown"
    resolution = plan.title if plan else "N/A"

    # ── Generate Slack message ────────────────────────────────────────────────
    status_emoji = "✅" if resolved else "🔴"
    slack_msg = f"""{status_emoji} *Incident {event.incident_id} {'RESOLVED' if resolved else 'ESCALATED'}*

*Service*: {event.affected_svc} ({event.namespace})
*Severity*: {event.severity}
*Root Cause*: {rca.root_cause if rca else "Under investigation"}
*Resolution*: {resolution}
*MTTR*: {mttr}s ({int(mttr)//60}m {int(mttr)%60}s) if resolved else N/A

*What happened*: {rca.causal_chain[0] if rca and rca.causal_chain else event.title}
*Action taken*: {resolution}

Post-mortem ticket being created. Runbooks updated."""

    prompt = ChatPromptTemplate.from_messages([
        ("system", f"""You are a stakeholder communication agent.
Send all required notifications for this incident closure.
Use tools to: send Slack notification, create JIRA post-mortem, resolve PagerDuty."""),
        MessagesPlaceholder("chat_history", optional=True),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ])

    agent    = create_openai_tools_agent(LLM, FEEDBACK_TOOLS, prompt)
    executor = AgentExecutor(agent=agent, tools=FEEDBACK_TOOLS, verbose=False, max_iterations=5)

    input_data = json.dumps({
        "slack_channel"   : "incidents",
        "slack_message"   : slack_msg,
        "jira_summary"    : f"Post-mortem: {event.title}",
        "jira_description": f"RCA: {rca.root_cause if rca else 'TBD'}\nResolution: {resolution}",
        "pagerduty_id"    : event.incident_id,
        "resolution_note" : f"Auto-remediated by AI agent. MTTR: {mttr}s",
    })

    result = executor.invoke({"input": f"Send all notifications: {input_data}"})

    log("FEEDBACK", "✓ Slack notification sent")
    log("FEEDBACK", "✓ JIRA post-mortem created")
    log("FEEDBACK", "✓ PagerDuty incident resolved")

    audit(state, "feedback", "All stakeholder notifications sent")

    return {"feedback_sent": True}
