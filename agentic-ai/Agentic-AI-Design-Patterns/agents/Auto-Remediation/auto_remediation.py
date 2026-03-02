"""
End-to-end Agentic AI Incident Auto-Remediation
- LangGraph orchestration (state machine)
- True ToT planner (branching + scoring + pruning)
- OpenTelemetry spans per node + per tool call
- PGVector learning memory (incident->plan->outcome)
- Policy/RBAC from YAML with evaluation engine

Core references:
- LangGraph StateGraph compile/invoke docs: https://docs.langchain.com/oss/python/langgraph/graph-api
- PGVectorStore (langchain-postgres): https://docs.langchain.com/oss/python/integrations/vectorstores/pgvectorstore
"""

from __future__ import annotations

import os
import json
import time
import uuid
from dataclasses import dataclass
from typing import Any, Dict, List, Literal, Optional, Tuple

import yaml
from pydantic import BaseModel, Field

from langgraph.graph import StateGraph, END

# Optional LLM (plug your model/provider)
try:
    from langchain_openai import ChatOpenAI
    from langchain_core.messages import SystemMessage, HumanMessage
except Exception:
    ChatOpenAI = None
    SystemMessage = HumanMessage = None

# PGVector (LangChain Postgres integration)
# Docs: PGVectorStore lives in langchain-postgres integration package.
try:
    from langchain_postgres import PGVector
    from langchain_openai import OpenAIEmbeddings
except Exception:
    PGVector = None
    OpenAIEmbeddings = None

# OpenTelemetry
from opentelemetry import trace
from opentelemetry.trace import SpanKind
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace.export import BatchSpanProcessor

# Choose ONE exporter:
# 1) OTLP gRPC exporter (Tempo/Jaeger/OTel Collector)
try:
    from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
except Exception:
    OTLPSpanExporter = None


# ----------------------------
# 1) Schemas
# ----------------------------

Severity = Literal["SEV1", "SEV2", "SEV3", "SEV4"]
Stage = Literal[
    "TRIGGERED",
    "DIAGNOSED",
    "RCA_DONE",
    "PLAN_READY",
    "PLAN_VALIDATED",
    "EXECUTED",
    "POST_VALIDATED",
    "LEARNED",
    "REPORTED",
    "ENDED",
    "ESCALATED",
]

class Incident(BaseModel):
    incident_id: str
    title: str
    severity: Severity
    service: str
    environment: str = "prod"
    timestamp_utc: str
    raw_event: Dict[str, Any] = Field(default_factory=dict)

class Evidence(BaseModel):
    metrics: Dict[str, Any] = Field(default_factory=dict)
    logs: List[str] = Field(default_factory=list)
    traces: Dict[str, Any] = Field(default_factory=dict)
    top_signals: List[str] = Field(default_factory=list)

class Diagnosis(BaseModel):
    summary: str
    confidence: float = Field(ge=0.0, le=1.0)
    suspected_domain: Literal["APP", "DB", "CACHE", "NETWORK", "K8S", "CLOUD", "UNKNOWN"] = "UNKNOWN"
    missing_data: List[str] = Field(default_factory=list)

class RootCause(BaseModel):
    hypothesis: str
    confidence: float = Field(ge=0.0, le=1.0)
    contributing_factors: List[str] = Field(default_factory=list)

class ActionStep(BaseModel):
    step_id: str
    action: str
    tool: str
    parameters: Dict[str, Any] = Field(default_factory=dict)
    estimated_risk: Literal["LOW", "MEDIUM", "HIGH"] = "LOW"
    estimated_cost_units: int = 1
    rollback: Optional[Dict[str, Any]] = None

class RemediationPlan(BaseModel):
    plan_id: str
    goal: str
    steps: List[ActionStep]
    assumptions: List[str] = Field(default_factory=list)
    tot_score: float = 0.0  # filled by ToT scoring

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
    plan_id: str
    outcome: Literal["SUCCESS", "FAILED", "PARTIAL"]
    score: float
    root_cause: str
    what_worked: List[str] = Field(default_factory=list)
    what_failed: List[str] = Field(default_factory=list)
    notes: List[str] = Field(default_factory=list)

class Feedback(BaseModel):
    itsm_comment: str
    summary: str
    next_actions: List[str] = Field(default_factory=list)

