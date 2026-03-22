# 08 - Regression and Generalization Statistics

## 8.1 Linear Regression Refresher
Model: `y = beta0 + beta1*x1 + ... + betak*xk + error`

## 8.2 OLS Assumptions (Practical)
- Linear relationship (or transformed to near-linear)
- Independent errors
- Constant variance (homoscedasticity)
- Limited multicollinearity

## 8.3 Coefficient Interpretation
Coefficient indicates expected change in y for one unit x increase, holding others fixed.

## 8.4 Residual Diagnostics
- Residual plots
- QQ plot intuition
- Outlier and leverage checks

## 8.5 Regularization Statistics
- Ridge reduces variance
- Lasso supports sparsity
- Elastic net combines both

## 8.6 Generalization
Focus on out-of-sample performance, not only training fit.

## 8.7 Real-Time Example
Predict delivery delay from traffic/weather features and compare OLS vs Ridge on validation RMSE.

