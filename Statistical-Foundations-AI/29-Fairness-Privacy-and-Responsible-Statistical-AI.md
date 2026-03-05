# 29 - Fairness, Privacy, and Responsible Statistical AI

## 29.1 Fairness Metrics
Common group-level metrics:
- Demographic parity
- Equal opportunity
- Equalized odds
- Calibration within groups

Metrics can conflict; selection depends on context, harm model, and policy.

## 29.2 Counterfactual Fairness Intuition
Assess whether prediction would remain similar under counterfactual changes to protected attributes.

## 29.3 Bias Diagnostics
- Performance by subgroup
- Error asymmetry analysis
- Threshold impact analysis

## 29.4 Privacy-Preserving Statistics
- Differential privacy basics (`epsilon`, `delta`)
- Noise mechanisms for aggregate statistics
- Membership-inference risk awareness

## 29.5 Governance Practices
- Model cards and data cards
- Decision logs for high-impact thresholds
- Human override and escalation paths

## 29.6 Compliance-Oriented Reporting
Every deployment report should include:
- fairness metrics by segment
- uncertainty and confidence reporting
- privacy risk notes
- approved mitigations

## 29.7 Real-Time Example
Loan-risk model:
- optimize recall subject to fairness constraints
- calibrate probabilities separately by allowed policy framework
- require manual review for high-uncertainty borderline decisions

