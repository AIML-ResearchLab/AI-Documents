# 26 - Privacy, Security, and Compliance in Speech Data

## Objective
Protect sensitive voice and transcript data across collection, storage, processing, and sharing.

## Security Baseline
- Encryption in transit and at rest
- Role-based access and least privilege
- Key management and secret rotation
- Immutable audit logging

## Privacy Controls
- PII/PCI redaction in transcripts and audio snippets
- Data minimization and retention windows
- Consent tracking and jurisdiction-aware policy routing

## Compliance Workflow
- Control mapping to internal/legal policies
- Automated evidence collection for audits
- Continuous control testing in CI/CD

## Real-Time Example
A healthcare call platform redacts PHI entities in near real time and blocks unauthorized playback requests via policy-based access checks.

## SLP3 Coverage Mapping
- Ch. 15 and Ch. 25 outputs as sensitive operational data requiring governance
