import json
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from state import IncidentState, IncidentEvent
from utils import log, audit

LLM = ChatOpenAI(model="gpt-4o", temperature=0)

async def trigger_node(state: IncidentState) -> dict:
    """
    Stage 1 — Trigger Agent
    Receives raw alert, enriches it, classifies severity, emits structured IncidentEvent.
    """
    event = state["incident_event"]
    log("TRIGGER", f"Ingesting incident {event.incident_id} from {event.source}")

    prompt = f"""
You are an incident triage agent. Analyze this alert and extract key information.

Incident ID : {event.incident_id}
Title       : {event.title}
Severity    : {event.severity}
Source      : {event.source}
Service     : {event.affected_svc}
Namespace   : {event.namespace}
Raw Alert   :
{json.dumps(event.raw_alert, indent=2)}

Produce a JSON triage summary with keys:
- confirmed_severity (P1/P2/P3/P4)
- incident_type (resource_exhaustion / config_drift / dependency_failure / code_bug / unknown)
- affected_components (list)
- immediate_impact (string)
- requires_immediate_action (bool)
- enriched_context (string, 2-3 sentences)

Respond ONLY with valid JSON.
"""
    resp   = LLM.invoke([HumanMessage(content=prompt)])
    triage = json.loads(resp.content.strip().strip("```json").strip("```"))

    log("TRIGGER", f"Triage complete: {triage['incident_type']} [{triage['confirmed_severity']}]")
    log("TRIGGER", f"Impact: {triage['immediate_impact']}")

    audit(state, "trigger", f"Triaged as {triage['incident_type']}, severity={triage['confirmed_severity']}")

    return {
        "audit_trail": state["audit_trail"] + [{
            "stage": "trigger",
            "triage": triage,
            "timestamp": __import__("datetime").datetime.utcnow().isoformat(),
        }]
    }
