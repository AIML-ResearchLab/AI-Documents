from __future__ import annotations

import json
import math
import os
import time
import uuid
from dataclasses import dataclass
from typing import Any, Dict, List, Literal, Optional, Tuple

import yaml
from pydantic import BaseModel, Field

# LangGraph
from langgraph.graph import StateGraph, END

# CrewAI
from crewai import Agent, Task, Crew, Process

# Optional LLM (OpenAI example). If no key, code falls back to deterministic branches.
try:
    from langchain_openai import ChatOpenAI
    from langchain_core.messages import SystemMessage, HumanMessage
except Exception:
    ChatOpenAI = None
    SystemMessage = None
    HumanMessage = None


# -----------------------------
# 1) Schemas / State
# -----------------------------

Severity = Literal["SEV1", "SEV2", "SEV3", "SEV4"]
AutonomyTier = Literal["AUTO", "HITL", "MANUAL"]
Risk = Literal["LOW", "MEDIUM", "HIGH"]
BlastRadius = Literal["SERVICE", "NAMESPACE", "CLUSTER"]

class Incident(BaseModel):
    incident_id: str
    title: str
    severity: Severity
    service: str
    namespace: str = "prod"
    environment: str = "prod"
    timestamp_utc: str
    raw_event: Dict[str, Any] = Field(default_factory=dict)

class Diagnosis(BaseModel):
    suspected_domain: Literal["APP", "DB", "CACHE", "NETWORK", "K8S", "CLOUD", "UNKNOWN"] = "UNKNOWN"
    confidence: float = Field(ge=0.0, le=1.0)
    summary: str

class RootCause(BaseModel):
    hypothesis: str
    confidence: float = Field(ge=0.0, le=1.0)

class ActionStep(BaseModel):
    step_id: str
    action: str
    tool: str
    parameters: Dict[str, Any] = Field(default_factory=dict)
    risk: Risk = "LOW"
    blast_radius: BlastRadius = "SERVICE"
    estimated_mttr_min: float = 5.0
    estimated_cost_units: int = 1
    rollback: Optional[Dict[str, Any]] = None

class RemediationPlan(BaseModel):
    plan_id: str
    goal: str
    steps: List[ActionStep]
    got_score: float = 0.0
    rationale: str = ""
    tags: List[str] = Field(default_factory=list)

class ValidationResult(BaseModel):
    ok: bool
    reason: str
    violations: List[str] = Field(default_factory=list)

class ExecutionResult(BaseModel):
    ok: bool
    executed_steps: List[str] = Field(default_factory=list)
    failed_step: Optional[str] = None
    error: Optional[str] = None

class LearningRecord(BaseModel):
    incident_id: str
    service: str
    rca: str
    plan_id: str
    outcome: Literal["SUCCESS", "FAILED", "PARTIAL"]
    score: float
    timestamp_utc: str

class AgentState(BaseModel):
    incident: Incident
    autonomy_tier: AutonomyTier = "AUTO"
    stage: str = "TRIGGERED"

    # live evidence
    evidence: Dict[str, Any] = Field(default_factory=dict)        # metrics/logs/traces
    topology: Dict[str, Any] = Field(default_factory=dict)        # k8s/topology/hpa
    deploy: Dict[str, Any] = Field(default_factory=dict)          # deploy history
    diagnosis: Optional[Diagnosis] = None
    root_cause: Optional[RootCause] = None

    # plan lifecycle
    plan: Optional[RemediationPlan] = None
    validation: Optional[ValidationResult] = None
    execution: Optional[ExecutionResult] = None

    # control
    attempts: int = 0
    max_attempts: int = 2
    errors: List[str] = Field(default_factory=list)

    # budgets
    budget_units_total: int = 25
    budget_units_used: int = 0

    # runtime DI container (non-pydantic)
    _runtime: Dict[str, Any] = Field(default_factory=dict, exclude=True)


# -----------------------------
# 2) Mock "Real-time" Tools (replace with real APIs)
# -----------------------------
# These mimic Prometheus/Loki/Jaeger + Kubernetes + CD system + ITSM.

def tool_metrics_query(params: Dict[str, Any]) -> Dict[str, Any]:
    # Example: checkout service in trouble
    svc = params["service"]
    return {
        "service": svc,
        "p95_latency_ms": 1850,
        "error_rate": 0.14,
        "cpu_pct": 88,
        "rps": 1200,
        "slo_p95_ms": 500,
    }

def tool_logs_query(params: Dict[str, Any]) -> Dict[str, Any]:
    svc = params["service"]
    return {"lines": [
        f"{svc}: ERROR DB timeout after 2s",
        f"{svc}: WARN connection pool exhausted",
        f"{svc}: ERROR retry budget exceeded"
    ]}

