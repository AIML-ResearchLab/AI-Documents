# 27 - Uncertainty Quantification, Calibration, and Conformal

## 27.1 Types of Uncertainty
- Aleatoric: inherent data noise
- Epistemic: uncertainty from limited knowledge/data

## 27.2 Predictive Intervals
For regression or forecasts, provide interval estimates with target coverage.

## 27.3 Probability Calibration
Classification probabilities should match observed frequencies.

Methods:
- Temperature scaling
- Platt scaling
- Isotonic regression

## 27.4 Calibration Diagnostics
- Reliability diagrams
- Expected calibration error (ECE)
- Brier score

## 27.5 Conformal Prediction
Distribution-free uncertainty sets with finite-sample coverage guarantees (under assumptions).

Variants:
- Split conformal
- Cross-conformal
- Mondrian conformal (group-conditional)

## 27.6 Real-Time Example
Medical triage model:
- output risk score + conformal prediction set
- defer uncertain cases to clinicians
- monitor empirical coverage by subgroup

## 27.7 Deployment Guidance
- Recalibrate after significant drift
- Track interval width and coverage together
- Use selective prediction/defer policies in high-risk systems

