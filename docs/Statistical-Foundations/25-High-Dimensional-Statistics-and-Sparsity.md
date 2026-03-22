# 25 - High-Dimensional Statistics and Sparsity

## 25.1 High-Dimensional Regime
When features `p` are comparable to or greater than samples `n`, classical estimators become unstable.

## 25.2 Regularization Strategies
- Ridge (L2): shrink coefficients smoothly
- Lasso (L1): sparse feature selection
- Elastic Net: balance sparsity and stability

## 25.3 Feature Selection Stability
Selection can vary strongly across samples.
Use stability selection and repeated resampling.

## 25.4 Sparse Covariance and Graphical Models
Estimate sparse precision matrices for conditional dependency structure.

## 25.5 Multiple Testing in High Dimensions
Control false discoveries with:
- Benjamini-Hochberg FDR
- Knockoff-style methods

## 25.6 Dimension Reduction
- PCA and sparse PCA
- Autoencoder embeddings (statistical caution on interpretability)

## 25.7 Real-Time Example
Text-based risk model with 100k sparse features:
- train elastic-net logistic model
- monitor selected-feature drift across retrains

## 25.8 Practical Guardrails
- Standardize features
- Validate under repeated folds
- Report confidence/stability for selected features

