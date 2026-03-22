# ReAct (Reason + Act)

**ReAct** (Reason + Act)

`Reason → Act → Observe → Repeat`

It is one of the **most widely used agent patterns** in real AI agents.

ReAct combines:

- **reasoning** to decide what to do next
- **action** to call a tool or perform an operation
- **observation** to read the tool result
- then loops again until done

## 1. Core idea

Instead of only thinking or only acting, the agent does both in a loop.

```
Question / Goal
   ↓
Reason
   ↓
Act
   ↓
Observe
   ↓
Reason
   ↓
Act
   ↓
Observe
   ↓
Finish
```

This makes ReAct very useful for:

- tool-using agents
- search agents
- incident remediation agents
- RAG agents
- DevOps agents
- support agents


## 2. Why ReAct is important

Without ReAct, an agent may:

- reason too much without using tools
- act too early without enough evidence
- fail to adapt after seeing tool results

ReAct solves this by making the agent:

- think before action
- use tools
- learn from tool outputs
- revise next steps dynamically


## 3. Standard ReAct loop

The classic loop is:

```
Thought
Action
Observation
Thought
Action
Observation
Final Answer
```

In enterprise wording:

```
Reason
Action
Observation
Repeat
```

## 4. Simple example

**User asks**

`What is the weather in Bangalore?`

**ReAct flow**

```
Reason:
I need current weather data, so I should use a weather tool.

Action:
get_weather("Bangalore")

Observation:
28°C, cloudy

Reason:
I have the answer now.

Final Answer:
The current weather in Bangalore is 28°C and cloudy.
```

## 5. Enterprise incident example

**Incident**

`Database connection pool exhausted`

**Goal**

`Restore healthy database connectivity for user-api`

**ReAct flow**

```
Reason:
I should first inspect DB connection usage.

Action:
query_metrics(service="user-api")

Observation:
db_active_connections_pct = 100
api_latency_ms = 2400

Reason:
The DB connection pool is saturated. I should inspect DB sessions.

Action:
query_db_sessions(database="postgres-primary")

Observation:
many idle sessions tied to app pods

Reason:
Application-side stale connections are likely. Rolling restart is safer than DB restart.

Action:
kubectl_rollout_restart(deployment="user-api", namespace="prod")

Observation:
connections dropped to 42
latency dropped to 120 ms

Reason:
Success criteria are met.

Final Answer:
Incident mitigated by rolling restart of user-api pods.
```

## 6. ReAct structure

| Step    | Meaning                     |
| ------- | --------------------------- |
| Reason  | think about current state   |
| Act     | call tool / take step       |
| Observe | inspect result              |
| Repeat  | continue until goal reached |


## 7. ReAct vs CoT

| Aspect           | CoT               | ReAct                    |
| ---------------- | ----------------- | ------------------------ |
| Main purpose     | reasoning         | reasoning + tool use     |
| Tool interaction | optional          | core part                |
| Flow             | think then answer | think, act, observe loop |
| Best for         | analysis          | dynamic tasks            |


## Simple difference

**CoT**

`Think step by step → answer`

**ReAct**

`Think → use tool → inspect result → think again`

## 8. ReAct vs ToT

| Aspect     | ReAct                   | ToT                                   |
| ---------- | ----------------------- | ------------------------------------- |
| Structure  | sequential loop         | branching search                      |
| Main focus | tool-driven interaction | exploring multiple reasoning branches |
| Best for   | execution agents        | planner / strategy agents             |


## 9. ReAct in agent architecture

ReAct is most often used in the **execution layer**.

```
Goal
 ↓
Planning
 ↓
ReAct Executor
   ├─ Reason
   ├─ Act
   ├─ Observe
   └─ Repeat
 ↓
Validation
 ↓
Finish
```

So:

- **Planner** may use CoT / ToT / GoT
- **Executor** often uses ReAct

## 10. ReAct prompt template

Here is a practical ReAct system prompt.

```
You are an enterprise autonomous execution agent.

Your job is to solve the task by alternating between reasoning and tool use.

Rules:
1. Think about the current situation before taking an action.
2. Use available tools when needed.
3. After each tool call, inspect the observation carefully.
4. Decide the next best action based on the latest observation.
5. Continue until the goal is achieved or blocked.
6. Prefer low-risk actions first.
7. Return structured output.

Use this format:
Thought: what you infer and what you want to do next
Action: tool name and arguments
Observation: result of the action
Final: final outcome
```

## 11. Enterprise ReAct schema — Pydantic v2

