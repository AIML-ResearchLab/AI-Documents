# 06 - Graph Ingestion, ETL, and Data Quality Engineering

## 6.1 Ingestion Pipeline
extract -> normalize -> identity resolution -> edge construction -> validation -> load.

## 6.2 Entity Resolution
Match duplicate entities using deterministic rules and probabilistic scoring.

## 6.3 Quality Controls
Track missing relations, orphan nodes, invalid edge types, and freshness metrics.

## 6.4 Incremental Updates
Use change-data-capture and idempotent writes for near-real-time graph sync.

## 6.5 Real-Time Example
Fraud graph updates every minute from transaction streams and account events.
