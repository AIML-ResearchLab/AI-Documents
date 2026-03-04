# 06 - Structured Outputs, Tools, and Agents

## 6.1 Structured Outputs
Machine-integrated applications require predictable outputs.

Core practices:
- Request strict JSON
- Define required and optional fields
- Use enums for constrained categories
- Include explicit unknown/null policy
- Validate and retry on parse failure

## 6.2 JSON Schema-First Prompting
Example instruction:
```text
Return JSON only. Do not include markdown or prose outside the schema.
If required field is unavailable, use "unknown".
```

## 6.3 Function and Tool Calling
When external data/actions are needed:
1. Model decides if tool is needed
2. Application executes tool
3. Model receives tool result
4. Model produces final response

Design goals:
- Tool descriptions must be explicit
- Arguments must be typed and validated
- Tool failure paths must be handled

## 6.4 Agent Patterns

### Single Agent
One model handles planning and execution. Simple but can drift.

### Planner-Executor
Planner creates steps, executor performs each step. Better control and observability.

### Supervisor + Specialists
A coordinator routes tasks to specialized agents (legal, finance, technical).

## 6.5 Memory Patterns
- Session memory: current conversation state
- Task memory: workflow state and outputs
- Long-term memory: user preferences, approved facts, policies

Memory safety:
- avoid storing secrets in free-text memory
- version memory schema
- expire stale memory records

## 6.6 Agent Guardrails
- Enforce tool allow-lists
- Require confirmation for sensitive actions
- Limit recursive planning depth
- Add watchdog timeouts and retry limits

## 6.7 Real-Time Tool Example
Task: "Check order status and draft an update email"

Workflow:
1. Use order lookup tool with order_id
2. Parse tool output for status, ETA
3. Draft customer update using fixed template
4. Return JSON with `status`, `eta`, `email_draft`

