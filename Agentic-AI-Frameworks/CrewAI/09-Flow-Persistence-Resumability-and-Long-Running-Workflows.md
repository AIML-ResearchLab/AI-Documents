# 09 - Flow Persistence, Resumability, and Long-Running Workflows

## 9.1 Persistence Purpose
Persist flow state to survive restarts and continue long-running automations.

## 9.2 Persistence Scopes
Apply `@persist` at class level or method level based on control needs.

## 9.3 Resume Strategy
Use state IDs and checkpointed data to safely resume interrupted workflows.

## 9.4 Reliability Patterns
Combine persistence with retry logic and idempotent side-effect boundaries.

## 9.5 Real-Time Example
Background onboarding flow resumes after outage without losing user progress.