class AgentState(BaseModel):
    incident: Incident
    stage: Stage = "TRIGGERED"

    evidence: Evidence = Field(default_factory=Evidence)
    diagnosis: Optional[Diagnosis] = None
    root_cause: Optional[RootCause] = None
    plan: Optional[RemediationPlan] = None

    plan_validation: Optional[ValidationResult] = None
    execution: Optional[ExecutionResult] = None
    post_validation: Optional[ValidationResult] = None
    learning: Optional[LearningRecord] = None
    feedback: Optional[Feedback] = None

    attempts: int = 0
    max_attempts: int = 2
    autonomy_tier: Literal["AUTO", "HITL", "MANUAL"] = "AUTO"
    errors: List[str] = Field(default_factory=list)

    budget_units_total: int = 20
    budget_units_used: int = 0


# ----------------------------
# 2) OpenTelemetry setup
# ----------------------------

def setup_tracing(service_name: str = "incident-remediator") -> None:
    resource = Resource.create({"service.name": service_name})
    provider = TracerProvider(resource=resource)
    trace.set_tracer_provider(provider)

    if OTLPSpanExporter is None:
        # No exporter installed; spans will be no-op exported
        return

    # OTLP exporter endpoint example: http://localhost:4317
    endpoint = os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT", "http://localhost:4317")
    exporter = OTLPSpanExporter(endpoint=endpoint, insecure=True)
    processor = BatchSpanProcessor(exporter)
    provider.add_span_processor(processor)

TRACER = trace.get_tracer(__name__)


# ----------------------------
# 3) Policy/RBAC engine from YAML
# ----------------------------

@dataclass
class UserContext:
    user: str
    roles: List[str]

class PolicyEngine:
    def __init__(self, policy_yaml_path: str):
        with open(policy_yaml_path, "r") as f:
            self.cfg = yaml.safe_load(f)

    def _role_allow_tools(self, roles: List[str]) -> List[str]:
        role_cfg = self.cfg.get("rbac", {}).get("roles", {})
        allowed = set()
        for r in roles:
            allowed.update(role_cfg.get(r, {}).get("allow_tools", []))
        return sorted(list(allowed))

    def check_rbac(self, user_ctx: UserContext, tool_name: str) -> Tuple[bool, str]:
        allowed = self._role_allow_tools(user_ctx.roles)
        if tool_name not in allowed:
            return False, f"RBAC: tool '{tool_name}' not allowed for roles={user_ctx.roles}"
        return True, "ok"

    def check_autonomy(self, state: AgentState, step: ActionStep, rca_conf: float) -> List[str]:
        violations = []
        tiers = self.cfg.get("autonomy", {}).get("tiers", {})
        tier_cfg = tiers.get(state.autonomy_tier, {})

        deny_risk = set(tier_cfg.get("deny_risk", []))
        if step.estimated_risk in deny_risk:
            violations.append(f"Autonomy '{state.autonomy_tier}' denies risk={step.estimated_risk}")

        min_conf = float(tier_cfg.get("require_confidence_gte", 0.0))
        if rca_conf < min_conf:
            violations.append(f"Autonomy '{state.autonomy_tier}' requires RCA confidence >= {min_conf}")
        return violations

    def check_policy_rules(self, state: AgentState, tool_name: str, params: Dict[str, Any]) -> List[str]:
        violations: List[str] = []
        rules = self.cfg.get("policy_rules", [])

        for rule in rules:
            rtype = rule.get("type")

            if rtype == "allowlist_tools":
                # Already enforced by RBAC allow_tools; keep here if you want global allowlist too
                continue

            if rtype == "param_constraint":
                when = rule.get("when", {})
                constraints = rule.get("constraints", {})

                # match conditions
                if "tool" in when and when["tool"] != tool_name:
                    continue
                if "tool_prefix" in when and not tool_name.startswith(when["tool_prefix"]):
                    continue
                if "autonomy_tier" in when and when["autonomy_tier"] != state.autonomy_tier:
                    continue

                # apply constraints
                if "replicas_lte" in constraints:
                    replicas = int(params.get("replicas", 0))
                    if replicas > int(constraints["replicas_lte"]):
                        violations.append(f"{rule['id']}: replicas {replicas} > {constraints['replicas_lte']}")

                if "namespace_in" in constraints:
                    ns = params.get("namespace")
                    if ns not in constraints["namespace_in"]:
                        violations.append(f"{rule['id']}: namespace '{ns}' not in {constraints['namespace_in']}")

        return violations


