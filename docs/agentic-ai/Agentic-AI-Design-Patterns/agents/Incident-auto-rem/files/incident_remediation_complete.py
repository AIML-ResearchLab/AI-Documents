"""
╔══════════════════════════════════════════════════════════════════════════════╗
║   INFRASTRUCTURE & APPLICATION INCIDENT AUTO-REMEDIATION                   ║
║   Agentic AI Pipeline — LangGraph + LangChain + Tree-of-Thoughts           ║
╠══════════════════════════════════════════════════════════════════════════════╣
║                                                                              ║
║  PIPELINE STAGES:                                                            ║
║  1. Trigger Agent      — Ingest & triage incoming alert                     ║
║  2. Diagnosis Agent    — Collect metrics/logs, ToT hypothesis exploration    ║
║  3. RCA Agent          — Causal chain, vector DB lookup, runbook match       ║
║  4. Planning Agent     — ToT plan generation, risk scoring, atomic steps     ║
║  5. Pre-Validate Agent — Blast radius, RBAC, safety check, human gate        ║
║  6. Execution Agent    — Sequential step execution, auto-rollback            ║
║  7. Post-Validate Agent— Health checks, SLO verification, MTTR              ║
║  8. Learning Agent     — Lessons extraction, vector DB update               ║
║  9. Feedback Agent     — Slack/JIRA/PagerDuty notifications                 ║
║                                                                              ║
║  GRAPH EDGES:                                                                ║
║  pre_validate → replan (if unsafe) | execute (if safe)                      ║
║  execution    → post_validate (always, rollback handled inside)             ║
║  post_validate→ retry (if degraded, max 3) | learn (if resolved)            ║
║  post_validate→ escalate (if max retries hit)                               ║
║                                                                              ║
║  Install: pip install langgraph langchain langchain-openai                  ║
║           langchain-community openai duckduckgo-search                      ║
║  Run:     export OPENAI_API_KEY="sk-..."                                    ║
║           python incident_remediation_all_in_one.py                         ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

from __future__ import annotations
import asyncio
import json
import os
import uuid
import random
from dataclasses import dataclass, field
from datetime    import datetime
from typing      import Any, Optional

# ── LangGraph / LangChain imports ────────────────────────────────────────────
from langgraph.graph              import StateGraph, END
from langgraph.checkpoint.memory  import MemorySaver
from langchain_openai             import ChatOpenAI
from langchain.agents             import AgentExecutor, create_openai_tools_agent
from langchain_community.tools    import DuckDuckGoSearchRun
from langchain.tools              import tool
from langchain_core.prompts       import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages      import HumanMessage
from typing                       import TypedDict

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-api-key-here")
MODEL          = "gpt-4o"
MAX_RETRIES    = 3
MAX_REPLANS    = 2
RISK_THRESHOLD = 7.0


# ══════════════════════════════════════════════════════════════════════════════
# 1. DOMAIN MODELS & GRAPH STATE
# ══════════════════════════════════════════════════════════════════════════════

@dataclass
class IncidentEvent:
    incident_id  : str
    title        : str
    severity     : str          # P1 / P2 / P3 / P4
    source       : str
    affected_svc : str
    namespace    : str
    raw_alert    : dict

@dataclass
class DiagnosisReport:
    symptoms         : list[str]
    metric_snapshot  : dict[str, Any]
    log_excerpt      : str
    hypothesis_tree  : list[dict]
    best_hypothesis  : str
    confidence       : float

@dataclass
class RCAResult:
    root_cause        : str
    causal_chain      : list[str]
    confidence        : float
    similar_incidents : list[dict]
    matched_runbooks  : list[str]

@dataclass
class RemediationStep:
    step_id     : str
    description : str
    command     : str
    tool        : str
    rollback    : str
    timeout_s   : int = 120

@dataclass
class RemediationPlan:
    plan_id      : str
    title        : str
    steps        : list[RemediationStep]
    risk_score   : float
    impact       : str
    duration_est : str
    rollback_plan: list[str]

@dataclass
class ExecutionResult:
    plan_id      : str
    steps_done   : list[dict]
    success      : bool
    rolled_back  : bool
    error        : Optional[str] = None

@dataclass
class HealthStatus:
    resolved           : bool
    metrics_recovered  : dict[str, Any]
    checks_passed      : list[str]
    checks_failed      : list[str]
    slo_restored       : bool
    mttr_seconds       : int

@dataclass
class LessonsLearned:
    incident_id     : str
    root_cause      : str
    resolution      : str
    what_worked     : list[str]
    what_failed     : list[str]
    runbook_updates : list[str]
    vector_db_entry : dict

class IncidentState(TypedDict):
    incident_event    : IncidentEvent
    diagnosis_report  : Optional[DiagnosisReport]
    rca_result        : Optional[RCAResult]
    remediation_plan  : Optional[RemediationPlan]
    validation_status : Optional[dict]
    execution_result  : Optional[ExecutionResult]
    health_status     : Optional[HealthStatus]
    lessons_learned   : Optional[LessonsLearned]
    feedback_sent     : bool
    retry_count       : int
    replan_count      : int
    error_log         : list[str]
    audit_trail       : list[dict]
    human_approved    : bool


# ══════════════════════════════════════════════════════════════════════════════
# 2. UTILITIES
# ══════════════════════════════════════════════════════════════════════════════

def log(agent: str, msg: str):
    ts = datetime.utcnow().strftime("%H:%M:%S")
    print(f"  [{ts}] [{agent:<14}] {msg}")

def audit(state: IncidentState, stage: str, detail: str):
    entry = {"stage": stage, "detail": detail, "timestamp": datetime.utcnow().isoformat()}
    state.setdefault("audit_trail", []).append(entry)

def _strip_json(raw: str) -> str:
    raw = raw.strip()
    if raw.startswith("```"):
        parts = raw.split("```")
        raw   = parts[1] if len(parts) > 1 else raw
        if raw.startswith("json"):
            raw = raw[4:]
    return raw.strip()

def tot_generate(llm, prompt: str, n: int = 3) -> list[str]:
    resp = llm.invoke([HumanMessage(content=prompt)])
    return json.loads(_strip_json(resp.content))[:n]

def tot_evaluate(llm, prompt: str, items: list[str]) -> list[str]:
    resp = llm.invoke([HumanMessage(content=prompt)])
    return json.loads(_strip_json(resp.content))[:len(items)]

def tot_select(items: list[str], scores: list[str]) -> str:
    priority = {"sure": 0, "maybe": 1, "impossible": 2}
    ranked   = sorted(zip(items, scores), key=lambda x: priority.get(x[1], 3))
    for item, score in ranked:
        if score != "impossible":
            return item
    return items[0]

def banner():
    print("\n" + "═"*70)
    print("  INCIDENT AUTO-REMEDIATION — AGENTIC AI PIPELINE")
    print("  LangGraph + LangChain + Tree-of-Thoughts + 9 Agents")
    print("═"*70 + "\n")


# ══════════════════════════════════════════════════════════════════════════════
# 3. TOOLS
# ══════════════════════════════════════════════════════════════════════════════

@tool
def fetch_pod_metrics(namespace: str, service: str) -> str:
    """Fetch CPU, memory, restart counts for pods in a namespace/service."""
    return json.dumps({
        "service": service, "namespace": namespace,
        "cpu_usage_pct": 94.7, "memory_usage_mi": 510, "memory_limit_mi": 512,
        "restart_count": 7, "pod_status": "CrashLoopBackOff",
        "ready_replicas": 0, "desired_replicas": 3,
    }, indent=2)

@tool
def fetch_application_logs(namespace: str, service: str, lines: int = 100) -> str:
    """Fetch recent application logs for a service."""
    logs = [
        "2024-03-15T10:23:41Z ERROR OutOfMemoryError: Java heap space",
        "2024-03-15T10:23:40Z WARN  Memory usage at 98%, GC overhead exceeded",
        "2024-03-15T10:23:38Z ERROR Connection pool exhausted: max=100 active=100",
        "2024-03-15T10:23:35Z INFO  Processing payment batch size=5000",
        "2024-03-15T10:23:30Z INFO  Received 2847 concurrent requests",
        "2024-03-15T10:20:00Z INFO  Deployment rollout started v2.4.1",
        "2024-03-15T10:19:50Z INFO  Config updated: payment.batch.size=5000 (was 500)",
    ]
    return "\n".join(logs[:lines])

@tool
def fetch_recent_deployments(namespace: str, service: str) -> str:
    """List recent deployments and config changes for a service."""
    return json.dumps({"recent_deployments": [
        {"version": "v2.4.1", "deployed_at": "2024-03-15T10:20:00Z",
         "changes": ["payment.batch.size: 500 → 5000", "heap.size: unchanged at 512Mi"]},
        {"version": "v2.4.0", "deployed_at": "2024-03-14T14:30:00Z",
         "changes": ["Added async payment processor"]},
    ]}, indent=2)

@tool
def fetch_service_dependencies(service: str, namespace: str) -> str:
    """Get upstream and downstream service dependencies."""
    return json.dumps({
        "upstream": ["api-gateway", "auth-service"],
        "downstream": ["postgres-primary", "redis-cache", "kafka-payments"],
        "external": ["stripe-api", "fraud-detection-svc"],
    }, indent=2)

@tool
def kubectl_get_pods(namespace: str, service: str) -> str:
    """Get pod status for a service."""
    return json.dumps({"pods": [
        {"name": f"{service}-xk2p9", "status": "OOMKilled", "restarts": 7},
        {"name": f"{service}-mn3r1", "status": "OOMKilled", "restarts": 5},
        {"name": f"{service}-pq7s4", "status": "Running",   "restarts": 3},
    ]}, indent=2)

@tool
def kubectl_describe_pod(namespace: str, pod_name: str) -> str:
    """Describe a pod including events and resource usage."""
    return json.dumps({
        "pod": pod_name, "namespace": namespace,
        "last_state": {"terminated": {"reason": "OOMKilled", "exit_code": 137}},
        "limits": {"memory": "512Mi", "cpu": "500m"},
        "events": ["BackOff: Back-off restarting failed container",
                   "OOMKilling: Memory cgroup out of memory: Kill process"],
    }, indent=2)

@tool
def kubectl_scale_deployment(namespace: str, deployment: str, replicas: int) -> str:
    """Scale a Kubernetes deployment."""
    return json.dumps({"action": "scale", "deployment": deployment,
                        "replicas": replicas, "status": "success"})

@tool
def kubectl_patch_resource_limits(namespace: str, deployment: str,
                                   memory_limit: str, cpu_limit: str) -> str:
    """Patch memory and CPU limits on a deployment."""
    return json.dumps({"action": "patch_limits", "deployment": deployment,
                        "new_limits": {"memory": memory_limit, "cpu": cpu_limit},
                        "status": "success"})

@tool
def kubectl_rollout_restart(namespace: str, deployment: str) -> str:
    """Perform a rolling restart of a deployment."""
    return json.dumps({"action": "rollout_restart", "deployment": deployment,
                        "status": "success", "message": "Rolling restart initiated"})

@tool
def kubectl_rollback_deployment(namespace: str, deployment: str, revision: int = 0) -> str:
    """Rollback a deployment to previous revision."""
    return json.dumps({"action": "rollback", "deployment": deployment,
                        "status": "success", "revision": revision or "previous"})

@tool
def update_config_map(namespace: str, configmap: str, key: str, value: str) -> str:
    """Update a Kubernetes ConfigMap key."""
    return json.dumps({"action": "update_configmap", "configmap": configmap,
                        "key": key, "new_value": value, "status": "success"})

@tool
def run_health_check(namespace: str, service: str) -> str:
    """Run synthetic health check against a service endpoint."""
    recovered = random.random() > 0.25   # 75% chance of recovery
    return json.dumps({
        "service": service, "namespace": namespace,
        "http_status": 200 if recovered else 503,
        "response_time_ms": 140 if recovered else 9999,
        "pod_ready_count": 3 if recovered else 0,
        "error_rate_pct": 0.1 if recovered else 45.3,
        "cpu_usage_pct": 41.0 if recovered else 94.7,
        "memory_usage_pct": 67.0 if recovered else 99.6,
        "recovered": recovered,
    })

@tool
def search_similar_incidents(query: str, top_k: int = 3) -> str:
    """Search vector DB for similar past incidents and resolutions."""
    return json.dumps([
        {"id": "INC-20240201-044", "title": "payments-service OOMKilled after batch size increase",
         "root_cause": "JVM heap exhausted due to large batch processing",
         "resolution": "Increased memory limit to 1Gi, reduced batch size to 1000",
         "similarity": 0.94},
        {"id": "INC-20231115-089", "title": "checkout-service crash loop after config change",
         "root_cause": "Connection pool exhausted under high concurrency",
         "resolution": "Rolled back config, increased connection pool size",
         "similarity": 0.81},
    ], indent=2)

@tool
def fetch_runbook(service: str, symptom: str) -> str:
    """Fetch the most relevant runbook for a service and symptom."""
    return json.dumps({
        "runbook_id": "RB-PAYMENTS-OOM-001",
        "title": "payments-service OOMKilled Remediation",
        "steps": [
            "1. Check current memory limits: kubectl describe pod",
            "2. Increase memory limit to 2x current: kubectl patch deployment",
            "3. Reduce payment.batch.size to 1000 in ConfigMap",
            "4. Rolling restart to apply changes",
            "5. Monitor for 5 min — verify pod restarts stop",
        ],
        "owner": "payments-team", "last_updated": "2024-02-01",
    }, indent=2)

@tool
def store_incident_lesson(incident_id: str, lesson: dict) -> str:
    """Store an incident lesson in the vector DB."""
    return json.dumps({"status": "stored", "incident_id": incident_id,
                        "vector_id": f"vec_{incident_id}"})

@tool
def send_slack_notification(channel: str, message: str) -> str:
    """Send a Slack notification to a channel."""
    print(f"\n  📣 [SLACK → #{channel}]\n  {message[:300]}\n")
    return json.dumps({"status": "sent", "channel": channel})

@tool
def create_jira_ticket(summary: str, description: str, issue_type: str = "Post-Mortem") -> str:
    """Create a JIRA ticket for post-mortem."""
    ticket_id = f"OPS-{random.randint(1000,9999)}"
    print(f"\n  🎫 [JIRA] Created {ticket_id}: {summary}\n")
    return json.dumps({"ticket_id": ticket_id, "status": "created"})

@tool
def resolve_pagerduty_incident(incident_id: str, resolution_note: str) -> str:
    """Mark a PagerDuty incident as resolved."""
    return json.dumps({"incident_id": incident_id, "status": "resolved",
                        "resolution_note": resolution_note})

# Tool groups per agent
DIAGNOSIS_TOOLS     = [fetch_pod_metrics, fetch_application_logs,
                        fetch_recent_deployments, fetch_service_dependencies,
                        kubectl_get_pods, kubectl_describe_pod]
RCA_TOOLS           = [search_similar_incidents, fetch_runbook, fetch_service_dependencies]
PLANNING_TOOLS      = [fetch_runbook, search_similar_incidents]
PRE_VALIDATE_TOOLS  = [fetch_service_dependencies, kubectl_get_pods]
EXECUTION_TOOLS     = [kubectl_scale_deployment, kubectl_patch_resource_limits,
                        kubectl_rollout_restart, kubectl_rollback_deployment,
                        update_config_map, run_health_check]
POST_VALIDATE_TOOLS = [run_health_check, fetch_pod_metrics, fetch_application_logs]
LEARNING_TOOLS      = [store_incident_lesson, fetch_runbook]
FEEDBACK_TOOLS      = [send_slack_notification, create_jira_ticket, resolve_pagerduty_incident]


# ══════════════════════════════════════════════════════════════════════════════
# 4. LLM INSTANCES
# ══════════════════════════════════════════════════════════════════════════════
LLM       = ChatOpenAI(model=MODEL, temperature=0.3, api_key=OPENAI_API_KEY)
LLM_ZERO  = ChatOpenAI(model=MODEL, temperature=0.0, api_key=OPENAI_API_KEY)

def make_agent_executor(llm, tools, system_prompt: str, max_iter: int = 8) -> AgentExecutor:
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        MessagesPlaceholder("chat_history", optional=True),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ])
    agent = create_openai_tools_agent(llm, tools, prompt)
    return AgentExecutor(agent=agent, tools=tools, verbose=False, max_iterations=max_iter)


# ══════════════════════════════════════════════════════════════════════════════
# 5. AGENT NODES
# ══════════════════════════════════════════════════════════════════════════════

# ── Stage 1: Trigger ──────────────────────────────────────────────────────────
async def trigger_node(state: IncidentState) -> dict:
    """Ingest alert, enrich with CMDB context, classify severity."""
    event = state["incident_event"]
    log("TRIGGER", f"Ingesting {event.incident_id} [{event.severity}] from {event.source}")

    resp   = LLM_ZERO.invoke([HumanMessage(content=f"""
