# 19 - Resampling, Bootstrap, and Nonparametric Inference

## 19.1 Why Resampling
Resampling quantifies uncertainty when analytic formulas are hard or assumptions are weak.

## 19.2 Bootstrap
Procedure:
1. Resample with replacement from dataset
2. Recompute statistic many times
3. Use empirical distribution for intervals/SE

Common intervals:
- Percentile interval
- BCa interval (bias-corrected and accelerated)

## 19.3 Jackknife
Leave-one-out resampling for bias/variance approximation.

## 19.4 Permutation Tests
Assess significance by shuffling labels under null hypothesis.
Useful for robust nonparametric hypothesis testing.

## 19.5 Rank-Based Tests
- Mann-Whitney U
- Wilcoxon signed-rank
- Kruskal-Wallis

Useful when normality assumptions are unreliable.

## 19.6 Cross-Validation as Statistical Estimator
CV estimates generalization error with variance; report mean and spread.

## 19.7 Real-Time Example
Evaluate F1 uplift of a new classifier with bootstrap CIs:
- If CI excludes zero uplift threshold, promote candidate model

## 19.8 Best Practices
- Preserve grouping/time structure in resampling
- Use stratified resampling for imbalanced classes
- Report number of resamples and random seed

