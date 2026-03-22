# 20 - Production Architecture, Deployment, and Scaling with CrewAI

## 20.1 Reference Topology
API gateway -> flow runtime -> crews -> tools/integrations -> observability and storage.

## 20.2 Deployment Models
Choose managed, self-hosted, or hybrid deployment based on compliance and control needs.

## 20.3 Scaling Patterns
Scale by queue depth, flow concurrency, and tool dependency bottlenecks.

## 20.4 Operational Discipline
Use canary releases, feature flags, and rollback automation.

## 20.5 Real-Time Example
Automation platform scales flows during end-of-month spikes without SLA violations.
