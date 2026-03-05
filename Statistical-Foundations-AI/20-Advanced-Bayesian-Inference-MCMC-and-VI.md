# 20 - Advanced Bayesian Inference: MCMC and VI

## 20.1 Bayesian Inference at Scale
Closed-form posteriors are rare in complex models.
Approximate methods are required.

## 20.2 MCMC Basics
Markov Chain Monte Carlo draws samples from posterior.

Common methods:
- Metropolis-Hastings
- Gibbs sampling
- Hamiltonian Monte Carlo (HMC)
- NUTS (adaptive HMC)

## 20.3 Variational Inference (VI)
VI converts inference to optimization by fitting a tractable distribution to posterior.

Tradeoff:
- Faster than MCMC in large systems
- May underestimate posterior uncertainty

## 20.4 Diagnostics
Mandatory checks:
- Trace plots
- Effective sample size
- R-hat convergence metric
- Posterior predictive checks

## 20.5 Prior Sensitivity Analysis
Evaluate how conclusions change under alternative reasonable priors.

## 20.6 Hierarchical Bayesian Models
Useful for multi-group AI systems (regions, products, segments) with partial pooling.

## 20.7 Real-Time Example
Bayesian conversion model:
- Update posteriors daily
- Produce credible intervals by segment
- Escalate when posterior probability of decline exceeds threshold

## 20.8 Deployment Guidance
- Cache posterior summaries
- Monitor inference runtime
- Use VI for low-latency approximations with periodic MCMC calibration

