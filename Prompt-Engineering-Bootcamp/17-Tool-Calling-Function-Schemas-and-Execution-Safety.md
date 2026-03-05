# 17 - Tool Calling, Function Schemas, and Execution Safety

## 17.1 Tool Use Contract
Tool calls require strict interface definitions:
- function name
- typed arguments
- validation rules
- failure responses

## 17.2 Schema-First Tool Prompts
Prompt should instruct model to:
- call tools only when needed
- never fabricate tool outputs
- handle tool errors explicitly

## 17.3 Tool Selection Strategy
Define criteria:
- confidence threshold for tool call
- priority among tools
- max tool call count per request

## 17.4 Safety Guardrails
- allow-list approved tools
- confirm sensitive actions
- deny unauthorized tool arguments

## 17.5 Recovery Patterns
- retry transient failures
- fallback to human escalation
- return deterministic error codes

## 17.6 Real-Time Example
Order-status bot:
- calls `get_order_status(order_id)`
- validates returned fields
- drafts response only from tool output

## 17.7 Observability
Log each tool decision and argument set for auditability.

