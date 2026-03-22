# 24 - Unstructured Data Pipelines for LLM and RAG

## 24.1 Pipeline Steps
- document ingestion
- parsing and cleaning
- chunking
- embedding generation
- indexing and retrieval

## 24.2 Chunking Strategy
Choose chunk size and overlap based on retrieval quality and latency tradeoffs.

## 24.3 Metadata Schema
Store source, section, timestamp, access policy, and trust level.

## 24.4 Quality Checks
- OCR confidence thresholds
- duplicate chunk detection
- citation traceability

## 24.5 Real-Time Example
Policy assistant refreshes vector index daily and validates citation coverage before release.