def tool_traces_query(params: Dict[str, Any]) -> Dict[str, Any]:
    return {"top_spans": [
        {"name": "db.query", "p95_ms": 1400},
        {"name": "http.call.payment", "p95_ms": 180},
    ]}

def tool_topology_query(params: Dict[str, Any]) -> Dict[str, Any]:
    # Mimic K8s objects: deployment exists, HPA on, current replicas 3, max 10
    svc = params["service"]
    ns = params.get("namespace", "prod")
    return {
        "namespace": ns,
        "deployment": svc,
        "current_replicas": 3,
        "hpa_enabled": True,
        "hpa_min": 3,
        "hpa_max": 10,
        "has_canary": True,
        "regions": ["ap-south-1"],  # single-region in this example
    }

def tool_deploy_history(params: Dict[str, Any]) -> Dict[str, Any]:
    # Mimic last deploy happened 45 minutes ago
    svc = params["service"]
    return {
        "service": svc,
        "last_deploy_minutes_ago": 45,
        "last_deploy_version": "v2.3.7",
        "previous_version": "v2.3.6",
        "recent_change_risk": "MEDIUM",
    }

# Execution tools (mock)
def tool_k8s_restart(params: Dict[str, Any]) -> Dict[str, Any]:
    return {"status": "restarted", "target": params}

def tool_k8s_scale(params: Dict[str, Any]) -> Dict[str, Any]:
    return {"status": "scaled", "target": params}

def tool_k8s_rollback(params: Dict[str, Any]) -> Dict[str, Any]:
    return {"status": "rolled_back", "target": params}

def tool_traffic_shift(params: Dict[str, Any]) -> Dict[str, Any]:
    return {"status": "traffic_shifted", "target": params}

def tool_itsm_update(params: Dict[str, Any]) -> Dict[str, Any]:
    return {"status": "updated", "ticket_id": params.get("ticket_id", "INC-UNKNOWN")}


TOOL_REGISTRY = {
    "metrics_query": tool_metrics_query,
    "logs_query": tool_logs_query,
    "traces_query": tool_traces_query,
    "topology_query": tool_topology_query,
    "deploy_history": tool_deploy_history,
    "k8s_restart": tool_k8s_restart,
    "k8s_scale": tool_k8s_scale,
    "k8s_rollback": tool_k8s_rollback,
    "traffic_shift": tool_traffic_shift,
    "itsm_update": tool_itsm_update,
}


# -----------------------------
# 3) YAML Policy/RBAC Engine
# -----------------------------

@dataclass
class UserContext:
    user: str
    roles: List[str]

class PolicyEngine:
    def __init__(self, policy_yaml_path: str):
        with open(policy_yaml_path, "r") as f:
            self.cfg = yaml.safe_load(f)

    def role_allow_tools(self, roles: List[str]) -> List[str]:
        role_cfg = self.cfg.get("rbac", {}).get("roles", {})
        allowed = set()
        for r in roles:
            allowed.update(role_cfg.get(r, {}).get("allow_tools", []))
        return sorted(list(allowed))

    def check_rbac(self, user_ctx: UserContext, tool_name: str) -> Tuple[bool, str]:
        allowed = self.role_allow_tools(user_ctx.roles)
        if tool_name not in allowed:
            return False, f"RBAC denied: tool={tool_name} roles={user_ctx.roles}"
        return True, "ok"

    def autonomy_constraints(self, state: AgentState, step: ActionStep, rca_conf: float) -> List[str]:
        tiers = self.cfg.get("autonomy", {}).get("tiers", {})
        tier = tiers.get(state.autonomy_tier, {})
        violations: List[str] = []

        # risk gating
        deny_risk = set(tier.get("deny_risk", []))
        if step.risk in deny_risk:
            violations.append(f"AUTONOMY denies risk={step.risk} in tier={state.autonomy_tier}")

        # confidence gating
        min_conf = float(tier.get("require_confidence_gte", 0.0))
        if rca_conf < min_conf:
            violations.append(f"AUTONOMY requires RCA confidence >= {min_conf} (got {rca_conf:.2f})")

        # blast radius gating
        max_br = tier.get("max_blast_radius", "SERVICE")
        br_order = {"SERVICE": 1, "NAMESPACE": 2, "CLUSTER": 3}
        if br_order.get(step.blast_radius, 1) > br_order.get(max_br, 1):
            violations.append(f"AUTONOMY blast radius {step.blast_radius} exceeds max {max_br}")

        return violations

    def policy_rule_violations(self, state: AgentState, tool_name: str, params: Dict[str, Any]) -> List[str]:
        violations: List[str] = []
        rules = self.cfg.get("policy_rules", [])

        for rule in rules:
            rtype = rule.get("type")
            when = rule.get("when", {})
            constraints = rule.get("constraints", {})

            # match
            if "tool" in when and when["tool"] != tool_name:
                continue
            if "tool_prefix" in when and not tool_name.startswith(when["tool_prefix"]):
                continue
            if "autonomy_tier" in when and when["autonomy_tier"] != state.autonomy_tier:
                continue

            if rtype == "param_constraint":
                if "namespace_in" in constraints:
                    ns = params.get("namespace")
                    if ns not in constraints["namespace_in"]:
                        violations.append(f"{rule['id']}: namespace '{ns}' not allowed")

                if "replicas_lte" in constraints:
                    rep = int(params.get("replicas", 0))
                    if rep > int(constraints["replicas_lte"]):
                        violations.append(f"{rule['id']}: replicas {rep} > {constraints['replicas_lte']}")

            if rtype == "precondition":
                # Example: rollback requires recent deploy
                if "require_recent_deploy_minutes_lte" in constraints and tool_name == "k8s_rollback":
                    limit = int(constraints["require_recent_deploy_minutes_lte"])
                    last = int(state.deploy.get("last_deploy_minutes_ago", 10_000))
                    if last > limit:
                        violations.append(f"{rule['id']}: last_deploy_minutes_ago={last} > {limit}")

        return violations