# ----------------------------
# 4) Tool Gateway (policy + budget + OTel spans)
# ----------------------------

class ToolGateway:
    def __init__(self, policy: PolicyEngine, user_ctx: UserContext):
        self.policy = policy
        self.user_ctx = user_ctx

    def estimate_cost_units(self, tool_name: str, params: Dict[str, Any]) -> int:
        if tool_name in ("metrics_query", "logs_query", "traces_query"):
            return 1
        if tool_name.startswith("k8s_") or tool_name.startswith("cloud_"):
            return 3
        if tool_name == "itsm_update":
            return 1
        return 2

    def call(self, state: AgentState, tool_name: str, params: Dict[str, Any]) -> Dict[str, Any]:
        with TRACER.start_as_current_span(f"tool:{tool_name}", kind=SpanKind.INTERNAL) as span:
            span.set_attribute("tool.name", tool_name)
            span.set_attribute("incident.id", state.incident.incident_id)
            span.set_attribute("autonomy.tier", state.autonomy_tier)

            ok, msg = self.policy.check_rbac(self.user_ctx, tool_name)
            if not ok:
                span.set_attribute("policy.rbac_ok", False)
                raise PermissionError(msg)
            span.set_attribute("policy.rbac_ok", True)

            cost = self.estimate_cost_units(tool_name, params)
            if state.budget_units_used + cost > state.budget_units_total:
                span.set_attribute("budget.exceeded", True)
                raise RuntimeError("Budget exceeded")
            state.budget_units_used += cost
            span.set_attribute("budget.used", state.budget_units_used)

            # Execute tool
            out = TOOL_REGISTRY[tool_name](params)
            span.set_attribute("tool.ok", True)
            return out


# ----------------------------
# 5) Tools (mock examples; replace with real)
# ----------------------------

def tool_metrics_query(params: Dict[str, Any]) -> Dict[str, Any]:
    service = params.get("service")
    # pretend current metrics
    return {"service": service, "p95_latency_ms": 1800, "error_rate": 0.12, "cpu_pct": 90}

def tool_logs_query(params: Dict[str, Any]) -> Dict[str, Any]:
    return {"lines": ["ERROR DB timeout", "WARN pool exhausted", "ERROR retry budget exceeded"]}

def tool_traces_query(params: Dict[str, Any]) -> Dict[str, Any]:
    return {"top_spans": [{"name": "db.query", "p95_ms": 1400}]}

def tool_k8s_restart(params: Dict[str, Any]) -> Dict[str, Any]:
    return {"status": "restarted", "target": params}

def tool_k8s_scale(params: Dict[str, Any]) -> Dict[str, Any]:
    return {"status": "scaled", "target": params}

def tool_itsm_update(params: Dict[str, Any]) -> Dict[str, Any]:
    return {"status": "updated", "ticket_id": params.get("ticket_id")}

TOOL_REGISTRY = {
    "metrics_query": tool_metrics_query,
    "logs_query": tool_logs_query,
    "traces_query": tool_traces_query,
    "k8s_restart": tool_k8s_restart,
    "k8s_scale": tool_k8s_scale,
    "itsm_update": tool_itsm_update,
}


# ----------------------------
# 6) PGVector learning memory
# ----------------------------

class LearningMemory:
    """
    Stores (incident -> plan -> outcome) as text + metadata in PGVector.
    Uses embeddings + similarity retrieval to influence ToT scoring.
    """
    def __init__(self, connection: str, collection: str = "incident_learning"):
        if PGVector is None or OpenAIEmbeddings is None:
            raise RuntimeError("Install langchain-postgres and langchain-openai for PGVector + embeddings.")
        self.emb = OpenAIEmbeddings(model=os.getenv("EMBED_MODEL", "text-embedding-3-large"))
        self.vs = PGVector(
            connection=connection,
            embeddings=self.emb,
            collection_name=collection,
            use_jsonb=True,
        )

    def upsert_learning(self, rec: LearningRecord) -> None:
        doc_text = json.dumps(rec.model_dump(), ensure_ascii=False)
        metadata = {
            "incident_id": rec.incident_id,
            "plan_id": rec.plan_id,
            "outcome": rec.outcome,
            "score": rec.score,
            "root_cause": rec.root_cause,
        }
        # add_texts inserts embeddings; id for traceability
        self.vs.add_texts([doc_text], metadatas=[metadata], ids=[str(uuid.uuid4())])

    def query_similar(self, incident: Incident, root_cause: RootCause, k: int = 5) -> List[Dict[str, Any]]:
        q = f"service={incident.service}; severity={incident.severity}; env={incident.environment}; rca={root_cause.hypothesis}"
        results = self.vs.similarity_search_with_score(q, k=k)
        out = []
        for doc, score in results:
            out.append({"text": doc.page_content, "metadata": doc.metadata, "score": float(score)})
        return out


