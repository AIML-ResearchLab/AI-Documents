# 25 - Testing, Evaluation, and Regression Quality Gates

## 25.1 Test Pyramid
Combine unit tests for plugins, integration tests for kernel flows, and scenario tests for agents.

## 25.2 Evaluation Metrics
Track task success, factual consistency, policy adherence, latency, and cost.

## 25.3 Regression Harness
Run fixed benchmark suites for every prompt/model/configuration update.

## 25.4 Release Gates
Prevent deployment when quality or safety metrics regress.

## 25.5 Real-Time Example
Release pipeline blocks prompt change after benchmark detects reduced grounding accuracy.
