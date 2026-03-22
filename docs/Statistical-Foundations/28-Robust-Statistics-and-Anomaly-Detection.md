# 28 - Robust Statistics and Anomaly Detection

## 28.1 Why Robust Methods
Real-world AI data often contains outliers, heavy tails, and labeling noise.

## 28.2 Robust Location and Scale
- Median and MAD
- Trimmed means
- Winsorization

## 28.3 Robust Estimation Frameworks
- Huber loss
- Tukey biweight
- M-estimators

## 28.4 Influence and Breakdown
- Influence function measures estimator sensitivity
- Breakdown point quantifies robustness under contamination

## 28.5 Anomaly Detection Methods
- Statistical z-score and robust z-score
- Isolation Forest
- One-class SVM
- Local Outlier Factor
- Extreme Value Theory thresholding

## 28.6 Contamination Modeling
Explicitly model expected contamination fraction for stable thresholds.

## 28.7 Real-Time Example
Fraud pipeline:
- robustly estimate transaction baseline
- detect anomalies with EVT-calibrated threshold
- update thresholds by region and time-of-day

## 28.8 Operational Rules
- Separate anomaly detection from final decision policy
- Track false-positive burden on review teams
- Recompute baselines periodically