You are an incident triage agent. Analyze this alert and produce a JSON triage summary.

Incident: {event.incident_id}
Title   : {event.title}
Severity: {event.severity}
Service : {event.affected_svc}
Alert   : {json.dumps(event.raw_alert, indent=2)}

Return JSON with keys:
- confirmed_severity (P1/P2/P3/P4)
- incident_type (resource_exhaustion|config_drift|dependency_failure|code_bug|unknown)
- affected_components (list)
- immediate_impact (string)
- enriched_context (string)

Respond ONLY with JSON.
""")])
    triage = json.loads(_strip_json(resp.content))
    log("TRIGGER", f"Type: {triage['incident_type']} | Impact: {triage['immediate_impact'][:60]}")
    audit(state, "trigger", f"triaged={triage['incident_type']}")
    return {"audit_trail": state.get("audit_trail", []) + [{"stage": "trigger", "triage": triage}]}


# ── Stage 2: Diagnosis (with ToT) ─────────────────────────────────────────────
async def diagnosis_node(state: IncidentState) -> dict:
    """Collect metrics/logs/traces. Use ToT to explore and prune hypotheses."""
    event = state["incident_event"]
    log("DIAGNOSIS", f"Collecting data for {event.affected_svc}")

    executor = make_agent_executor(LLM, DIAGNOSIS_TOOLS, f"""
