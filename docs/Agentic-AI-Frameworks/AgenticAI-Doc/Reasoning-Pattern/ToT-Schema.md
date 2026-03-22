# ToT Schema
Below is a **complete enterprise Tree-of-Thoughts (ToT) schema in Pydantic v2**, in a style similar to the CoT schema, but designed for:

- branching reasoning
- candidate plan exploration
- branch scoring
- pruning
- backtracking
- selecting best path
- auditability for enterprise agents

This works well for:

- incident auto-remediation
- planner agents
- RCA agents
- strategy selection agents
- complex multi-step decision systems

## Enterprise ToT Schema — Pydantic v2

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
    TOT_PLANNER = "tot_planner"
    TOT_EXECUTOR = "tot_executor"
    TOT_EVALUATOR = "tot_evaluator"
    TOT_VALIDATOR = "tot_validator"


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
    SELECT_BRANCH = "select_branch"
    PRUNE_BRANCH = "prune_branch"
    BACKTRACK = "backtrack"


class ThoughtNodeStatus(str, Enum):
    GENERATED = "generated"
    EXPANDED = "expanded"
    EVALUATED = "evaluated"
    PRUNED = "pruned"
    SELECTED = "selected"
    EXECUTED = "executed"
    REJECTED = "rejected"
    BACKTRACKED = "backtracked"


class ThoughtNodeType(str, Enum):
    ROOT = "root"
    HYPOTHESIS = "hypothesis"
    PLAN = "plan"
    ACTION = "action"
    DIAGNOSTIC = "diagnostic"
    REMEDIATION = "remediation"
    VALIDATION = "validation"
    TERMINAL = "terminal"


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
# ToT Scoring and Search Models
# =========================================================

class ThoughtScore(BaseTraceModel):
    feasibility: float = Field(ge=0.0, le=1.0, default=0.5)
    safety: float = Field(ge=0.0, le=1.0, default=0.5)
    expected_effectiveness: float = Field(ge=0.0, le=1.0, default=0.5)
    cost_efficiency: float = Field(ge=0.0, le=1.0, default=0.5)
    latency_efficiency: float = Field(ge=0.0, le=1.0, default=0.5)
    policy_alignment: float = Field(ge=0.0, le=1.0, default=0.5)
    confidence: float = Field(ge=0.0, le=1.0, default=0.5)
    overall_score: float = Field(ge=0.0, le=1.0, default=0.5)
    scoring_notes: List[str] = Field(default_factory=list)


class SearchPolicy(BaseTraceModel):
    max_depth: int = Field(ge=1, default=4)
    max_branches_per_node: int = Field(ge=1, default=5)
    beam_width: int = Field(ge=1, default=3)
    allow_backtracking: bool = True
    pruning_threshold: float = Field(ge=0.0, le=1.0, default=0.35)
    stop_on_high_confidence_terminal: bool = True
    stop_score_threshold: float = Field(ge=0.0, le=1.0, default=0.9)


class BranchEvaluation(BaseTraceModel):
    node_id: str
    branch_id: str
    score: ThoughtScore
    strengths: List[str] = Field(default_factory=list)
    weaknesses: List[str] = Field(default_factory=list)
    risks: List[str] = Field(default_factory=list)
    evaluator_summary: str
    prune_recommendation: bool = False
    selected_for_expansion: bool = False


# =========================================================
# ToT Node Models
# =========================================================

class ThoughtNode(BaseTraceModel):
    node_id: str
    parent_node_id: Optional[str] = None
    depth: int = Field(ge=0, default=0)
    branch_id: str
    node_type: ThoughtNodeType = ThoughtNodeType.PLAN
    title: str
    thought: str
    reasoning_summary: Optional[str] = None
    assumptions: List[str] = Field(default_factory=list)
    supporting_evidence: List[str] = Field(default_factory=list)
    conflicting_evidence: List[str] = Field(default_factory=list)
    proposed_actions: List[str] = Field(default_factory=list)
    expected_outcomes: List[str] = Field(default_factory=list)
    risk_assessment: Optional[RiskAssessment] = None
    score: Optional[ThoughtScore] = None
    status: ThoughtNodeStatus = ThoughtNodeStatus.GENERATED
    generated_by: Optional[str] = None
    tool_calls_used: List[ToolCall] = Field(default_factory=list)
    tags: Dict[str, str] = Field(default_factory=dict)


class ThoughtEdge(BaseTraceModel):
    edge_id: str
    from_node_id: str
    to_node_id: str
    relation: Literal[
        "expands",
        "refines",
        "branches_to",
        "validates",
        "contradicts",
        "backtracks_to",
        "selects"
    ]
    rationale: Optional[str] = None


