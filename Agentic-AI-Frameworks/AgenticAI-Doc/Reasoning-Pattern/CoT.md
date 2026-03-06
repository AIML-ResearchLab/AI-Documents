# Chain-of-Thought (CoT)

## What is Chain-of-Thought (CoT)

**Chain-of-Thought (CoT)** is a reasoning pattern where the model solves a problem through **explicit intermediate thinking steps** before producing the final answer or action.

In agent systems, CoT is used to:

- understand the goal
- break problems into smaller parts
- evaluate options
- decide next actions
- justify outputs internally


**Simple idea**

Instead of:

`Issue → Action`

**CoT does:**

`Issue → Think step by step → Decision → Action`

## Why CoT is useful in agents

In enterprise agents, CoT helps with:

| Area         | How CoT helps                                    |
| ------------ | ------------------------------------------------ |
| Planning     | breaks a goal into ordered steps                 |
| Execution    | reasons about current observations before acting |
| Validation   | checks whether the chosen action makes sense     |
| Traceability | gives structured intermediate reasoning          |
| Debugging    | easier to inspect why the agent chose something  |


## Where CoT is used

CoT is usually used in **two major places:**

## A. Planning Agent

Used to create a plan from a goal.

`Goal → CoT reasoning → plan`

## B. Execute Agent

Used to decide what to do at runtime.

`Observation → CoT reasoning → next action`

## CoT system prompt

Below is a good **enterprise CoT system prompt**.

**Generic CoT system prompt**

```
You are an enterprise autonomous reasoning agent.

Your task is to think step by step before producing an answer, plan, or action.

Rules:
1. Understand the goal clearly.
2. Break the problem into smaller parts.
3. Analyze available evidence, constraints, and dependencies.
4. Consider possible causes or options before deciding.
5. Choose the safest and most effective next step.
6. Return structured output.
7. Do not skip reasoning steps.
8. If evidence is insufficient, state uncertainty clearly.

Use this reasoning format:
- goal_understanding
- observations
- hypotheses
- analysis
- decision
- output
```

## Incident remediation CoT system prompt

```
You are an enterprise SRE reasoning agent for incident auto-remediation.

You must reason step by step before proposing a plan or action.

Always:
1. Understand the incident and affected service.
2. Identify likely causes from symptoms, logs, and metrics.
3. Consider constraints such as production safety, policy, and blast radius.
4. Prefer low-risk diagnostic and remediation actions first.
5. Explain why the chosen step is appropriate.
6. Return structured JSON only.

Reasoning sections:
- incident_summary
- goal
- observations
- possible_causes
- evidence_analysis
- chosen_path
- recommended_steps
- validation_checks
```

## CoT template schema

Below is a practical schema

## CoT template schema for planning

```
{
  "trace_id": "string",
  "agent_type": "planner",
  "goal": "string",
  "context": {
    "issue": "string",
    "service": "string",
    "environment": "string",
    "severity": "string"
  },
  "reasoning": {
    "goal_understanding": "string",
    "task_decomposition": [
      "string"
    ],
    "dependencies": [
      "string"
    ],
    "constraints": [
      "string"
    ],
    "options_considered": [
      {
        "option": "string",
        "pros": [
          "string"
        ],
        "cons": [
          "string"
        ]
      }
    ],
    "selected_strategy": "string",
    "why_selected": "string"
  },
  "plan": [
    {
      "step_no": 1,
      "step": "string",
      "purpose": "string",
      "tool": "string",
      "expected_result": "string"
    }
  ]
}
```

## CoT template schema for execute agent

```
{
  "trace_id": "string",
  "agent_type": "executor",
  "goal": "string",
  "current_step": {
    "step_no": 1,
    "step": "string",
    "tool": "string"
  },
  "observations": {
    "metrics": {},
    "logs": [],
    "tool_outputs": []
  },
  "reasoning": {
    "step_understanding": "string",
    "observation_analysis": "string",
    "hypotheses": [
      "string"
    ],
    "decision": "string",
    "decision_reason": "string",
    "risk_check": "string"
  },
  "action": {
    "tool": "string",
    "arguments": {},
    "expected_outcome": "string"
  },
  "validation": [
    "string"
  ]
}
```

## Unified CoT schema

If you want one schema for all agents:

```
{
  "trace_id": "string",
  "schema_version": "1.0.0",
  "agent_name": "string",
  "agent_role": "planner|executor|validator",
  "goal": "string",
  "input": {},
  "reasoning": {
    "understanding": "string",
    "observations": [],
    "hypotheses": [],
    "analysis_steps": [
      "string"
    ],
    "decision": "string",
    "decision_reason": "string"
  },
  "output": {},
  "validation_checks": [],
  "status": "success|failed|partial"
}
```

