# 07 - Evaluation and Experimentation

## 7.1 Why Evaluation Is Mandatory
Without evaluation, prompt changes are opinion-driven. Production systems need measurable quality and regression control.

## 7.2 Build an Evaluation Dataset
Include:
- Typical cases
- Edge cases
- Adversarial inputs
- Policy-sensitive cases
- Negative controls

Recommended minimum: 30 to 100 examples for early-stage systems.

## 7.3 Core Metrics
- Accuracy: factual correctness
- Relevance: task alignment
- Completeness: required fields/sections present
- Groundedness: evidence-backed claims
- Consistency: stable outputs across runs
- Latency: response time
- Cost: tokens and API spend

## 7.4 Rubric Design
Create a 1-5 rubric with clear scoring guidance for each metric.

Example:
- 5 = fully correct, complete, grounded, format-valid
- 3 = partially correct or missing minor elements
- 1 = incorrect, ungrounded, or unusable

## 7.5 Evaluation Methods
- Automated checks: schema validity, regex rules, exact match checks
- LLM-as-judge: useful but calibrate against human labels
- Human review: final authority for nuanced quality and policy issues

## 7.6 Regression Testing
Every prompt change should run against a fixed benchmark suite.

Track:
- pass rate
- average rubric score
- failure categories
- latency and cost deltas

## 7.7 A/B Testing in Production
- Split traffic across prompt versions
- Compare quality and operational metrics
- Define stop rules for negative drift

## 7.8 Real-Time Experiment Example
Objective: improve support triage accuracy from 82% to 92%.

Plan:
1. Baseline current prompt on 100 labeled tickets
2. Add explicit category definitions and examples
3. Re-test and compare confusion matrix
4. Promote only if accuracy and latency targets pass

