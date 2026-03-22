# GoT Schema

Below is a **complete enterprise Graph-of-Thoughts (GoT) schema in Pydantic v2**, in the same style as the earlier CoT and ToT schemas.

This version is designed for **non-linear reasoning graphs**, where thoughts can:

- branch
- merge
- refine
- contradict
- validate each other
- form reusable subgraphs

It is especially useful for:

- incident auto-remediation
- RCA systems
- multi-source investigation
- architecture decisioning
- complex enterprise planning where reasoning is **not just a tree**


## Enterprise GoT Schema — Pydantic v2

```
from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field, field_validator


# =========================================================
# Common Enums
# =========================================================

class TraceStatus(str, Enum):
    SUCCESS = "success"
    FAILED = "failed"
    PARTIAL = "partial"
    SKIPPED = "skipped"
    BLOCKED = "blocked"


class RiskLevel(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class Environment(str, Enum):
    DEV = "dev"
    QA = "qa"
    STAGE = "stage"
    PROD = "prod"
    UNKNOWN = "unknown"


class Severity(str, Enum):
    INFO = "info"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class AgentRole(str, Enum):
    GOT_PLANNER = "got_planner"
    GOT_EXECUTOR = "got_executor"
    GOT_VALIDATOR = "got_validator"
    GOT_ANALYZER = "got_analyzer"


class ValidationResult(str, Enum):
    PASS = "pass"
    FAIL = "fail"
    WARN = "warn"
    UNKNOWN = "unknown"


class DecisionType(str, Enum):
    PROCEED = "proceed"
    REPLAN = "replan"
    RETRY = "retry"
    ESCALATE = "escalate"
    BLOCK = "block"
    STOP = "stop"
    SELECT_SUBGRAPH = "select_subgraph"
    MERGE_THOUGHTS = "merge_thoughts"
    REFINE = "refine"


class ThoughtNodeStatus(str, Enum):
    GENERATED = "generated"
    LINKED = "linked"
    EVALUATED = "evaluated"
    MERGED = "merged"
    SELECTED = "selected"
    REJECTED = "rejected"
    EXECUTED = "executed"
    TERMINAL = "terminal"


class ThoughtNodeType(str, Enum):
    ROOT = "root"
    HYPOTHESIS = "hypothesis"
    OBSERVATION = "observation"
    PLAN = "plan"
    ACTION = "action"
    DIAGNOSTIC = "diagnostic"
    REMEDIATION = "remediation"
    VALIDATION = "validation"
    SYNTHESIS = "synthesis"
    DECISION = "decision"
    TERMINAL = "terminal"


class EdgeRelation(str, Enum):
    SUPPORTS = "supports"
    CONTRADICTS = "contradicts"
    REFINES = "refines"
    EXPANDS = "expands"
    DERIVES = "derives"
    MERGES_INTO = "merges_into"
    VALIDATES = "validates"
    DEPENDS_ON = "depends_on"
    LEADS_TO = "leads_to"
    ALTERNATIVE_TO = "alternative_to"
    SELECTS = "selects"


# =========================================================
# Shared Base Models
# =========================================================

class BaseTraceModel(BaseModel):
    model_config = ConfigDict(
        extra="forbid",
        validate_assignment=True,
        use_enum_values=True,
        populate_by_name=True,
    )


class TraceMetadata(BaseTraceModel):
    trace_id: str = Field(default_factory=lambda: str(uuid4()))
    parent_trace_id: Optional[str] = None
    run_id: Optional[str] = None
    correlation_id: Optional[str] = None
    schema_version: str = Field(default="1.0.0")
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    completed_at: Optional[datetime] = None
    agent_name: str
    agent_role: AgentRole
    status: TraceStatus = TraceStatus.SUCCESS

    @field_validator("completed_at")
    @classmethod
    def completed_after_created(cls, v: Optional[datetime], info):
        if v is not None and "created_at" in info.data:
            created_at = info.data["created_at"]
            if v < created_at:
                raise ValueError("completed_at must be >= created_at")
        return v


class IncidentContext(BaseTraceModel):
    incident_id: Optional[str] = None
    issue_key: Optional[str] = None
    issue_description: str
    title: Optional[str] = None
    service: str
    application: Optional[str] = None
    environment: Environment = Environment.UNKNOWN
    severity: Severity = Severity.MEDIUM
    source: Optional[str] = None
    detected_at: Optional[datetime] = None
    symptoms: List[str] = Field(default_factory=list)
    tags: Dict[str, str] = Field(default_factory=dict)


class GoalContext(BaseTraceModel):
    goal: str
    success_criteria: List[str] = Field(default_factory=list)
    priority: Optional[str] = None
    constraints: List[str] = Field(default_factory=list)
    assumptions: List[str] = Field(default_factory=list)


class ToolReference(BaseTraceModel):
    tool_name: str
    tool_version: Optional[str] = None
    tool_type: Optional[str] = None
    allowed: bool = True
    description: Optional[str] = None


class ToolCall(BaseTraceModel):
    tool_name: str
    arguments: Dict[str, Any] = Field(default_factory=dict)
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    status: TraceStatus = TraceStatus.SUCCESS
    latency_ms: Optional[int] = None
    result_summary: Optional[str] = None
    raw_result: Optional[Dict[str, Any]] = None
    error_message: Optional[str] = None


class ObservationBundle(BaseTraceModel):
    metrics: Dict[str, Union[int, float, str, bool, None]] = Field(default_factory=dict)
    logs: List[str] = Field(default_factory=list)
    events: List[str] = Field(default_factory=list)
    tool_outputs: List[ToolCall] = Field(default_factory=list)
    retrieved_context: Dict[str, Any] = Field(default_factory=dict)
    notes: List[str] = Field(default_factory=list)


class RiskAssessment(BaseTraceModel):
    risk_level: RiskLevel = RiskLevel.MEDIUM
    blast_radius: Optional[str] = None
    risk_factors: List[str] = Field(default_factory=list)
    mitigations: List[str] = Field(default_factory=list)
    approval_required: bool = False
    approved_by: Optional[str] = None


class ValidationCheck(BaseTraceModel):
    name: str
    description: Optional[str] = None
    expected_condition: str
    actual_value: Optional[str] = None
    result: ValidationResult = ValidationResult.UNKNOWN
    severity: Severity = Severity.MEDIUM
    blocking: bool = True
    evidence: List[str] = Field(default_factory=list)


class DecisionRecord(BaseTraceModel):
    decision: str
    decision_type: DecisionType
    rationale: str
    selected_option: Optional[str] = None
    rejected_options: List[str] = Field(default_factory=list)
    confidence: float = Field(ge=0.0, le=1.0, default=0.8)


# =========================================================
# GoT Graph Models
# =========================================================

class ThoughtScore(BaseTraceModel):
    relevance: float = Field(ge=0.0, le=1.0, default=0.5)
    feasibility: float = Field(ge=0.0, le=1.0, default=0.5)
    safety: float = Field(ge=0.0, le=1.0, default=0.5)
    evidence_strength: float = Field(ge=0.0, le=1.0, default=0.5)
    policy_alignment: float = Field(ge=0.0, le=1.0, default=0.5)
    confidence: float = Field(ge=0.0, le=1.0, default=0.5)
    overall_score: float = Field(ge=0.0, le=1.0, default=0.5)
    scoring_notes: List[str] = Field(default_factory=list)


class GraphPolicy(BaseTraceModel):
    max_nodes: int = Field(ge=1, default=50)
    max_edges: int = Field(ge=0, default=120)
    max_depth_hint: int = Field(ge=1, default=6)
    allow_merging: bool = True
    allow_contradictions: bool = True
    allow_cycles: bool = False
    min_selection_score: float = Field(ge=0.0, le=1.0, default=0.60)


class ThoughtNode(BaseTraceModel):
    node_id: str
    node_type: ThoughtNodeType = ThoughtNodeType.PLAN
    title: str
    content: str
    summary: Optional[str] = None
    status: ThoughtNodeStatus = ThoughtNodeStatus.GENERATED
    depth_hint: int = Field(ge=0, default=0)
    assumptions: List[str] = Field(default_factory=list)
    evidence: List[str] = Field(default_factory=list)
    counter_evidence: List[str] = Field(default_factory=list)
    proposed_actions: List[str] = Field(default_factory=list)
    expected_outcomes: List[str] = Field(default_factory=list)
    tool_calls_used: List[ToolCall] = Field(default_factory=list)
    risk_assessment: Optional[RiskAssessment] = None
    score: Optional[ThoughtScore] = None
    metadata: Dict[str, str] = Field(default_factory=dict)


class ThoughtEdge(BaseTraceModel):
    edge_id: str
    from_node_id: str
    to_node_id: str
    relation: EdgeRelation
    rationale: Optional[str] = None
    weight: float = Field(ge=0.0, le=1.0, default=0.5)
    bidirectional: bool = False


class ThoughtCluster(BaseTraceModel):
    cluster_id: str
    name: str
    description: Optional[str] = None
    node_ids: List[str] = Field(default_factory=list)
    cluster_type: Literal[
        "diagnostic",
        "evidence",
        "remediation",
        "validation",
        "decision",
        "synthesis"
    ] = "diagnostic"
    cluster_score: Optional[ThoughtScore] = None


class MergeOperation(BaseTraceModel):
    merge_id: str
    source_node_ids: List[str] = Field(default_factory=list)
    target_node_id: str
    reason: str
    merge_strategy: Literal[
        "synthesize",
        "deduplicate",
        "aggregate_evidence",
        "combine_actions"
    ] = "synthesize"


class SubgraphSelection(BaseTraceModel):
    selection_id: str
    selected_node_ids: List[str] = Field(default_factory=list)
    selected_edge_ids: List[str] = Field(default_factory=list)
    selected_cluster_ids: List[str] = Field(default_factory=list)
    rationale: str
    confidence: float = Field(ge=0.0, le=1.0, default=0.8)


# =========================================================
# GoT Reasoning Models
# =========================================================

class GraphConstructionStep(BaseTraceModel):
    round_no: int = Field(ge=1)
    created_node_ids: List[str] = Field(default_factory=list)
    created_edge_ids: List[str] = Field(default_factory=list)
    notes: List[str] = Field(default_factory=list)


class GraphEvaluationStep(BaseTraceModel):
    round_no: int = Field(ge=1)
    evaluated_node_ids: List[str] = Field(default_factory=list)
    evaluated_cluster_ids: List[str] = Field(default_factory=list)
    notes: List[str] = Field(default_factory=list)


class GraphMergeStep(BaseTraceModel):
    round_no: int = Field(ge=1)
    operations: List[MergeOperation] = Field(default_factory=list)
    notes: List[str] = Field(default_factory=list)


class GraphSelectionStep(BaseTraceModel):
    round_no: int = Field(ge=1)
    selection: SubgraphSelection
    notes: List[str] = Field(default_factory=list)


class GoTReasoning(BaseTraceModel):
    problem_understanding: str
    initial_thoughts: List[str] = Field(default_factory=list)
    graph_strategy: str
    graph_policy: GraphPolicy
    construction_steps: List[GraphConstructionStep] = Field(default_factory=list)
    evaluation_steps: List[GraphEvaluationStep] = Field(default_factory=list)
    merge_steps: List[GraphMergeStep] = Field(default_factory=list)
    selection_steps: List[GraphSelectionStep] = Field(default_factory=list)
    reasoning_log: List[str] = Field(default_factory=list)
    final_synthesis_reason: str


# =========================================================
# GoT Output Models
# =========================================================

class GoTPlanStep(BaseTraceModel):
    step_no: int = Field(ge=1)
    step_id: str
    step_name: str
    description: str
    source_node_ids: List[str] = Field(default_factory=list)
    purpose: Optional[str] = None
    tool_name: Optional[str] = None
    expected_outcome: Optional[str] = None
    validation_checks: List[str] = Field(default_factory=list)
    risk_level: RiskLevel = RiskLevel.MEDIUM


class GraphSynthesis(BaseTraceModel):
    synthesis_node_id: str
    summary: str
    selected_reasoning_path: List[str] = Field(default_factory=list)
    merged_from_node_ids: List[str] = Field(default_factory=list)
    confidence: float = Field(ge=0.0, le=1.0, default=0.8)
    risk_assessment: Optional[RiskAssessment] = None


class GoTOutput(BaseTraceModel):
    decision: DecisionRecord
    selected_subgraph: SubgraphSelection
    synthesis: GraphSynthesis
    final_plan: List[GoTPlanStep] = Field(default_factory=list)
    required_tools: List[ToolReference] = Field(default_factory=list)
    validation_checks: List[ValidationCheck] = Field(default_factory=list)


# =========================================================
# Main Enterprise GoT Trace Models
# =========================================================

class GoTPlannerTrace(BaseTraceModel):
    metadata: TraceMetadata
    incident: IncidentContext
    goal_context: GoalContext
    input_context: ObservationBundle = Field(default_factory=ObservationBundle)
    reasoning: GoTReasoning
    nodes: List[ThoughtNode] = Field(default_factory=list)
    edges: List[ThoughtEdge] = Field(default_factory=list)
    clusters: List[ThoughtCluster] = Field(default_factory=list)
    output: GoTOutput
    tags: Dict[str, str] = Field(default_factory=dict)


class GoTExecutorStepTrace(BaseTraceModel):
    metadata: TraceMetadata
    incident: IncidentContext
    goal_context: GoalContext
    selected_node_ids: List[str] = Field(default_factory=list)
    current_plan_step: GoTPlanStep
    observations: ObservationBundle = Field(default_factory=ObservationBundle)
    execution_reasoning: List[str] = Field(default_factory=list)
    action: ToolCall
    post_checks: List[ValidationCheck] = Field(default_factory=list)
    decision: DecisionRecord
    tags: Dict[str, str] = Field(default_factory=dict)


class GoTValidatorTrace(BaseTraceModel):
    metadata: TraceMetadata
    incident: IncidentContext
    goal_context: GoalContext
    validation_target: Literal["graph", "cluster", "node", "plan", "execution_result"]
    target_ids: List[str] = Field(default_factory=list)
    reasoning_steps: List[str] = Field(default_factory=list)
    checks: List[ValidationCheck] = Field(default_factory=list)
    summary: DecisionRecord
    risk_assessment: Optional[RiskAssessment] = None
    tags: Dict[str, str] = Field(default_factory=dict)


# =========================================================
# Helper Factory Functions
# =========================================================

def make_got_planner_metadata(agent_name: str = "got_planner") -> TraceMetadata:
    return TraceMetadata(
        agent_name=agent_name,
        agent_role=AgentRole.GOT_PLANNER,
        status=TraceStatus.SUCCESS,
    )


def make_got_executor_metadata(agent_name: str = "got_executor") -> TraceMetadata:
    return TraceMetadata(
        agent_name=agent_name,
        agent_role=AgentRole.GOT_EXECUTOR,
        status=TraceStatus.SUCCESS,
    )


def make_got_validator_metadata(agent_name: str = "got_validator") -> TraceMetadata:
    return TraceMetadata(
        agent_name=agent_name,
        agent_role=AgentRole.GOT_VALIDATOR,
        status=TraceStatus.SUCCESS,
    )


# =========================================================
# Example Usage
# =========================================================

if __name__ == "__main__":
    incident = IncidentContext(
        incident_id="INC_20260306_201",
        issue_key="DB_CONNECTION_POOL_EXHAUSTED",
        issue_description="Database connection pool exhausted",
        service="user-api",
        application="customer-platform",
        environment=Environment.PROD,
        severity=Severity.CRITICAL,
        source="Prometheus Alertmanager",
        symptoms=[
            "API latency above 2000 ms",
            "HTTP 500 errors increased",
            "DB active connections at 100%",
        ],
    )

    goal = GoalContext(
        goal="Restore healthy database connectivity for user-api",
        success_criteria=[
            "DB active connections below 80%",
            "API latency below 200 ms",
            "HTTP 500 rate below 1%",
        ],
        priority="critical",
        constraints=[
            "avoid database restart unless necessary",
            "prefer low-risk remediation first",
            "production changes must be logged",
        ],
    )

    n_root = ThoughtNode(
        node_id="node_root",
        node_type=ThoughtNodeType.ROOT,
        title="Incident root state",
        content="Production user-api is degraded by DB connection pool exhaustion.",
        summary="Starting point for graph construction.",
        status=ThoughtNodeStatus.LINKED,
        depth_hint=0,
        evidence=[
            "DB active connections at 100%",
            "API latency > 2000 ms",
            "HTTP 500 errors increased",
        ],
        score=ThoughtScore(
            relevance=1.0,
            confidence=0.95,
            overall_score=0.95,
            scoring_notes=["Primary incident anchor node"],
        ),
    )

    n_obs_1 = ThoughtNode(
        node_id="node_obs_1",
        node_type=ThoughtNodeType.OBSERVATION,
        title="Metrics indicate saturation",
        content="Database active connections are fully saturated.",
        status=ThoughtNodeStatus.LINKED,
        depth_hint=1,
        evidence=["db_active_connections_pct=100"],
        score=ThoughtScore(
            relevance=0.95,
            evidence_strength=0.95,
            confidence=0.93,
            overall_score=0.92,
        ),
    )

    n_hyp_1 = ThoughtNode(
        node_id="node_hyp_1",
        node_type=ThoughtNodeType.HYPOTHESIS,
        title="Application-side connection leak",
        content="Application pods may be holding stale DB connections and exhausting the pool.",
        status=ThoughtNodeStatus.EVALUATED,
        depth_hint=2,
        evidence=[
            "Many similar incidents are caused by stale app-side pools",
            "High API latency aligns with blocked connection acquisition",
        ],
        score=ThoughtScore(
            relevance=0.91,
            feasibility=0.85,
            safety=0.86,
            evidence_strength=0.82,
            policy_alignment=0.90,
            confidence=0.84,
            overall_score=0.87,
            scoring_notes=["Strong candidate hypothesis"],
        ),
    )

    n_hyp_2 = ThoughtNode(
        node_id="node_hyp_2",
        node_type=ThoughtNodeType.HYPOTHESIS,
        title="Long-running DB sessions",
        content="Long-running or blocked sessions may be consuming the pool.",
        status=ThoughtNodeStatus.EVALUATED,
        depth_hint=2,
        evidence=[
            "Pool exhaustion can be caused by blocked sessions",
            "Database-side evidence needed to confirm",
        ],
        score=ThoughtScore(
            relevance=0.88,
            feasibility=0.80,
            safety=0.78,
            evidence_strength=0.76,
            policy_alignment=0.88,
            confidence=0.78,
            overall_score=0.81,
        ),
    )

    n_rem_1 = ThoughtNode(
        node_id="node_rem_1",
        node_type=ThoughtNodeType.REMEDIATION,
        title="Rolling restart application pods",
        content="Perform rolling restart of user-api pods to clear stale app-side DB connections.",
        status=ThoughtNodeStatus.SELECTED,
        depth_hint=3,
        proposed_actions=["kubectl rollout restart deployment user-api"],
        expected_outcomes=[
            "DB active connections decrease",
            "API latency improves",
            "HTTP 500 errors reduce",
        ],
        risk_assessment=RiskAssessment(
            risk_level=RiskLevel.MEDIUM,
            blast_radius="user-api deployment only",
            risk_factors=["production service impact during rollout"],
            mitigations=["rolling restart", "health checks"],
        ),
        score=ThoughtScore(
            relevance=0.93,
            feasibility=0.91,
            safety=0.82,
            evidence_strength=0.83,
            policy_alignment=0.94,
            confidence=0.86,
            overall_score=0.89,
        ),
    )

    n_syn_1 = ThoughtNode(
        node_id="node_syn_1",
        node_type=ThoughtNodeType.SYNTHESIS,
        title="Merged remediation synthesis",
        content="The strongest graph path combines metric saturation evidence with the app-side connection leak hypothesis and selects rolling restart as the first remediation.",
        summary="Best low-risk synthesis of current graph.",
        status=ThoughtNodeStatus.MERGED,
        depth_hint=4,
        evidence=[
            "Metrics support saturation",
            "Hypothesis aligns with common failure mode",
            "Selected remediation is low-risk and policy-aligned",
        ],
        score=ThoughtScore(
            relevance=0.96,
            feasibility=0.90,
            safety=0.84,
            evidence_strength=0.88,
            policy_alignment=0.95,
            confidence=0.88,
            overall_score=0.91,
        ),
    )

    trace = GoTPlannerTrace(
        metadata=make_got_planner_metadata(),
        incident=incident,
        goal_context=goal,
        input_context=ObservationBundle(
            metrics={
                "db_active_connections_pct": 100,
                "api_latency_ms": 2400,
                "http_500_rate_pct": 8.5,
            },
            logs=[
                "timeout acquiring connection from pool",
                "pool exhausted for datasource primary-db",
            ],
            notes=[
                "Past similar incident recovered after rolling restart of app pods"
            ],
        ),
        reasoning=GoTReasoning(
            problem_understanding="This is a production incident with multiple possible causes. The reasoning should connect evidence, hypotheses, and remediation options in a graph, then synthesize the strongest subgraph.",
            initial_thoughts=[
                "Need to separate evidence nodes from hypothesis nodes",
                "Need to support multiple competing explanations",
                "Need a merged synthesis before selecting remediation",
            ],
            graph_strategy="Construct evidence and hypothesis nodes, connect supporting and alternative relationships, merge strongest reasoning paths into a synthesis node, then derive final remediation plan.",
            graph_policy=GraphPolicy(
                max_nodes=30,
                max_edges=60,
                max_depth_hint=5,
                allow_merging=True,
                allow_contradictions=True,
                allow_cycles=False,
                min_selection_score=0.70,
            ),
            construction_steps=[
                GraphConstructionStep(
                    round_no=1,
                    created_node_ids=["node_root", "node_obs_1", "node_hyp_1", "node_hyp_2"],
                    created_edge_ids=["edge_1", "edge_2", "edge_3"],
                    notes=[
                        "Built initial evidence and hypothesis graph"
                    ],
                ),
                GraphConstructionStep(
                    round_no=2,
                    created_node_ids=["node_rem_1", "node_syn_1"],
                    created_edge_ids=["edge_4", "edge_5", "edge_6"],
                    notes=[
                        "Derived remediation node and synthesis node"
                    ],
                ),
            ],
            evaluation_steps=[
                GraphEvaluationStep(
                    round_no=1,
                    evaluated_node_ids=[
                        "node_obs_1",
                        "node_hyp_1",
                        "node_hyp_2",
                        "node_rem_1",
                        "node_syn_1",
                    ],
                    evaluated_cluster_ids=["cluster_diag", "cluster_remediation"],
                    notes=[
                        "Hypothesis 1 and remediation 1 dominate on safety and policy alignment"
                    ],
                )
            ],
            merge_steps=[
                GraphMergeStep(
                    round_no=1,
                    operations=[
                        MergeOperation(
                            merge_id="merge_1",
                            source_node_ids=["node_obs_1", "node_hyp_1", "node_rem_1"],
                            target_node_id="node_syn_1",
                            reason="Create final synthesis from strongest evidence-hypothesis-remediation chain",
                            merge_strategy="synthesize",
                        )
                    ],
                    notes=["Merged strongest subgraph into synthesis node"],
                )
            ],
            selection_steps=[
                GraphSelectionStep(
                    round_no=1,
                    selection=SubgraphSelection(
                        selection_id="sel_1",
                        selected_node_ids=["node_obs_1", "node_hyp_1", "node_rem_1", "node_syn_1"],
                        selected_edge_ids=["edge_1", "edge_4", "edge_6"],
                        selected_cluster_ids=["cluster_diag", "cluster_remediation", "cluster_synthesis"],
                        rationale="Selected subgraph best explains the incident and proposes the safest effective remediation.",
                        confidence=0.89,
                    ),
                    notes=["Selected synthesis-driven remediation subgraph"],
                )
            ],
            reasoning_log=[
                "Created separate nodes for evidence, hypotheses, and remediations.",
                "Linked support and alternative relationships.",
                "Merged strongest path into a synthesis node.",
                "Selected the highest-confidence low-risk subgraph.",
            ],
            final_synthesis_reason="The selected graph path provides the strongest evidence-backed and policy-aligned remediation sequence for this production incident.",
        ),
        nodes=[n_root, n_obs_1, n_hyp_1, n_hyp_2, n_rem_1, n_syn_1],
        edges=[
            ThoughtEdge(
                edge_id="edge_1",
                from_node_id="node_obs_1",
                to_node_id="node_hyp_1",
                relation=EdgeRelation.SUPPORTS,
                rationale="Saturation supports stale app-side pool hypothesis",
                weight=0.86,
            ),
            ThoughtEdge(
                edge_id="edge_2",
                from_node_id="node_obs_1",
                to_node_id="node_hyp_2",
                relation=EdgeRelation.SUPPORTS,
                rationale="Saturation also supports long-running session hypothesis",
                weight=0.73,
            ),
            ThoughtEdge(
                edge_id="edge_3",
                from_node_id="node_hyp_1",
                to_node_id="node_hyp_2",
                relation=EdgeRelation.ALTERNATIVE_TO,
                rationale="Competing hypotheses for the same symptom cluster",
                weight=0.60,
                bidirectional=True,
            ),
            ThoughtEdge(
                edge_id="edge_4",
                from_node_id="node_hyp_1",
                to_node_id="node_rem_1",
                relation=EdgeRelation.LEADS_TO,
                rationale="If app-side connection leak is primary cause, rolling restart is appropriate",
                weight=0.88,
            ),
            ThoughtEdge(
                edge_id="edge_5",
                from_node_id="node_obs_1",
                to_node_id="node_syn_1",
                relation=EdgeRelation.MERGES_INTO,
                rationale="Evidence included in final synthesis",
                weight=0.90,
            ),
            ThoughtEdge(
                edge_id="edge_6",
                from_node_id="node_rem_1",
                to_node_id="node_syn_1",
                relation=EdgeRelation.MERGES_INTO,
                rationale="Selected remediation included in final synthesis",
                weight=0.92,
            ),
        ],
        clusters=[
            ThoughtCluster(
                cluster_id="cluster_diag",
                name="Diagnostic reasoning cluster",
                description="Evidence and hypotheses related to the cause of pool exhaustion",
                node_ids=["node_obs_1", "node_hyp_1", "node_hyp_2"],
                cluster_type="diagnostic",
                cluster_score=ThoughtScore(
                    relevance=0.91,
                    evidence_strength=0.85,
                    confidence=0.84,
                    overall_score=0.87,
                ),
            ),
            ThoughtCluster(
                cluster_id="cluster_remediation",
                name="Remediation cluster",
                description="Candidate remediation actions",
                node_ids=["node_rem_1"],
                cluster_type="remediation",
                cluster_score=ThoughtScore(
                    feasibility=0.91,
                    safety=0.82,
                    policy_alignment=0.94,
                    confidence=0.86,
                    overall_score=0.88,
                ),
            ),
            ThoughtCluster(
                cluster_id="cluster_synthesis",
                name="Synthesis cluster",
                description="Merged final reasoning for selected response path",
                node_ids=["node_syn_1"],
                cluster_type="synthesis",
                cluster_score=ThoughtScore(
                    relevance=0.96,
                    confidence=0.88,
                    overall_score=0.91,
                ),
            ),
        ],
        output=GoTOutput(
            decision=DecisionRecord(
                decision="Select synthesis-driven subgraph and proceed with app-side rolling restart plan",
                decision_type=DecisionType.SELECT_SUBGRAPH,
                rationale="This subgraph best combines evidence, hypothesis strength, safety, and policy alignment.",
                selected_option="sel_1",
                rejected_options=["subgraph centered on long-running DB sessions only"],
                confidence=0.89,
            ),
            selected_subgraph=SubgraphSelection(
                selection_id="sel_1",
                selected_node_ids=["node_obs_1", "node_hyp_1", "node_rem_1", "node_syn_1"],
                selected_edge_ids=["edge_1", "edge_4", "edge_6"],
                selected_cluster_ids=["cluster_diag", "cluster_remediation", "cluster_synthesis"],
                rationale="Selected because it gives the best low-risk, evidence-backed remediation path.",
                confidence=0.89,
            ),
            synthesis=GraphSynthesis(
                synthesis_node_id="node_syn_1",
                summary="Metrics indicate saturation, strongest hypothesis is stale app-side DB connections, and the safest first remediation is rolling restart of user-api pods.",
                selected_reasoning_path=["node_obs_1", "node_hyp_1", "node_rem_1", "node_syn_1"],
                merged_from_node_ids=["node_obs_1", "node_hyp_1", "node_rem_1"],
                confidence=0.89,
                risk_assessment=RiskAssessment(
                    risk_level=RiskLevel.MEDIUM,
                    blast_radius="user-api deployment only",
                    risk_factors=["rolling restart in production"],
                    mitigations=["health checks", "controlled rollout"],
                ),
            ),
            final_plan=[
                GoTPlanStep(
                    step_no=1,
                    step_id="step_1",
                    step_name="Inspect DB sessions",
                    description="Check active, idle, and blocked sessions to enrich graph evidence before action.",
                    source_node_ids=["node_obs_1", "node_hyp_2"],
                    purpose="Confirm or weaken DB-side hypothesis.",
                    tool_name="query_db_sessions",
                    expected_outcome="Session evidence becomes clearer.",
                    validation_checks=["session_query_success"],
                    risk_level=RiskLevel.LOW,
                ),
                GoTPlanStep(
                    step_no=2,
                    step_id="step_2",
                    step_name="Capture metrics baseline",
                    description="Confirm DB connections, latency, and HTTP 500 baseline before remediation.",
                    source_node_ids=["node_obs_1"],
                    purpose="Establish comparison point.",
                    tool_name="query_metrics",
                    expected_outcome="Metrics baseline recorded.",
                    validation_checks=["metrics_freshness_ok"],
                    risk_level=RiskLevel.LOW,
                ),
                GoTPlanStep(
                    step_no=3,
                    step_id="step_3",
                    step_name="Rolling restart user-api",
                    description="Restart user-api pods to clear stale application-side DB connections.",
                    source_node_ids=["node_hyp_1", "node_rem_1", "node_syn_1"],
                    purpose="Apply selected low-risk remediation.",
                    tool_name="kubectl_rollout_restart",
                    expected_outcome="Pool pressure decreases and API health improves.",
                    validation_checks=["deployment_rollout_success"],
                    risk_level=RiskLevel.MEDIUM,
                ),
                GoTPlanStep(
                    step_no=4,
                    step_id="step_4",
                    step_name="Validate recovery",
                    description="Check whether success criteria are met after restart.",
                    source_node_ids=["node_syn_1"],
                    purpose="Confirm incident resolution.",
                    tool_name="run_health_check",
                    expected_outcome="Latency and connection usage normalize.",
                    validation_checks=[
                        "db_active_connections_below_80",
                        "api_latency_below_200",
                        "http_500_rate_below_1",
                    ],
                    risk_level=RiskLevel.LOW,
                ),
            ],
            required_tools=[
                ToolReference(tool_name="query_db_sessions"),
                ToolReference(tool_name="query_metrics"),
                ToolReference(tool_name="kubectl_rollout_restart"),
                ToolReference(tool_name="run_health_check"),
            ],
            validation_checks=[
                ValidationCheck(
                    name="selected_subgraph_policy_check",
                    expected_condition="Selected graph does not require high-risk DB restart as first action",
                    result=ValidationResult.PASS,
                    severity=Severity.HIGH,
                    blocking=True,
                )
            ],
        ),
        tags={"pattern": "graph-of-thought", "domain": "incident-remediation"},
    )

    print(trace.model_dump_json(indent=2))
```

