# 13 - Reliability, Retry, Idempotency, and Compensation Pattern

## 13.1 Pattern Intent
Maintain correctness under partial failures and retries.

## 13.2 Retry Design
Use bounded backoff with error-type-aware retry policies.

## 13.3 Idempotency
Ensure repeated execution does not duplicate side effects.

## 13.4 Compensation
Define undo workflows for partially completed multi-step actions.

## 13.5 Real-Time Example
Order workflow retries inventory check but avoids duplicate reservation.
