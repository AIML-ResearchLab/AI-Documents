# 24 - Advanced Experimental Design and Sequential Testing

## 24.1 Beyond Basic A/B Testing
Production experimentation often includes repeated looks, multiple metrics, and operational constraints.

## 24.2 Sequential and Group-Sequential Testing
Allow interim analyses while controlling type-I error.

Tools:
- Alpha-spending functions
- O'Brien-Fleming and Pocock-style boundaries

## 24.3 CUPED and Variance Reduction
Use pre-experiment covariates to reduce variance and shorten test duration.

## 24.4 Multi-Armed Bandits
Adaptive allocation methods improve cumulative reward but complicate unbiased effect estimation.

## 24.5 Interference and Network Effects
When units affect each other, standard independence assumptions fail.
Use cluster-based designs where possible.

## 24.6 Cluster and Switchback Designs
- Cluster randomized trials for spillover contexts
- Switchback tests for marketplace/logistics systems

## 24.7 Metric Governance
Define:
- Primary metric
- Guardrail metrics
- Kill-switch rules
- Pre-registered analysis plan

## 24.8 Real-Time Example
Ranking experiment in marketplace:
- Switchback by hour/region
- Guardrail on cancellation rate
- Sequential stopping with controlled false-positive risk

