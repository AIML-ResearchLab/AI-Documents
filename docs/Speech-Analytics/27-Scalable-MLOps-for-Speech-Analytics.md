# 27 - Scalable MLOps for Speech Analytics

## Objective
Operate speech analytics models across environments with reliable delivery, observability, and rollback.

## MLOps Foundations
- CI/CD for model + feature + policy artifacts
- Staged promotion (dev -> staging -> prod)
- Canary and champion/challenger evaluation
- Automated rollback rules tied to SLO breaches

## Platform Considerations
- GPU/CPU mix and autoscaling
- Feature stores for reusable speech/text features
- Registry for model and decoder versions
- Workflow orchestration for retraining and evaluation

## Real-Time Example
A platform rollout uses canary traffic on one call queue; rising DER triggers automatic rollback before full deployment.

## SLP3 Coverage Mapping
- Ch. 15 model changes directly affect WER and downstream KPIs
- Ch. 4 disciplined evaluation in deployment loops
