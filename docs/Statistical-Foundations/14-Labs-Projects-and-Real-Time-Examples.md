# 14 - Labs, Projects, and Real-Time Examples

## Lab 1 - Probability and Bayes in AI Alerts
Build a notebook that:
1. Simulates rare event detection
2. Computes base-rate adjusted posterior alert probability
3. Compares naive vs Bayes-calibrated interpretation

## Lab 2 - Confidence Intervals on Model Metrics
Given classification outputs:
- estimate accuracy and F1
- compute bootstrap confidence intervals
- report uncertainty-aware conclusion

## Lab 3 - Hypothesis Test for Model Upgrade
Test whether new model improves conversion or reduces error rate.

Required output:
- null/alternative
- p-value
- confidence interval
- practical effect recommendation

## Lab 4 - A/B Test Analysis
Analyze treatment/control outcomes with guardrails:
- sample ratio mismatch check
- primary and secondary metric review
- stopping rule compliance check

## Lab 5 - Time-Series Drift Monitoring
Build rolling dashboard for:
- mean prediction score
- error rate by week
- drift alerts

## Real-Time Example 1: Support Priority Confidence
Input stream:
```text
Ticket classifier predicts P1 with probability 0.62
```

Decision pattern:
- if calibrated probability > business threshold, auto-escalate
- else route for manual review
- log confidence interval trend weekly

## Real-Time Example 2: Fraud Threshold Adjustment
Scenario:
- false negatives are expensive
- investigation capacity limited

Task:
- simulate thresholds from 0.1 to 0.9
- compute precision, recall, and expected cost
- select threshold minimizing expected loss

## Capstone Project
Choose one domain (support, fraud, marketing, healthcare ops) and deliver:
1. statistical problem framing
2. data summary + assumptions
3. test/estimation workflow
4. uncertainty-aware recommendations
5. reproducible report

