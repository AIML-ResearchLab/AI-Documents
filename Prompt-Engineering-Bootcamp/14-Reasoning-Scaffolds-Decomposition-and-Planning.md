# 14 - Reasoning Scaffolds, Decomposition, and Planning

## 14.1 Why Scaffolding Matters
Complex tasks fail when requested in one step. Decomposition improves reliability and observability.

## 14.2 Decomposition Pattern
1. Parse intent
2. Extract facts
3. Decide strategy
4. Produce answer in schema

## 14.3 Planning and Execution Separation
Use planner-executor separation for multi-step tasks:
- planner outputs step list
- executor runs steps with tool context

## 14.4 Verification Step
Add explicit check phase:
- schema validity
- evidence support
- policy compliance

## 14.5 Structured Reasoning Fields
Instead of opaque reasoning, require explicit fields:
- assumptions
- evidence
- confidence
- unresolved questions

## 14.6 Real-Time Example
Policy QA workflow:
- planner selects relevant policy sections
- executor drafts answer with citations
- verifier checks unsupported claims

## 14.7 Failure Controls
If verification fails, return fallback object with remediation instructions.

