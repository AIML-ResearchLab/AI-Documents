# 26 - Versioning, Experimentation, and Release Engineering

## 26.1 Prompt Versioning Standard
Each version should include:
- prompt diff
- rationale
- benchmark results
- rollback pointer

## 26.2 Experiment Types
- offline benchmark experiments
- shadow testing in production
- A/B controlled rollout

## 26.3 Release Gates
Promote only when gates pass:
- quality thresholds
- safety thresholds
- latency/cost thresholds

## 26.4 Canary and Rollback
Start with small traffic share and auto-rollback on guardrail breach.

## 26.5 Change Taxonomy
Tag changes as:
- instruction change
- context strategy change
- model parameter change
- validator change

## 26.6 Real-Time Example
Prompt v12 rollout:
- 5% canary for 2 hours
- no safety regression
- quality +2.4 points
- promote to 100%

## 26.7 Documentation Requirement
No release without experiment report and post-release monitoring plan.