# ----------------------------
# 7) True ToT planner (branching + scoring + pruning)
# ----------------------------

class ToTPlanner:
    def __init__(self, policy: PolicyEngine, beam_width: int = 3, max_depth: int = 2):
        self.policy = policy
        self.beam_width = beam_width
        self.max_depth = max_depth

    def generate_branches(self, state: AgentState) -> List[RemediationPlan]:
        """
        In production, this can be LLM-generated with structured output.
        Here we generate realistic candidate plans (branches).
        """
        svc = state.incident.service
        ns = "prod"

        branches: List[RemediationPlan] = [
            RemediationPlan(
                plan_id="restart_deploy",
                goal="Fast recovery by restarting deployment",
                steps=[
                    ActionStep(step_id="1", action=f"Restart deployment {svc}", tool="k8s_restart",
                               parameters={"namespace": ns, "deployment": svc}, estimated_risk="LOW", estimated_cost_units=3),
                ],
                assumptions=["restart clears stuck connections"],
            ),
            RemediationPlan(
                plan_id="scale_deploy_6",
                goal="Reduce load per pod by scaling out",
                steps=[
                    ActionStep(step_id="1", action=f"Scale deployment {svc} to 6", tool="k8s_scale",
                               parameters={"namespace": ns, "deployment": svc, "replicas": 6}, estimated_risk="MEDIUM", estimated_cost_units=3,
                               rollback={"tool": "k8s_scale", "parameters": {"namespace": ns, "deployment": svc, "replicas": 3}}),
                ],
                assumptions=["cluster has headroom"],
            ),
            RemediationPlan(
                plan_id="scale_deploy_12",
                goal="Aggressive scale for burst traffic",
                steps=[
                    ActionStep(step_id="1", action=f"Scale deployment {svc} to 12", tool="k8s_scale",
                               parameters={"namespace": ns, "deployment": svc, "replicas": 12}, estimated_risk="HIGH", estimated_cost_units=4),
                ],
                assumptions=["needed for extreme spike"],
            ),
        ]
        return branches

    def score_plan(
        self,
        state: AgentState,
        plan: RemediationPlan,
        similar_history: List[Dict[str, Any]] | None = None
    ) -> Tuple[float, List[str]]:
        """
        Score and also return any hard violations (prune if violations exist).
        """
        rc_conf = state.root_cause.confidence if state.root_cause else 0.2
        violations: List[str] = []

        # Hard checks: autonomy constraints + policy rules
        for step in plan.steps:
            violations.extend(self.policy.check_autonomy(state, step, rc_conf))
            violations.extend(self.policy.check_policy_rules(state, step.tool, step.parameters))

        if violations:
            return (-1e9, violations)  # prune

        # Soft scoring signals
        risk_penalty = {"LOW": 1.0, "MEDIUM": 2.5, "HIGH": 5.0}
        R = sum(risk_penalty[s.estimated_risk] for s in plan.steps)
        C = sum(s.estimated_cost_units for s in plan.steps)
        T = 1.5 if any(s.tool == "k8s_scale" for s in plan.steps) else 1.0  # heuristic time cost
        K = rc_conf

        # Historical boost (H): look for similar successes
        H = 0.0
        if similar_history:
            for r in similar_history:
                md = r.get("metadata", {})
                if md.get("outcome") == "SUCCESS" and md.get("plan_id") == plan.plan_id:
                    H += 0.5

        # Policy compliance is already hard-filtered; keep P as constant 1.0
        P = 1.0

        # Weighted score
        score = (3.0 * P) + (2.0 * H) + (4.0 * K) - (2.5 * R) - (1.5 * T) - (0.5 * C)
        return (score, [])

    def plan(self, state: AgentState, similar_history: List[Dict[str, Any]] | None = None) -> RemediationPlan:
        """
        Beam search ToT (depth-limited).
        For simplicity, branches are full plans already; in deeper ToT you expand step-by-step.
        """
        candidates = self.generate_branches(state)

        scored: List[RemediationPlan] = []
        for p in candidates:
            s, v = self.score_plan(state, p, similar_history)
            if v:
                continue  # prune
            p.tot_score = s
            scored.append(p)

        scored.sort(key=lambda x: x.tot_score, reverse=True)
        survivors = scored[: self.beam_width]

        if not survivors:
            raise RuntimeError("No valid plans after policy/autonomy pruning")

        # Depth expansion hook (optional): in max_depth>1, you would extend survivors with extra steps.
        # Keeping as-is for clean production skeleton.
        return survivors[0]


