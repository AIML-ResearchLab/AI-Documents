# 07 - Tools Design, ToolRuntime, and Execution Safety

## 7.1 Tool Contracts
Tools are callable functions with explicit inputs, outputs, and behavior constraints.

## 7.2 ToolRuntime Access
`ToolRuntime` provides state, store, context, and stream writer access inside tools.

## 7.3 Safety Controls
Validate arguments, enforce authorization, and limit side-effectful operations.

## 7.4 Error Handling
Use deterministic tool error responses and retry policies where appropriate.

## 7.5 Real-Time Example
Payment tool requires validated account scope and explicit approval before transfer execution.
