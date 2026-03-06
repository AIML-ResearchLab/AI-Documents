# 19 - Advanced Speaker Verification and Biometrics

## Objective
Design secure speaker verification pipelines with explicit risk controls.

## Verification Architecture
- Enrollment (reference voiceprint creation)
- Verification scoring against claimed identity
- Thresholding based on risk policy
- Liveness and anti-spoof checks

## Key Metrics
- FAR (false accept rate)
- FRR (false reject rate)
- EER (equal error rate)
- Detection performance under spoof attacks

## Real-Time Example
A phone-banking IVR adds liveness checks and adaptive thresholds for high-value transactions, reducing fraud attempts while keeping customer friction manageable.

## SLP3 Coverage Mapping
- Ch. 15 speech representation relevance to speaker modeling
- Ch. 4 thresholding and classification tradeoffs
