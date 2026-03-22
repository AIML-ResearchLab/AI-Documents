# 26 - Statistical Learning Theory and Generalization

## 26.1 Empirical Risk Minimization
Models optimize training loss, but objective is low expected risk on unseen data.

## 26.2 Bias-Variance Decomposition
Generalization error combines approximation bias and estimation variance.

## 26.3 Capacity and Complexity
Model capacity concepts:
- VC dimension intuition
- Rademacher complexity intuition

Higher capacity increases overfitting risk without enough data or regularization.

## 26.4 Generalization Bounds (Conceptual)
PAC-style guarantees provide probabilistic upper bounds on test risk given complexity and sample size.

## 26.5 Domain Shift and OOD
Training and deployment distributions may differ.
Track:
- covariate shift
- label shift
- concept shift

## 26.6 Validation Design
- Nested CV for model selection fairness
- Time-aware splits for sequential data
- Segment-aware validation for reliability

## 26.7 Real-Time Example
Model retains offline AUC but fails in new geography due to covariate shift.
Mitigation: region-aware calibration + monitoring + targeted retraining.