You are a diagnosis agent for {event.affected_svc} in {event.namespace}.
Collect: pod metrics, recent logs, deployment history, service dependencies.
Be thorough — use multiple tools.""", max_iter=8)

    raw    = executor.invoke({"input": f"Collect all diagnostics for {event.affected_svc}"})["output"]
    log("DIAGNOSIS", "Data collected — starting ToT hypothesis exploration")

    # ToT: Generate → Evaluate → Select
    hypotheses = tot_generate(LLM, f"""
Diagnostic data for {event.affected_svc}: {raw[:1000]}
Alert: {event.title}
Generate 3 DISTINCT specific root-cause hypotheses.
Respond ONLY with JSON array of 3 strings.""", n=3)

    scores = tot_evaluate(LLM_ZERO, f"""
Data: {raw[:800]}
Hypotheses: {json.dumps(hypotheses)}
Score each: "sure"/"maybe"/"impossible"
Respond ONLY with JSON array of 3 scores.""", hypotheses)

    best = tot_select(hypotheses, scores)
    hypo_tree = [{"hypothesis": h, "score": s} for h, s in zip(hypotheses, scores)]

    metrics_raw = LLM_ZERO.invoke([HumanMessage(content=f"""
From: {raw[:600]}
Extract JSON: {{cpu_usage_pct, memory_usage_pct, restart_count, error_rate_pct, pod_ready_count}}
Respond ONLY with JSON.""")])
    metric_snap = json.loads(_strip_json(metrics_raw.content))

    for h, s in zip(hypotheses, scores):
        icon = {"sure":"✅","maybe":"⚠️ ","impossible":"❌"}.get(s,"❓")
        log("DIAGNOSIS", f"  ToT {icon} [{s:>10}] {h[:65]}")
    log("DIAGNOSIS", f"Best hypothesis selected ✓")

    report = DiagnosisReport(
        symptoms=["OOMKilled","CrashLoopBackOff", event.title],
        metric_snapshot=metric_snap, log_excerpt=raw[:500],
        hypothesis_tree=hypo_tree, best_hypothesis=best, confidence=0.87)
    audit(state, "diagnosis", f"best={best[:50]}")
    return {"diagnosis_report": report}


# ── Stage 3: RCA ──────────────────────────────────────────────────────────────
async def rca_node(state: IncidentState) -> dict:
    """Build causal chain, cross-reference vector DB, match runbooks."""
    event     = state["incident_event"]
    diagnosis = state["diagnosis_report"]
    log("RCA", f"Building causal chain for {event.affected_svc}")

    executor = make_agent_executor(LLM, RCA_TOOLS, f"""
