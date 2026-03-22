# 15 - Glossary, Templates, and Checklists

## Essential Glossary
- **WER**: Word Error Rate for ASR quality
- **DER**: Diarization Error Rate for speaker segmentation
- **VAD**: Voice Activity Detection for speech/non-speech segmentation
- **CTC**: alignment-free sequence objective in ASR
- **RTF**: Real-Time Factor, processing speed vs audio duration

## Deployment Readiness Checklist
- Data and consent review complete
- Bias and subgroup performance report approved
- Latency and throughput tested at expected peak
- Alerting and rollback drills completed
- PII redaction and access controls verified

## Incident Template
- Detection timestamp and impacted services
- Blast radius (users, regions, call queues)
- Root cause hypothesis and evidence
- Mitigation actions and rollback status
- Post-incident prevention tasks

## Real-Time Example
A release checklist catches missing redaction in one locale before launch, preventing a privacy breach.

## SLP3 Coverage Mapping
- Ch. 15 metrics terminology
- Ch. 22 affect terminology
- Ch. 25 conversation terminology
