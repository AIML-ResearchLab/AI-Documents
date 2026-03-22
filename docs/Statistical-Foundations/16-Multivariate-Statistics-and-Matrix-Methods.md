# 16 - Multivariate Statistics and Matrix Methods

## 16.1 Random Vectors and Covariance Structure
For a random vector `X in R^d`:
- Mean vector: `mu = E[X]`
- Covariance matrix: `Sigma = E[(X-mu)(X-mu)^T]`

`Sigma` is symmetric and positive semi-definite. Its structure drives feature dependence modeling.

## 16.2 Multivariate Normal Distribution
`X ~ N(mu, Sigma)` is central to many AI methods.

Key properties:
- Marginals and conditionals are Gaussian
- Linear transforms preserve Gaussianity
- Mahalanobis distance defines ellipsoidal contours

## 16.3 Covariance and Precision Matrices
- Covariance matrix captures pairwise dependence
- Precision matrix `Omega = Sigma^{-1}` encodes conditional independence patterns (Gaussian setting)

## 16.4 Eigenvalues, SVD, and PCA
- Eigendecomposition and SVD are core matrix tools
- PCA projects to low-dimensional subspace maximizing variance
- Explained-variance analysis guides dimensionality selection

## 16.5 Whitening and Feature Decorrelation
Whitening transforms reduce feature correlation and can stabilize optimization in some pipelines.

## 16.6 High-Dimensional Covariance Estimation
When `d` approaches or exceeds `n`, sample covariance is unstable.
Use:
- Shrinkage estimators
- Factor models
- Sparse precision estimation

## 16.7 Real-Time AI Example
Embedding monitoring:
1. Track mean vector and covariance of embedding batches
2. Measure drift with Mahalanobis distance
3. Alert when drift exceeds calibrated threshold

## 16.8 Practical Checklist
- Standardize features before covariance analysis
- Check condition number of covariance matrix
- Use robust alternatives when outliers are present

