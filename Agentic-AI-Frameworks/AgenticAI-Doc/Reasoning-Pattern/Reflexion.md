# Reflexion

Below is a complete enterprise **Reflexion schema** in Pydantic v2.

This is designed for agents that:

 - attempt a task
 - evaluate the result
 - reflect on failures or weaknesses
 - revise strategy
 - retry with improved guidance
 - store lessons for future runs

It is useful for:

 - incident auto-remediation
 - code generation agents
 - RCA agents
 - planning agents
 - execution agents
 - self-improving enterprise workflows


## Enterprise Reflexion Schema — Pydantic v2

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
    BLOCKED = "blocked"
    SKIPPED = "skipped"


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
    REFLEXION_PLANNER = "reflexion_planner"
    REFLEXION_EXECUTOR = "reflexion_executor"
    REFLEXION_REFLECTOR = "reflexion_reflector"
    REFLEXION_VALIDATOR = "reflexion_validator"


class ValidationResult(str, Enum):
    PASS = "pass"
    FAIL = "fail"
    WARN = "warn"
    UNKNOWN = "unknown"


class DecisionType(str, Enum):
    PROCEED = "proceed"
    RETRY = "retry"
    REPLAN = "replan"
    ESCALATE = "escalate"
    STOP = "stop"
    BLOCK = "block"
    FINISH = "finish"
    STORE_LESSON = "store_lesson"
    REVISE_STRATEGY = "revise_strategy"


class ReflectionOutcome(str, Enum):
    IMPROVE_AND_RETRY = "improve_and_retry"
    ACCEPT_RESULT = "accept_result"
    REPLAN = "replan"
    ESCALATE = "escalate"
    ABORT = "abort"


class LessonType(str, Enum):
    FAILURE_PATTERN = "failure_pattern"
    SUCCESS_PATTERN = "success_pattern"
    POLICY_LESSON = "policy_lesson"
    TOOLING_LESSON = "tooling_lesson"
    DIAGNOSTIC_LESSON = "diagnostic_lesson"
    REMEDIATION_LESSON = "remediation_lesson"


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
            if v < info.data["created_at"]:
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
# Attempt / Execution Models
# =========================================================

class AttemptPlanStep(BaseTraceModel):
    step_no: int = Field(ge=1)
    step_id: str
    name: str
    description: str
    tool_name: Optional[str] = None
    expected_outcome: Optional[str] = None
    risk_level: RiskLevel = RiskLevel.MEDIUM


class AttemptContext(BaseTraceModel):
    attempt_no: int = Field(ge=1)
    plan_id: Optional[str] = None
    strategy_name: Optional[str] = None
    strategy_summary: Optional[str] = None
    planned_steps: List[AttemptPlanStep] = Field(default_factory=list)


class AttemptExecutionStep(BaseTraceModel):
    step_no: int = Field(ge=1)
    thought: str
    action_name: str
    tool_name: Optional[str] = None
    arguments: Dict[str, Any] = Field(default_factory=dict)
    tool_call: Optional[ToolCall] = None
    observation_summary: Optional[str] = None
    status: TraceStatus = TraceStatus.SUCCESS
    notes: List[str] = Field(default_factory=list)


class AttemptResult(BaseTraceModel):
    summary: str
    success: bool
    partial_success: bool = False
    blockers: List[str] = Field(default_factory=list)
    observed_failures: List[str] = Field(default_factory=list)
    metrics_after_attempt: Dict[str, Union[int, float, str, bool, None]] = Field(default_factory=dict)
    validation_checks: List[ValidationCheck] = Field(default_factory=list)
    decision: Optional[DecisionRecord] = None


# =========================================================
# Reflexion Models
# =========================================================

class FailureAnalysis(BaseTraceModel):
    immediate_failure_reason: str
    root_causes: List[str] = Field(default_factory=list)
    contributing_factors: List[str] = Field(default_factory=list)
    incorrect_assumptions: List[str] = Field(default_factory=list)
    missed_signals: List[str] = Field(default_factory=list)
    policy_or_safety_issues: List[str] = Field(default_factory=list)


class ReflectionInsight(BaseTraceModel):
    insight_id: str
    category: Literal[
        "reasoning_error",
        "tool_error",
        "policy_issue",
        "insufficient_context",
        "bad_strategy",
        "bad_ordering",
        "validation_gap",
        "success_pattern"
    ]
    insight: str
    importance: float = Field(ge=0.0, le=1.0, default=0.8)
    evidence: List[str] = Field(default_factory=list)
    recommended_change: Optional[str] = None


