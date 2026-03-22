# 19 - Multi-Agent Systems and Coordination Patterns

## 19.1 When Multi-Agent Helps
Use multiple agents when tasks require distinct skills, independent checks, or parallel processing.

## 19.2 Coordination Patterns
- supervisor-routed specialists
- debate/critic pattern
- parallel gather and consolidate
- planner with specialist executors

## 19.3 Communication Protocols
Use structured inter-agent messages:
- task
- assumptions
- evidence
- confidence
- next action

## 19.4 Conflict Resolution
Supervisor resolves disagreement with rules:
- evidence quality priority
- policy compliance priority
- tie-break by deterministic rubric

## 19.5 Cost and Latency Tradeoff
Multi-agent systems improve quality but increase latency and token usage.

## 19.6 Real-Time Example
Compliance report generation:
- legal agent validates policy clauses
- finance agent validates numbers
- editor agent creates final report

## 19.7 Safety Controls
Prevent recursive loops and unbounded delegation depth.