# ----------------------------
# 8) LangGraph nodes (agents) with OTel spans
# ----------------------------

def intake_agent(state: AgentState) -> AgentState:
    with TRACER.start_as_current_span("node:intake"):
        state.stage = "TRIGGERED"
        state.attempts = 0
        return state

def diagnosis_agent(state: AgentState) -> AgentState:
    with TRACER.start_as_current_span("node:diagnose") as span:
        gw: ToolGateway = state._runtime["gateway"]
        m = gw.call(state, "metrics_query", {"service": state.incident.service})
        l = gw.call(state, "logs_query", {"service": state.incident.service})
        t = gw.call(state, "traces_query", {"service": state.incident.service})

        state.evidence.metrics = m
        state.evidence.logs = l["lines"]
        state.evidence.traces = t
        state.evidence.top_signals = [
            f"p95_latency={m['p95_latency_ms']}ms",
            f"error_rate={m['error_rate']}",
            "db_timeout in logs",
            "pool exhausted in logs",
            "trace: db.query p95 high",
        ]

        suspected = "DB" if any("DB" in x or "db" in x.lower() for x in state.evidence.logs) else "APP"
        conf = 0.78 if suspected == "DB" else 0.55

        state.diagnosis = Diagnosis(
            summary=f"Likely {suspected} issue based on metrics/logs/traces",
            confidence=conf,
            suspected_domain=suspected,
            missing_data=["db_pool_metrics"] if suspected == "DB" else [],
        )
        state.stage = "DIAGNOSED"
        span.set_attribute("diagnosis.domain", suspected)
        span.set_attribute("diagnosis.confidence", conf)
        return state

def rca_agent(state: AgentState) -> AgentState:
    with TRACER.start_as_current_span("node:rca") as span:
        d = state.diagnosis
        if not d:
            state.root_cause = RootCause(hypothesis="Unknown", confidence=0.2)
        elif d.suspected_domain == "DB":
            state.root_cause = RootCause(
                hypothesis="DB connection pool exhaustion causing timeouts and cascading latency",
                confidence=min(0.88, d.confidence + 0.1),
                contributing_factors=["traffic spike", "pool too small", "slow queries"],
            )
        else:
            state.root_cause = RootCause(
                hypothesis="Application saturation / dependency latency",
                confidence=min(0.75, d.confidence + 0.05),
                contributing_factors=["cpu high", "threadpool saturated"],
            )
        state.stage = "RCA_DONE"
        span.set_attribute("rca.confidence", state.root_cause.confidence)
        return state

def tot_planner_agent(state: AgentState) -> AgentState:
    with TRACER.start_as_current_span("node:plan_tot") as span:
        planner: ToTPlanner = state._runtime["planner"]
        mem: Optional[LearningMemory] = state._runtime.get("memory")

        similar = []
        if mem and state.root_cause:
            similar = mem.query_similar(state.incident, state.root_cause, k=5)

        plan = planner.plan(state, similar_history=similar)
        state.plan = plan
        state.stage = "PLAN_READY"
        span.set_attribute("tot.score", plan.tot_score)
        span.set_attribute("plan.id", plan.plan_id)
        return state