class StrategyRevision(BaseTraceModel):
    previous_strategy: Optional[str] = None
    revised_strategy: str
    why_revision_needed: str
    changes_to_plan: List[str] = Field(default_factory=list)
    new_constraints_or_checks: List[str] = Field(default_factory=list)
    expected_improvement: Optional[str] = None


class ReflectionSummary(BaseTraceModel):
    attempt_quality: float = Field(ge=0.0, le=1.0, default=0.5)
    what_worked: List[str] = Field(default_factory=list)
    what_failed: List[str] = Field(default_factory=list)
    what_should_change: List[str] = Field(default_factory=list)
    final_reflection: str
    outcome: ReflectionOutcome


class LessonRecord(BaseTraceModel):
    lesson_id: str
    lesson_type: LessonType
    title: str
    lesson: str
    applicability: List[str] = Field(default_factory=list)
    trigger_conditions: List[str] = Field(default_factory=list)
    do_this_next_time: List[str] = Field(default_factory=list)
    avoid_this_next_time: List[str] = Field(default_factory=list)
    confidence: float = Field(ge=0.0, le=1.0, default=0.8)
    should_store_to_memory: bool = True


# =========================================================
# Reflexion Trace Models
# =========================================================

class ReflexionReasoning(BaseTraceModel):
    current_understanding: str
    reasoning_steps: List[str] = Field(default_factory=list)
    reflection_prompt_summary: Optional[str] = None
    evidence_reviewed: List[str] = Field(default_factory=list)
    confidence_before_reflection: float = Field(ge=0.0, le=1.0, default=0.5)
    confidence_after_reflection: float = Field(ge=0.0, le=1.0, default=0.7)


class ReflexionTrace(BaseTraceModel):
    metadata: TraceMetadata
    incident: IncidentContext
    goal_context: GoalContext
    attempt_context: AttemptContext
    attempt_observations: ObservationBundle = Field(default_factory=ObservationBundle)
    attempt_execution_steps: List[AttemptExecutionStep] = Field(default_factory=list)
    attempt_result: AttemptResult
    reasoning: ReflexionReasoning
    failure_analysis: Optional[FailureAnalysis] = None
    insights: List[ReflectionInsight] = Field(default_factory=list)
    strategy_revision: Optional[StrategyRevision] = None
    reflection_summary: ReflectionSummary
    lessons: List[LessonRecord] = Field(default_factory=list)
    next_decision: DecisionRecord
    risk_assessment: Optional[RiskAssessment] = None
    tags: Dict[str, str] = Field(default_factory=dict)


# =========================================================
# Separate Enterprise Models Requested
# =========================================================

class ReflexionPlannerTrace(BaseTraceModel):
    metadata: TraceMetadata
    incident: IncidentContext
    goal_context: GoalContext
    planning_attempt: AttemptContext
    input_context: ObservationBundle = Field(default_factory=ObservationBundle)
    generated_plan_steps: List[AttemptPlanStep] = Field(default_factory=list)
    attempt_result: AttemptResult
    reasoning: ReflexionReasoning
    failure_analysis: Optional[FailureAnalysis] = None
    insights: List[ReflectionInsight] = Field(default_factory=list)
    strategy_revision: Optional[StrategyRevision] = None
    reflection_summary: ReflectionSummary
    lessons: List[LessonRecord] = Field(default_factory=list)
    next_decision: DecisionRecord
    tags: Dict[str, str] = Field(default_factory=dict)


class ReflexionExecutorTrace(BaseTraceModel):
    metadata: TraceMetadata
    incident: IncidentContext
    goal_context: GoalContext
    attempt_context: AttemptContext
    initial_observations: ObservationBundle = Field(default_factory=ObservationBundle)
    execution_steps: List[AttemptExecutionStep] = Field(default_factory=list)
    attempt_result: AttemptResult
    reasoning: ReflexionReasoning
    failure_analysis: Optional[FailureAnalysis] = None
    insights: List[ReflectionInsight] = Field(default_factory=list)
    strategy_revision: Optional[StrategyRevision] = None
    reflection_summary: ReflectionSummary
    lessons: List[LessonRecord] = Field(default_factory=list)
    next_decision: DecisionRecord
    risk_assessment: Optional[RiskAssessment] = None
    tags: Dict[str, str] = Field(default_factory=dict)


