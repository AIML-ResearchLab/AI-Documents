# 23 - Advanced Causal Inference for AI

## 23.1 Potential Outcomes Framework
- `Y(1)` outcome under treatment
- `Y(0)` outcome under control
- Individual treatment effect is unobservable jointly

Targets:
- ATE (average treatment effect)
- ATT (effect on treated)

## 23.2 Identification Assumptions
- Consistency
- Positivity
- Exchangeability / no unmeasured confounding (for observational designs)

## 23.3 Propensity Score Methods
- Matching
- Stratification
- Inverse probability weighting
- Overlap diagnostics required

## 23.4 Doubly Robust Estimation
Combines outcome model and propensity model; consistent if one is correctly specified.

## 23.5 Instrumental Variables
Use when unmeasured confounding exists and valid instrument is available.

## 23.6 Difference-in-Differences
Estimate treatment effect from pre/post changes in treated vs control.
Requires parallel-trends assessment.

## 23.7 Regression Discontinuity
Exploit cutoff-based treatment assignment for local causal effects.

## 23.8 Real-Time Example
Policy change in recommender ranking:
- Estimate causal impact on retention
- Run observational doubly robust estimate
- Validate with randomized holdout where feasible

