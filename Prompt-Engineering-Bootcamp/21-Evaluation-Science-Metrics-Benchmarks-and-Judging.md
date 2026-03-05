# 21 - Evaluation Science, Metrics, Benchmarks, and Judging

## 21.1 Evaluation Strategy
Use layered evaluation:
- unit-like prompt checks
- benchmark dataset scoring
- human review
- production telemetry

## 21.2 Metric Design
Task metrics may include:
- exact match / extraction accuracy
- groundedness
- schema pass rate
- refusal correctness
- latency and cost

## 21.3 Benchmark Construction
Include:
- normal cases
- edge cases
- adversarial cases
- policy-sensitive cases

## 21.4 LLM-as-Judge Usage
Use judge models with calibration:
- anchor against human labels
- monitor judge drift
- avoid single-judge dependence

## 21.5 Regression Gates
Any prompt/version change should run benchmark regression before release.

## 21.6 Real-Time Example
Customer reply assistant:
- benchmark 200 tickets weekly
- compare relevance and tone rubric
- auto-block release on policy failure rate increase

## 21.7 Reporting Standard
Publish scorecards with confidence intervals and failure taxonomy.