class ReflexionValidatorTrace(BaseTraceModel):
    metadata: TraceMetadata
    incident: IncidentContext
    goal_context: GoalContext
    validation_target: Literal["plan", "execution_result", "reflection_result", "lesson_candidate"]
    target_id: Optional[str] = None
    observations: ObservationBundle = Field(default_factory=ObservationBundle)
    reasoning: ReflexionReasoning
    checks: List[ValidationCheck] = Field(default_factory=list)
    attempt_result: Optional[AttemptResult] = None
    failure_analysis: Optional[FailureAnalysis] = None
    insights: List[ReflectionInsight] = Field(default_factory=list)
    reflection_summary: Optional[ReflectionSummary] = None
    lessons: List[LessonRecord] = Field(default_factory=list)
    next_decision: DecisionRecord
    risk_assessment: Optional[RiskAssessment] = None
    tags: Dict[str, str] = Field(default_factory=dict)


# =========================================================
# Helper Factory Functions
# =========================================================

def make_reflexion_planner_metadata(agent_name: str = "reflexion_planner") -> TraceMetadata:
    return TraceMetadata(
        agent_name=agent_name,
        agent_role=AgentRole.REFLEXION_PLANNER,
        status=TraceStatus.SUCCESS,
    )


def make_reflexion_executor_metadata(agent_name: str = "reflexion_executor") -> TraceMetadata:
    return TraceMetadata(
        agent_name=agent_name,
        agent_role=AgentRole.REFLEXION_EXECUTOR,
        status=TraceStatus.SUCCESS,
    )


def make_reflexion_validator_metadata(agent_name: str = "reflexion_validator") -> TraceMetadata:
    return TraceMetadata(
        agent_name=agent_name,
        agent_role=AgentRole.REFLEXION_VALIDATOR,
        status=TraceStatus.SUCCESS,
    )


# =========================================================
# Example Usage
# =========================================================