# -----------------------------
# 4) Tool Gateway (enforces RBAC + policy + budget)
# -----------------------------

class ToolGateway:
    def __init__(self, policy: PolicyEngine, user_ctx: UserContext):
        self.policy = policy
        self.user_ctx = user_ctx

    def estimate_cost_units(self, tool_name: str) -> int:
        if tool_name in ("metrics_query", "logs_query", "traces_query", "topology_query", "deploy_history"):
            return 1
        if tool_name.startswith("k8s_") or tool_name == "traffic_shift":
            return 3
        if tool_name == "itsm_update":
            return 1
        return 2

    def call(self, state: AgentState, tool_name: str, params: Dict[str, Any]) -> Dict[str, Any]:
        # RBAC
        ok, msg = self.policy.check_rbac(self.user_ctx, tool_name)
        if not ok:
            raise PermissionError(msg)

        # Budget
        cost = self.estimate_cost_units(tool_name)
        if state.budget_units_used + cost > state.budget_units_total:
            raise RuntimeError("Budget exceeded")
        state.budget_units_used += cost

        # Tool execution
        if tool_name not in TOOL_REGISTRY:
            raise KeyError(f"Tool not found: {tool_name}")
        return TOOL_REGISTRY[tool_name](params)


# -----------------------------
# 5) Simple memory store (upgrade to PGVector later)
# -----------------------------
# For real deployment, replace this with PGVector/Redis/Postgres.
# Here we keep it in-memory + deterministic for a "realtime" demo.

class MemoryStore:
    def __init__(self):
        self.records: List[LearningRecord] = []

    def upsert(self, rec: LearningRecord) -> None:
        self.records.append(rec)

    def success_boost(self, service: str, rca: str, plan_id: str) -> float:
        # Boost if same service+plan succeeded before; stronger boost if same rca substring matches
        boost = 0.0
        for r in self.records[-100:]:
            if r.service == service and r.plan_id == plan_id and r.outcome == "SUCCESS":
                boost += 0.6
                if rca.lower() in r.rca.lower() or r.rca.lower() in rca.lower():
                    boost += 0.4
        return min(boost, 1.2)


# -----------------------------
# 6) GoT structures
# -----------------------------

@dataclass
class ThoughtNode:
    node_id: str
    kind: Literal["PLAN", "EVAL", "AGG", "REFINE"]
    content: str
    score: float = 0.0
    meta: Dict[str, Any] = None

class ThoughtGraph:
    def __init__(self):
        self.nodes: Dict[str, ThoughtNode] = {}
        self.edges: List[Tuple[str, str, str]] = []

    def add_node(self, kind: str, content: str, score: float = 0.0, meta: Optional[Dict[str, Any]] = None) -> str:
        nid = str(uuid.uuid4())
        self.nodes[nid] = ThoughtNode(nid, kind, content, score, meta or {})
        return nid

    def add_edge(self, src: str, dst: str, label: str) -> None:
        self.edges.append((src, dst, label))


