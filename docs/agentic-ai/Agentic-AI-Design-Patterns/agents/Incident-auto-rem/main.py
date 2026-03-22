"""
Infrastructure & Application Incident Auto-Remediation
=======================================================
End-to-end Agentic AI pipeline using LangChain + LangGraph

Flow:
  Trigger → Diagnosis → RCA → Planning → Pre-Validate →
  Execute → Post-Validate → Self-Learn → Feedback → END

Each stage is a dedicated LangChain agent with its own tools.
LangGraph orchestrates the state machine with conditional edges,
retry loops, rollback paths, and human-in-the-loop gates.

Install:
    pip install langgraph langchain langchain-openai langchain-community \
                openai duckduckgo-search redis chromadb sentence-transformers

Run:
    export OPENAI_API_KEY="sk-..."
    python incident_remediation/main.py
"""

# ── incident_remediation/main.py ──────────────────────────────────────────────

import asyncio
import json
import os
import sys
from datetime import datetime

# Add parent to path so sub-modules resolve
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from state       import IncidentState, IncidentEvent, RemediationPlan, ExecutionResult
from graph       import build_graph
from utils       import log, banner

async def main():
    banner()

    # ── Simulate an incoming incident (in prod: webhook / PagerDuty) ─────────
    incident = IncidentEvent(
        incident_id   = "INC-20240315-001",
        title         = "High CPU + OOMKilled pods in payments-service",
        severity      = "P1",
        source        = "prometheus",
        affected_svc  = "payments-service",
        namespace     = "production",
        raw_alert     = {
            "labels": {
                "alertname"   : "KubePodCrashLooping",
                "namespace"   : "production",
                "pod"         : "payments-service-7d9f8b-xk2p9",
                "container"   : "payments-api",
                "reason"      : "OOMKilled",
            },
            "annotations": {
                "summary"     : "Container OOMKilled 5 times in last 10 min",
                "cpu_usage"   : "95%",
                "memory_req"  : "512Mi",
                "memory_limit": "512Mi",
            },
            "startsAt"    : datetime.utcnow().isoformat(),
        },
    )

    # ── Initial graph state ───────────────────────────────────────────────────
    initial_state: IncidentState = {
        "incident_event"     : incident,
        "diagnosis_report"   : None,
        "rca_result"         : None,
        "remediation_plan"   : None,
        "validation_status"  : None,
        "execution_result"   : None,
        "health_status"      : None,
        "lessons_learned"    : None,
        "feedback_sent"      : False,
        "retry_count"        : 0,
        "replan_count"       : 0,
        "error_log"          : [],
        "audit_trail"        : [],
        "human_approved"     : False,
    }

    # ── Build and run graph ───────────────────────────────────────────────────
    graph = build_graph()

    log("ORCHESTRATOR", f"Starting pipeline for {incident.incident_id} [{incident.severity}]")

    final_state = await graph.ainvoke(
        initial_state,
        config={"configurable": {"thread_id": incident.incident_id}},
    )

    # ── Print summary ─────────────────────────────────────────────────────────
    print("\n" + "═"*70)
    print("  PIPELINE COMPLETE")
    print("═"*70)
    print(f"  Incident  : {incident.incident_id}")
    print(f"  Service   : {incident.affected_svc}")
    print(f"  Resolved  : {final_state.get('health_status', {}).get('resolved', False)}")
    print(f"  Retries   : {final_state.get('retry_count', 0)}")
    print(f"  Re-plans  : {final_state.get('replan_count', 0)}")
    print(f"  Feedback  : {'✓ sent' if final_state.get('feedback_sent') else '✗ pending'}")
    print("═"*70 + "\n")


if __name__ == "__main__":
    asyncio.run(main())
