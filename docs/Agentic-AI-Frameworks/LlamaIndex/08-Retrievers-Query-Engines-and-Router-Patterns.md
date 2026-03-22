# 08 - Retrievers, Query Engines, and Router Patterns

## 8.1 Retriever Role
Retrievers select candidate nodes relevant to user intent.

## 8.2 Query Engine Role
Query engines synthesize final responses using retriever outputs.

## 8.3 Router Patterns
Routers dispatch queries to specialized retrievers or engines.

## 8.4 Reliability Controls
Set fallback retrievers for low-confidence or empty-result scenarios.

## 8.5 Real-Time Example
Router sends pricing queries to structured index and policy queries to semantic index.
