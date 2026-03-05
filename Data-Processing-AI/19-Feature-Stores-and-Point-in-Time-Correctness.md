# 19 - Feature Stores and Point-in-Time Correctness

## 19.1 Why Feature Stores
Ensure training-serving feature consistency and reuse across teams.

## 19.2 Offline vs Online Stores
- offline for training and analysis
- online for low-latency inference

## 19.3 Point-in-Time Joins
Avoid future leakage by joining features using event timestamp boundaries.

## 19.4 Feature Definitions
Each feature should include owner, logic, freshness SLA, and monitoring metrics.

## 19.5 Real-Time Example
Churn model uses online features with 5-minute freshness guarantee.

