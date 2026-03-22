# 22 - Data Drift Detection and Monitoring

## 22.1 Drift Types
- covariate drift
- label drift
- concept drift (via outcome behavior)

## 22.2 Monitoring Metrics
- distribution divergence
- null and missingness shifts
- category frequency shifts
- freshness and latency metrics

## 22.3 Alerting Policy
Set severity levels and response actions for drift thresholds.

## 22.4 Retraining Triggers
Define clear rules for when drift requires retraining or rollback.

## 22.5 Real-Time Example
Alert when top-10 categorical distribution shifts beyond weekly baseline tolerance.