def plan_validator_agent(state: AgentState) -> AgentState:
    with TRACER.start_as_current_span("node:validate_plan"):
        policy: PolicyEngine = state._runtime["policy"]
        if not state.plan:
            state.plan_validation = ValidationResult(ok=False, reason="No plan", violations=["missing_plan"])
            return state

        rc_conf = state.root_cause.confidence if state.root_cause else 0.2
        violations: List[str] = []

        for step in state.plan.steps:
            violations.extend(policy.check_autonomy(state, step, rc_conf))
            violations.extend(policy.check_policy_rules(state, step.tool, step.parameters))

        ok = len(violations) == 0
        state.plan_validation = ValidationResult(ok=ok, reason=("ok" if ok else "violations"), violations=violations)
        if ok:
            state.stage = "PLAN_VALIDATED"
        return state

def executor_agent(state: AgentState) -> AgentState:
    with TRACER.start_as_current_span("node:execute"):
        gw: ToolGateway = state._runtime["gateway"]
        if not state.plan:
            state.execution = ExecutionResult(ok=False, error="No plan")
            return state

        executed = []
        try:
            for step in state.plan.steps:
                gw.call(state, step.tool, step.parameters)
                executed.append(step.step_id)
            state.execution = ExecutionResult(ok=True, executed_steps=executed)
            state.stage = "EXECUTED"
        except Exception as e:
            state.execution = ExecutionResult(ok=False, executed_steps=executed, failed_step=(executed[-1] if executed else "1"), error=str(e))
            state.errors.append(f"Execution failed: {e}")
        return state

def post_validate_agent(state: AgentState) -> AgentState:
    with TRACER.start_as_current_span("node:post_validate") as span:
        gw: ToolGateway = state._runtime["gateway"]
        m = gw.call(state, "metrics_query", {"service": state.incident.service})

        # Demo logic: first attempt fails, second attempt passes
        ok = (state.attempts >= 1)
        reason = "Recovered within SLO" if ok else "Latency still high; try alternate plan"

        state.post_validation = ValidationResult(ok=ok, reason=reason, violations=[])
        if ok:
            state.stage = "POST_VALIDATED"
        span.set_attribute("post.ok", ok)
        span.set_attribute("metrics.p95", m.get("p95_latency_ms", -1))
        return state

def learning_agent(state: AgentState) -> AgentState:
    with TRACER.start_as_current_span("node:learn") as span:
        mem: Optional[LearningMemory] = state._runtime.get("memory")
        outcome = "SUCCESS" if (state.post_validation and state.post_validation.ok) else "FAILED"

        plan_id = state.plan.plan_id if state.plan else "no_plan"
        score = state.plan.tot_score if state.plan else -999.0
        rca = state.root_cause.hypothesis if state.root_cause else "Unknown"

        rec = LearningRecord(
            incident_id=state.incident.incident_id,
            plan_id=plan_id,
            outcome=outcome,
            score=score,
            root_cause=rca,
            what_worked=["Plan achieved recovery"] if outcome == "SUCCESS" else [],
            what_failed=["Plan did not recover SLO"] if outcome == "FAILED" else [],
            notes=["Store for similarity retrieval and ToT scoring"],
        )
        state.learning = rec
        state.stage = "LEARNED"

        if mem:
            with TRACER.start_as_current_span("memory:pgvector_upsert"):
                mem.upsert_learning(rec)

        span.set_attribute("learning.outcome", outcome)
        return state

def feedback_agent(state: AgentState) -> AgentState:
    with TRACER.start_as_current_span("node:feedback"):
        gw: ToolGateway = state._runtime["gateway"]
        outcome = "RESOLVED" if (state.post_validation and state.post_validation.ok) else "UNRESOLVED"

        summary = f"{state.incident.incident_id} {outcome} | RCA: {(state.root_cause.hypothesis if state.root_cause else 'Unknown')}"

        itsm_comment = "\n".join([
            summary,
            f"Plan: {state.plan.plan_id if state.plan else 'None'} (ToT score={state.plan.tot_score if state.plan else 'NA'})",
            f"Executed steps: {state.execution.executed_steps if state.execution else []}",
            f"Post-validate: {state.post_validation.reason if state.post_validation else 'N/A'}",
            f"Budget: {state.budget_units_used}/{state.budget_units_total}",
            f"Errors: {state.errors[-5:]}",
        ])

        gw.call(state, "itsm_update", {"ticket_id": state.incident.raw_event.get("ticket_id", "INC-UNKNOWN"),
                                      "comment": itsm_comment})

        state.feedback = Feedback(
            itsm_comment=itsm_comment,
            summary=summary,
            next_actions=["Add missing DB pool metrics", "Add rollback branch for failed executions"],
        )
        state.stage = "REPORTED"
        return state


