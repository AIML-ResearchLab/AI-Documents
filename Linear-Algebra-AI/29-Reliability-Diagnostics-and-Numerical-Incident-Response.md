# 29 - Reliability Diagnostics and Numerical Incident Response

## 29.1 Common Incidents
- exploding/vanishing values
- NaN propagation
- solver non-convergence
- unstable gradients

## 29.2 Monitoring Signals
- gradient norm statistics
- condition-number trend
- NaN/Inf counters
- residual and convergence logs

## 29.3 Response Runbook
1. detect and isolate
2. rollback to last stable config
3. patch numeric guardrails
4. validate on benchmark suite

## 29.4 Real-Time Example
Model training halted on NaN spike; root cause traced to mixed-precision overflow.

