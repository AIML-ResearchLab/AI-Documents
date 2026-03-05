# 07 - Tool Calling and Action Execution Pattern

## 7.1 Pattern Intent
Convert model decisions into validated, auditable external actions.

## 7.2 Contract Requirements
Tools require strict schema, side-effect classification, and timeout policies.

## 7.3 Execution Guardrails
Apply confirmation gates for high-impact or irreversible operations.

## 7.4 Reliability Controls
Use retries, idempotency keys, and compensation handlers.

## 7.5 Real-Time Example
Payment tool requires dual confirmation and idempotency token before transfer.
