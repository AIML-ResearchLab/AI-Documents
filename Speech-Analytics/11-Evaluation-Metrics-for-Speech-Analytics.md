# 11 - Evaluation Metrics for Speech Analytics

## Objective
Use the right metric per component, and avoid misleading “single score” reporting.

## Component-Wise Metrics
- **ASR**: WER, CER, domain-specific keyword recall
- **Diarization**: DER and overlap-aware DER
- **Intent/Compliance classifiers**: precision, recall, F1, AUPRC
- **Sentiment/Emotion**: macro F1, calibration error, subgroup parity gaps
- **Summarization**: task-grounded human eval + factuality checks

## Evaluation Strategy
- Split by channel, accent, region, and domain
- Report confidence intervals and significance when comparing models
- Track online-vs-offline performance drift

## Real-Time Example
A model with lower global WER still misses compliance phrases in accented calls. The team adds phrase-level recall KPI and catches the regression before production rollout.

## SLP3 Coverage Mapping
- Ch. 15.6 WER
- Ch. 4 evaluation metrics and significance
- Ch. 22 sentiment evaluation concerns
