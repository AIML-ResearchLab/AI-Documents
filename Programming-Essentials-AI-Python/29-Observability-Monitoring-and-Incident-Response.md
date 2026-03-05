# 29 - Observability, Monitoring, and Incident Response

## 29.1 Observability Stack
Collect logs, metrics, traces, and model-quality signals.

## 29.2 What to Monitor
- system metrics: latency, CPU, memory, errors
- model metrics: calibration, drift, accuracy proxy
- business metrics: conversion, resolution rate, churn impact

## 29.3 Drift Monitoring
Detect:
- covariate drift
- prediction drift
- label drift (when delayed labels arrive)

## 29.4 Alerting Strategy
- severity levels
- on-call ownership
- runbook links in alerts

## 29.5 Incident Lifecycle
1. detect
2. triage
3. contain
4. mitigate
5. postmortem and prevention

## 29.6 Postmortem Standard
Include timeline, root cause, blast radius, corrective actions, and validation steps.

## 29.7 Real-Time Example
Quality drop incident:
- drift alarm triggers
- traffic routed to prior stable model
- retraining hotfix initiated with expedited review

