# 13 - RAG Pipeline Orchestration and Reproducibility

## 13.1 Pipeline Steps
ingest -> index -> retrieve -> rerank -> generate -> validate.

## 13.2 Versioning
version corpus snapshot, embedding model, index config, and prompt templates.

## 13.3 Reproducibility
fixed eval set and deterministic pipeline config for release comparisons.

## 13.4 Real-Time Example
Rollback to prior embedding/index version after quality regression.