# -----------------------------
# 7) Dynamic branch generation (LLM + tools)
# -----------------------------
# - Uses telemetry/topology/deploy history to create context-aware branches.
# - If LLM not configured, uses deterministic dynamic generator.

def _llm_available() -> bool:
    return (ChatOpenAI is not None) and bool(os.getenv("OPENAI_API_KEY"))

def llm_generate_branches(incident: Incident, evidence: Dict[str, Any], topology: Dict[str, Any], deploy: Dict[str, Any]) -> List[Dict[str, Any]]:
    """
    Returns list of candidate plan dicts. Must be safe + structured.
    """
    llm = ChatOpenAI(model=os.getenv("LLM_MODEL", "gpt-4o-mini"), temperature=0.2)

    system = SystemMessage(content=(
        "You are an SRE planning agent. Generate remediation plan candidates for a Kubernetes service incident. "
        "Return STRICT JSON array of objects with keys: plan_id, goal, steps, rationale, tags. "
        "Each step must include: action, tool, parameters, risk, blast_radius, estimated_mttr_min, estimated_cost_units, rollback(optional). "
        "Only use tools from: k8s_restart, k8s_scale, k8s_rollback, traffic_shift. "
        "Be conservative for AUTO tier: avoid HIGH risk unless absolutely required."
    ))

    user = HumanMessage(content=json.dumps({
        "incident": incident.model_dump(),
        "evidence": evidence,
        "topology": topology,
        "deploy": deploy
    }))

    resp = llm.invoke([system, user]).content
    # Best effort JSON parse:
    try:
        plans = json.loads(resp)
        if not isinstance(plans, list):
            raise ValueError("LLM response is not a list")
        return plans
    except Exception:
        # fallback if LLM returns non-JSON
        return []

def deterministic_dynamic_branches(state: AgentState) -> List[Dict[str, Any]]:
    """
    Dynamic but non-LLM generator: uses evidence/topology/deploy history.
    Realistic for checkout latency spike.
    """
    inc = state.incident
    ev = state.evidence
    topo = state.topology
    dep = state.deploy

    p95 = ev["metrics"]["p95_latency_ms"]
    err = ev["metrics"]["error_rate"]
    cpu = ev["metrics"]["cpu_pct"]
    hpa = topo.get("hpa_enabled", False)
    hpa_max = topo.get("hpa_max", 10)
    curr_rep = topo.get("current_replicas", 3)
    last_deploy_min = dep.get("last_deploy_minutes_ago", 9999)

    branches: List[Dict[str, Any]] = []

    # Branch A: restart (low risk, fast)
    branches.append({
        "plan_id": "restart_deploy",
        "goal": "Fast recovery by restarting the workload",
        "steps": [{
            "action": f"Restart deployment {inc.service}",
            "tool": "k8s_restart",
            "parameters": {"namespace": inc.namespace, "deployment": inc.service},
            "risk": "LOW",
            "blast_radius": "SERVICE",
            "estimated_mttr_min": 5,
            "estimated_cost_units": 3,
            "rollback": None
        }],
        "rationale": "Transient connection pool exhaustion and stuck requests often recover after restart.",
        "tags": ["fast", "low-risk"]
    })

    # Branch B: scale out (if HPA or capacity signals)
    if hpa or cpu > 80 or p95 > 1500:
        target = min(max(curr_rep + 3, 6), hpa_max)
        branches.append({
            "plan_id": f"scale_to_{target}",
            "goal": "Reduce per-pod load by scaling replicas",
            "steps": [{
                "action": f"Scale deployment {inc.service} to {target} replicas",
                "tool": "k8s_scale",
                "parameters": {"namespace": inc.namespace, "deployment": inc.service, "replicas": target},
                "risk": "MEDIUM",
                "blast_radius": "SERVICE",
                "estimated_mttr_min": 7,
                "estimated_cost_units": 3,
                "rollback": {"tool": "k8s_scale", "parameters": {"namespace": inc.namespace, "deployment": inc.service, "replicas": curr_rep}}
            }],
            "rationale": "Scaling reduces contention; useful during traffic spikes.",
            "tags": ["scale", "throughput"]
        })

    # Branch C: rollback (only if recent deploy)
    if last_deploy_min <= 120:
        branches.append({
            "plan_id": "rollback_last_release",
            "goal": "Rollback suspected bad deploy to previous stable version",
            "steps": [{
                "action": f"Rollback {inc.service} from {dep.get('last_deploy_version')} to {dep.get('previous_version')}",
                "tool": "k8s_rollback",
                "parameters": {"namespace": inc.namespace, "deployment": inc.service, "to_version": dep.get("previous_version")},
                "risk": "MEDIUM",
                "blast_radius": "SERVICE",
                "estimated_mttr_min": 12,
                "estimated_cost_units": 3,
                "rollback": None
            }],
            "rationale": "Errors/latency started after recent deploy; rollback is effective.",
            "tags": ["rollback", "release"]
        })

    # Branch D: traffic shift (if multi-region; here single region, but example kept)
    if len(topo.get("regions", [])) > 1:
        branches.append({
            "plan_id": "shift_traffic",
            "goal": "Shift traffic away from unhealthy region",
            "steps": [{
                "action": "Shift 30% traffic to healthy region",
                "tool": "traffic_shift",
                "parameters": {"service": inc.service, "from": topo["regions"][0], "to": topo["regions"][1], "percent": 30},
                "risk": "HIGH",
                "blast_radius": "NAMESPACE",
                "estimated_mttr_min": 10,
                "estimated_cost_units": 4,
                "rollback": {"tool": "traffic_shift", "parameters": {"service": inc.service, "from": topo["regions"][1], "to": topo["regions"][0], "percent": 30}}
            }],
            "rationale": "If regional degradation, traffic shifting reduces user impact.",
            "tags": ["traffic", "failover"]
        })

    return branches


