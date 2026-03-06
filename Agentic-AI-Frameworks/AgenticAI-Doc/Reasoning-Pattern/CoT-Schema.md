# CoT Schema

Below is a complete enterprise CoT JSON schema in Pydantic v2 with separate models for:

- `PlannerCoTTrace`
- `ExecutorCoTTrace`
- `ValidatorTrace`

This is designed for enterprise Agentic AI systems, especially for:

- incident auto-remediation
- autonomous workflows
- auditability
- observability
- replay/debugging


## Enterprise CoT Schema — Pydantic v2

```
from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, List, Literal, Optional, Union
from uuid import uuid4

from pydantic import BaseModel, Field, ConfigDict, field_validator


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
    PLANNER = "planner"
    EXECUTOR = "executor"
    VALIDATOR = "validator"


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


class Hypothesis(BaseTraceModel):
    hypothesis: str
    confidence: float = Field(ge=0.0, le=1.0)
    supporting_evidence: List[str] = Field(default_factory=list)
    conflicting_evidence: List[str] = Field(default_factory=list)
    decision: Optional[str] = None


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
# Planner Models
# =========================================================

class PlanOption(BaseTraceModel):
    option_id: str
    strategy_name: str
    description: str
    pros: List[str] = Field(default_factory=list)
    cons: List[str] = Field(default_factory=list)
    estimated_risk: RiskLevel = RiskLevel.MEDIUM
    estimated_latency_seconds: Optional[int] = None
    estimated_cost: Optional[float] = None
    suitability_score: float = Field(ge=0.0, le=1.0, default=0.5)


class PlanStep(BaseTraceModel):
    step_no: int = Field(ge=1)
    step_id: str
    name: str
    description: str
    purpose: Optional[str] = None
    tool_name: Optional[str] = None
    action_type: Optional[str] = None
    inputs_required: List[str] = Field(default_factory=list)
    dependencies: List[str] = Field(default_factory=list)
    expected_outcome: Optional[str] = None
    success_conditions: List[str] = Field(default_factory=list)
    rollback_step: Optional[str] = None
    risk_level: RiskLevel = RiskLevel.MEDIUM
    validation_checks: List[str] = Field(default_factory=list)


class PlannerReasoning(BaseTraceModel):
    goal_understanding: str
    task_decomposition: List[str] = Field(default_factory=list)
    dependency_analysis: List[str] = Field(default_factory=list)
    constraints_analysis: List[str] = Field(default_factory=list)
    assumptions: List[str] = Field(default_factory=list)
    options_considered: List[PlanOption] = Field(default_factory=list)
    hypotheses: List[Hypothesis] = Field(default_factory=list)
    reasoning_steps: List[str] = Field(default_factory=list)
    selected_strategy: str
    why_selected: str


class PlannerOutput(BaseTraceModel):
    plan_summary: str
    steps: List[PlanStep] = Field(default_factory=list)
    decision: DecisionRecord
    risk_assessment: RiskAssessment
    required_tools: List[ToolReference] = Field(default_factory=list)
    pre_execution_checks: List[ValidationCheck] = Field(default_factory=list)


class PlannerCoTTrace(BaseTraceModel):
    metadata: TraceMetadata
    incident: IncidentContext
    goal_context: GoalContext
    input_context: ObservationBundle = Field(default_factory=ObservationBundle)
    reasoning: PlannerReasoning
    output: PlannerOutput
    validation_checks: List[ValidationCheck] = Field(default_factory=list)
    tags: Dict[str, str] = Field(default_factory=dict)


# =========================================================
# Executor Models
# =========================================================

class ExecutionStepContext(BaseTraceModel):
    current_step_no: int = Field(ge=1)
    current_step_id: str
    current_step_name: str
    current_step_description: str
    tool_name: Optional[str] = None
    planned_expected_outcome: Optional[str] = None


class ExecutionReasoning(BaseTraceModel):
    step_understanding: str
    observation_analysis: str
    hypotheses: List[Hypothesis] = Field(default_factory=list)
    reasoning_steps: List[str] = Field(default_factory=list)
    action_decision: str
    decision_reason: str
    safety_considerations: List[str] = Field(default_factory=list)
    fallback_options: List[str] = Field(default_factory=list)


class ActionPayload(BaseTraceModel):
    tool_name: str
    arguments: Dict[str, Any] = Field(default_factory=dict)
    expected_outcome: Optional[str] = None
    timeout_seconds: Optional[int] = None
    dry_run: bool = False


class ExecutionOutcome(BaseTraceModel):
    action_taken: ActionPayload
    tool_call: Optional[ToolCall] = None
    observed_result: str
    outcome_status: TraceStatus = TraceStatus.SUCCESS
    next_recommendation: Optional[str] = None
    should_continue: bool = True
    should_replan: bool = False
    should_escalate: bool = False


class ExecutorCoTTrace(BaseTraceModel):
    metadata: TraceMetadata
    incident: IncidentContext
    goal_context: GoalContext
    step_context: ExecutionStepContext
    observations: ObservationBundle = Field(default_factory=ObservationBundle)
    reasoning: ExecutionReasoning
    risk_assessment: RiskAssessment
    output: ExecutionOutcome
    validation_checks: List[ValidationCheck] = Field(default_factory=list)
    tags: Dict[str, str] = Field(default_factory=dict)


# =========================================================
# Validator Models
# =========================================================

class ValidationTarget(BaseTraceModel):
    target_type: Literal["plan", "step", "action", "result", "policy", "safety"]
    target_id: Optional[str] = None
    target_name: Optional[str] = None
    description: Optional[str] = None


class ValidatorReasoning(BaseTraceModel):
    validation_scope: str
    checks_considered: List[str] = Field(default_factory=list)
    evidence_reviewed: List[str] = Field(default_factory=list)
    reasoning_steps: List[str] = Field(default_factory=list)
    issues_found: List[str] = Field(default_factory=list)
    final_assessment: str


class ValidationSummary(BaseTraceModel):
    overall_result: ValidationResult
    passed_checks: int = 0
    failed_checks: int = 0
    warning_checks: int = 0
    blocking_failures: List[str] = Field(default_factory=list)
    non_blocking_warnings: List[str] = Field(default_factory=list)
    recommendation: DecisionType
    recommendation_reason: str


class ValidatorTrace(BaseTraceModel):
    metadata: TraceMetadata
    incident: IncidentContext
    goal_context: GoalContext
    validation_target: ValidationTarget
    observations: ObservationBundle = Field(default_factory=ObservationBundle)
    reasoning: ValidatorReasoning
    checks: List[ValidationCheck] = Field(default_factory=list)
    summary: ValidationSummary
    risk_assessment: Optional[RiskAssessment] = None
    tags: Dict[str, str] = Field(default_factory=dict)


# =========================================================
# Example Factory Helpers
# =========================================================

def make_planner_metadata(agent_name: str = "incident_planner") -> TraceMetadata:
    return TraceMetadata(
        agent_name=agent_name,
        agent_role=AgentRole.PLANNER,
        status=TraceStatus.SUCCESS,
    )


def make_executor_metadata(agent_name: str = "incident_executor") -> TraceMetadata:
    return TraceMetadata(
        agent_name=agent_name,
        agent_role=AgentRole.EXECUTOR,
        status=TraceStatus.SUCCESS,
    )


def make_validator_metadata(agent_name: str = "incident_validator") -> TraceMetadata:
    return TraceMetadata(
        agent_name=agent_name,
        agent_role=AgentRole.VALIDATOR,
        status=TraceStatus.SUCCESS,
    )


# =========================================================
# Example Usage
# =========================================================

if __name__ == "__main__":
    incident = IncidentContext(
        incident_id="INC_20260306_001",
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
            "production changes must be logged",
            "prefer app-side remediation first",
        ],
    )

    planner_trace = PlannerCoTTrace(
        metadata=make_planner_metadata(),
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
                "Past similar resolution used app restart",
            ],
        ),
        reasoning=PlannerReasoning(
            goal_understanding="Production user-api is degraded due to exhausted database connections causing latency and errors.",
            task_decomposition=[
                "inspect DB session state",
                "confirm severity through metrics",
                "apply low-risk remediation",
                "validate recovery",
            ],
            dependency_analysis=[
                "DB/session inspection should happen before remediation",
                "health validation should happen after remediation",
            ],
            constraints_analysis=[
                "DB restart is higher risk in prod",
                "prefer app-side remediation first",
            ],
            assumptions=[
                "Application-side stale connections may be contributing",
            ],
            options_considered=[
                PlanOption(
                    option_id="opt_1",
                    strategy_name="restart_app_first",
                    description="Restart user-api pods before DB-side actions",
                    pros=["low blast radius", "common fix for stale app pools"],
                    cons=["may not fix DB-side blocked sessions"],
                    estimated_risk=RiskLevel.MEDIUM,
                    suitability_score=0.87,
                ),
                PlanOption(
                    option_id="opt_2",
                    strategy_name="restart_db",
                    description="Restart primary database",
                    pros=["may clear all stuck sessions"],
                    cons=["high risk in prod", "possible wider impact"],
                    estimated_risk=RiskLevel.CRITICAL,
                    suitability_score=0.32,
                ),
            ],
            hypotheses=[
                Hypothesis(
                    hypothesis="Application connection leak or stale pool state",
                    confidence=0.82,
                    supporting_evidence=[
                        "DB connections saturated",
                        "API latency high",
                        "similar previous incidents",
                    ],
                )
            ],
            reasoning_steps=[
                "Symptoms indicate DB connection pool saturation.",
                "Need low-risk diagnostics and remediation.",
                "App restart is safer than DB restart.",
            ],
            selected_strategy="Inspect sessions and metrics, then perform rolling restart of user-api pods if consistent with evidence.",
            why_selected="This approach minimizes blast radius and aligns with production safety constraints.",
        ),
        output=PlannerOutput(
            plan_summary="Use diagnostics to confirm the issue, then perform app-side rolling restart and validate recovery.",
            steps=[
                PlanStep(
                    step_no=1,
                    step_id="step_1",
                    name="Inspect DB sessions",
                    description="Query database session state to identify active, idle, and blocked connections.",
                    purpose="Determine likely source of pool exhaustion.",
                    tool_name="query_db_sessions",
                    expected_outcome="Session state breakdown available.",
                    success_conditions=["Session inventory retrieved"],
                    risk_level=RiskLevel.LOW,
                    validation_checks=["DB session query returns valid data"],
                ),
                PlanStep(
                    step_no=2,
                    step_id="step_2",
                    name="Query current metrics",
                    description="Capture latest DB and API health metrics.",
                    purpose="Establish baseline before remediation.",
                    tool_name="query_metrics",
                    expected_outcome="Current metrics baseline recorded.",
                    success_conditions=["Metrics baseline available"],
                    risk_level=RiskLevel.LOW,
                    validation_checks=["Metrics freshness acceptable"],
                ),
                PlanStep(
                    step_no=3,
                    step_id="step_3",
                    name="Rolling restart user-api",
                    description="Perform rolling restart of user-api pods.",
                    purpose="Clear stale application-side DB connections.",
                    tool_name="kubectl_rollout_restart",
                    expected_outcome="Application pods reconnect with clean pool state.",
                    success_conditions=["Pods restarted successfully"],
                    risk_level=RiskLevel.MEDIUM,
                    validation_checks=["Deployment rollout successful"],
                ),
            ],
            decision=DecisionRecord(
                decision="Proceed with app-side remediation after diagnostics.",
                decision_type=DecisionType.PROCEED,
                rationale="Safer and likely effective based on evidence.",
                selected_option="restart_app_first",
                rejected_options=["restart_db"],
                confidence=0.86,
            ),
            risk_assessment=RiskAssessment(
                risk_level=RiskLevel.MEDIUM,
                blast_radius="user-api deployment only",
                risk_factors=["production environment", "customer-facing service"],
                mitigations=["rolling restart", "post-check validation"],
                approval_required=False,
            ),
            required_tools=[
                ToolReference(tool_name="query_db_sessions"),
                ToolReference(tool_name="query_metrics"),
                ToolReference(tool_name="kubectl_rollout_restart"),
            ],
            pre_execution_checks=[
                ValidationCheck(
                    name="prod_rbac_check",
                    expected_condition="executor has RBAC permission for rollout restart",
                    result=ValidationResult.PASS,
                    severity=Severity.HIGH,
                    blocking=True,
                )
            ],
        ),
        validation_checks=[
            ValidationCheck(
                name="plan_safety_check",
                expected_condition="no DB restart unless necessary",
                result=ValidationResult.PASS,
                severity=Severity.HIGH,
                blocking=True,
            )
        ],
        tags={"domain": "incident-remediation"},
    )

    print(planner_trace.model_dump_json(indent=2))
    ```

