# 29 - Incident Response, Runbooks, and Reliability

## 29.1 Common Data Incidents
- broken schema ingest
- delayed source feed
- corrupt partition
- feature freshness outage

## 29.2 Runbook Structure
1. detect
2. triage severity
3. contain impact
4. remediate
5. postmortem

## 29.3 Reliability Metrics
- MTTD
- MTTR
- pipeline success rate
- recurring incident rate

## 29.4 Fallback Patterns
- previous validated snapshot
- degraded feature mode
- traffic throttling for non-critical jobs

## 29.5 Real-Time Example
Rollback to last valid feature snapshot during upstream ingestion outage.