You are a root cause analysis agent.
Service: {event.affected_svc} | Best Hypothesis: {diagnosis.best_hypothesis}
Metrics: {json.dumps(diagnosis.metric_snapshot)}
1. Search for similar past incidents
2. Fetch the service runbook
Then build a complete causal chain from trigger to root cause.""", max_iter=6)

    result = executor.invoke({"input": "Perform complete RCA and fetch runbooks"})["output"]

    rca_raw = LLM_ZERO.invoke([HumanMessage(content=f"""
From this RCA: {result}
Extract JSON:
{{
  "root_cause": "string",
  "causal_chain": ["ordered list from trigger to root cause"],
  "confidence": float,
  "matched_runbooks": ["list"]
}}
Respond ONLY with JSON.""")])
    rca_data = json.loads(_strip_json(rca_raw.content))

    rca = RCAResult(
        root_cause=rca_data["root_cause"],
        causal_chain=rca_data["causal_chain"],
        confidence=rca_data.get("confidence", 0.85),
        similar_incidents=[], matched_runbooks=rca_data.get("matched_runbooks", []))

    log("RCA", f"Root cause: {rca.root_cause}")
    log("RCA", f"Causal chain: {' → '.join(rca.causal_chain[:3])}")
    audit(state, "rca", f"root_cause={rca.root_cause[:50]}")
    return {"rca_result": rca}


# ── Stage 4: Planning (with ToT) ──────────────────────────────────────────────
async def planning_node(state: IncidentState) -> dict:
    """Generate 3 plan candidates via ToT, score, select best, expand to atomic steps."""
    event = state["incident_event"]
    rca   = state["rca_result"]
    log("PLANNING", f"Generating remediation plans (replan #{state['replan_count']})")

    # ToT plan generation
    plans = tot_generate(LLM, f"""
