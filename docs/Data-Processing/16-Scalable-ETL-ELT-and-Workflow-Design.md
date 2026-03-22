# 16 - Scalable ETL/ELT and Workflow Design

## 16.1 Architecture Patterns
- ETL for strict transformations before load
- ELT for warehouse-native transformations

## 16.2 Workflow Design
- DAG-based dependency graph
- idempotent task design
- retry and checkpoint strategy

## 16.3 Batch Windowing
Define ingestion and processing windows with clear SLA boundaries.

## 16.4 Real-Time Example
Nightly ELT pipeline builds model features from event lakehouse tables.

