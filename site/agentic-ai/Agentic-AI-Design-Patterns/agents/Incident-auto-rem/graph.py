"""
LangGraph graph — wires all agents into the state machine.

Nodes:
  trigger_node → diagnosis_node → rca_node → planning_node
  → pre_validate_node → [human_gate] → execution_node
  → post_validate_node → learning_node → feedback_node → END

Conditional edges:
  pre_validate  → "replan"  (if unsafe)  or "execute"
  execution     → "rollback" (if failed) or "post_validate"
  post_validate → "retry"   (if degraded, max 3) or "learn"
"""

from langgraph.graph     import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver

from state   import IncidentState
from agents.trigger_agent      import trigger_node
from agents.diagnosis_agent    import diagnosis_node
from agents.rca_agent          import rca_node
from agents.planning_agent     import planning_node
from agents.pre_validate_agent import pre_validate_node
from agents.execution_agent    import execution_node
from agents.post_validate_agent import post_validate_node
from agents.learning_agent     import learning_node
from agents.feedback_agent     import feedback_node
from utils import log

MAX_RETRIES  = 3
MAX_REPLANS  = 2


# ── Conditional edge functions ────────────────────────────────────────────────

def route_after_pre_validate(state: IncidentState) -> str:
    v = state["validation_status"]
    if not v:
        return "replan"
    if not v.get("safe", False):
        log("ROUTER", f"Plan unsafe (risk={v.get('risk',0):.1f}), re-planning...")
        if state["replan_count"] >= MAX_REPLANS:
            log("ROUTER", "Max re-plans reached — escalating")
            return "feedback"   # escalate without fixing
        return "replan"
    log("ROUTER", "Plan validated — proceeding to execution")
    return "execute"


def route_after_execution(state: IncidentState) -> str:
    result = state["execution_result"]
    if result and not result.success:
        log("ROUTER", f"Execution failed: {result.error} — rollback triggered")
        # Rollback happened inside execution_node; go straight to post-validate
        # to assess damage / partial recovery
    return "post_validate"


def route_after_post_validate(state: IncidentState) -> str:
    h = state["health_status"]
    if h and h.resolved:
        log("ROUTER", "Incident resolved ✓ — moving to learning")
        return "learn"
    if state["retry_count"] >= MAX_RETRIES:
        log("ROUTER", "Max retries reached — escalating to humans")
        return "escalate"
    log("ROUTER", f"Not resolved (retry {state['retry_count']}) — re-executing plan")
    return "retry"


# ── Graph builder ─────────────────────────────────────────────────────────────

def build_graph() -> StateGraph:
    builder = StateGraph(IncidentState)

    # ── Register nodes ───────────────────────────────────────────────────────
    builder.add_node("trigger",       trigger_node)
    builder.add_node("diagnose",      diagnosis_node)
    builder.add_node("rca",           rca_node)
    builder.add_node("plan",          planning_node)
    builder.add_node("pre_validate",  pre_validate_node)
    builder.add_node("execute",       execution_node)
    builder.add_node("post_validate", post_validate_node)
    builder.add_node("learn",         learning_node)
    builder.add_node("feedback",      feedback_node)

    # ── Entry point ───────────────────────────────────────────────────────────
    builder.set_entry_point("trigger")

    # ── Linear edges ─────────────────────────────────────────────────────────
    builder.add_edge("trigger",   "diagnose")
    builder.add_edge("diagnose",  "rca")
    builder.add_edge("rca",       "plan")
    builder.add_edge("plan",      "pre_validate")
    builder.add_edge("learn",     "feedback")
    builder.add_edge("feedback",  END)

    # ── Conditional edges ─────────────────────────────────────────────────────
    builder.add_conditional_edges(
        "pre_validate",
        route_after_pre_validate,
        {
            "replan"   : "plan",       # loop back to re-plan
            "execute"  : "execute",
            "feedback" : "feedback",   # escalation path
        },
    )

    builder.add_conditional_edges(
        "execute",
        route_after_execution,
        {
            "post_validate": "post_validate",
        },
    )

    builder.add_conditional_edges(
        "post_validate",
        route_after_post_validate,
        {
            "learn"    : "learn",
            "retry"    : "execute",    # retry execution with same plan
            "escalate" : "feedback",   # human escalation
        },
    )

    # ── Compile with memory checkpointing ────────────────────────────────────
    memory = MemorySaver()
    graph  = builder.compile(checkpointer=memory)

    return graph
