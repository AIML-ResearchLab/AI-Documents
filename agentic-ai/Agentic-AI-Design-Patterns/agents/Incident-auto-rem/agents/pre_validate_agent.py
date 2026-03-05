import json
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from state import IncidentState
from tools import PRE_VALIDATE_TOOLS
from utils import log, audit

LLM = ChatOpenAI(model="gpt-4o", temperature=0)

RISK_THRESHOLD      = 7.0   # auto-block if plan risk > 7
P1_ALWAYS_APPROVE   = True  # human approval for P1 (simulate auto-approve in demo)

async def pre_validate_node(state: IncidentState) -> dict:
    """
    Stage 5 — Pre-Validation Agent
    Checks: risk score, blast radius, change freeze, RBAC, command syntax.
    Decides: safe to execute / needs replan / needs human approval.
    """
    event = state["incident_event"]
    plan  = state["remediation_plan"]
    log("PRE-VALIDATE", f"Validating plan {plan.plan_id} (risk={plan.risk_score})")

    validation_prompt = f"""
You are a change management validation agent.
Validate this remediation plan for {event.affected_svc}:

Plan: {plan.title}
Risk Score: {plan.risk_score}/10
Steps:
{json.dumps([{"step": s.step_id, "cmd": s.command, "tool": s.tool} for s in plan.steps], indent=2)}

Downstream services: {json.dumps(["postgres-primary", "redis-cache", "kafka-payments"])}
Incident Severity: {event.severity}
Current time: weekday business hours

Perform these checks and return JSON:
{{
  "safe": bool,
  "risk": float (recalculated 0-10),
  "issues": ["list of issues found"],
  "blast_radius": "low|medium|high",
  "change_freeze": bool,
  "rbac_ok": bool,
  "syntax_ok": bool,
  "recommendation": "proceed|replan|escalate",
  "notes": "string"
}}
Respond ONLY with JSON.
"""
    resp   = LLM.invoke([HumanMessage(content=validation_prompt)])
    result = json.loads(resp.content.strip().strip("```json").strip("```"))

    # Override: if risk too high, mark unsafe
    if result["risk"] > RISK_THRESHOLD:
        result["safe"] = False
        result["issues"].append(f"Risk score {result['risk']:.1f} exceeds threshold {RISK_THRESHOLD}")

    # P1 incidents: simulate human approval (in prod: send to PagerDuty approval flow)
    if event.severity == "P1" and result.get("safe"):
        log("PRE-VALIDATE", "P1 incident — human approval gate (auto-approving in demo)")
        result["human_approved"] = True

    status_icon = "✅" if result["safe"] else "❌"
    log("PRE-VALIDATE", f"{status_icon} Safe={result['safe']} | Risk={result['risk']:.1f} | Blast={result['blast_radius']}")

    if result["issues"]:
        for issue in result["issues"]:
            log("PRE-VALIDATE", f"  ⚠️  {issue}")

    audit(state, "pre_validate", f"safe={result['safe']}, risk={result['risk']:.1f}")

    return {
        "validation_status": result,
        "human_approved"   : result.get("human_approved", False),
    }