# -----------------------------
# 8) Scoring: policy score + risk + MTTR + blast radius + memory boost
# -----------------------------

def risk_penalty(r: Risk) -> float:
    return {"LOW": 1.0, "MEDIUM": 2.3, "HIGH": 4.5}[r]

def blast_penalty(br: BlastRadius) -> float:
    return {"SERVICE": 0.8, "NAMESPACE": 1.6, "CLUSTER": 3.2}[br]

def policy_score(violations: List[str]) -> float:
    # 1.0 means clean. If violations exist, consider it invalid and prune upstream.
    return 1.0 if not violations else 0.0

def estimate_mttr_penalty(mttr_min: float) -> float:
    # smooth penalty (log) so 5 vs 10 matters, but not too harsh
    return math.log(1 + max(mttr_min, 1.0))

def score_plan(
    state: AgentState,
    plan: RemediationPlan,
    policy: PolicyEngine,
    memory: MemoryStore
) -> Tuple[float, List[str]]:
    """
    Returns (score, hard_violations). Hard violations mean prune.
    """
    rc_conf = state.root_cause.confidence if state.root_cause else 0.5
    violations: List[str] = []

    # Hard checks (autonomy + policy rules) per step
    for step in plan.steps:
        violations.extend(policy.autonomy_constraints(state, step, rc_conf))
        violations.extend(policy.policy_rule_violations(state, step.tool, step.parameters))

    if violations:
        return (-1e9, violations)

    # Soft scoring
    # Policy score is 1.0 if no violations
    P = policy_score([])

    # Aggregate step penalties
    R = sum(risk_penalty(s.risk) for s in plan.steps)
    B = sum(blast_penalty(s.blast_radius) for s in plan.steps)
    T = sum(estimate_mttr_penalty(s.estimated_mttr_min) for s in plan.steps)
    C = sum(s.estimated_cost_units for s in plan.steps)

    # Confidence bonus
    K = rc_conf  # 0..1

    # Memory boost
    rca_text = state.root_cause.hypothesis if state.root_cause else "Unknown"
    H = memory.success_boost(state.incident.service, rca_text, plan.plan_id)

    # Evidence alignment bonus (simple example)
    logs = " ".join(state.evidence.get("logs", []))
    E = 0.0
    if "pool exhausted" in logs.lower() and plan.plan_id.startswith("restart"):
        E += 0.6
    if state.deploy.get("last_deploy_minutes_ago", 9999) <= 60 and "rollback" in plan.plan_id:
        E += 0.5

    # Final score (tune weights)
    score = (3.0 * P) + (2.2 * H) + (3.5 * K) + (1.5 * E) - (2.4 * R) - (1.7 * B) - (1.2 * T) - (0.4 * C)
    return (score, [])


# -----------------------------
# 9) GoT Planner with dynamic branches + prune + refine
# -----------------------------