if __name__ == "__main__":
    incident = IncidentContext(
        incident_id="INC_20260306_501",
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

    planner_trace = ReflexionPlannerTrace(
        metadata=make_reflexion_planner_metadata(),
        incident=incident,
        goal_context=goal,
        planning_attempt=AttemptContext(
            attempt_no=1,
            plan_id="plan_001",
            strategy_name="restart_db_first",
            strategy_summary="Use DB restart as primary remediation",
            planned_steps=[
                AttemptPlanStep(
                    step_no=1,
                    step_id="step_1",
                    name="Restart primary database",
                    description="Restart postgres-primary immediately",
                    tool_name="restart_database",
                    expected_outcome="All sessions cleared",
                    risk_level=RiskLevel.CRITICAL,
                )
            ],
        ),
        input_context=ObservationBundle(
            metrics={
                "db_active_connections_pct": 100,
                "api_latency_ms": 2400,
            },
            logs=[
                "timeout acquiring connection from pool",
                "pool exhausted for datasource primary-db",
            ],
            notes=["Past similar incidents often resolved by app restart instead"],
        ),
        generated_plan_steps=[
            AttemptPlanStep(
                step_no=1,
                step_id="step_1",
                name="Restart primary database",
                description="Restart postgres-primary immediately",
                tool_name="restart_database",
                expected_outcome="All sessions cleared",
                risk_level=RiskLevel.CRITICAL,
            )
        ],
        attempt_result=AttemptResult(
            summary="Initial plan deemed too risky for production and not aligned with least-risk-first policy.",
            success=False,
            partial_success=False,
            blockers=["High blast radius for first remediation step"],
            observed_failures=["Plan violates prod-first safety preference"],
        ),
        reasoning=ReflexionReasoning(
            current_understanding="Initial planning strategy over-prioritized effectiveness and underweighted production safety.",
            reasoning_steps=[
                "Reviewed initial plan against production constraints.",
                "Compared chosen plan to known safer alternatives.",
                "Detected policy misalignment in first-step DB restart.",
            ],
            evidence_reviewed=[
                "constraint: avoid database restart unless necessary",
                "production environment",
                "past incidents suggest app restart first",
            ],
            confidence_before_reflection=0.72,
            confidence_after_reflection=0.91,
        ),
        failure_analysis=FailureAnalysis(
            immediate_failure_reason="Initial plan used a high-risk DB restart as first action.",
            root_causes=[
                "Insufficient policy weighting in planning strategy",
                "Ignored lower-risk app-side remediation path",
            ],
            contributing_factors=[
                "Overemphasis on immediate clearance of DB sessions"
            ],
            incorrect_assumptions=[
                "Assumed DB-side action should come before app-side action"
            ],
            missed_signals=[
                "Past similar incidents resolved by app restart",
                "Constraint explicitly discouraged DB restart first"
            ],
            policy_or_safety_issues=[
                "Violates least-risk-first remediation approach in prod"
            ],
        ),
        insights=[
            ReflectionInsight(
                insight_id="insight_1",
                category="bad_strategy",
                insight="DB restart as first remediation is too aggressive for this production incident.",
                importance=0.95,
                evidence=[
                    "Prod constraint present",
                    "Safer app restart alternative available",
                ],
                recommended_change="Use app-side rolling restart as first remediation strategy.",
            ),
            ReflectionInsight(
                insight_id="insight_2",
                category="validation_gap",
                insight="Initial plan did not apply policy validation early enough.",
                importance=0.88,
                evidence=["No explicit pre-execution policy gate in attempt 1"],
                recommended_change="Add pre-execution policy validation step.",
            ),
        ],
        strategy_revision=StrategyRevision(
            previous_strategy="restart_db_first",
            revised_strategy="restart_app_first_with_validation",
            why_revision_needed="Need safer, policy-aligned first remediation path.",
            changes_to_plan=[
                "Replace DB restart with rolling restart of user-api",
                "Add explicit policy check before execution",
                "Add health validation after restart",
            ],
            new_constraints_or_checks=[
                "No DB restart unless app restart fails and escalation condition met"
            ],
            expected_improvement="Lower blast radius and better compliance with production guardrails.",
        ),
        reflection_summary=ReflectionSummary(
            attempt_quality=0.34,
            what_worked=[],
            what_failed=[
                "Initial strategy selection",
                "Risk weighting",
                "Policy alignment",
            ],
            what_should_change=[
                "Prefer app-side remediation",
                "Add explicit safety validation",
            ],
            final_reflection="The initial plan was effective in theory but unsafe in practice for production. The revised plan should start with lower-risk application-side remediation.",
            outcome=ReflectionOutcome.REPLAN,
        ),
        lessons=[
            LessonRecord(
                lesson_id="lesson_1",
                lesson_type=LessonType.POLICY_LESSON,
                title="Avoid DB restart as first remediation in prod pool exhaustion incidents",
                lesson="When DB pool exhaustion affects an app service in prod, prefer app-side restart before DB restart unless DB-side evidence is dominant.",
                applicability=[
                    "DB pool exhaustion",
                    "app-to-db connection incidents",
                    "production remediation planning",
                ],
                trigger_conditions=[
                    "prod environment",
                    "available lower-risk app remediation",
                ],
                do_this_next_time=[
                    "Check app-side stale connections",
                    "Prefer rolling restart of app service first",
                ],
                avoid_this_next_time=[
                    "Immediate DB restart as first action"
                ],
                confidence=0.93,
                should_store_to_memory=True,
            )
        ],
        next_decision=DecisionRecord(
            decision="Replan using safer app-side remediation strategy.",
            decision_type=DecisionType.REPLAN,
            rationale="Reflection identified a safer and policy-aligned remediation sequence.",
            selected_option="restart_app_first_with_validation",
            rejected_options=["restart_db_first"],
            confidence=0.92,
        ),
        tags={"pattern": "reflexion", "phase": "planning"},
    )

    executor_trace = ReflexionExecutorTrace(
        metadata=make_reflexion_executor_metadata(),
        incident=incident,
        goal_context=goal,
        attempt_context=AttemptContext(
            attempt_no=2,
            plan_id="plan_002",
            strategy_name="restart_app_first_with_validation",
            strategy_summary="Use app rolling restart and validate recovery",
            planned_steps=[
                AttemptPlanStep(
                    step_no=1,
                    step_id="step_1",
                    name="Rolling restart user-api",
                    description="Restart user-api pods",
                    tool_name="kubectl_rollout_restart",
                    expected_outcome="Fresh app connections",
                    risk_level=RiskLevel.MEDIUM,
                ),
                AttemptPlanStep(
                    step_no=2,
                    step_id="step_2",
                    name="Run health check",
                    description="Validate post-remediation recovery",
                    tool_name="run_health_check",
                    expected_outcome="Metrics normalize",
                    risk_level=RiskLevel.LOW,
                ),
            ],
        ),
        initial_observations=ObservationBundle(
            metrics={
                "db_active_connections_pct": 100,
                "api_latency_ms": 2400,
                "http_500_rate_pct": 8.5,
            },
            logs=[
                "timeout acquiring connection from pool",
                "many idle sessions tied to user-api pods",
            ],
        ),
        execution_steps=[
            AttemptExecutionStep(
                step_no=1,
                thought="Use safer app-side remediation before any DB-side escalation.",
                action_name="rolling_restart_user_api",
                tool_name="kubectl_rollout_restart",
                arguments={"deployment": "user-api", "namespace": "prod"},
                tool_call=ToolCall(
                    tool_name="kubectl_rollout_restart",
                    arguments={"deployment": "user-api", "namespace": "prod"},
                    status=TraceStatus.SUCCESS,
                    result_summary="Deployment restarted successfully",
                ),
                observation_summary="Rollout succeeded, but latency improved only partially at first check.",
                status=TraceStatus.SUCCESS,
                notes=["Need post-restart health validation"],
            ),
            AttemptExecutionStep(
                step_no=2,
                thought="Validate whether first remediation fully resolved the incident.",
                action_name="run_post_health_check",
                tool_name="run_health_check",
                arguments={"service": "user-api", "environment": "prod"},
                tool_call=ToolCall(
                    tool_name="run_health_check",
                    arguments={"service": "user-api", "environment": "prod"},
                    status=TraceStatus.SUCCESS,
                    result_summary="Latency 310 ms, DB connections 68%, HTTP 500 rate 0.7%",
                ),
                observation_summary="Most metrics improved, but latency still above target.",
                status=TraceStatus.SUCCESS,
                notes=["Partial success only"],
            ),
        ],
        attempt_result=AttemptResult(
            summary="App restart reduced pool pressure and errors, but latency remains above target.",
            success=False,
            partial_success=True,
            blockers=[],
            observed_failures=["API latency still above 200 ms"],
            metrics_after_attempt={
                "db_active_connections_pct": 68,
                "api_latency_ms": 310,
                "http_500_rate_pct": 0.7,
            },
            validation_checks=[
                ValidationCheck(
                    name="db_connections_recovered",
                    expected_condition="DB active connections below 80%",
                    actual_value="68%",
                    result=ValidationResult.PASS,
                    severity=Severity.HIGH,
                    blocking=True,
                ),
                ValidationCheck(
                    name="api_latency_recovered",
                    expected_condition="API latency below 200 ms",
                    actual_value="310 ms",
                    result=ValidationResult.FAIL,
                    severity=Severity.HIGH,
                    blocking=True,
                ),
            ],
        ),
        reasoning=ReflexionReasoning(
            current_understanding="The revised strategy partially worked, but one success criterion remains unmet.",
            reasoning_steps=[
                "Compared before/after metrics.",
                "Identified partial improvement in DB and error rate.",
                "Detected residual latency issue requiring refinement.",
            ],
            evidence_reviewed=[
                "db_active_connections_pct improved from 100 to 68",
                "http_500_rate improved from 8.5 to 0.7",
                "latency still 310 ms",
            ],
            confidence_before_reflection=0.79,
            confidence_after_reflection=0.89,
        ),
        failure_analysis=FailureAnalysis(
            immediate_failure_reason="Primary remediation improved system health but did not fully restore latency target.",
            root_causes=[
                "Residual performance bottleneck remains after connection cleanup"
            ],
            contributing_factors=[
                "Possible slow queries or warm-up effects after restart"
            ],
            incorrect_assumptions=[
                "Assumed app restart alone would fully resolve latency"
            ],
            missed_signals=[
                "Latency may have secondary causes beyond connection saturation"
            ],
            policy_or_safety_issues=[],
        ),
        insights=[
            ReflectionInsight(
                insight_id="insight_3",
                category="insufficient_context",
                insight="Post-restart latency remained high, indicating additional diagnosis is required.",
                importance=0.90,
                evidence=[
                    "Latency still 310 ms after restart",
                    "DB connections already normalized",
                ],
                recommended_change="Collect slow query and service performance evidence before next action.",
            ),
            ReflectionInsight(
                insight_id="insight_4",
                category="success_pattern",
                insight="App restart is effective for quickly reducing pool saturation and error rate.",
                importance=0.87,
                evidence=[
                    "DB connections reduced to 68%",
                    "HTTP 500 rate dropped to 0.7%",
                ],
                recommended_change="Retain app restart as first-line remediation for similar incidents.",
            ),
        ],
        strategy_revision=StrategyRevision(
            previous_strategy="restart_app_first_with_validation",
            revised_strategy="restart_app_then_diagnose_residual_latency",
            why_revision_needed="Need targeted follow-up diagnostics for remaining latency issue.",
            changes_to_plan=[
                "Add slow-query inspection",
                "Add app latency breakdown check",
            ],
            new_constraints_or_checks=[
                "Do not escalate to DB restart without DB-side evidence"
            ],
            expected_improvement="More precise next action and reduced unnecessary escalation risk.",
        ),
        reflection_summary=ReflectionSummary(
            attempt_quality=0.72,
            what_worked=[
                "Reduced DB pool pressure",
                "Reduced HTTP 500 rate",
                "Followed low-risk-first strategy",
            ],
            what_failed=[
                "Did not fully restore latency target",
            ],
            what_should_change=[
                "Investigate residual latency before next remediation",
            ],
            final_reflection="The revised remediation strategy was directionally correct and safe, but incomplete. A focused diagnostic follow-up is needed rather than immediate escalation.",
            outcome=ReflectionOutcome.IMPROVE_AND_RETRY,
        ),
        lessons=[
            LessonRecord(
                lesson_id="lesson_2",
                lesson_type=LessonType.REMEDIATION_LESSON,
                title="App restart may partially resolve DB pool incidents but not all residual latency",
                lesson="When app restart reduces DB pool saturation but latency remains high, follow with targeted latency diagnostics instead of repeating the same action.",
                applicability=[
                    "partial recovery after app restart",
                    "DB saturation incidents with lingering latency",
                ],
                trigger_conditions=[
                    "DB recovered but latency still above threshold",
                ],
                do_this_next_time=[
                    "Check slow queries",
                    "Check app-side latency contributors",
                ],
                avoid_this_next_time=[
                    "Repeating restart without new evidence"
                ],
                confidence=0.89,
                should_store_to_memory=True,
            )
        ],
        next_decision=DecisionRecord(
            decision="Retry with refined strategy and additional diagnostics.",
            decision_type=DecisionType.RETRY,
            rationale="The attempt partially succeeded and reflection identified a better next step.",
            selected_option="restart_app_then_diagnose_residual_latency",
            rejected_options=["repeat_restart", "restart_db_without_evidence"],
            confidence=0.90,
        ),
        risk_assessment=RiskAssessment(
            risk_level=RiskLevel.MEDIUM,
            blast_radius="user-api service only so far",
            risk_factors=["residual latency impacting users"],
            mitigations=["diagnose before escalating"],
        ),
        tags={"pattern": "reflexion", "phase": "execution"},
    )

    validator_trace = ReflexionValidatorTrace(
        metadata=make_reflexion_validator_metadata(),
        incident=incident,
        goal_context=goal,
        validation_target="reflection_result",
        target_id="attempt_2_reflection",
        observations=ObservationBundle(
            metrics={
                "db_active_connections_pct": 68,
                "api_latency_ms": 310,
                "http_500_rate_pct": 0.7,
            },
            notes=[
                "Reflection recommends targeted diagnostics before escalation"
            ],
        ),
        reasoning=ReflexionReasoning(
            current_understanding="Need to validate whether the reflection outcome is justified and safe.",
            reasoning_steps=[
                "Check whether partial success is accurately identified.",
                "Check whether retry decision is safer than escalation.",
                "Check whether proposed lesson is supported by evidence.",
            ],
            evidence_reviewed=[
                "DB improved",
                "error rate improved",
                "latency still above target",
                "no evidence justifying DB restart yet",
            ],
            confidence_before_reflection=0.84,
            confidence_after_reflection=0.91,
        ),
        checks=[
            ValidationCheck(
                name="partial_success_classification",
                expected_condition="Attempt should be classified as partial success, not full success",
                actual_value="partial_success=True",
                result=ValidationResult.PASS,
                severity=Severity.HIGH,
                blocking=True,
            ),
            ValidationCheck(
                name="retry_over_escalate",
                expected_condition="Retry with added diagnostics is safer than escalation without DB-side evidence",
                actual_value="retry selected",
                result=ValidationResult.PASS,
                severity=Severity.HIGH,
                blocking=True,
            ),
            ValidationCheck(
                name="lesson_supported",
                expected_condition="Lesson must be grounded in attempt evidence",
                actual_value="supported by before/after metrics",
                result=ValidationResult.PASS,
                severity=Severity.MEDIUM,
                blocking=False,
            ),
        ],
        attempt_result=AttemptResult(
            summary="Validator confirms partial success and supports refined retry path.",
            success=False,
            partial_success=True,
            observed_failures=["Residual latency remains"],
        ),
        failure_analysis=FailureAnalysis(
            immediate_failure_reason="Residual latency unresolved after first low-risk remediation.",
            root_causes=["Secondary performance issue likely remains"],
        ),
        insights=[
            ReflectionInsight(
                insight_id="insight_5",
                category="success_pattern",
                insight="Reflection correctly distinguishes between partial recovery and full recovery.",
                importance=0.84,
                evidence=["DB and errors recovered, latency did not"],
                recommended_change="Keep validation strict against all success criteria.",
            )
        ],
        reflection_summary=ReflectionSummary(
            attempt_quality=0.80,
            what_worked=["Correct partial-success identification"],
            what_failed=[],
            what_should_change=["Proceed with refined retry plan"],
            final_reflection="The reflection result is sound and should be approved for the next retry cycle.",
            outcome=ReflectionOutcome.IMPROVE_AND_RETRY,
        ),
        lessons=[
            LessonRecord(
                lesson_id="lesson_3",
                lesson_type=LessonType.DIAGNOSTIC_LESSON,
                title="Residual latency requires focused follow-up diagnostics",
                lesson="If latency remains after pool recovery, switch to targeted diagnosis instead of broad escalation.",
                applicability=["incident remediation refinement"],
                trigger_conditions=["latency above threshold after partial success"],
                do_this_next_time=["inspect slow queries", "inspect app latency breakdown"],
                avoid_this_next_time=["premature escalation"],
                confidence=0.88,
                should_store_to_memory=True,
            )
        ],
        next_decision=DecisionRecord(
            decision="Approve retry with refined diagnostic strategy.",
            decision_type=DecisionType.APPROVE,
            rationale="Reflection output is evidence-based, safe, and directionally correct.",
            confidence=0.92,
        ),
        risk_assessment=RiskAssessment(
            risk_level=RiskLevel.LOW,
            blast_radius="validation only",
            mitigations=["strict success criteria", "no escalation without evidence"],
        ),
        tags={"pattern": "reflexion", "phase": "validation"},
    )

    print("=== ReflexionPlannerTrace ===")
    print(planner_trace.model_dump_json(indent=2))
    print("\n=== ReflexionExecutorTrace ===")
    print(executor_trace.model_dump_json(indent=2))
    print("\n=== ReflexionValidatorTrace ===")
    print(validator_trace.model_dump_json(indent=2))
```

## What each model is for

`ReflexionPlannerTrace`

Use this when the **planner creates a plan, then reflects on whether that plan is weak, unsafe, incomplete, or poorly aligned with constraints**.

Typical planner reflexion:

 - initial plan too risky
 - missed a dependency
 - ignored policy
 - better lower-risk sequence exists


`ReflexionValidatorTrace`

Use this when a **validator reviews whether the reflection result itself is valid**.

Typical validator checks:

- was failure analysis grounded in evidence
- is retry safer than escalation
- is the lesson worth storing
- is the revised strategy justified


## Recommended enterprise sequence

Use Reflexion like this:

```
Incident / Goal
   ↓
Planner / Executor Attempt
   ↓
Measure Result
   ↓
Reflexion
   ├─ what failed
   ├─ why it failed
   ├─ what to change
   └─ what lesson to store
   ↓
Validator
   ↓
Retry / Replan / Escalate / Finish
```

Or with the trace models:

```
ReflexionPlannerTrace
   ↓
ReflexionExecutorTrace
   ↓
ReflexionValidatorTrace
   ↓
Memory / Audit / Observability Store
```

## How Reflexion differs from ReAct, CoT, ToT, GoT

| Pattern   | Main role                           |
| --------- | ----------------------------------- |
| CoT       | linear reasoning                    |
| ToT       | explore multiple branches           |
| GoT       | connect and merge thought graphs    |
| ReAct     | think-act-observe loop              |
| Reflexion | self-critique, learn, revise, retry |


The easiest way to understand:

- **Reflexion = self-improvement**
- **Validator = correctness / safety check**


## How Reflexion differs from ReAct, CoT, ToT, GoT

| Pattern   | Main role                           |
| --------- | ----------------------------------- |
| CoT       | linear reasoning                    |
| ToT       | explore multiple branches           |
| GoT       | connect and merge thought graphs    |
| ReAct     | think-act-observe loop              |
| Reflexion | self-critique, learn, revise, retry |


So Reflexion is usually not the first reasoning pattern.
It is a post-attempt improvement loop.


## Practical mental model

```
CoT     = think step by step
ToT     = explore multiple paths
GoT     = connect many ideas
ReAct   = think and act in a loop
Reflexion = review your own attempt, learn, revise, retry
```

## 1. Simple intuition

**Reflexion**

The agent **looks at its own attempt and learns how to improve.**

“What went wrong? What should I do better next time?”

**Validator**

A separate component **checks if the output is correct, safe, or policy compliant**.

“Is this result acceptable?”

## 2. Core difference

| Aspect          | Reflexion                      | Validator                      |
| --------------- | ------------------------------ | ------------------------------ |
| Purpose         | Improve the next attempt       | Verify correctness/safety      |
| Focus           | learning and strategy revision | pass/fail decision             |
| Timing          | after attempt but before retry | after step or final output     |
| Who performs it | same agent or reflection agent | independent validation agent   |
| Output          | insights, strategy revision    | pass / fail / approve / reject |
| Effect          | modifies next plan             | gates execution or completion  |


## 3. Conceptual flow

**Without Reflexion**

```
Plan
 ↓
Execute
 ↓
Validate
 ↓
Finish
```

If validation fails → human intervention or replan.


**With Reflexion**

```
Plan
 ↓
Execute
 ↓
Validate
 ↓
Reflexion
 ↓
Retry / Improve
```

## 4. Real enterprise example

**Incident**

`Database connection pool exhausted`

## Step 1 — Executor

**Agent performs action:**

```Restart user-api pods```


## Step 2 — Validator

Validator checks success criteria.

Example checks:

```
DB active connections < 80%
API latency < 200 ms
HTTP 500 < 1%
```

Result:

```
DB connections = 68% ✔
HTTP 500 = 0.7% ✔
Latency = 310 ms ✖
```

Validator result: `FAIL`



## Step 3 — Reflexion

Now the agent analyzes the failure.


Example reflexion:

```
Observation:
DB pool recovered but latency remains high.

Reflection:
Restart fixed connection pressure but not performance.

Insight:
Another root cause likely exists.

Improvement strategy:
Investigate slow queries or app latency.
```

Reflexion output:

```
New plan:
1. Inspect slow queries
2. Check service latency breakdown
3. Then decide remediation
```
**With Reflexion**

```
Plan
 ↓
Execute
 ↓
Validate
 ↓
Reflexion
 ↓
Retry / Improve
```

Now the system **learns from the failure automatically**.


## 4. Real enterprise example

**Incident**

`Database connection pool exhausted`

## Step 1 — Executor

Agent performs action:

`Restart user-api pods`

## Step 2 — Validator

Validator checks success criteria.

Example checks:

```
DB active connections < 80%
API latency < 200 ms
HTTP 500 < 1%
```

Result:

```
DB connections = 68% ✔
HTTP 500 = 0.7% ✔
Latency = 310 ms ✖
```

Validator result:

`FAIL`

Validator does NOT explain improvement strategy.

It only says:

"Goal not fully achieved."

## Step 3 — Reflexion

Now the agent analyzes the failure.

Example reflexion:

```
Observation:
DB pool recovered but latency remains high.

Reflection:
Restart fixed connection pressure but not performance.

Insight:
Another root cause likely exists.

Improvement strategy:
Investigate slow queries or app latency.
```

Reflexion output:

```
New plan:
1. Inspect slow queries
2. Check service latency breakdown
3. Then decide remediation
```

## 5. Role in the architecture

**Validator is a gatekeeper**

Ensures:

- safety
- correctness
- policy compliance
- success criteria


Example checks:

```
Did remediation violate policy?
Did the system recover?
Did we exceed risk threshold?
```

**Reflexion is a teacher**

It asks:

```
Why did the attempt fail?
What assumptions were wrong?
What strategy should change?
What lesson should we store?
```

It improves the next attempt.

## 6. Comparison in tabular form

| Feature          | Reflexion                   | Validator          |
| ---------------- | --------------------------- | ------------------ |
| Main goal        | learning                    | correctness        |
| Output type      | insight + strategy revision | pass / fail        |
| Used for         | retry improvement           | execution gating   |
| Produces lessons | yes                         | no                 |
| Uses history     | yes                         | usually no         |
| Focus            | reasoning quality           | result correctness |


## 7. Mental model

Think of a student solving math problems.

Validator = teacher grading

```
Answer: 42
Teacher: ❌ Incorrect
```

Reflexion = student self-analysis

```
Why was I wrong?
Oh — I applied the wrong formula.
Next time I should use formula X.
```

## 8. Where each is used in agent pipelines

Typical enterprise pipeline:

```
Goal
 ↓
Planning
 ↓
Execution
 ↓
Validation
 ↓
Reflexion (if needed)
 ↓
Retry / Replan
```
