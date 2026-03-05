# 28 - Production Playbooks, Runbooks, and Incident Response

## 28.1 Why Runbooks Matter
Prompt systems fail in production due to drift, policy changes, context issues, and tool outages.

## 28.2 Incident Types
- quality degradation
- safety violation
- latency spike
- cost anomaly
- tool dependency failure

## 28.3 Incident Runbook Template
1. detect and classify severity
2. contain impact (fallback/rollback)
3. diagnose root cause
4. patch and validate
5. publish postmortem

## 28.4 Rollback Strategy
Maintain last-known-good prompt version and deterministic rollback command path.

## 28.5 On-Call Metrics
- MTTD
- MTTR
- recurrence rate

## 28.6 Real-Time Example
Retrieval outage:
- switch to cached evidence mode
- reduce feature set
- notify users of degraded confidence

## 28.7 Postmortem Quality
Record timeline, blast radius, root cause, preventive actions, and owner deadlines.

