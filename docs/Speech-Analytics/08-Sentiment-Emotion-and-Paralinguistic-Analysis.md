# 08 - Sentiment, Emotion, and Paralinguistic Analysis

## Objective
Estimate customer affect with lexical + acoustic evidence, while controlling for bias and uncertainty.

## Task Breakdown
- **Sentiment**: polarity (positive/neutral/negative)
- **Emotion**: anger, frustration, relief, confusion, etc.
- **Paralinguistics**: cues from tone, loudness, pause, and speaking rate

## Modeling Notes
- Fuse transcript features with prosody for stronger robustness.
- Use calibration and confidence bands in high-stakes workflows.
- Track subgroup performance to avoid demographic harm.

## Real-Time Example
A utility provider flags calls with sustained negative sentiment plus raised vocal intensity, then inserts de-escalation guidance into the agent-assist panel.

## SLP3 Coverage Mapping
- Ch. 22 sentiment and affect lexicons
- Ch. 14.3 prosody
- Ch. 4 precision/recall and error analysis