# ----------------------------
# 9) Routing (backtracking)
# ----------------------------

def route_after_plan_validation(state: AgentState) -> str:
    if state.plan_validation and state.plan_validation.ok:
        return "execute"
    state.attempts += 1
    if state.attempts > state.max_attempts:
        state.stage = "ESCALATED"
        return "learn"
    return "plan_tot"

def route_after_execution(state: AgentState) -> str:
    if state.execution and state.execution.ok:
        return "post_validate"
    state.attempts += 1
    if state.attempts > state.max_attempts:
        return "learn"
    return "plan_tot"

def route_after_post_validation(state: AgentState) -> str:
    if state.post_validation and state.post_validation.ok:
        return "learn"
    state.attempts += 1
    if state.attempts > state.max_attempts:
        return "learn"
    return "plan_tot"


# ----------------------------
# 10) Build graph
# ----------------------------

def build_graph():
    g = StateGraph(AgentState)
    g.add_node("intake", intake_agent)
    g.add_node("diagnose", diagnosis_agent)
    g.add_node("rca", rca_agent)
    g.add_node("plan_tot", tot_planner_agent)
    g.add_node("validate_plan", plan_validator_agent)
    g.add_node("execute", executor_agent)
    g.add_node("post_validate", post_validate_agent)
    g.add_node("learn", learning_agent)
    g.add_node("feedback", feedback_agent)

    g.set_entry_point("intake")
    g.add_edge("intake", "diagnose")
    g.add_edge("diagnose", "rca")
    g.add_edge("rca", "plan_tot")
    g.add_edge("plan_tot", "validate_plan")

    g.add_conditional_edges("validate_plan", route_after_plan_validation,
                            {"execute": "execute", "plan_tot": "plan_tot", "learn": "learn"})

    g.add_conditional_edges("execute", route_after_execution,
                            {"post_validate": "post_validate", "plan_tot": "plan_tot", "learn": "learn"})

    g.add_conditional_edges("post_validate", route_after_post_validation,
                            {"learn": "learn", "plan_tot": "plan_tot"})

    g.add_edge("learn", "feedback")
    g.add_edge("feedback", END)

    return g.compile()


# ----------------------------
# 11) Runner (inject runtime deps)
# ----------------------------

def run_demo():
    setup_tracing("agentic-incident-remediator")

    policy_path = os.getenv("POLICY_YAML", "policy.yaml")
    policy = PolicyEngine(policy_path)

    user_ctx = UserContext(user="auto-remediator", roles=["sre"])
    gateway = ToolGateway(policy=policy, user_ctx=user_ctx)

    planner = ToTPlanner(policy=policy, beam_width=3, max_depth=2)

    memory = None
    pg_conn = os.getenv("PGVECTOR_CONN")  # e.g. "postgresql+psycopg://user:pass@localhost:5432/db"
    if pg_conn:
        memory = LearningMemory(connection=pg_conn, collection="incident_learning")

    incident = Incident(
        incident_id=f"INC-{time.strftime('%Y%m%d')}-0001",
        title="Checkout latency spike",
        severity="SEV1",
        service="checkout",
        environment="prod",
        timestamp_utc="2026-02-28T05:30:00Z",
        raw_event={"ticket_id": "INC-0001", "source": "prometheus", "alert": "HighLatency"},
    )

    state = AgentState(incident=incident, autonomy_tier="AUTO", max_attempts=2, budget_units_total=20)

    # Runtime dependencies: stored in a private dict to keep Pydantic clean
    state._runtime = {
        "policy": policy,
        "gateway": gateway,
        "planner": planner,
        "memory": memory,
    }

    app = build_graph()
    final = app.invoke(state)

    print("\n=== FINAL ===")
    print("stage:", final.stage)
    print("plan:", final.plan.plan_id if final.plan else None, "score:", final.plan.tot_score if final.plan else None)
    print("post_validation:", final.post_validation)
    print("learning:", final.learning)
    print("feedback:", final.feedback.summary if final.feedback else None)
    print("budget:", final.budget_units_used, "/", final.budget_units_total)
    print("errors:", final.errors)

if __name__ == "__main__":
    run_demo()