# 28 - Security, Privacy, and Compliance for Python AI

## 28.1 Threat Model Basics
- data exfiltration
- model abuse
- prompt injection (LLM systems)
- unauthorized API access

## 28.2 Secure Coding Practices
- validate all external input
- avoid unsafe deserialization
- use dependency vulnerability scanning

## 28.3 Secrets Management
Never hardcode credentials. Use secure secret stores and rotate credentials.

## 28.4 Data Privacy Controls
- PII minimization
- encryption in transit and at rest
- retention and deletion policies

## 28.5 Compliance Readiness
- audit logs
- access controls
- policy-based approvals for high-impact workflows

## 28.6 Secure MLOps
- signed artifacts
- immutable model versions
- provenance checks before deployment

## 28.7 Real-Time Example
Sensitive support model:
- redact personal data before inference
- enforce scoped tokens
- log access per request id

