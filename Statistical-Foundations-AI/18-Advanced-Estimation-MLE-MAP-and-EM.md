# 18 - Advanced Estimation: MLE, MAP, and EM

## 18.1 Maximum Likelihood Estimation (MLE)
MLE chooses parameter `theta` maximizing likelihood of observed data.

Properties (under regularity):
- Consistent
- Asymptotically normal
- Often efficient

## 18.2 Score and Fisher Information
- Score: gradient of log-likelihood
- Fisher information: expected curvature of log-likelihood

These quantify identifiability and estimator uncertainty.

## 18.3 MAP Estimation
MAP adds prior information:
`theta_MAP = argmax log p(data|theta) + log p(theta)`

Useful under data sparsity or when domain priors are strong.

## 18.4 Expectation-Maximization (EM)
EM handles latent variables/incomplete data.

Iteration:
1. E-step: compute expected complete-data log-likelihood
2. M-step: maximize expectation w.r.t. parameters

## 18.5 EM Use Cases in AI
- Gaussian Mixture Models
- Missing-data imputation workflows
- Hidden-variable models

## 18.6 Identifiability and Local Optima
EM and likelihood methods can converge to local maxima.
Use multi-start initialization and stability checks.

## 18.7 Uncertainty Estimation
- Hessian-based approximation
- Bootstrap confidence intervals
- Bayesian posterior alternatives

## 18.8 Real-Time Example
Customer segmentation with GMM:
- Fit with EM
- Validate cluster stability across seeds
- Reject unstable segment solution before deployment

