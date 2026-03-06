# 13 - Speech Pipelines, Tracking, and Reproducibility

## Objective
Ensure every model result can be reproduced from versioned code, data, and configuration.

## Pipeline Stages to Version
- Raw audio snapshot and ingestion manifest
- Preprocessing config (VAD, denoise, normalization)
- Feature extractor version
- Model weights and decoding parameters
- Postprocessing rules (normalization, redaction)

## Experiment Tracking
- Log runs with dataset hash, hyperparameters, metrics, artifacts
- Record slice-level metrics (accent, noise, region, call type)
- Attach failure examples for error analysis

## Real-Time Example
A regression appears after model upgrade. Because feature and decoder versions are pinned, the team reproduces the issue and rolls back in under 20 minutes.

## SLP3 Coverage Mapping
- Ch. 15 ASR architecture/evaluation dependencies
- Ch. 4 reproducible evaluation discipline