## What makes GoT different from ToT

The key difference is:

**Tree-of-Thought**

Reasoning structure is mostly:

```
root
 ├─ branch A
 ├─ branch B
 └─ branch C
```

Good for:

- branch generation
- scoring alternatives
- pruning
- backtracking


## Graph-of-Thought

Reasoning structure can be:

```
evidence node → hypothesis node
evidence node → another hypothesis
two hypotheses → merged synthesis
synthesis → remediation
validation node → supports remediation
```

Good for:

- many-to-many relationships
- merging ideas
- contradiction handling
- reusable reasoning subgraphs
- multi-source evidence synthesis

## Main enterprise models in GoT

**ThoughtNode**

Represents any reasoning unit:

- observation
- hypothesis
- remediation
- validation
- synthesis
- decision


**ThoughtEdge**

Represents non-linear relationships:

- supports
- contradicts
- refines
- derives
- merges_into
- alternative_to
- depends_on


**ThoughtCluster**

Groups related nodes into logical regions:

- diagnostic cluster
- remediation cluster
- synthesis cluster

**MergeOperation**

Captures when multiple nodes become one synthesized node.

**SubgraphSelection**

Selects a subset of the graph as the final chosen reasoning path.

**GraphSynthesis**

Represents the merged reasoning summary that drives the final plan.

## Recommended enterprise usage

Use the GoT schema like this:

```
Incident / Goal
   ↓
GoTPlannerTrace
   ↓
Selected subgraph + synthesis + final plan
   ↓
GoTExecutorStepTrace
   ↓
GoTValidatorTrace
   ↓
Observability / audit / replay store
```

## Best-fit use cases

GoT is especially useful when reasoning is **not just branching, but interconnected**:

- RCA with evidence from logs, metrics, topology, and incidents
- enterprise architecture decisioning
- remediation planning with competing and mergeable strategies
- multi-agent synthesis
- knowledge graph-assisted agent reasoning


## Mental model

**CoT**

`One line of thought`

**ToT**

`Many branches of thought`

**GoT**

`A network of thoughts that can branch, connect, merge, and synthesize`

