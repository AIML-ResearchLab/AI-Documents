# 25 - Reliability Patterns: Retries, Idempotency, and Failure Recovery

## 25.1 Retry Design
Use bounded exponential backoff with error-class-aware retry policies.

## 25.2 Idempotent Operations
Guarantee safe replays for task submission and artifact updates.

## 25.3 Failure Domains
Contain faults and prevent cascading failure across agent networks.

## 25.4 Real-Time Example
Payment-advice agent recovers from timeout without duplicate transaction recommendations.
