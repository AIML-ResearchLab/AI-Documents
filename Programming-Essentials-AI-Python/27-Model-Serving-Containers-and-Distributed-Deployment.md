# 27 - Model Serving, Containers, and Distributed Deployment

## 27.1 Serving Patterns
- batch scoring
- online synchronous inference
- asynchronous job-based inference

## 27.2 Containerization
Package service with pinned dependencies and health checks.

## 27.3 Deployment Strategies
- blue/green
- canary
- shadow deployments

## 27.4 Horizontal Scaling
Scale stateless inference replicas by latency/throughput targets.

## 27.5 Stateful Dependencies
Plan for feature store, cache, and model registry connectivity and failover.

## 27.6 Performance SLOs
Define and monitor:
- p50/p95 latency
- error rate
- throughput
- timeout rate

## 27.7 Real-Time Example
Canary rollout:
- send 5% traffic to new model
- monitor guardrail metrics
- auto-rollback on threshold breach