```
from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, List, Optional, Union
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
    REACT_EXECUTOR = "react_executor"
    REACT_VALIDATOR = "react_validator"


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
    schema_version: str = "1.0.0"
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
    service: str
    application: Optional[str] = None
    environment: Environment = Environment.UNKNOWN
    severity: Severity = Severity.MEDIUM
    source: Optional[str] = None
    symptoms: List[str] = Field(default_factory=list)


class GoalContext(BaseTraceModel):
    goal: str
    success_criteria: List[str] = Field(default_factory=list)
    constraints: List[str] = Field(default_factory=list)
    assumptions: List[str] = Field(default_factory=list)


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
    notes: List[str] = Field(default_factory=list)


class RiskAssessment(BaseTraceModel):
    risk_level: RiskLevel = RiskLevel.MEDIUM
    blast_radius: Optional[str] = None
    risk_factors: List[str] = Field(default_factory=list)
    mitigations: List[str] = Field(default_factory=list)
    approval_required: bool = False


class ValidationCheck(BaseTraceModel):
    name: str
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
    confidence: float = Field(ge=0.0, le=1.0, default=0.8)


# =========================================================
# ReAct Models
# =========================================================

class ReActStep(BaseTraceModel):
    step_no: int = Field(ge=1)
    thought: str
    action_name: str
    action_arguments: Dict[str, Any] = Field(default_factory=dict)
    tool_call: Optional[ToolCall] = None
    observation: str
    observation_bundle: Optional[ObservationBundle] = None
    decision_after_observation: Optional[str] = None
    risk_assessment: Optional[RiskAssessment] = None
    status: TraceStatus = TraceStatus.SUCCESS


class ReActFinalOutcome(BaseTraceModel):
    summary: str
    decision: DecisionRecord
    success: bool
    should_replan: bool = False
    should_escalate: bool = False
    final_state: Dict[str, Any] = Field(default_factory=dict)


class ReActTrace(BaseTraceModel):
    metadata: TraceMetadata
    incident: IncidentContext
    goal_context: GoalContext
    initial_observations: ObservationBundle = Field(default_factory=ObservationBundle)
    steps: List[ReActStep] = Field(default_factory=list)
    validation_checks: List[ValidationCheck] = Field(default_factory=list)
    final_outcome: ReActFinalOutcome
    tags: Dict[str, str] = Field(default_factory=dict)


# =========================================================
# Example Usage
# =========================================================

if __name__ == "__main__":
    trace = ReActTrace(
        metadata=TraceMetadata(
            agent_name="incident_react_executor",
            agent_role=AgentRole.REACT_EXECUTOR,
            status=TraceStatus.SUCCESS,
        ),
        incident=IncidentContext(
            incident_id="INC_20260306_301",
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
        ),
        goal_context=GoalContext(
            goal="Restore healthy database connectivity for user-api",
            success_criteria=[
                "DB active connections below 80%",
                "API latency below 200 ms",
                "HTTP 500 rate below 1%",
            ],
            constraints=[
                "avoid database restart unless necessary",
                "prefer low-risk remediation first",
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
                "pool exhausted for datasource primary-db",
            ],
        ),
        steps=[
            ReActStep(
                step_no=1,
                thought="The database connection pool is saturated. I should inspect DB sessions before taking remediation action.",
                action_name="query_db_sessions",
                action_arguments={"database": "postgres-primary"},
                tool_call=ToolCall(
                    tool_name="query_db_sessions",
                    arguments={"database": "postgres-primary"},
                    status=TraceStatus.SUCCESS,
                    result_summary="Many idle sessions associated with application pods",
                ),
                observation="DB sessions show many idle connections associated with user-api pods.",
                decision_after_observation="Application-side stale connections are likely. App restart is safer than DB restart.",
                risk_assessment=RiskAssessment(
                    risk_level=RiskLevel.LOW,
                    blast_radius="read-only diagnostic query",
                ),
            ),
            ReActStep(
                step_no=2,
                thought="Rolling restart of user-api pods is the safest likely-effective remediation.",
                action_name="kubectl_rollout_restart",
                action_arguments={"deployment": "user-api", "namespace": "prod"},
                tool_call=ToolCall(
                    tool_name="kubectl_rollout_restart",
                    arguments={"deployment": "user-api", "namespace": "prod"},
                    status=TraceStatus.SUCCESS,
                    result_summary="Deployment restarted successfully",
                ),
                observation="Deployment restarted successfully. New pods are becoming ready.",
                decision_after_observation="Run health checks and verify metrics against success criteria.",
                risk_assessment=RiskAssessment(
                    risk_level=RiskLevel.MEDIUM,
                    blast_radius="user-api deployment only",
                    risk_factors=["temporary service impact during rollout"],
                    mitigations=["rolling restart", "health checks"],
                ),
            ),
            ReActStep(
                step_no=3,
                thought="I should validate whether the remediation worked.",
                action_name="run_health_check",
                action_arguments={"service": "user-api", "environment": "prod"},
                tool_call=ToolCall(
                    tool_name="run_health_check",
                    arguments={"service": "user-api", "environment": "prod"},
                    status=TraceStatus.SUCCESS,
                    result_summary="Latency 120 ms, DB connections 42%, HTTP 500 rate 0.4%",
                ),
                observation="Metrics recovered: latency is 120 ms, DB active connections are 42%, and HTTP 500 rate is 0.4%.",
                decision_after_observation="Success criteria are met. Finish execution.",
                risk_assessment=RiskAssessment(
                    risk_level=RiskLevel.LOW,
                    blast_radius="post-check only",
                ),
            ),
        ],
        validation_checks=[
            ValidationCheck(
                name="db_connections_recovered",
                expected_condition="DB active connections below 80%",
                actual_value="42%",
                result=ValidationResult.PASS,
                severity=Severity.HIGH,
                blocking=True,
            ),
            ValidationCheck(
                name="api_latency_recovered",
                expected_condition="API latency below 200 ms",
                actual_value="120 ms",
                result=ValidationResult.PASS,
                severity=Severity.HIGH,
                blocking=True,
            ),
        ],
        final_outcome=ReActFinalOutcome(
            summary="Incident mitigated successfully by inspecting DB sessions, performing rolling restart of user-api pods, and validating recovered service health.",
            decision=DecisionRecord(
                decision="Finish incident execution",
                decision_type=DecisionType.FINISH,
                rationale="All success criteria are satisfied after low-risk remediation.",
                confidence=0.91,
            ),
            success=True,
            final_state={
                "db_active_connections_pct": 42,
                "api_latency_ms": 120,
                "http_500_rate_pct": 0.4,
            },
        ),
        tags={"pattern": "react", "domain": "incident-remediation"},
    )

    print(trace.model_dump_json(indent=2))
```

## 12. ReAct trace format

A ReAct trace usually looks like this:

```
Thought: I should inspect DB sessions first.
Action: query_db_sessions(...)
Observation: many idle sessions from app pods

Thought: App-side stale connections are likely.
Action: kubectl_rollout_restart(...)
Observation: rollout successful

Thought: Now I should validate recovery.
Action: run_health_check(...)
Observation: latency and DB connections normalized

Final: incident mitigated
```

## 13. How to use ReAct in Planning Agent vs Execute Agent

## In Planning Agent

ReAct is **less common** as the main planning method, but it can still be used when the planner needs to gather context dynamically.


Example:

```
Thought: I need metrics before planning.
Action: query_metrics()
Observation: DB connections = 100%

Thought: I need DB session details too.
Action: query_db_sessions()
Observation: many idle sessions

Thought: Now I can build a better plan.
Final: create remediation plan
```

So in planners, ReAct is often used as:

- **context collection before planning**
- **dynamic planning support**


## In Execute Agent

ReAct is **extremely common**.

Why?

Because execution is naturally:

```
reason about current state
→ take tool action
→ inspect output
→ decide next action
```

This is exactly what ReAct is designed for.

For enterprise systems:

