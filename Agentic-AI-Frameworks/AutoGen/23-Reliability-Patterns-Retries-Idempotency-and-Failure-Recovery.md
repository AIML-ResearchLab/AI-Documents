# 23 - Reliability Patterns: Retries, Idempotency, and Failure Recovery

## 23.1 Retry Policies
Use bounded retries with error-class-aware backoff strategies.

## 23.2 Idempotent Design
Ensure replay-safe execution for tool actions and state transitions.

## 23.3 Failure Isolation
Contain faults to local sub-workflows and avoid cascade failures.

## 23.4 Recovery Playbooks
Define checkpoint resume, compensation, and rollback actions.

## 23.5 Real-Time Example
Order workflow recovers from API timeout without duplicate order placement.