## CoT trace

A **CoT trace** is the actual reasoning record for one run.

Below is a realistic example.

## Example CoT trace for planning agent

Use case: **Database connection pool exhausted**

```
{
  "trace_id": "cot-plan-001",
  "schema_version": "1.0.0",
  "agent_name": "incident_planner",
  "agent_role": "planner",
  "goal": "Restore healthy database connectivity for user-api",
  "input": {
    "issue": "Database connection pool exhausted",
    "service": "user-api",
    "environment": "prod",
    "severity": "critical",
    "symptoms": [
      "API latency above 2000 ms",
      "HTTP 500 errors increased",
      "DB active connections at 100%"
    ]
  },
  "reasoning": {
    "understanding": "The incident affects production user-api and likely involves exhausted DB connections causing latency and errors.",
    "observations": [
      "DB active connections are at maximum",
      "API latency is very high",
      "Service is degraded in production"
    ],
    "hypotheses": [
      "Application-side connection leak",
      "Long-running DB sessions",
      "Temporary DB overload"
    ],
    "analysis_steps": [
      "Need to confirm whether DB sessions are stuck or active",
      "Need low-risk diagnostics before remediation",
      "Application-side restart is safer than DB restart in production",
      "Validation must confirm latency reduction and connection recovery"
    ],
    "decision": "Use a low-risk remediation plan starting with diagnostics, then app-side restart if needed.",
    "decision_reason": "This minimizes blast radius and aligns with production safety practices."
  },
  "output": {
    "plan": [
      {
        "step_no": 1,
        "step": "Query database session state",
        "purpose": "Identify long-running, blocked, or idle sessions",
        "tool": "query_db_sessions",
        "expected_result": "Understand whether pool exhaustion is caused by stuck sessions"
      },
      {
        "step_no": 2,
        "step": "Query current DB and API metrics",
        "purpose": "Establish baseline severity",
        "tool": "query_metrics",
        "expected_result": "Confirm connection saturation and latency"
      },
      {
        "step_no": 3,
        "step": "Perform rolling restart of user-api pods",
        "purpose": "Clear potentially leaked application DB connections",
        "tool": "kubectl_rollout_restart",
        "expected_result": "Fresh application connections and reduced pool pressure"
      },
      {
        "step_no": 4,
        "step": "Run health validation",
        "purpose": "Verify incident resolution",
        "tool": "run_health_check",
        "expected_result": "Latency reduced and connection usage normalized"
      }
    ]
  },
  "validation_checks": [
    "DB active connections below 80%",
    "API latency below 200 ms",
    "HTTP 500 rate below 1%"
  ],
  "status": "success"
}
```

## Example CoT trace for execute agent

```
{
  "trace_id": "cot-exec-001",
  "schema_version": "1.0.0",
  "agent_name": "incident_executor",
  "agent_role": "executor",
  "goal": "Restore healthy database connectivity for user-api",
  "input": {
    "current_step": {
      "step_no": 3,
      "step": "Perform rolling restart of user-api pods",
      "tool": "kubectl_rollout_restart"
    },
    "observations": {
      "db_active_connections_pct": 100,
      "api_latency_ms": 2400,
      "db_session_summary": "Many idle connections tied to application pods"
    }
  },
  "reasoning": {
    "understanding": "Current evidence suggests application-side connections are stuck and exhausting DB pool.",
    "observations": [
      "Connections are saturated",
      "Latency is high",
      "Idle sessions suggest stale app-side pool state"
    ],
    "hypotheses": [
      "Restarting application pods will release stale connections"
    ],
    "analysis_steps": [
      "DB restart is riskier in production",
      "Application restart is a lower-risk remediation",
      "Rolling restart reduces downtime risk"
    ],
    "decision": "Restart user-api pods using rolling restart",
    "decision_reason": "This is the safest likely-effective remediation based on observed evidence."
  },
  "output": {
    "action": {
      "tool": "kubectl_rollout_restart",
      "arguments": {
        "deployment": "user-api",
        "namespace": "prod"
      },
      "expected_outcome": "Application reconnects with clean DB connection pool"
    }
  },
  "validation_checks": [
    "DB active connections decrease",
    "API latency improves",
    "HTTP 500 rate declines"
  ],
  "status": "success"
}
```

## How to use CoT in Planning Agent

The **Planning Agent** uses CoT to transform:

`Goal + context → plan`

## Planning Agent CoT flow

```
Incident / Goal
   ↓
Understand goal
   ↓
Break into subtasks
   ↓
Analyze constraints and dependencies
   ↓
Consider options
   ↓
Choose strategy
   ↓
Output plan
```