class ThoughtBranch(BaseTraceModel):
    branch_id: str
    root_node_id: str
    node_ids: List[str] = Field(default_factory=list)
    current_depth: int = Field(ge=0, default=0)
    status: ThoughtNodeStatus = ThoughtNodeStatus.GENERATED
    branch_summary: Optional[str] = None
    score: Optional[ThoughtScore] = None
    selected: bool = False
    pruned_reason: Optional[str] = None


# =========================================================
# ToT Reasoning Models
# =========================================================

class ToTGenerationStep(BaseTraceModel):
    round_no: int = Field(ge=1)
    expanded_node_id: str
    expansion_prompt_summary: Optional[str] = None
    generated_child_node_ids: List[str] = Field(default_factory=list)
    generation_notes: List[str] = Field(default_factory=list)


class ToTEvaluationStep(BaseTraceModel):
    round_no: int = Field(ge=1)
    evaluated_node_ids: List[str] = Field(default_factory=list)
    evaluations: List[BranchEvaluation] = Field(default_factory=list)
    evaluation_notes: List[str] = Field(default_factory=list)


class ToTPruningStep(BaseTraceModel):
    round_no: int = Field(ge=1)
    pruned_node_ids: List[str] = Field(default_factory=list)
    pruned_branch_ids: List[str] = Field(default_factory=list)
    prune_reasoning: List[str] = Field(default_factory=list)


class ToTBacktrackStep(BaseTraceModel):
    round_no: int = Field(ge=1)
    from_node_id: str
    to_node_id: str
    reason: str


class ToTReasoning(BaseTraceModel):
    problem_understanding: str
    initial_hypotheses: List[str] = Field(default_factory=list)
    search_strategy: str
    search_policy: SearchPolicy
    generation_steps: List[ToTGenerationStep] = Field(default_factory=list)
    evaluation_steps: List[ToTEvaluationStep] = Field(default_factory=list)
    pruning_steps: List[ToTPruningStep] = Field(default_factory=list)
    backtracking_steps: List[ToTBacktrackStep] = Field(default_factory=list)
    reasoning_log: List[str] = Field(default_factory=list)
    final_selection_reason: str


# =========================================================
# ToT Output Models
# =========================================================

class SelectedSolution(BaseTraceModel):
    selected_branch_id: str
    selected_terminal_node_id: str
    solution_summary: str
    chosen_actions: List[str] = Field(default_factory=list)
    expected_outcomes: List[str] = Field(default_factory=list)
    confidence: float = Field(ge=0.0, le=1.0, default=0.8)
    risk_assessment: Optional[RiskAssessment] = None


class ToTPlanStep(BaseTraceModel):
    step_no: int = Field(ge=1)
    step_id: str
    step_name: str
    description: str
    purpose: Optional[str] = None
    tool_name: Optional[str] = None
    expected_outcome: Optional[str] = None
    validation_checks: List[str] = Field(default_factory=list)
    risk_level: RiskLevel = RiskLevel.MEDIUM


class ToTOutput(BaseTraceModel):
    decision: DecisionRecord
    selected_solution: SelectedSolution
    final_plan: List[ToTPlanStep] = Field(default_factory=list)
    required_tools: List[ToolReference] = Field(default_factory=list)
    validation_checks: List[ValidationCheck] = Field(default_factory=list)


# =========================================================
# Main Enterprise ToT Trace Models
# =========================================================

class ToTPlannerTrace(BaseTraceModel):
    metadata: TraceMetadata
    incident: IncidentContext
    goal_context: GoalContext
    input_context: ObservationBundle = Field(default_factory=ObservationBundle)
    reasoning: ToTReasoning
    nodes: List[ThoughtNode] = Field(default_factory=list)
    edges: List[ThoughtEdge] = Field(default_factory=list)
    branches: List[ThoughtBranch] = Field(default_factory=list)
    output: ToTOutput
    tags: Dict[str, str] = Field(default_factory=dict)


class ToTExecutorStepTrace(BaseTraceModel):
    metadata: TraceMetadata
    incident: IncidentContext
    goal_context: GoalContext
    selected_branch_id: str
    selected_node_id: str
    current_plan_step: ToTPlanStep
    observations: ObservationBundle = Field(default_factory=ObservationBundle)
    execution_reasoning: List[str] = Field(default_factory=list)
    action: ToolCall
    post_checks: List[ValidationCheck] = Field(default_factory=list)
    decision: DecisionRecord
    tags: Dict[str, str] = Field(default_factory=dict)