- **Planner** → CoT / ToT / GoT
- **Executor** → ReAct
- **Validator** → policy / checks / result validation

## 14. Where ReAct fits in your 11 categories

| Category          | ReAct role                                     |
| ----------------- | ---------------------------------------------- |
| Reasoning         | core                                           |
| Tool-Use / Action | core                                           |
| Validation        | often after each action or at end              |
| Memory            | optional, can use previous observations        |
| Reflection        | light reflection after observation             |
| Observability     | very strong fit because each step is traceable |


So ReAct is not a standalone “category” like planning or memory.
It is more like a **runtime execution pattern** using several categories together.

## 15. Best use cases for ReAct

ReAct is best when the agent must interact with tools step by step.

Good fit:

- incident remediation
- support troubleshooting
- search + retrieval agents
- API orchestration agents
- cloud / infra execution agents
- debugging agents

Poor fit:

- purely static planning
- heavy multi-branch strategic exploration
- tasks where no tools or observations are needed


## summary

**ReAct = an execution loop where the agent reasons, takes an action, observes the result, and repeats until the goal is reached.**


## 1. What is ReAct

**ReAct** means:

`Reason → Act → Observe → Repeat`

It is an agent pattern where the model:

- reasons about the current state
- takes an action using a tool
- observes the result
- reasons again based on the new observation
- reasons again based on the new observation

So ReAct is not just “thinking.”

It is **thinking** + **tool use** + **feedback loop**.

## 2. Why ReAct is useful in enterprise agents

ReAct is very useful when the agent must operate in a changing environment.

**Enterprise benefits**

| Area                  | How ReAct helps                                    |
| --------------------- | -------------------------------------------------- |
| Tool-driven execution | agent can use APIs, CLI, DB, monitoring tools      |
| Adaptive behavior     | next step depends on latest observation            |
| Troubleshooting       | inspect → act → verify loop fits incident handling |
| Auditability          | each step can be logged                            |
| Safety                | action can be checked after every observation      |


## 3. Where ReAct is used

ReAct is mainly used in:

**A. Execute Agent**

Most common use.

`Current step / goal → reason → act → observe → repeat`


**B. Planning Agent**

Sometimes used when planner must gather runtime context before making the plan.

`Need context → query tools → observe → reason → build plan`

So:

- **Planner ReAct** = context-aware planning
- **Executor ReAct** = runtime execution loop


## 4. Enterprise ReAct system prompt

Below are practical enterprise prompts.

## A. Generic enterprise ReAct system prompt

```
You are an enterprise autonomous execution agent.

Your job is to solve tasks by alternating between reasoning and tool use.

Rules:
1. Think about the current situation before taking an action.
2. Use tools only when needed.
3. After every action, inspect the observation carefully.
4. Base the next action only on the latest verified evidence.
5. Prefer the lowest-risk action that can move the task forward.
6. If the result is insufficient, continue the loop.
7. If the goal is achieved, stop and return the final outcome.
8. If blocked, return the blocker and recommended next step.
9. Return structured JSON only.

Use this reasoning structure:
- current_understanding
- next_action_reason
- action
- observation
- next_decision
```

## B. Incident auto-remediation ReAct system prompt

```
You are an enterprise SRE execution agent for incident auto-remediation.

You must operate using a Reason → Act → Observe loop.

Your responsibilities:
1. Understand the current incident state.
2. Decide the safest next action based on available evidence.
3. Use approved tools only.
4. Observe the result of every tool call before continuing.
5. Prefer low-risk remediation before high-risk remediation.
6. Do not assume success without validation.
7. Stop when success criteria are met, or return blocked/escalate if unresolved.

Execution policy:
- diagnose before destructive action
- prefer application-side remediation before database restart
- log all production actions
- validate after each significant action

Return JSON only with:
- goal
- current_state
- reasoning
- action
- observation
- decision
- status
```

## 5. ReAct JSON template schema

Below is a reusable enterprise schema.

## A. ReAct step schema

```
{
  "step_no": 1,
  "thought": "The database connection pool is saturated. I should inspect sessions first.",
  "action": {
    "tool_name": "query_db_sessions",
    "arguments": {
      "database": "postgres-primary"
    }
  },
  "observation": {
    "summary": "Many idle sessions are tied to application pods",
    "tool_result": {}
  },
  "decision_after_observation": "Application-side stale connections are likely. Next action should be rolling restart of app pods.",
  "risk_level": "low",
  "status": "success"
}
```

## B. Full ReAct trace schema

```
{
  "trace_id": "string",
  "schema_version": "1.0.0",
  "agent_name": "string",
  "agent_role": "react_executor",
  "goal": "string",
  "incident": {
    "incident_id": "string",
    "issue_key": "string",
    "issue_description": "string",
    "service": "string",
    "environment": "prod",
    "severity": "critical"
  },
  "initial_observations": {
    "metrics": {},
    "logs": [],
    "notes": []
  },
  "steps": [
    {
      "step_no": 1,
      "thought": "string",
      "action": {
        "tool_name": "string",
        "arguments": {}
      },
      "observation": {
        "summary": "string",
        "tool_result": {}
      },
      "decision_after_observation": "string",
      "risk_level": "low|medium|high|critical",
      "status": "success|failed|partial|blocked"
    }
  ],
  "validation_checks": [
    {
      "name": "string",
      "expected_condition": "string",
      "actual_value": "string",
      "result": "pass|fail|warn|unknown"
    }
  ],
  "final_outcome": {
    "summary": "string",
    "success": true,
    "should_replan": false,
    "should_escalate": false,
    "final_state": {}
  },
  "status": "success|failed|partial|blocked"
}
```

## 6. ReAct trace example

Use case: **Incident auto-remediation**
Incident: **Database connection pool exhausted**

## ReAct trace example

