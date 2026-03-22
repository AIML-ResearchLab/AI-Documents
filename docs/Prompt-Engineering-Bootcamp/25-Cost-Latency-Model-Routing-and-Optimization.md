# 25 - Cost, Latency, Model Routing, and Optimization

## 25.1 Optimization Objectives
Balance:
- output quality
- response latency
- operational cost

## 25.2 Cost Drivers
- input token volume
- output token volume
- model tier choice
- retry frequency

## 25.3 Latency Controls
- prompt compression
- context pruning
- async tool calls
- caching common results

## 25.4 Model Routing
Route requests by complexity and risk:
- small model for simple classification
- larger model for complex reasoning
- specialized model for domain tasks

## 25.5 Budget Guardrails
Enforce per-request and per-tenant budgets with fallback behavior.

## 25.6 Real-Time Example
Routing policy:
- FAQ -> low-cost model
- policy-sensitive case -> high-reliability model + verifier

## 25.7 Optimization Workflow
1. baseline quality/cost
2. apply one change at a time
3. evaluate regression suite
4. promote only if SLO/SLA targets pass