class ToTValidatorTrace(BaseTraceModel):
    metadata: TraceMetadata
    incident: IncidentContext
    goal_context: GoalContext
    selected_branch_id: str
    selected_node_id: str
    validation_target: Literal["branch", "node", "plan", "execution_result"]
    reasoning_steps: List[str] = Field(default_factory=list)
    checks: List[ValidationCheck] = Field(default_factory=list)
    summary: DecisionRecord
    risk_assessment: Optional[RiskAssessment] = None
    tags: Dict[str, str] = Field(default_factory=dict)


# =========================================================
# Helper Factory Functions
# =========================================================

def make_tot_planner_metadata(agent_name: str = "tot_planner") -> TraceMetadata:
    return TraceMetadata(
        agent_name=agent_name,
        agent_role=AgentRole.TOT_PLANNER,
        status=TraceStatus.SUCCESS,
    )


def make_tot_executor_metadata(agent_name: str = "tot_executor") -> TraceMetadata:
    return TraceMetadata(
        agent_name=agent_name,
        agent_role=AgentRole.TOT_EXECUTOR,
        status=TraceStatus.SUCCESS,
    )


def make_tot_validator_metadata(agent_name: str = "tot_validator") -> TraceMetadata:
    return TraceMetadata(
        agent_name=agent_name,
        agent_role=AgentRole.TOT_VALIDATOR,
        status=TraceStatus.SUCCESS,
    )


# =========================================================
# Example Usage
# =========================================================