Service: {event.affected_svc} | Root Cause: {rca.root_cause}
Causal chain: {json.dumps(rca.causal_chain)}
Generate 3 DISTINCT remediation strategies (quick fix / permanent / hybrid).
Each should address root cause differently with specific kubectl/config actions.
Respond ONLY with JSON array of 3 plan description strings.""", n=3)

    scores = tot_evaluate(LLM_ZERO, f"""
Root Cause: {rca.root_cause} | Service: {event.affected_svc}
Plans: {json.dumps(plans)}
Score each: "sure"/"maybe"/"impossible" based on effectiveness + safety.
Respond ONLY with JSON array of 3 scores.""", plans)

    best_plan = tot_select(plans, scores)
    for p, s in zip(plans, scores):
        icon = {"sure":"✅","maybe":"⚠️ ","impossible":"❌"}.get(s,"❓")
        log("PLANNING", f"  ToT {icon} [{s:>10}] {p[:65]}")
    log("PLANNING", f"Best plan selected ✓")

    # Expand to atomic steps
    expand_raw = LLM_ZERO.invoke([HumanMessage(content=f"""
Service: {event.affected_svc} | Namespace: {event.namespace}
Root Cause: {rca.root_cause}
Strategy: {best_plan}

Expand into JSON remediation plan:
{{
  "title": "string",
  "risk_score": float,
  "impact": "string",
  "duration_est": "string",
  "steps": [
    {{
      "step_id": "step-001",
      "description": "string",
      "command": "exact kubectl/configmap command",
      "tool": "kubectl|configmap|ansible",
      "rollback": "exact rollback command",
      "timeout_s": 120
    }}
  ],
  "rollback_plan": ["ordered rollback steps"]
}}
Include 3-5 steps. Make commands specific and executable.
Respond ONLY with JSON.""")])
    plan_data = json.loads(_strip_json(expand_raw.content))

    steps = [RemediationStep(
        step_id=s["step_id"], description=s["description"],
        command=s["command"], tool=s["tool"],
        rollback=s["rollback"], timeout_s=s.get("timeout_s", 120))
        for s in plan_data["steps"]]

    plan = RemediationPlan(
        plan_id=f"PLAN-{uuid.uuid4().hex[:8].upper()}",
        title=plan_data["title"], steps=steps,
        risk_score=plan_data["risk_score"], impact=plan_data["impact"],
        duration_est=plan_data["duration_est"], rollback_plan=plan_data["rollback_plan"])

    log("PLANNING", f"Plan {plan.plan_id}: '{plan.title}'")
    log("PLANNING", f"  Risk={plan.risk_score}/10 | Steps={len(plan.steps)} | ETA={plan.duration_est}")
    for s in plan.steps:
        log("PLANNING", f"  📌 [{s.step_id}] {s.description[:60]}")
    audit(state, "planning", f"plan_id={plan.plan_id}, risk={plan.risk_score}")
    return {"remediation_plan": plan, "replan_count": state["replan_count"] + 1}


# ── Stage 5: Pre-Validation ───────────────────────────────────────────────────
async def pre_validate_node(state: IncidentState) -> dict:
    """Check blast radius, RBAC, change freeze, risk threshold. Human gate for P1."""
    event = state["incident_event"]
    plan  = state["remediation_plan"]
    log("PRE-VALIDATE", f"Validating plan {plan.plan_id} (risk={plan.risk_score})")

    resp = LLM_ZERO.invoke([HumanMessage(content=f"""
