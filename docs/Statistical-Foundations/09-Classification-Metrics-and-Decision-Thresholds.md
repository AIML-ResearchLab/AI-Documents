# 09 - Classification Metrics and Decision Thresholds

## 9.1 Confusion Matrix
- True Positive
- False Positive
- True Negative
- False Negative

## 9.2 Metric Definitions
- Accuracy
- Precision
- Recall
- F1 score
- Specificity

## 9.3 Threshold Tuning
Predicted probability must be converted to class using threshold.

Lower threshold:
- more positives found
- more false positives

Higher threshold:
- fewer false positives
- more missed positives

## 9.4 ROC and PR Curves
- ROC useful for balanced classes
- PR more informative for rare positive classes

## 9.5 Calibration
Probability outputs should match observed frequencies.

## 9.6 Cost-Sensitive Decisions
Choose threshold based on business cost matrix, not metric alone.

## 9.7 Real-Time Example
Fraud model threshold moved from 0.5 to 0.3 to reduce missed fraud, with controlled review capacity.