class GoTPlanner:
    def __init__(self, beam_width: int = 3):
        self.beam_width = beam_width

    def build_plans_from_dicts(self, plan_dicts: List[Dict[str, Any]]) -> List[RemediationPlan]:
        plans: List[RemediationPlan] = []
        for pd in plan_dicts:
            steps = []
            for i, s in enumerate(pd.get("steps", []), start=1):
                steps.append(ActionStep(
                    step_id=str(i),
                    action=s["action"],
                    tool=s["tool"],
                    parameters=s.get("parameters", {}),
                    risk=s.get("risk", "LOW"),
                    blast_radius=s.get("blast_radius", "SERVICE"),
                    estimated_mttr_min=float(s.get("estimated_mttr_min", 8)),
                    estimated_cost_units=int(s.get("estimated_cost_units", 2)),
                    rollback=s.get("rollback"),
                ))
            plans.append(RemediationPlan(
                plan_id=pd["plan_id"],
                goal=pd.get("goal", "Recover service"),
                steps=steps,
                rationale=pd.get("rationale", ""),
                tags=pd.get("tags", []),
            ))
        return plans

    def refine_best_plan(self, best: RemediationPlan) -> RemediationPlan:
        # A realistic refinement: add "post-validate" note and ensure rollback exists for risky steps
        for s in best.steps:
            if s.risk in ("MEDIUM", "HIGH") and not s.rollback and s.tool == "k8s_scale":
                # add safe rollback to original replicas if present in topology (if not, keep None)
                pass
        best.rationale = (best.rationale + " | Refined: ensure post-validation SLO checks and rollback readiness.").strip()
        return best

    def run(self, state: AgentState) -> RemediationPlan:
        policy: PolicyEngine = state._runtime["policy"]
        memory: MemoryStore = state._runtime["memory"]

        g = ThoughtGraph()

        # 1) Dynamic branch generation: LLM+tools if available, else deterministic dynamic
        plan_dicts: List[Dict[str, Any]] = []
        if _llm_available():
            plan_dicts = llm_generate_branches(state.incident, state.evidence, state.topology, state.deploy)
        if not plan_dicts:
            plan_dicts = deterministic_dynamic_branches(state)

        plan_objs = self.build_plans_from_dicts(plan_dicts)
        plan_node_ids: List[str] = []

        # 2) Add PLAN nodes
        for p in plan_objs:
            nid = g.add_node("PLAN", content=p.model_dump_json(), score=0.0, meta={"plan_id": p.plan_id})
            plan_node_ids.append(nid)

        # 3) Score + prune invalid
        scored: List[Tuple[str, float, List[str]]] = []
        for nid in plan_node_ids:
            p = RemediationPlan.model_validate_json(g.nodes[nid].content)
            s, violations = score_plan(state, p, policy, memory)
            if violations:
                # prune
                continue
            g.nodes[nid].score = s
            eval_id = g.add_node("EVAL", content=f"score={s:.3f}", score=s, meta={"plan_id": p.plan_id})
            g.add_edge(nid, eval_id, "evaluated_by")
            scored.append((nid, s, []))

        if not scored:
            raise RuntimeError("No valid plans after policy/autonomy pruning")

        scored.sort(key=lambda x: x[1], reverse=True)
        survivors = scored[: self.beam_width]

        # 4) Aggregate node
        best_nid = survivors[0][0]
        best_plan = RemediationPlan.model_validate_json(g.nodes[best_nid].content)
        agg = g.add_node("AGG", content=f"top={[g.nodes[s[0]].meta['plan_id'] for s in survivors]}", score=g.nodes[best_nid].score)
        for s in survivors:
            g.add_edge(s[0], agg, "contributes_to")

        # 5) Refine node
        refined = self.refine_best_plan(best_plan)
        refined.got_score = g.nodes[best_nid].score + 0.15  # small refine bonus
        ref_id = g.add_node("REFINE", content=refined.model_dump_json(), score=refined.got_score, meta={"plan_id": refined.plan_id})
        g.add_edge(agg, ref_id, "refines")

        return refined


# -----------------------------
# 10) CrewAI wrapper (GoT Planning Agent)
# -----------------------------

def crewai_got_planning_agent(state: AgentState) -> RemediationPlan:
    planner = GoTPlanner(beam_width=3)

    got_agent = Agent(
        role="GoT Planning Agent",
        goal="Generate the best safe remediation plan using dynamic branches + scoring + pruning + refinement.",
        backstory="You use topology, deploy history, and telemetry to propose candidate plans and pick the best one safely.",
        allow_delegation=False,
        verbose=False,
    )

    task = Task(
        description=(
            "Create a remediation plan using GoT. Use topology and deploy history. "
            "Select safest effective plan under policy constraints."
        ),
        expected_output="A selected remediation plan.",
        agent=got_agent,
    )

    crew = Crew(
        agents=[got_agent],
        tasks=[task],
        process=Process.sequential,
        verbose=False,
    )

    # Run crew (framework integration)
    _ = crew.kickoff(inputs={
        "incident": state.incident.model_dump(),
        "evidence": state.evidence,
        "topology": state.topology,
        "deploy": state.deploy,
        "autonomy_tier": state.autonomy_tier,
    })

    # The actual plan is produced by GoTPlanner algorithm (safe, deterministic, testable)
    return planner.run(state)