You are a change management validation agent.
Plan: {plan.title} | Risk: {plan.risk_score}/10
Steps: {json.dumps([{{"id": s.step_id, "cmd": s.command}} for s in plan.steps])}
Downstream: postgres-primary, redis-cache, kafka-payments
Severity: {event.severity}

Validate and return JSON:
{{
  "safe": bool,
  "risk": float,
  "issues": ["list of issues"],
  "blast_radius": "low|medium|high",
  "change_freeze": false,
  "rbac_ok": true,
  "syntax_ok": true,
  "recommendation": "proceed|replan|escalate",
  "notes": "string"
}}
Mark safe=false only if risk>7, change_freeze=true, or critical syntax error.
Respond ONLY with JSON.""")])
    result = json.loads(_strip_json(resp.content))

    if result["risk"] > RISK_THRESHOLD:
        result["safe"] = False
        result["issues"].append(f"Risk {result['risk']:.1f} exceeds threshold {RISK_THRESHOLD}")

    if event.severity == "P1" and result.get("safe"):
        log("PRE-VALIDATE", "P1 incident — human approval gate [AUTO-APPROVED in demo]")
        result["human_approved"] = True

    icon = "✅" if result["safe"] else "❌"
    log("PRE-VALIDATE", f"{icon} safe={result['safe']} | risk={result['risk']:.1f} | blast={result['blast_radius']}")
    for issue in result.get("issues", []):
        log("PRE-VALIDATE", f"  ⚠️  {issue}")

    audit(state, "pre_validate", f"safe={result['safe']}, risk={result['risk']:.1f}")
    return {"validation_status": result, "human_approved": result.get("human_approved", False)}


# ── Stage 6: Execution ────────────────────────────────────────────────────────
async def execution_node(state: IncidentState) -> dict:
    """Execute plan steps sequentially. Auto-rollback on failure."""
    event = state["incident_event"]
    plan  = state["remediation_plan"]
    log("EXECUTION", f"Executing plan {plan.plan_id} (attempt {state['retry_count']+1})")

    executor = make_agent_executor(LLM, EXECUTION_TOOLS, f"""
You are an execution agent performing infrastructure remediation.
Service: {event.affected_svc} | Namespace: {event.namespace}
Plan: {plan.title}

RULES:
- Execute each step IN ORDER using exact tool calls
- After each step verify success via tool output
- On step failure: execute its rollback command immediately
- Use kubectl_rollback_deployment as last resort if multiple failures""", max_iter=12)

    steps_json = json.dumps([{
        "step_id": s.step_id, "description": s.description,
        "command": s.command, "tool": s.tool, "rollback": s.rollback
    } for s in plan.steps], indent=2)

    result = executor.invoke({"input": f"Execute steps in order:\n{steps_json}"})["output"]

    parse_raw = LLM_ZERO.invoke([HumanMessage(content=f"""
From this execution output: {result}
Extract JSON:
{{
  "success": bool,
  "rolled_back": bool,
  "steps_done": [{{"step_id": "str", "status": "success|failed|skipped", "output": "str", "duration_s": 10}}],
  "error": null
}}
Respond ONLY with JSON.""")])
    exec_data = json.loads(_strip_json(parse_raw.content))

    exec_result = ExecutionResult(
        plan_id=plan.plan_id, steps_done=exec_data["steps_done"],
        success=exec_data["success"], rolled_back=exec_data.get("rolled_back", False),
        error=exec_data.get("error"))

    icon = "✅" if exec_result.success else "❌"
    log("EXECUTION", f"{icon} {'Succeeded' if exec_result.success else 'FAILED'} | rolled_back={exec_result.rolled_back}")
    for s in exec_result.steps_done:
        step_icon = "✅" if s["status"] == "success" else "❌"
        log("EXECUTION", f"  {step_icon} [{s['step_id']}] {s['status'].upper()} — {str(s.get('output',''))[:50]}")
    if exec_result.error:
        log("EXECUTION", f"  Error: {exec_result.error}")
    audit(state, "execution", f"success={exec_result.success}")
    return {"execution_result": exec_result, "retry_count": state["retry_count"] + 1}


# ── Stage 7: Post-Validation ──────────────────────────────────────────────────
async def post_validate_node(state: IncidentState) -> dict:
    """Re-poll metrics, run health checks, compare pre/post, determine resolution."""
    event     = state["incident_event"]
    diagnosis = state["diagnosis_report"]
    log("POST-VALIDATE", f"Running health checks for {event.affected_svc}")

    executor = make_agent_executor(LLM, POST_VALIDATE_TOOLS, f"""
You are a health validation agent.
Service: {event.affected_svc} | Namespace: {event.namespace}
Pre-incident metrics: {json.dumps(diagnosis.metric_snapshot)}

Run:
1. run_health_check — verify service responding
2. fetch_pod_metrics — compare with pre-incident
3. fetch_application_logs — check for remaining errors
Determine: RESOLVED / DEGRADED / STILL_FAILING""", max_iter=6)

    result = executor.invoke({"input": "Run all health checks and validate recovery"})["output"]

    parse_raw = LLM_ZERO.invoke([HumanMessage(content=f"""
