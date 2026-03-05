# 24 - PromptOps, Observability, Tracing, and Quality Monitoring

## 24.1 PromptOps Scope
PromptOps covers lifecycle operations:
- prompt development
- evaluation
- release
- monitoring
- incident response

## 24.2 Required Telemetry
Track per request:
- prompt version
- model and parameters
- context sources
- tool calls
- validation outcome
- quality signals

## 24.3 Tracing
Use end-to-end traces for multi-step and agentic workflows to diagnose failures fast.

## 24.4 Quality Dashboards
Monitor:
- schema pass rate
- groundedness score
- refusal correctness
- latency/cost trends

## 24.5 Alerting
Set alerts for sudden increases in:
- unsupported claims
- policy failures
- retry loops

## 24.6 Real-Time Example
Support bot quality regression:
- alert triggers on policy violation spike
- route traffic to prior stable prompt
- run targeted failure analysis

## 24.7 Operational Maturity
Adopt on-call runbooks and weekly quality review cadences.

