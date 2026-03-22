import json
import uuid
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from state import IncidentState, RemediationPlan, RemediationStep
from utils import log, audit, tot_generate, tot_evaluate, tot_select

LLM = ChatOpenAI(model="gpt-4o", temperature=0.4)

async def planning_node(state: IncidentState) -> dict:
    """
    Stage 4 — Planning Agent (with ToT)
    Generates 3 candidate remediation plans via ToT, scores, selects best.
    Breaks into atomic, reversible steps with rollback commands.
    """
    event = state["incident_event"]
    rca   = state["rca_result"]
    log("PLANNING", f"Generating remediation plans for: {rca.root_cause[:60]}")

    # ── ToT: Generate 3 plan candidates ──────────────────────────────────────
    plan_prompt = f"""
Service: {event.affected_svc} | Namespace: {event.namespace}
Root Cause: {rca.root_cause}
Causal Chain: {json.dumps(rca.causal_chain)}

Generate 3 DISTINCT remediation strategies. Each should:
- Address the root cause differently (quick fix vs permanent vs hybrid)
- Include estimated risk (low/medium/high)
- Be specific to this service

Respond ONLY with JSON array of 3 plan description strings.
"""
    plans  = tot_generate(LLM, plan_prompt, n=3)

    eval_prompt = f"""
Root Cause: {rca.root_cause}
Service: {event.affected_svc}
Candidate plans:
{json.dumps(plans, indent=2)}

Score each plan: "sure" (best approach), "maybe" (workable), "impossible" (risky/won't work)
Consider: speed of resolution, risk level, reversibility, blast radius.
Respond ONLY with JSON array of scores.
"""
    scores   = tot_evaluate(LLM, eval_prompt, plans)
    best_plan = tot_select(plans, scores)

    log("PLANNING", f"Selected plan: {best_plan[:80]}")

    # ── Expand best plan into atomic steps ───────────────────────────────────
    expand_prompt = f"""
Service: {event.affected_svc} | Namespace: {event.namespace}
Root Cause: {rca.root_cause}
Selected remediation strategy: {best_plan}

Expand this into a detailed JSON remediation plan with this exact structure:
{{
  "title": "string",
  "risk_score": float (0-10),
  "impact": "string",
  "duration_est": "string",
  "steps": [
    {{
      "step_id": "step-001",
      "description": "string",
      "command": "exact kubectl/ansible command",
      "tool": "kubectl|ansible|aws-cli|configmap",
      "rollback": "exact rollback command",
      "timeout_s": 120
    }}
  ],
  "rollback_plan": ["ordered rollback steps as strings"]
}}

Make commands specific and executable. Include 3-6 steps.
Respond ONLY with JSON.
"""
    resp      = LLM.invoke([HumanMessage(content=expand_prompt)])
    plan_data = json.loads(resp.content.strip().strip("```json").strip("```"))

    steps = [
        RemediationStep(
            step_id    = s["step_id"],
            description= s["description"],
            command    = s["command"],
            tool       = s["tool"],
            rollback   = s["rollback"],
            timeout_s  = s.get("timeout_s", 120),
        )
        for s in plan_data["steps"]
    ]

    plan = RemediationPlan(
        plan_id      = f"PLAN-{uuid.uuid4().hex[:8].upper()}",
        title        = plan_data["title"],
        steps        = steps,
        risk_score   = plan_data["risk_score"],
        impact       = plan_data["impact"],
        duration_est = plan_data["duration_est"],
        rollback_plan= plan_data["rollback_plan"],
    )

    log("PLANNING", f"Plan {plan.plan_id}: {plan.title} | Risk: {plan.risk_score}/10 | Steps: {len(plan.steps)}")
    audit(state, "planning", f"Plan {plan.plan_id} generated, risk={plan.risk_score}")

    return {"remediation_plan": plan, "replan_count": state["replan_count"] + (1 if state["replan_count"] > 0 else 0)}
