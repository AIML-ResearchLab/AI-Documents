# 22 - Survival Analysis and Event-Time Modeling

## 22.1 Event-Time Data
Outcome is time until event (churn, failure, conversion), often with censoring.

## 22.2 Censoring Types
- Right censoring (most common)
- Left censoring
- Interval censoring

Ignoring censoring biases naive estimates.

## 22.3 Survival and Hazard Functions
- Survival: `S(t) = P(T > t)`
- Hazard: instantaneous event rate at time t

## 22.4 Kaplan-Meier Estimator
Nonparametric estimator of survival curve with censoring.

## 22.5 Cox Proportional Hazards Model
Semi-parametric model:
- interpretable hazard ratios
- proportional hazards assumption needs checking

## 22.6 Competing Risks
When multiple event types can terminate process, use competing-risk analysis.

## 22.7 Calibration and Utility
For churn-risk interventions, calibrate predicted survival probabilities and optimize intervention timing.

## 22.8 Real-Time Example
Subscription churn system:
- Estimate survival curve by cohort
- Trigger retention offers where hazard peaks
- Evaluate lift with controlled experiments