From: {result}
Extract JSON:
{{
  "resolved": bool,
  "slo_restored": bool,
  "checks_passed": ["list"],
  "checks_failed": ["list"],
  "metrics_recovered": {{"cpu_pct": 0.0, "memory_pct": 0.0, "error_rate": 0.0}},
  "status": "resolved|degraded|failed"
}}
Respond ONLY with JSON.""")])
    hdata = json.loads(_strip_json(parse_raw.content))

    health = HealthStatus(
        resolved=hdata["resolved"], metrics_recovered=hdata.get("metrics_recovered", {}),
        checks_passed=hdata.get("checks_passed", []), checks_failed=hdata.get("checks_failed", []),
        slo_restored=hdata.get("slo_restored", False), mttr_seconds=420)

    icon = "✅" if health.resolved else "⚠️ "
    log("POST-VALIDATE", f"{icon} Status: {hdata['status'].upper()} | SLO: {'✓' if health.slo_restored else '✗'} | MTTR: {health.mttr_seconds}s")
    for c in health.checks_passed:
        log("POST-VALIDATE", f"  ✅ {c}")
    for c in health.checks_failed:
        log("POST-VALIDATE", f"  ❌ {c}")
    audit(state, "post_validate", f"resolved={health.resolved}")
    return {"health_status": health}


# ── Stage 8: Learning ─────────────────────────────────────────────────────────
async def learning_node(state: IncidentState) -> dict:
    """Extract lessons, update vector DB, score runbook effectiveness."""
    event    = state["incident_event"]
    rca      = state["rca_result"]
    plan     = state["remediation_plan"]
    exec_res = state["execution_result"]
    health   = state["health_status"]
    log("LEARNING", f"Extracting lessons from {event.incident_id}")

    executor = make_agent_executor(LLM, LEARNING_TOOLS, f"""
You are a self-learning agent that improves future incident response.
Incident: {event.title} | Root Cause: {rca.root_cause}
Plan: {plan.title} | Resolved: {health.resolved} | MTTR: {health.mttr_seconds}s
1. Fetch runbook to identify what to improve
2. Store lesson in vector DB with incident signature + resolution
3. Note automation opportunities""", max_iter=5)

    result = executor.invoke({"input": "Extract lessons, update runbook, store in vector DB"})["output"]

    l_raw = LLM_ZERO.invoke([HumanMessage(content=f"""
From: {result}
Extract JSON:
{{
  "what_worked": ["list"],
  "what_failed": ["list or empty"],
  "runbook_updates": ["improvements needed"],
  "prevention": "how to prevent recurrence",
  "automation_opportunity": "what could be automated"
}}
Respond ONLY with JSON.""")])
    ldata = json.loads(_strip_json(l_raw.content))

    lessons = LessonsLearned(
        incident_id=event.incident_id, root_cause=rca.root_cause,
        resolution=plan.title, what_worked=ldata["what_worked"],
        what_failed=ldata.get("what_failed", []),
        runbook_updates=ldata["runbook_updates"],
        vector_db_entry={"prevention": ldata["prevention"]})

    log("LEARNING", f"✓ Vector DB updated | Runbook updates: {len(lessons.runbook_updates)}")
    log("LEARNING", f"  Prevention: {ldata['prevention'][:70]}")
    log("LEARNING", f"  Automation: {ldata['automation_opportunity'][:70]}")
    for w in lessons.what_worked:
        log("LEARNING", f"  ✅ Worked: {w[:60]}")
    for f in lessons.what_failed:
        log("LEARNING", f"  ❌ Failed: {f[:60]}")
    audit(state, "learning", f"lessons stored for {event.incident_id}")
    return {"lessons_learned": lessons}


# ── Stage 9: Feedback ─────────────────────────────────────────────────────────
async def feedback_node(state: IncidentState) -> dict:
    """Send Slack notification, create JIRA post-mortem, resolve PagerDuty."""
    event   = state["incident_event"]
    rca     = state.get("rca_result")
    plan    = state.get("remediation_plan")
    health  = state.get("health_status")
    lessons = state.get("lessons_learned")

    log("FEEDBACK", f"Sending notifications for {event.incident_id}")
    resolved = health.resolved if health else False
    mttr     = health.mttr_seconds if health else 0

    slack_msg = f"""{'✅' if resolved else '🔴'} *Incident {event.incident_id} {'RESOLVED' if resolved else 'ESCALATED'}*
