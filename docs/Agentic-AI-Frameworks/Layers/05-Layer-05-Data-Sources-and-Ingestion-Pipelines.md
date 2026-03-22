# 05 - Layer 05: Data Sources and Ingestion Pipelines

## 5.1 Purpose
Bring enterprise data into the agentic system with controlled freshness.

## 5.2 Core Decisions
Choose connectors, update cadence, and ingestion reliability model.

## 5.3 Design Artifacts
Source inventory, ingestion DAGs, and freshness SLOs.

## 5.4 Failure Mode
Stale or partial data leads to incorrect agent reasoning.

## 5.5 Real-Time Example
CRM and policy documents ingest hourly with change-data-capture updates.
