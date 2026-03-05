# 17 - Exponential Family, GLM, and Probabilistic Modeling

## 17.1 Exponential Family Form
Many common distributions can be written as:
`p(y|theta) = h(y) exp(theta^T T(y) - A(theta))`

This unifies estimation and inference across models.

## 17.2 Sufficient Statistics
`T(y)` summarizes information needed for parameter inference, reducing complexity.

## 17.3 Generalized Linear Models (GLMs)
GLMs connect predictors to non-Gaussian outcomes.

Components:
- Random component (distribution family)
- Linear predictor `eta = X beta`
- Link function `g(E[y]) = eta`

## 17.4 Common GLMs in AI
- Logistic regression for binary outcomes
- Poisson regression for counts
- Gamma regression for positive skewed targets

## 17.5 Estimation and Diagnostics
- MLE via iterative optimization (IRLS for many GLMs)
- Residual diagnostics and deviance
- Overdispersion checks in count models

## 17.6 Regularized GLMs
Use L1/L2 penalties to reduce variance and improve generalization.

## 17.7 Probabilistic Modeling Perspective
GLMs are probabilistic prediction systems, not only curve-fitting methods. They provide uncertainty-aware outputs.

## 17.8 Real-Time Example
Demand forecasting for ticket arrivals:
- Model hourly counts via Poisson/Negative Binomial
- Include calendar and event features
- Output confidence bounds for staffing decisions