*Service*: `{event.affected_svc}` | *Severity*: {event.severity}
*Root Cause*: {rca.root_cause if rca else 'Under investigation'}
*Resolution*: {plan.title if plan else 'N/A'}
*MTTR*: {mttr//60}m {mttr%60}s
*What worked*: {', '.join((lessons.what_worked[:2] if lessons else ['auto-remediation']))}
Post-mortem ticket being created. Vector DB updated."""

    executor = make_agent_executor(LLM, FEEDBACK_TOOLS, """
You are a stakeholder communication agent. Send all notifications.""", max_iter=5)

    executor.invoke({"input": json.dumps({
        "slack_channel"   : "incidents",
        "slack_message"   : slack_msg,
        "jira_summary"    : f"Post-mortem: {event.title}",
        "jira_description": f"RCA: {rca.root_cause if rca else 'TBD'}\nResolution: {plan.title if plan else 'N/A'}",
        "pagerduty_id"    : event.incident_id,
        "resolution_note" : f"Auto-remediated. MTTR: {mttr}s",
    })})

    log("FEEDBACK", "✓ All notifications sent (Slack + JIRA + PagerDuty)")
    audit(state, "feedback", "notifications sent")
    return {"feedback_sent": True}


# ══════════════════════════════════════════════════════════════════════════════
# 6. CONDITIONAL EDGE ROUTERS
# ══════════════════════════════════════════════════════════════════════════════

def route_pre_validate(state: IncidentState) -> str:
    v = state.get("validation_status", {})
    if not v or not v.get("safe", False):
        if state["replan_count"] >= MAX_REPLANS:
            log("ROUTER", "Max re-plans reached → escalate")
            return "feedback"
        log("ROUTER", f"Plan unsafe → re-planning (replan #{state['replan_count']})")
        return "replan"
    log("ROUTER", "Plan safe → executing ✓")
    return "execute"

def route_post_validate(state: IncidentState) -> str:
    h = state.get("health_status")
    if h and h.resolved:
        log("ROUTER", "Incident resolved → learning ✓")
        return "learn"
    if state["retry_count"] >= MAX_RETRIES:
        log("ROUTER", f"Max retries ({MAX_RETRIES}) reached → escalating")
        return "escalate"
    log("ROUTER", f"Not resolved → retry {state['retry_count']+1}/{MAX_RETRIES}")
    return "retry"


# ══════════════════════════════════════════════════════════════════════════════
# 7. LANGGRAPH GRAPH BUILDER
# ══════════════════════════════════════════════════════════════════════════════

def build_graph() -> StateGraph:
    builder = StateGraph(IncidentState)

    # Register all nodes
    builder.add_node("trigger",       trigger_node)
    builder.add_node("diagnose",      diagnosis_node)
    builder.add_node("rca",           rca_node)
    builder.add_node("plan",          planning_node)
    builder.add_node("pre_validate",  pre_validate_node)
    builder.add_node("execute",       execution_node)
    builder.add_node("post_validate", post_validate_node)
    builder.add_node("learn",         learning_node)
    builder.add_node("feedback",      feedback_node)

    # Entry
    builder.set_entry_point("trigger")

    # Linear edges
    builder.add_edge("trigger",  "diagnose")
    builder.add_edge("diagnose", "rca")
    builder.add_edge("rca",      "plan")
    builder.add_edge("plan",     "pre_validate")
    builder.add_edge("execute",  "post_validate")
    builder.add_edge("learn",    "feedback")
    builder.add_edge("feedback", END)

    # Conditional edges
    builder.add_conditional_edges("pre_validate", route_pre_validate,
        {"replan": "plan", "execute": "execute", "feedback": "feedback"})
    builder.add_conditional_edges("post_validate", route_post_validate,
        {"learn": "learn", "retry": "execute", "escalate": "feedback"})

    memory = MemorySaver()
    return builder.compile(checkpointer=memory)


# ══════════════════════════════════════════════════════════════════════════════
# 8. MAIN ENTRYPOINT
# ══════════════════════════════════════════════════════════════════════════════

async def main():
    banner()

    # Simulated P1 incident — OOMKilled payments service after bad config deploy
    incident = IncidentEvent(
        incident_id  = "INC-20240315-001",
        title        = "High CPU + OOMKilled pods in payments-service",
        severity     = "P1",
        source       = "prometheus",
        affected_svc = "payments-service",
        namespace    = "production",
        raw_alert    = {
            "labels": {
                "alertname": "KubePodCrashLooping",
                "namespace": "production",
                "pod"      : "payments-service-7d9f8b-xk2p9",
                "reason"   : "OOMKilled",
            },
            "annotations": {
                "summary"      : "Container OOMKilled 5 times in last 10 min",
                "cpu_usage"    : "95%",
                "memory_limit" : "512Mi",
            },
            "startsAt": datetime.utcnow().isoformat(),
        },
    )

    initial_state: IncidentState = {
        "incident_event"   : incident,
        "diagnosis_report" : None,
        "rca_result"       : None,
        "remediation_plan" : None,
        "validation_status": None,
        "execution_result" : None,
        "health_status"    : None,
        "lessons_learned"  : None,
        "feedback_sent"    : False,
        "retry_count"      : 0,
        "replan_count"     : 0,
        "error_log"        : [],
        "audit_trail"      : [],
        "human_approved"   : False,
    }

    graph = build_graph()
    log("ORCHESTRATOR", f"Pipeline started for {incident.incident_id} [{incident.severity}]")

    final = await graph.ainvoke(
        initial_state,
        config={"configurable": {"thread_id": incident.incident_id}},
    )

    # ── Final summary ──────────────────────────────────────────────────────────
    print("\n" + "═"*70)
    print("  PIPELINE COMPLETE — AUDIT TRAIL")
    print("═"*70)
    for entry in final.get("audit_trail", []):
        print(f"  [{entry['stage']:>14}] {entry['detail']}")
    print()
    h = final.get("health_status")
    print(f"  Resolved : {h.resolved if h else False}")
    print(f"  MTTR     : {h.mttr_seconds if h else 'N/A'}s")
    print(f"  Retries  : {final.get('retry_count', 0)}")
    print(f"  Re-plans : {final.get('replan_count', 0)}")
    print(f"  Feedback : {'✓ sent' if final.get('feedback_sent') else '✗'}")
    print("═"*70 + "\n")


if __name__ == "__main__":
    asyncio.run(main())