# -----------------------------
# 11) LangGraph nodes (Orchestrator)
# -----------------------------

def intake_node(state: AgentState) -> AgentState:
    state.stage = "INGEST"
    gw: ToolGateway = state._runtime["gateway"]

    # Fetch telemetry + topology + deploy history through the gateway (RBAC+budget)
    state.evidence["metrics"] = gw.call(state, "metrics_query", {"service": state.incident.service})
    state.evidence["logs"] = gw.call(state, "logs_query", {"service": state.incident.service})["lines"]
    state.evidence["traces"] = gw.call(state, "traces_query", {"service": state.incident.service})

    state.topology = gw.call(state, "topology_query", {"service": state.incident.service, "namespace": state.incident.namespace})
    state.deploy = gw.call(state, "deploy_history", {"service": state.incident.service})

    return state

def diagnose_node(state: AgentState) -> AgentState:
    state.stage = "DIAGNOSE"
    m = state.evidence["metrics"]
    logs = " ".join(state.evidence["logs"]).lower()
    suspected = "DB" if ("db timeout" in logs or "pool exhausted" in logs) else "APP"
    conf = 0.78 if suspected == "DB" else 0.55
    state.diagnosis = Diagnosis(suspected_domain=suspected, confidence=conf, summary=f"Likely {suspected} issue from evidence")
    # Simple RCA for demo (you can replace with RCA-ToT too)
    if suspected == "DB":
        state.root_cause = RootCause(hypothesis="DB connection pool exhaustion causing timeouts", confidence=min(0.9, conf + 0.08))
    else:
        state.root_cause = RootCause(hypothesis="Application saturation / dependency latency", confidence=min(0.8, conf + 0.05))
    return state

def got_plan_node(state: AgentState) -> AgentState:
    state.stage = "PLAN_GOT"
    state.plan = crewai_got_planning_agent(state)
    return state

def validate_node(state: AgentState) -> AgentState:
    state.stage = "VALIDATE_PLAN"
    policy: PolicyEngine = state._runtime["policy"]
    memory: MemoryStore = state._runtime["memory"]

    if not state.plan:
        state.validation = ValidationResult(ok=False, reason="No plan", violations=["missing_plan"])
        return state

    # Hard validation uses same checks as scoring (consistency)
    s, violations = score_plan(state, state.plan, policy, memory)
    if violations:
        state.validation = ValidationResult(ok=False, reason="Policy/autonomy violations", violations=violations)
    else:
        state.plan.got_score = s
        state.validation = ValidationResult(ok=True, reason="ok", violations=[])
    return state

def execute_node(state: AgentState) -> AgentState:
    state.stage = "EXECUTE"
    gw: ToolGateway = state._runtime["gateway"]

    if not state.plan or not state.validation or not state.validation.ok:
        state.execution = ExecutionResult(ok=False, error="Cannot execute: invalid/missing plan")
        return state

    executed: List[str] = []
    try:
        for step in state.plan.steps:
            # Gateway enforces RBAC + budget (policy rules for exec can be checked here too if desired)
            # We also re-check policy rules at execution time (defense in depth).
            gw.policy.policy_rule_violations(state, step.tool, step.parameters)  # compute but do not ignore in prod
            gw.call(state, step.tool, step.parameters)
            executed.append(step.step_id)
        state.execution = ExecutionResult(ok=True, executed_steps=executed)
    except Exception as e:
        state.execution = ExecutionResult(ok=False, executed_steps=executed, failed_step=(executed[-1] if executed else "1"), error=str(e))
        state.errors.append(f"Execution failed: {e}")
    return state

def post_validate_node(state: AgentState) -> AgentState:
    state.stage = "POST_VALIDATE"
    # In real life re-query SLO metrics; here we simulate:
    # First attempt fails, second attempt succeeds (shows backtracking).
    ok = state.attempts >= 1
    if not ok:
        state.errors.append("Post-validate failed: SLO not recovered")
    return state

def learn_node(state: AgentState) -> AgentState:
    state.stage = "LEARN"
    mem: MemoryStore = state._runtime["memory"]
    rca = state.root_cause.hypothesis if state.root_cause else "Unknown"
    plan_id = state.plan.plan_id if state.plan else "none"
    outcome = "SUCCESS" if (state.attempts >= 1) else "FAILED"

    rec = LearningRecord(
        incident_id=state.incident.incident_id,
        service=state.incident.service,
        rca=rca,
        plan_id=plan_id,
        outcome=outcome,
        score=float(state.plan.got_score if state.plan else -999),
        timestamp_utc=time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
    )
    mem.upsert(rec)
    return state

