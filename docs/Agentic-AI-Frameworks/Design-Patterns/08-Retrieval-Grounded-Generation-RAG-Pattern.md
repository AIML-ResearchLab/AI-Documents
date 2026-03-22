# 08 - Retrieval Grounded Generation (RAG) Pattern

## 8.1 Pattern Intent
Ground model outputs on retrieved evidence to improve factual reliability.

## 8.2 Core Stages
Ingest -> index -> retrieve -> rerank -> synthesize -> cite.

## 8.3 Quality Controls
Use citation coverage and faithfulness checks before response release.

## 8.4 Failure Handling
Trigger re-retrieval when evidence confidence is insufficient.

## 8.5 Real-Time Example
Policy assistant refuses answer when retrieval sources are stale or conflicting.
