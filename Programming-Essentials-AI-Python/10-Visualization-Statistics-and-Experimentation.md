# 10 - Visualization, Statistics, and Experimentation

## 10.1 Visualization Basics
Use plots to validate data assumptions before modeling.

Libraries:
- matplotlib
- seaborn

## 10.2 Common Plot Types
- Histogram for distribution
- Box plot for outliers
- Scatter plot for relationships
- Line chart for time trends

## 10.3 Descriptive Statistics
- Mean, median, mode
- Variance and standard deviation
- Percentiles and quantiles

## 10.4 Statistical Concepts for AI
- Sampling bias
- Correlation vs causation
- Confidence intervals
- Hypothesis testing basics

## 10.5 Experiment Design
- Define hypothesis
- Set primary metric
- Select baseline/control
- Run test and analyze significance

## 10.6 Metrics by Task
- Classification: accuracy, precision, recall, F1, ROC-AUC
- Regression: MAE, MSE, RMSE, R2

## 10.7 Real-Time Experiment Example
Goal: increase support intent classifier F1 from 0.84 to 0.90.

Plan:
1. Baseline current features and model
2. Add engineered text features
3. Retrain with same split
4. Compare F1 and calibration

