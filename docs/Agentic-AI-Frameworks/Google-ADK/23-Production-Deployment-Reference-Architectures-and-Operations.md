# 23 - Production Deployment Reference Architectures and Operations

## 23.1 Reference Topology
Ingress -> runtime/API layer -> orchestration workers -> tool services -> observability plane.

## 23.2 Platform Options
Deploy on Agent Engine, Cloud Run, GKE, or hybrid combinations.

## 23.3 Release Engineering
Adopt canary rollout, feature flags, and automated rollback.

## 23.4 Operability
Prepare runbooks for model outages, tool failures, and policy incidents.

## 23.5 Real-Time Example
Enterprise rollout uses staged regional deployment with automatic rollback thresholds.
