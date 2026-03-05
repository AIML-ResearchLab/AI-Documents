# 13 - Production MLOps and Deployment

## 13.1 Deployment Patterns
- Batch inference
- Real-time API inference
- Streaming inference

## 13.2 Inference Contract
Define strict input/output schema and version it.

## 13.3 Packaging
- Bundle model + preprocessors
- Pin dependency versions
- Store artifacts with metadata

## 13.4 Monitoring
Track:
- latency
- error rate
- feature drift
- prediction drift
- business KPI impact

## 13.5 Retraining Triggers
- data drift threshold crossed
- metric degradation
- policy change or new data availability

## 13.6 CI/CD for ML
Pipeline should include:
- tests
- data checks
- model evaluation gate
- security and compliance checks

## 13.7 Governance
- Model cards
- Approval workflows
- Audit logs
- Responsible AI checks

## 13.8 Incident Response
Create runbooks for:
- failed deployments
- spike in bad predictions
- degraded latency
- unexpected model bias