```
{
  "trace_id": "react-exec-001",
  "schema_version": "1.0.0",
  "agent_name": "incident_react_executor",
  "agent_role": "react_executor",
  "goal": "Restore healthy database connectivity for user-api",
  "incident": {
    "incident_id": "INC_20260306_301",
    "issue_key": "DB_CONNECTION_POOL_EXHAUSTED",
    "issue_description": "Database connection pool exhausted",
    "service": "user-api",
    "environment": "prod",
    "severity": "critical"
  },
  "initial_observations": {
    "metrics": {
      "db_active_connections_pct": 100,
      "api_latency_ms": 2400,
      "http_500_rate_pct": 8.5
    },
    "logs": [
      "timeout acquiring connection from pool",
      "pool exhausted for datasource primary-db"
    ],
    "notes": [
      "Customer-facing service degradation detected"
    ]
  },
  "steps": [
    {
      "step_no": 1,
      "thought": "The DB connection pool is saturated. I should inspect DB sessions before remediation.",
      "action": {
        "tool_name": "query_db_sessions",
        "arguments": {
          "database": "postgres-primary"
        }
      },
      "observation": {
        "summary": "Many idle sessions are associated with user-api pods",
        "tool_result": {
          "idle_sessions": 43,
          "blocked_sessions": 2
        }
      },
      "decision_after_observation": "Application-side stale connections are likely. Rolling restart is safer than DB restart.",
      "risk_level": "low",
      "status": "success"
    },
    {
      "step_no": 2,
      "thought": "A rolling restart of user-api pods is the safest likely-effective remediation.",
      "action": {
        "tool_name": "kubectl_rollout_restart",
        "arguments": {
          "deployment": "user-api",
          "namespace": "prod"
        }
      },
      "observation": {
        "summary": "Rolling restart completed successfully",
        "tool_result": {
          "rollout_status": "successful"
        }
      },
      "decision_after_observation": "Now validate whether DB connections and API latency recovered.",
      "risk_level": "medium",
      "status": "success"
    },
    {
      "step_no": 3,
      "thought": "I should verify success criteria using health checks and metrics.",
      "action": {
        "tool_name": "run_health_check",
        "arguments": {
          "service": "user-api",
          "environment": "prod"
        }
      },
      "observation": {
        "summary": "Metrics normalized after restart",
        "tool_result": {
          "db_active_connections_pct": 42,
          "api_latency_ms": 120,
          "http_500_rate_pct": 0.4
        }
      },
      "decision_after_observation": "Success criteria are met. Finish execution.",
      "risk_level": "low",
      "status": "success"
    }
  ],
  "validation_checks": [
    {
      "name": "db_connections_recovered",
      "expected_condition": "DB active connections below 80%",
      "actual_value": "42%",
      "result": "pass"
    },
    {
      "name": "api_latency_recovered",
      "expected_condition": "API latency below 200 ms",
      "actual_value": "120 ms",
      "result": "pass"
    },
    {
      "name": "http_500_rate_recovered",
      "expected_condition": "HTTP 500 rate below 1%",
      "actual_value": "0.4%",
      "result": "pass"
    }
  ],
  "final_outcome": {
    "summary": "Incident mitigated successfully by inspecting DB sessions, performing rolling restart of user-api pods, and validating recovered health.",
    "success": true,
    "should_replan": false,
    "should_escalate": false,
    "final_state": {
      "db_active_connections_pct": 42,
      "api_latency_ms": 120,
      "http_500_rate_pct": 0.4
    }
  },
  "status": "success"
}
```

## 7. How to use ReAct in Planning Agent

ReAct is **not usually the main reasoning pattern for static planning**, but it is very useful in **context-aware planning**.

## Planning Agent with ReAct

The planner may not know enough from the incident alone.
So it uses ReAct to gather context before creating the final plan.

**Flow**

```
Goal
 ↓
Thought: I need more context
 ↓
Action: call metrics/logs/topology tools
 ↓
Observation: get live system state
 ↓
Thought: now I can build a better plan
 ↓
Final: output plan
```

**Example**

**Goal**

`Restore healthy database connectivity for user-api`

**Planner ReAct run**

```
Thought:
I need current DB and API metrics before planning.

Action:
query_metrics(service="user-api")

Observation:
DB active connections = 100%
API latency = 2400 ms

Thought:
I also need DB session evidence to distinguish app leak vs DB-side issue.

Action:
query_db_sessions(database="postgres-primary")

Observation:
Many idle sessions tied to app pods

Thought:
Now I have enough context. The best initial plan is app-side diagnostics and rolling restart before DB restart.

Final Plan:
1 Inspect DB sessions
2 Record metrics baseline
3 Perform rolling restart of user-api
4 Validate recovery
```

## ReAct planner prompt example

```
You are an enterprise planning agent.

Goal:
Restore healthy database connectivity for user-api.

Before generating the plan, you may use tools to collect missing context.

Available tools:
- query_metrics
- query_logs
- query_db_sessions
- get_service_topology

Rules:
1. Gather only the context needed to improve planning.
2. Think before every tool call.
3. After each observation, decide whether more context is needed.
4. Once context is sufficient, produce the final plan.
5. Return structured JSON only.
```

## When ReAct is useful in planners

Use ReAct in a planner when:

- real-time system state matters
- static runbook is insufficient
- planning quality depends on live observations
- environment is dynamic


## 8. How to use ReAct in Execute Agent

This is the **most common and best use of ReAct**.

The execute agent already has a goal or a planned step and must safely move forward based on tool outputs.

## Execute Agent with ReAct

**Flow**

```
Current step / goal
 ↓
Thought
 ↓
Action
 ↓
Observation
 ↓
Thought
 ↓
Next Action
 ↓
Observation
 ↓
Finish / Replan / Escalate
```

## Example

**Input**

```
Goal: Restore healthy database connectivity for user-api
Planned step: Apply low-risk remediation
```

**ReAct execution**

```
Thought:
I should inspect DB sessions first before restarting anything.

Action:
query_db_sessions()

Observation:
Many idle sessions from user-api pods

Thought:
This suggests stale app-side connections. Rolling restart is safer than DB restart.

Action:
kubectl_rollout_restart()

Observation:
Rollout successful

Thought:
Now validate health.

Action:
run_health_check()

Observation:
Latency and connection usage normalized

Final:
Incident mitigated
```

## Executor prompt example

```
You are an enterprise execution agent.

Goal:
Restore healthy database connectivity for user-api.

Current context:
- DB active connections = 100%
- API latency = 2400 ms
- Logs show pool exhaustion

Execution rules:
1. Think before every action.
2. Use only approved tools.
3. After each action, inspect observation carefully.
4. Choose the lowest-risk next step.
5. Validate before declaring success.
6. If unsuccessful, continue the loop or recommend replan/escalation.

Return structured JSON only.
```

