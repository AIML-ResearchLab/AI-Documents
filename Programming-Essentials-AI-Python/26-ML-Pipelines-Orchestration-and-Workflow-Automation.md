# 26 - ML Pipelines, Orchestration, and Workflow Automation

## 26.1 Pipeline Components
- data ingestion
- validation
- feature engineering
- training
- evaluation
- registration
- deployment

## 26.2 Orchestration Concepts
Use DAG-based orchestration with explicit dependencies and retries.

## 26.3 Reproducible Pipeline Runs
Track:
- code version
- dataset snapshot
- config values
- environment image

## 26.4 Scheduling and Backfills
- periodic retraining schedule
- historical backfill with deterministic configs

## 26.5 Artifact and Metadata Management
Store models, metrics, and lineage in central registry/metadata store.

## 26.6 Failure Handling
- task-level retry policy
- idempotent writes
- alerting on repeated stage failures

## 26.7 Real-Time Example
Nightly churn pipeline:
- ingest latest events
- run quality gates
- train candidate
- promote only if gate metrics pass