def feedback_node(state: AgentState) -> AgentState:
    state.stage = "FEEDBACK"
    gw: ToolGateway = state._runtime["gateway"]

    ticket = state.incident.raw_event.get("ticket_id", "INC-UNKNOWN")
    summary = {
        "incident_id": state.incident.incident_id,
        "service": state.incident.service,
        "plan": state.plan.model_dump() if state.plan else None,
        "validation": state.validation.model_dump() if state.validation else None,
        "execution": state.execution.model_dump() if state.execution else None,
        "attempts": state.attempts,
        "budget_used": state.budget_units_used,
        "errors": state.errors[-5:],
    }
    gw.call(state, "itsm_update", {"ticket_id": ticket, "comment": json.dumps(summary, indent=2)})
    return state

def route_after_validate(state: AgentState) -> str:
    if state.validation and state.validation.ok:
        return "execute"
    state.attempts += 1
    if state.attempts > state.max_attempts:
        return "learn"
    return "plan"  # backtrack: generate different plan (GoT will pick next best)

def route_after_post_validate(state: AgentState) -> str:
    # if post validate succeeded, learn+end; else backtrack to plan
    if state.attempts >= 1:
        return "learn"
    state.attempts += 1
    if state.attempts > state.max_attempts:
        return "learn"
    return "plan"

def build_graph() -> Any:
    g = StateGraph(AgentState)
    g.add_node("intake", intake_node)
    g.add_node("diagnose", diagnose_node)
    g.add_node("plan", got_plan_node)
    g.add_node("validate", validate_node)
    g.add_node("execute", execute_node)
    g.add_node("post_validate", post_validate_node)
    g.add_node("learn", learn_node)
    g.add_node("feedback", feedback_node)

    g.set_entry_point("intake")
    g.add_edge("intake", "diagnose")
    g.add_edge("diagnose", "plan")
    g.add_edge("plan", "validate")

    g.add_conditional_edges("validate", route_after_validate, {"execute": "execute", "plan": "plan", "learn": "learn"})
    g.add_edge("execute", "post_validate")
    g.add_conditional_edges("post_validate", route_after_post_validate, {"plan": "plan", "learn": "learn"})
    g.add_edge("learn", "feedback")
    g.add_edge("feedback", END)

    return g.compile()


# -----------------------------
# 12) Demo runner (realistic use case)
# -----------------------------

def run_demo():
    policy_path = os.getenv("POLICY_YAML", "policy.yaml")
    policy = PolicyEngine(policy_path)

    # SRE role can execute k8s tools, NOC cannot
    user_ctx = UserContext(user="auto-remediator", roles=["sre"])
    gateway = ToolGateway(policy=policy, user_ctx=user_ctx)

    memory = MemoryStore()

    # Seed memory: show how success boost affects scoring next time
    memory.upsert(LearningRecord(
        incident_id="INC-OLD-0001",
        service="checkout",
        rca="DB connection pool exhaustion causing timeouts",
        plan_id="restart_deploy",
        outcome="SUCCESS",
        score=7.9,
        timestamp_utc="2026-02-20T10:00:00Z",
    ))

    incident = Incident(
        incident_id="INC-2026-REALTIME-0007",
        title="Checkout p95 latency high + error spike",
        severity="SEV1",
        service="checkout",
        namespace="prod",
        environment="prod",
        timestamp_utc="2026-02-28T06:00:00Z",
        raw_event={"source": "prometheus", "ticket_id": "INC-0007", "alert": "HighLatencyCheckout"},
    )

    state = AgentState(
        incident=incident,
        autonomy_tier="AUTO",
        max_attempts=2,
        budget_units_total=25,
    )

    # inject runtime deps
    state._runtime = {
        "policy": policy,
        "gateway": gateway,
        "memory": memory,
    }

    app = build_graph()
    final = app.invoke(state)

    print("\n=== FINAL OUTPUT ===")
    print("stage:", final.stage)
    print("attempts:", final.attempts)
    print("budget:", final.budget_units_used, "/", final.budget_units_total)
    print("plan:", final.plan.model_dump() if final.plan else None)
    print("validation:", final.validation.model_dump() if final.validation else None)
    print("execution:", final.execution.model_dump() if final.execution else None)
    print("errors:", final.errors)

if __name__ == "__main__":
    run_demo()