## 9. Planning Agent vs Execute Agent usage

| Area        | Planning Agent with ReAct    | Execute Agent with ReAct         |
| ----------- | ---------------------------- | -------------------------------- |
| Purpose     | gather context before plan   | perform actions step by step     |
| Main input  | goal + incomplete context    | current step + live system state |
| Main output | final plan                   | final action sequence / result   |
| Tool use    | selective, context gathering | frequent, core part of loop      |
| Best fit    | context-aware planner        | runtime executor                 |


## 10. Recommended enterprise design

For enterprise agents, a strong pattern is:

```
Incident / Goal
   ↓
Planning Agent
   ├─ CoT / ToT / GoT for strategy
   └─ ReAct only if live context is needed
   ↓
Plan
   ↓
Execute Agent
   └─ ReAct loop for runtime execution
   ↓
Validator
   ↓
Observability / Audit
```

So in practice:

- **Planning Agent** → mostly CoT / ToT / GoT
- **Execute Agent** → mostly ReAct


## 11. Enterprise best practices for ReAct

**Use structured steps**

Do not keep ReAct as raw free text only.
Store each step as structured trace data.

**Validate after important actions**

Especially in prod:

- restarts
- scaling
- failover
- DB actions


## Prefer low-risk-first
ReAct can become too action-heavy without guardrails.

Always enforce safety policy.

## Limit step count

Avoid infinite loops. Use:

- max iterations
- timeout
- escalation threshold

## Keep traces auditable

Keep traces auditable

- thought
- action
- observation
- next decision


## 12. Minimal reusable ReAct template

```
{
  "goal": "string",
  "current_state": {},
  "steps": [
    {
      "step_no": 1,
      "thought": "string",
      "action": {
        "tool_name": "string",
        "arguments": {}
      },
      "observation": {
        "summary": "string",
        "tool_result": {}
      },
      "decision_after_observation": "string",
      "risk_level": "low|medium|high|critical",
      "status": "success|failed|partial|blocked"
    }
  ],
  "final_outcome": {
    "summary": "string",
    "success": true,
    "should_replan": false,
    "should_escalate": false
  }
}
```

## Enterprise ReAct Schema — Pydantic v2

Below is a **complete enterprise ReAct Pydantic v2 schema** with separate models for:

- `ReActPlannerTrace`
- `ReActExecutorTrace`
- `ReActValidatorTrace`

This design is meant for **enterprise agent systems** where ReAct is used for:

- context-aware planning
- tool-driven execution
- validation after each step or at the end
- observability, audit, and replay


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
    REACT_PLANNER = "react_planner"
    REACT_EXECUTOR = "react_executor"
    REACT_VALIDATOR = "react_validator"


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
    CONTINUE = "continue"
    GATHER_MORE_CONTEXT = "gather_more_context"
    APPROVE = "approve"
    REJECT = "reject"


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
# ReAct Shared Models
# =========================================================

class ReActThought(BaseTraceModel):
    current_understanding: str
    reasoning: str
    next_action_reason: str
    safety_notes: List[str] = Field(default_factory=list)
    uncertainties: List[str] = Field(default_factory=list)


class ReActAction(BaseTraceModel):
    action_name: str
    tool_name: str
    arguments: Dict[str, Any] = Field(default_factory=dict)
    expected_outcome: Optional[str] = None
    dry_run: bool = False
    timeout_seconds: Optional[int] = None


class ReActObservation(BaseTraceModel):
    summary: str
    metrics: Dict[str, Union[int, float, str, bool, None]] = Field(default_factory=dict)
    logs: List[str] = Field(default_factory=list)
    events: List[str] = Field(default_factory=list)
    tool_result: Dict[str, Any] = Field(default_factory=dict)
    notes: List[str] = Field(default_factory=list)


class ReActStep(BaseTraceModel):
    step_no: int = Field(ge=1)
    thought: ReActThought
    action: ReActAction
    tool_call: Optional[ToolCall] = None
    observation: ReActObservation
    decision_after_observation: DecisionRecord
    risk_assessment: Optional[RiskAssessment] = None
    status: TraceStatus = TraceStatus.SUCCESS


class ReActFinalOutcome(BaseTraceModel):
    summary: str
    decision: DecisionRecord
    success: bool
    should_replan: bool = False
    should_escalate: bool = False
    final_state: Dict[str, Any] = Field(default_factory=dict)


# =========================================================
# Planner Models
# =========================================================

class PlannerPlanStep(BaseTraceModel):
    step_no: int = Field(ge=1)
    step_id: str
    name: str
    description: str
    purpose: Optional[str] = None
    tool_name: Optional[str] = None
    expected_outcome: Optional[str] = None
    validation_checks: List[str] = Field(default_factory=list)
    risk_level: RiskLevel = RiskLevel.MEDIUM


class PlannerPlanOutput(BaseTraceModel):
    plan_summary: str
    steps: List[PlannerPlanStep] = Field(default_factory=list)
    decision: DecisionRecord
    risk_assessment: Optional[RiskAssessment] = None
    required_tools: List[ToolReference] = Field(default_factory=list)
    pre_execution_checks: List[ValidationCheck] = Field(default_factory=list)


class ReActPlannerTrace(BaseTraceModel):
    metadata: TraceMetadata
    incident: IncidentContext
    goal_context: GoalContext
    initial_observations: ObservationBundle = Field(default_factory=ObservationBundle)
    react_steps: List[ReActStep] = Field(default_factory=list)
    final_plan: PlannerPlanOutput
    validation_checks: List[ValidationCheck] = Field(default_factory=list)
    tags: Dict[str, str] = Field(default_factory=dict)


# =========================================================
# Executor Models
# =========================================================

class ExecutionContext(BaseTraceModel):
    plan_id: Optional[str] = None
    current_step_no: Optional[int] = None
    current_step_id: Optional[str] = None
    current_step_name: Optional[str] = None
    current_step_description: Optional[str] = None