if __name__ == "__main__":
    incident = IncidentContext(
        incident_id="INC_20260306_101",
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
            "prefer app-side remediation first",
            "production changes must be logged",
        ],
    )

    root_node = ThoughtNode(
        node_id="node_root",
        parent_node_id=None,
        depth=0,
        branch_id="branch_root",
        node_type=ThoughtNodeType.ROOT,
        title="Root incident state",
        thought="The service is degraded due to DB connection pool exhaustion. Need to explore safe remediation branches.",
        reasoning_summary="Start with alternative remediation strategies.",
        supporting_evidence=[
            "DB active connections at 100%",
            "API latency > 2000 ms"
        ],
        status=ThoughtNodeStatus.EXPANDED,
    )

    node_a = ThoughtNode(
        node_id="node_a",
        parent_node_id="node_root",
        depth=1,
        branch_id="branch_a",
        node_type=ThoughtNodeType.REMEDIATION,
        title="Restart application pods first",
        thought="Application-side stale connections may be exhausting the pool; rolling restart may clear them with lower risk.",
        proposed_actions=["kubectl rollout restart deployment user-api"],
        expected_outcomes=[
            "DB active connections decrease",
            "API latency improves"
        ],
        risk_assessment=RiskAssessment(
            risk_level=RiskLevel.MEDIUM,
            blast_radius="user-api deployment only",
            risk_factors=["production user-facing service"],
            mitigations=["rolling restart", "health checks"],
        ),
        score=ThoughtScore(
            feasibility=0.90,
            safety=0.80,
            expected_effectiveness=0.82,
            cost_efficiency=0.95,
            latency_efficiency=0.88,
            policy_alignment=0.92,
            confidence=0.84,
            overall_score=0.87,
            scoring_notes=["Low-risk, common fix for stale app pools"],
        ),
        status=ThoughtNodeStatus.SELECTED,
    )

    node_b = ThoughtNode(
        node_id="node_b",
        parent_node_id="node_root",
        depth=1,
        branch_id="branch_b",
        node_type=ThoughtNodeType.REMEDIATION,
        title="Restart database",
        thought="A DB restart may clear all connections, but has high risk in production.",
        proposed_actions=["restart postgres-primary"],
        expected_outcomes=["All sessions reset"],
        risk_assessment=RiskAssessment(
            risk_level=RiskLevel.CRITICAL,
            blast_radius="shared database",
            risk_factors=["high production blast radius"],
            mitigations=[],
            approval_required=True,
        ),
        score=ThoughtScore(
            feasibility=0.75,
            safety=0.20,
            expected_effectiveness=0.78,
            cost_efficiency=0.70,
            latency_efficiency=0.60,
            policy_alignment=0.15,
            confidence=0.68,
            overall_score=0.41,
            scoring_notes=["Effective but too risky for first action in prod"],
        ),
        status=ThoughtNodeStatus.PRUNED,
    )

    trace = ToTPlannerTrace(
        metadata=make_tot_planner_metadata(),
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
        reasoning=ToTReasoning(
            problem_understanding="Production incident caused by exhausted DB connections. Need to explore multiple remediation branches and select the safest effective one.",
            initial_hypotheses=[
                "Application-side connection leak",
                "Long-running DB sessions",
                "Temporary DB overload"
            ],
            search_strategy="Generate multiple remediation branches, score for safety and effectiveness, prune risky paths, select best low-risk branch.",
            search_policy=SearchPolicy(
                max_depth=3,
                max_branches_per_node=3,
                beam_width=2,
                allow_backtracking=True,
                pruning_threshold=0.45,
                stop_on_high_confidence_terminal=True,
                stop_score_threshold=0.90,
            ),
            generation_steps=[
                ToTGenerationStep(
                    round_no=1,
                    expanded_node_id="node_root",
                    generated_child_node_ids=["node_a", "node_b"],
                    generation_notes=[
                        "Generated app-side remediation and DB-side remediation branches"
                    ],
                )
            ],
            evaluation_steps=[
                ToTEvaluationStep(
                    round_no=1,
                    evaluated_node_ids=["node_a", "node_b"],
                    evaluations=[
                        BranchEvaluation(
                            node_id="node_a",
                            branch_id="branch_a",
                            score=node_a.score,
                            strengths=[
                                "lower blast radius",
                                "policy-aligned",
                                "fast rollback path"
                            ],
                            weaknesses=[
                                "may not fix DB-side blocked sessions"
                            ],
                            risks=[
                                "temporary pod restart impact"
                            ],
                            evaluator_summary="Best first-step remediation candidate",
                            prune_recommendation=False,
                            selected_for_expansion=True,
                        ),
                        BranchEvaluation(
                            node_id="node_b",
                            branch_id="branch_b",
                            score=node_b.score,
                            strengths=[
                                "could clear all sessions"
                            ],
                            weaknesses=[
                                "high blast radius",
                                "approval required"
                            ],
                            risks=[
                                "shared DB disruption",
                                "customer-facing impact"
                            ],
                            evaluator_summary="Too risky for first remediation action",
                            prune_recommendation=True,
                            selected_for_expansion=False,
                        ),
                    ],
                    evaluation_notes=[
                        "App restart branch dominates on safety and policy alignment"
                    ],
                )
            ],
            pruning_steps=[
                ToTPruningStep(
                    round_no=1,
                    pruned_node_ids=["node_b"],
                    pruned_branch_ids=["branch_b"],
                    prune_reasoning=[
                        "Branch score below acceptable first-action threshold",
                        "Production DB restart violates least-risk-first strategy"
                    ],
                )
            ],
            backtracking_steps=[],
            reasoning_log=[
                "Explored competing remediation options.",
                "Scored branches for safety, effectiveness, and policy alignment.",
                "Pruned DB restart branch.",
                "Selected rolling restart branch."
            ],
            final_selection_reason="The selected branch offers the best balance of safety, likely effectiveness, and policy compliance for a production-first response.",
        ),
        nodes=[root_node, node_a, node_b],
        edges=[
            ThoughtEdge(
                edge_id="edge_1",
                from_node_id="node_root",
                to_node_id="node_a",
                relation="branches_to",
                rationale="Explore app-side remediation path",
            ),
            ThoughtEdge(
                edge_id="edge_2",
                from_node_id="node_root",
                to_node_id="node_b",
                relation="branches_to",
                rationale="Explore DB restart remediation path",
            ),
        ],
        branches=[
            ThoughtBranch(
                branch_id="branch_a",
                root_node_id="node_a",
                node_ids=["node_a"],
                current_depth=1,
                status=ThoughtNodeStatus.SELECTED,
                branch_summary="Rolling restart application pods first",
                score=node_a.score,
                selected=True,
            ),
            ThoughtBranch(
                branch_id="branch_b",
                root_node_id="node_b",
                node_ids=["node_b"],
                current_depth=1,
                status=ThoughtNodeStatus.PRUNED,
                branch_summary="Restart database",
                score=node_b.score,
                selected=False,
                pruned_reason="Too risky in prod for first-line remediation",
            ),
        ],
        output=ToTOutput(
            decision=DecisionRecord(
                decision="Select application rolling restart branch",
                decision_type=DecisionType.SELECT_BRANCH,
                rationale="Best low-risk, policy-aligned remediation candidate",
                selected_option="branch_a",
                rejected_options=["branch_b"],
                confidence=0.87,
            ),
            selected_solution=SelectedSolution(
                selected_branch_id="branch_a",
                selected_terminal_node_id="node_a",
                solution_summary="Use rolling restart of user-api pods after confirming session state and metrics baseline.",
                chosen_actions=[
                    "query_db_sessions",
                    "query_metrics",
                    "kubectl_rollout_restart",
                    "run_health_check",
                ],
                expected_outcomes=[
                    "reduced DB active connections",
                    "reduced API latency",
                    "reduced HTTP 500 rate",
                ],
                confidence=0.87,
                risk_assessment=node_a.risk_assessment,
            ),
            final_plan=[
                ToTPlanStep(
                    step_no=1,
                    step_id="step_1",
                    step_name="Inspect DB sessions",
                    description="Check active, idle, and blocked sessions.",
                    purpose="Confirm likely source of pool exhaustion.",
                    tool_name="query_db_sessions",
                    expected_outcome="Session state available for diagnosis.",
                    validation_checks=["session_query_success"],
                    risk_level=RiskLevel.LOW,
                ),
                ToTPlanStep(
                    step_no=2,
                    step_id="step_2",
                    step_name="Query current metrics",
                    description="Capture latest DB and API health baseline.",
                    purpose="Establish severity before remediation.",
                    tool_name="query_metrics",
                    expected_outcome="Metrics baseline recorded.",
                    validation_checks=["metrics_freshness_ok"],
                    risk_level=RiskLevel.LOW,
                ),
                ToTPlanStep(
                    step_no=3,
                    step_id="step_3",
                    step_name="Rolling restart user-api",
                    description="Restart user-api pods to clear stale app-side DB connections.",
                    purpose="Apply low-risk remediation.",
                    tool_name="kubectl_rollout_restart",
                    expected_outcome="Application reconnects with clean pool state.",
                    validation_checks=["deployment_rollout_success"],
                    risk_level=RiskLevel.MEDIUM,
                ),
                ToTPlanStep(
                    step_no=4,
                    step_id="step_4",
                    step_name="Validate recovery",
                    description="Run health check and compare metrics against success criteria.",
                    purpose="Ensure resolution is complete.",
                    tool_name="run_health_check",
                    expected_outcome="Latency and DB connection usage normalize.",
                    validation_checks=[
                        "db_active_connections_below_80",
                        "api_latency_below_200",
                        "http_500_rate_below_1"
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
                    name="policy_alignment_check",
                    expected_condition="No high-risk DB restart for first-line remediation",
                    result=ValidationResult.PASS,
                    severity=Severity.HIGH,
                    blocking=True,
                )
            ],
        ),
        tags={"pattern": "tree-of-thought", "domain": "incident-remediation"},
    )

    print(trace.model_dump_json(indent=2))
```


## What this ToT schema captures

A ToT schema must capture more than CoT because ToT is **branching search**, not a single line of reasoning.

## Main additions over CoT

| Area             | CoT      | ToT               |
| ---------------- | -------- | ----------------- |
| Reasoning path   | single   | multiple branches |
| Alternatives     | optional | first-class       |
| Scoring          | light    | core mechanism    |
| Pruning          | no       | yes               |
| Backtracking     | no       | yes               |
| Branch selection | minimal  | explicit          |
| Graph structure  | linear   | tree / DAG-like   |


## Main enterprise models

**ThoughtNode**

Represents one reasoning node or candidate thought.

Examples:

- “restart app pods first”
- “kill long-running sessions”
- “restart DB”
- “scale DB connections”

**ThoughtBranch**

Represents one branch made of one or more nodes.

**ThoughtEdge**

Represents how nodes are related:

- expands
- refines
- branches_to
- backtracks_to
- selects

**ThoughtScore**

Captures how each node/branch is evaluated:

- feasibility
- safety
- effectiveness
- cost
- latency
- policy alignment
- confidence
- overall score

**ToTReasoning**

Stores the search process:

- branch generation
- evaluation rounds
- pruning rounds
- backtracking rounds
- final branch selection reason

**ToTOutput**

Stores the final selected branch and the execution-ready plan.


## Recommended enterprise usage

Use the ToT schema like this:

```
Incident / Goal
   ↓
ToTPlannerTrace
   ↓
Selected branch + final plan
   ↓
ToTExecutorStepTrace
   ↓
ToTValidatorTrace
   ↓
Audit / observability store
```

## Best fit use cases

This ToT schema is most useful when the agent must explore multiple strategies before acting, such as:

- incident auto-remediation
- RCA strategy generation
- cloud optimization planning
- rollback vs retry vs failover decisions
- multi-step recovery planning


## Mental model

**CoT**

`Think step by step → one path`

**ToT**

```
Generate multiple paths
→ score each path
→ prune weak paths
→ optionally backtrack
→ select best path
```

