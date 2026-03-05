# 07 - Bayesian Statistics for AI

## 7.1 Bayesian Core Equation
Posterior is proportional to prior times likelihood:
`P(theta|data) proportional to P(data|theta) * P(theta)`

## 7.2 Components
- Prior: belief before seeing data
- Likelihood: data generation model
- Posterior: updated belief
- Posterior predictive: prediction with uncertainty

## 7.3 MAP vs MLE
- MLE maximizes likelihood
- MAP maximizes posterior (includes prior)

## 7.4 Conjugate Prior Intuition
Some prior-likelihood pairs yield closed-form posteriors, enabling fast updates.

## 7.5 Bayesian Decision Making
Use expected utility or expected loss for action selection.

## 7.6 Real-Time Example
Spam probability update after observing words in an email stream using prior spam rate and likelihood ratios.

## 7.7 Practical Benefits in AI
- Better uncertainty handling in low-data settings
- Natural incorporation of prior domain knowledge
- Continuous online updates