class ReActExecutorTrace(BaseTraceModel):
    metadata: TraceMetadata
    incident: IncidentContext
    goal_context: GoalContext
    execution_context: ExecutionContext
    initial_observations: ObservationBundle = Field(default_factory=ObservationBundle)
    react_steps: List[ReActStep] = Field(default_factory=list)
    validation_checks: List[ValidationCheck] = Field(default_factory=list)
    final_outcome: ReActFinalOutcome
    tags: Dict[str, str] = Field(default_factory=dict)


# =========================================================
# Validator Models
# =========================================================

class ValidationTarget(BaseTraceModel):
    target_type: Literal["plan", "execution_step", "execution_result", "policy", "safety"]
    target_id: Optional[str] = None
    target_name: Optional[str] = None
    description: Optional[str] = None


class ReActValidatorReasoning(BaseTraceModel):
    current_understanding: str
    reasoning_steps: List[str] = Field(default_factory=list)
    evidence_reviewed: List[str] = Field(default_factory=list)
    issues_found: List[str] = Field(default_factory=list)
    final_assessment: str


class ValidatorSummary(BaseTraceModel):
    overall_result: ValidationResult
    passed_checks: int = 0
    failed_checks: int = 0
    warning_checks: int = 0
    blocking_failures: List[str] = Field(default_factory=list)
    non_blocking_warnings: List[str] = Field(default_factory=list)
    recommendation: DecisionType
    recommendation_reason: str


class ReActValidatorTrace(BaseTraceModel):
    metadata: TraceMetadata
    incident: IncidentContext
    goal_context: GoalContext
    validation_target: ValidationTarget
    observations: ObservationBundle = Field(default_factory=ObservationBundle)
    reasoning: ReActValidatorReasoning
    checks: List[ValidationCheck] = Field(default_factory=list)
    summary: ValidatorSummary
    risk_assessment: Optional[RiskAssessment] = None
    tags: Dict[str, str] = Field(default_factory=dict)


# =========================================================
# Helper Factory Functions
# =========================================================

def make_react_planner_metadata(agent_name: str = "react_planner") -> TraceMetadata:
    return TraceMetadata(
        agent_name=agent_name,
        agent_role=AgentRole.REACT_PLANNER,
        status=TraceStatus.SUCCESS,
    )


def make_react_executor_metadata(agent_name: str = "react_executor") -> TraceMetadata:
    return TraceMetadata(
        agent_name=agent_name,
        agent_role=AgentRole.REACT_EXECUTOR,
        status=TraceStatus.SUCCESS,
    )


def make_react_validator_metadata(agent_name: str = "react_validator") -> TraceMetadata:
    return TraceMetadata(
        agent_name=agent_name,
        agent_role=AgentRole.REACT_VALIDATOR,
        status=TraceStatus.SUCCESS,
    )


# =========================================================
# Example Usage
# =========================================================

