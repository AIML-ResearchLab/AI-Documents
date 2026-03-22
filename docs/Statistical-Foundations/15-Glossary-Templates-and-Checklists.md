# 15 - Glossary, Templates, and Checklists

## 15.1 Glossary
- Estimator: rule to estimate parameter from data
- Standard error: uncertainty of estimator across samples
- Confidence interval: plausible range from repeated-sampling procedure
- p-value: extremeness probability under null model
- Power: probability of detecting true effect
- Calibration: probability predictions matching empirical frequency
- Drift: distributional change over time
- Confounder: variable affecting both treatment and outcome

## 15.2 Statistical Report Template
```text
Objective
Data description
Assumptions
Method
Results (point estimate + uncertainty)
Sensitivity checks
Recommendation
Limitations
```

## 15.3 Model Metric Reporting Template
```text
Metric: {{name}}
Point estimate: {{value}}
95% CI: {{lower}} to {{upper}}
Segment breakdown: {{segments}}
Trend vs baseline: {{delta}}
```

## 15.4 Pre-Deployment Statistical Checklist
- Data sampling method documented
- Leakage checks passed
- Confidence intervals reported
- Threshold selected by cost and risk
- Drift monitors configured
- Rollback criteria defined

## 15.5 Post-Deployment Checklist
- Weekly metric uncertainty review
- Segment-wise fairness checks
- Drift alerts operational
- Incident root-cause analysis template ready

## 15.6 30-Day Revision Plan
1. Week 1: probability + random variables
2. Week 2: estimation + hypothesis testing
3. Week 3: Bayesian + regression + metrics
4. Week 4: experiments + causality + robustness labs

