# 03 - Data Collection, Ingestion, and APIs

## 3.1 Ingestion Sources
- batch files
- transactional databases
- event streams
- external APIs

## 3.2 Ingestion Patterns
- full refresh
- incremental loads
- CDC (change data capture)

## 3.3 API Ingestion
- pagination handling
- retry/backoff
- idempotency keys

## 3.4 Metadata Capture
Store ingestion timestamp, source id, and extraction version for auditability.

## 3.5 Real-Time Example
Fetch daily CRM updates via API and merge into warehouse with upsert logic.