if __name__ == "__main__":
    incident = IncidentContext(
        incident_id="INC_20260306_401",
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

    planner_trace = ReActPlannerTrace(
        metadata=make_react_planner_metadata(),
        incident=incident,
        goal_context=goal,
        initial_observations=ObservationBundle(
            metrics={
                "db_active_connections_pct": 100,
                "api_latency_ms": 2400,
                "http_500_rate_pct": 8.5,
            },
            logs=[
                "timeout acquiring connection from pool",
                "pool exhausted for datasource primary-db",
            ],
        ),
        react_steps=[
            ReActStep(
                step_no=1,
                thought=ReActThought(
                    current_understanding="Need live DB and API state before producing a safe plan.",
                    reasoning="The incident may be caused by app-side stale connections or DB-side session issues.",
                    next_action_reason="Query current DB and API metrics first.",
                    safety_notes=["diagnostic action only"],
                ),
                action=ReActAction(
                    action_name="query_metrics",
                    tool_name="query_metrics",
                    arguments={"service": "user-api"},
                    expected_outcome="current DB and API health metrics",
                ),
                tool_call=ToolCall(
                    tool_name="query_metrics",
                    arguments={"service": "user-api"},
                    status=TraceStatus.SUCCESS,
                    result_summary="DB active connections 100%, API latency 2400 ms",
                ),
                observation=ReActObservation(
                    summary="Metrics confirm severe DB connection saturation and API degradation.",
                    metrics={
                        "db_active_connections_pct": 100,
                        "api_latency_ms": 2400,
                    },
                ),
                decision_after_observation=DecisionRecord(
                    decision="Gather DB session details before planning remediation.",
                    decision_type=DecisionType.GATHER_MORE_CONTEXT,
                    rationale="Need DB-side evidence to distinguish app leak from blocked sessions.",
                    confidence=0.90,
                ),
                risk_assessment=RiskAssessment(
                    risk_level=RiskLevel.LOW,
                    blast_radius="read-only diagnostics",
                ),
            ),
            ReActStep(
                step_no=2,
                thought=ReActThought(
                    current_understanding="Metrics show saturation; session-level evidence is still needed.",
                    reasoning="DB session information will improve the remediation plan quality.",
                    next_action_reason="Inspect DB sessions.",
                    safety_notes=["diagnostic action only"],
                ),
                action=ReActAction(
                    action_name="query_db_sessions",
                    tool_name="query_db_sessions",
                    arguments={"database": "postgres-primary"},
                    expected_outcome="session breakdown of active/idle/blocked connections",
                ),
                tool_call=ToolCall(
                    tool_name="query_db_sessions",
                    arguments={"database": "postgres-primary"},
                    status=TraceStatus.SUCCESS,
                    result_summary="Many idle sessions tied to app pods",
                ),
                observation=ReActObservation(
                    summary="Many idle sessions are associated with user-api pods.",
                    tool_result={
                        "idle_sessions": 43,
                        "blocked_sessions": 2,
                    },
                ),
                decision_after_observation=DecisionRecord(
                    decision="Build plan using app-side rolling restart as first remediation.",
                    decision_type=DecisionType.PROCEED,
                    rationale="Evidence points to stale app-side connections; rolling restart is lower risk than DB restart.",
                    confidence=0.88,
                ),
                risk_assessment=RiskAssessment(
                    risk_level=RiskLevel.LOW,
                    blast_radius="read-only diagnostics",
                ),
            ),
        ],
        final_plan=PlannerPlanOutput(
            plan_summary="Use diagnostics to confirm evidence, then apply app-side rolling restart and validate recovery.",
            steps=[
                PlannerPlanStep(
                    step_no=1,
                    step_id="step_1",
                    name="Inspect DB sessions",
                    description="Query DB sessions to identify idle or blocked connections.",
                    purpose="Confirm likely source of pool exhaustion.",
                    tool_name="query_db_sessions",
                    expected_outcome="Session evidence available.",
                    validation_checks=["session_query_success"],
                    risk_level=RiskLevel.LOW,
                ),
                PlannerPlanStep(
                    step_no=2,
                    step_id="step_2",
                    name="Capture metrics baseline",
                    description="Record latest DB and API metrics before remediation.",
                    purpose="Establish severity baseline.",
                    tool_name="query_metrics",
                    expected_outcome="Metrics baseline recorded.",
                    validation_checks=["metrics_freshness_ok"],
                    risk_level=RiskLevel.LOW,
                ),
                PlannerPlanStep(
                    step_no=3,
                    step_id="step_3",
                    name="Rolling restart user-api",
                    description="Perform rolling restart of user-api pods.",
                    purpose="Clear stale app-side DB connections.",
                    tool_name="kubectl_rollout_restart",
                    expected_outcome="Application reconnects with cleaner DB pool state.",
                    validation_checks=["deployment_rollout_success"],
                    risk_level=RiskLevel.MEDIUM,
                ),
                PlannerPlanStep(
                    step_no=4,
                    step_id="step_4",
                    name="Validate recovery",
                    description="Run health checks and verify success criteria.",
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
            decision=DecisionRecord(
                decision="Proceed with app-side rolling restart plan.",
                decision_type=DecisionType.PROCEED,
                rationale="This plan best balances safety, effectiveness, and production policy alignment.",
                selected_option="app_restart_first",
                rejected_options=["restart_db_first"],
                confidence=0.89,
            ),
            risk_assessment=RiskAssessment(
                risk_level=RiskLevel.MEDIUM,
                blast_radius="user-api deployment only",
                risk_factors=["production customer-facing service"],
                mitigations=["rolling restart", "health checks", "post-action validation"],
            ),
            required_tools=[
                ToolReference(tool_name="query_metrics"),
                ToolReference(tool_name="query_db_sessions"),
                ToolReference(tool_name="kubectl_rollout_restart"),
                ToolReference(tool_name="run_health_check"),
            ],
            pre_execution_checks=[
                ValidationCheck(
                    name="rbac_check",
                    expected_condition="Executor has permission to restart user-api deployment",
                    result=ValidationResult.PASS,
                    severity=Severity.HIGH,
                    blocking=True,
                )
            ],
        ),
        validation_checks=[
            ValidationCheck(
                name="plan_policy_check",
                expected_condition="No DB restart used as first remediation in prod",
                result=ValidationResult.PASS,
                severity=Severity.HIGH,
                blocking=True,
            )
        ],
        tags={"pattern": "react", "phase": "planning"},
    )

    executor_trace = ReActExecutorTrace(
        metadata=make_react_executor_metadata(),
        incident=incident,
        goal_context=goal,
        execution_context=ExecutionContext(
            plan_id="plan_001",
            current_step_no=3,
            current_step_id="step_3",
            current_step_name="Rolling restart user-api",
            current_step_description="Perform rolling restart of user-api pods.",
        ),
        initial_observations=ObservationBundle(
            metrics={
                "db_active_connections_pct": 100,
                "api_latency_ms": 2400,
                "http_500_rate_pct": 8.5,
            },
            logs=[
                "timeout acquiring connection from pool",
                "pool exhausted for datasource primary-db",
            ],
            notes=["Ready to execute remediation step."],
        ),
        react_steps=[
            ReActStep(
                step_no=1,
                thought=ReActThought(
                    current_understanding="DB sessions point to stale app-side connections.",
                    reasoning="Rolling restart is a lower-risk likely-effective remediation.",
                    next_action_reason="Restart user-api deployment using rolling restart.",
                    safety_notes=["avoid DB restart", "use rolling restart only"],
                ),
                action=ReActAction(
                    action_name="rolling_restart_user_api",
                    tool_name="kubectl_rollout_restart",
                    arguments={"deployment": "user-api", "namespace": "prod"},
                    expected_outcome="Fresh pods reconnect with clean DB pool state.",
                ),
                tool_call=ToolCall(
                    tool_name="kubectl_rollout_restart",
                    arguments={"deployment": "user-api", "namespace": "prod"},
                    status=TraceStatus.SUCCESS,
                    result_summary="Deployment restarted successfully",
                ),
                observation=ReActObservation(
                    summary="Rolling restart completed successfully and new pods are ready.",
                    tool_result={"rollout_status": "successful"},
                ),
                decision_after_observation=DecisionRecord(
                    decision="Run health validation checks.",
                    decision_type=DecisionType.CONTINUE,
                    rationale="Need to verify whether restart actually resolved the incident.",
                    confidence=0.92,
                ),
                risk_assessment=RiskAssessment(
                    risk_level=RiskLevel.MEDIUM,
                    blast_radius="user-api deployment only",
                    risk_factors=["temporary rollout impact"],
                    mitigations=["rolling restart", "readiness checks"],
                ),
            ),
            ReActStep(
                step_no=2,
                thought=ReActThought(
                    current_understanding="Restart completed; need to verify success criteria.",
                    reasoning="Metrics and health checks will confirm resolution.",
                    next_action_reason="Run post-remediation health check.",
                    safety_notes=["validation only"],
                ),
                action=ReActAction(
                    action_name="run_post_health_check",
                    tool_name="run_health_check",
                    arguments={"service": "user-api", "environment": "prod"},
                    expected_outcome="Recovered DB connections, latency, and error rate.",
                ),
                tool_call=ToolCall(
                    tool_name="run_health_check",
                    arguments={"service": "user-api", "environment": "prod"},
                    status=TraceStatus.SUCCESS,
                    result_summary="Latency 120 ms, DB connections 42%, HTTP 500 rate 0.4%",
                ),
                observation=ReActObservation(
                    summary="All major health metrics recovered after restart.",
                    metrics={
                        "db_active_connections_pct": 42,
                        "api_latency_ms": 120,
                        "http_500_rate_pct": 0.4,
                    },
                ),
                decision_after_observation=DecisionRecord(
                    decision="Finish execution successfully.",
                    decision_type=DecisionType.FINISH,
                    rationale="Success criteria are satisfied after low-risk remediation.",
                    confidence=0.95,
                ),
                risk_assessment=RiskAssessment(
                    risk_level=RiskLevel.LOW,
                    blast_radius="post-check only",
                ),
            ),
        ],
        validation_checks=[
            ValidationCheck(
                name="db_connections_recovered",
                expected_condition="DB active connections below 80%",
                actual_value="42%",
                result=ValidationResult.PASS,
                severity=Severity.HIGH,
                blocking=True,
            ),
            ValidationCheck(
                name="api_latency_recovered",
                expected_condition="API latency below 200 ms",
                actual_value="120 ms",
                result=ValidationResult.PASS,
                severity=Severity.HIGH,
                blocking=True,
            ),
            ValidationCheck(
                name="http_500_rate_recovered",
                expected_condition="HTTP 500 rate below 1%",
                actual_value="0.4%",
                result=ValidationResult.PASS,
                severity=Severity.HIGH,
                blocking=True,
            ),
        ],
        final_outcome=ReActFinalOutcome(
            summary="Incident mitigated successfully via rolling restart of user-api and validated recovered health.",
            decision=DecisionRecord(
                decision="Finish incident execution.",
                decision_type=DecisionType.FINISH,
                rationale="All success criteria are met.",
                confidence=0.95,
            ),
            success=True,
            should_replan=False,
            should_escalate=False,
            final_state={
                "db_active_connections_pct": 42,
                "api_latency_ms": 120,
                "http_500_rate_pct": 0.4,
            },
        ),
        tags={"pattern": "react", "phase": "execution"},
    )

    validator_trace = ReActValidatorTrace(
        metadata=make_react_validator_metadata(),
        incident=incident,
        goal_context=goal,
        validation_target=ValidationTarget(
            target_type="execution_result",
            target_id="exec_result_001",
            target_name="user-api remediation result",
            description="Validate whether execution result satisfies policy and success criteria.",
        ),
        observations=ObservationBundle(
            metrics={
                "db_active_connections_pct": 42,
                "api_latency_ms": 120,
                "http_500_rate_pct": 0.4,
            },
            notes=[
                "Execution used rolling restart only",
                "No DB restart occurred",
            ],
        ),
        reasoning=ReActValidatorReasoning(
            current_understanding="Execution result appears compliant and successful.",
            reasoning_steps=[
                "Check success criteria against final metrics.",
                "Check policy compliance for production remediation.",
                "Check whether any blocking failure remains.",
            ],
            evidence_reviewed=[
                "db_active_connections_pct=42",
                "api_latency_ms=120",
                "http_500_rate_pct=0.4",
                "no DB restart used",
            ],
            issues_found=[],
            final_assessment="Execution result satisfies both success criteria and safety constraints.",
        ),
        checks=[
            ValidationCheck(
                name="policy_no_db_restart_first",
                expected_condition="DB restart must not be first-line remediation in prod",
                actual_value="rolling restart of user-api used",
                result=ValidationResult.PASS,
                severity=Severity.HIGH,
                blocking=True,
            ),
            ValidationCheck(
                name="success_db_connections",
                expected_condition="DB active connections below 80%",
                actual_value="42%",
                result=ValidationResult.PASS,
                severity=Severity.HIGH,
                blocking=True,
            ),
            ValidationCheck(
                name="success_api_latency",
                expected_condition="API latency below 200 ms",
                actual_value="120 ms",
                result=ValidationResult.PASS,
                severity=Severity.HIGH,
                blocking=True,
            ),
            ValidationCheck(
                name="success_http_500",
                expected_condition="HTTP 500 rate below 1%",
                actual_value="0.4%",
                result=ValidationResult.PASS,
                severity=Severity.HIGH,
                blocking=True,
            ),
        ],
        summary=ValidatorSummary(
            overall_result=ValidationResult.PASS,
            passed_checks=4,
            failed_checks=0,
            warning_checks=0,
            blocking_failures=[],
            non_blocking_warnings=[],
            recommendation=DecisionType.APPROVE,
            recommendation_reason="Execution result is safe, compliant, and successful.",
        ),
        risk_assessment=RiskAssessment(
            risk_level=RiskLevel.LOW,
            blast_radius="validation only",
            risk_factors=[],
            mitigations=[],
            approval_required=False,
        ),
        tags={"pattern": "react", "phase": "validation"},
    )

    print("=== ReActPlannerTrace ===")
    print(planner_trace.model_dump_json(indent=2))
    print("\n=== ReActExecutorTrace ===")
    print(executor_trace.model_dump_json(indent=2))
    print("\n=== ReActValidatorTrace ===")
    print(validator_trace.model_dump_json(indent=2))
```

## What each model is for

`ReActPlannerTrace`

Use this when the planner needs to gather live context before finalizing a plan.

Typical usage:

- query metrics
- inspect logs
- inspect sessions
- then produce a better plan

So this is context-aware planning with ReAct.


`ReActExecutorTrace`

Use this when the executor is doing the classic runtime loop:

`Thought → Action → Observation → Next Decision`

Typical usage:

- inspect system state
- run remediation command
- observe result
- validate health
- continue or stop

This is the main ReAct runtime model.

`ReActValidatorTrace`

Use this when you want a validator agent to confirm:

- policy compliance
- success criteria
- safety requirements
- whether to approve / reject / replan / escalate

This is especially useful in production and regulated environments.


## Recommended enterprise sequence

```
Incident / Goal
   ↓
ReActPlannerTrace
   ↓
Plan
   ↓
ReActExecutorTrace
   ↓
Execution Result
   ↓
ReActValidatorTrace
   ↓
Observability / Audit / Replay Store
```

## Practical difference from CoT / ToT / GoT

| Pattern | Best use                   |
| ------- | -------------------------- |
| CoT     | linear reasoning           |
| ToT     | branching alternatives     |
| GoT     | non-linear graph reasoning |
| ReAct   | tool-driven runtime loop   |

So in most enterprise systems:

 - **Planner** may use CoT / ToT / GoT
 - **Planner** can also use ReAct if runtime context is needed first
 - **Executor most naturally uses ReAct**
 - **Validator uses checks + decision logic**