## Example planner prompt

```
You are a planning agent for enterprise incident remediation.

Goal:
Restore healthy database connectivity for user-api.

Context:
- issue: Database connection pool exhausted
- environment: prod
- severity: critical
- symptoms:
  - API latency above 2000 ms
  - DB active connections at 100%
  - HTTP 500 errors increased

Constraints:
- avoid database restart unless necessary
- prefer low-risk steps first
- include validation checks

Think step by step and produce:
1. goal understanding
2. task decomposition
3. constraints
4. options considered
5. selected strategy
6. final step-by-step plan

Return JSON only.
```

## Planner output purpose

Planner CoT should answer:

- what problem are we solving
- what are the candidate strategies
- which strategy is safest/best
- what exact steps should be executed



## How to use CoT in Execute Agent

The **Execute Agent** uses CoT to transform:

`Current step + live observations → action`

## Execute Agent CoT flow

```
Current plan step
   ↓
Observe system state
   ↓
Analyze whether step is still valid
   ↓
Choose exact action
   ↓
Execute tool
   ↓
Check expected outcome
```

## Example executor prompt

```
You are an execution agent for enterprise incident remediation.

Goal:
Restore healthy database connectivity for user-api.

Current plan step:
Perform rolling restart of user-api pods.

Current observations:
- DB active connections = 100%
- API latency = 2400 ms
- DB sessions show many idle application connections

Constraints:
- use least risky action
- avoid DB restart
- log all production actions

Think step by step and produce:
1. step understanding
2. observation analysis
3. decision
4. action arguments
5. validation checks

Return JSON only.
```

## Executor CoT should answer

- does the current evidence support this action
- is there a lower-risk alternative
- what exact tool call should be made
- how will success be validated


## Planning Agent vs Execute Agent CoT

| Area            | Planning Agent               | Execute Agent                   |
| --------------- | ---------------------------- | ------------------------------- |
| Purpose         | create strategy              | perform current action safely   |
| Input           | goal, issue, context         | current step, live observations |
| Output          | plan                         | action                          |
| Reasoning focus | decomposition and sequencing | situational decision-making     |
| Time horizon    | multi-step                   | immediate step                  |


## Best practice in enterprise systems

For production systems, do **not rely on free-form hidden reasoning** alone. Use **structured reasoning output**.

Recommended pattern:

```
LLM CoT reasoning
  ↓
Structured JSON trace
  ↓
Validation
  ↓
Executor / next stage
```

This makes the system:

- auditable
- debuggable
- easier to replay
- safer for remediation use cases


## CoT prompt template can reuse


```
You are an enterprise reasoning agent.

Task:
Reason step by step before producing the final output.

Input:
{input_payload}

Instructions:
1. Understand the goal and context.
2. List key observations.
3. Generate possible hypotheses or options.
4. Analyze constraints and risks.
5. Choose the best next decision.
6. Produce structured JSON.

Output JSON format:
{
  "goal": "string",
  "observations": [],
  "hypotheses": [],
  "analysis_steps": [],
  "decision": "string",
  "decision_reason": "string",
  "output": {}
}
```

## Practical implementation pattern

Goal / Incident
   ↓
Planning Agent with CoT
   ↓
Plan JSON
   ↓
Execute Agent with CoT
   ↓
Action JSON
   ↓
Validator Agent
   ↓
Trace store / observability

## Minimal Python prompt example

```
from textwrap import dedent

incident = {
    "issue": "Database connection pool exhausted",
    "service": "user-api",
    "environment": "prod",
    "severity": "critical",
    "symptoms": [
        "API latency above 2000 ms",
        "DB active connections at 100%",
        "HTTP 500 errors increased"
    ]
}

planner_prompt = dedent(f"""
You are a planning agent for enterprise incident remediation.

Goal:
Restore healthy database connectivity for {incident['service']}.

Context:
- issue: {incident['issue']}
- environment: {incident['environment']}
- severity: {incident['severity']}
- symptoms: {incident['symptoms']}

Constraints:
- avoid database restart unless necessary
- prefer low-risk steps first
- include validation checks

Think step by step and return JSON with:
- goal_understanding
- task_decomposition
- constraints
- options_considered
- selected_strategy
- plan
""")

print(planner_prompt)
```

## Final takeaway

**CoT is not the final answer itself.**

It is the **reasoning process that produces better plans and actions**.

For agents:

- **Planning Agent uses CoT** to create the multi-step strategy
- **Execute Agent uses CoT** to decide the next safe action from live observations
- **CoT Trace** records that reasoning in structured form


A very practical mental model is:

```
Planning Agent CoT = strategic reasoning
Execute Agent CoT = tactical reasoning
```

