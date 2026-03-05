# 21 - Data Versioning, Lineage, and Reproducibility

## 21.1 Versioning Strategy
Version:
- raw data snapshots
- transformation code
- output datasets
- feature definitions

## 21.2 Lineage Tracking
Capture source-to-output dependency graph for every produced dataset.

## 21.3 Reproducibility Contract
A dataset should be regenerable from pinned source versions and transformation config.

## 21.4 Auditability
Store who changed what, when, and why.

## 21.5 Real-Time Example
Reproduce model training dataset from prior month during incident investigation.

