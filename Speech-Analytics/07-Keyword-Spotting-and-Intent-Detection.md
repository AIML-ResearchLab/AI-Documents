# 07 - Keyword Spotting and Intent Detection

## Objective
Detect critical phrases and classify intent quickly enough to trigger real-time actions.

## Two Complementary Tasks
- **Keyword spotting (KWS)**: phrase-level trigger detection (e.g., cancellation, legal risk).
- **Intent detection**: classify user goal from utterance or turn window.

## Design Patterns
- Fast KWS model for immediate alerts
- Contextual intent model on rolling transcript window
- Confidence thresholds + fallback routing logic

## Error Handling
- Calibrate thresholds to reduce false alarms.
- Use confusion matrices by business intent.
- Include abstain/unknown class for out-of-domain utterances.

## Real-Time Example
During subscription calls, a “cancel my plan” phrase triggers retention flow suggestions and instantly displays eligible offer playbooks to the agent.

## SLP3 Coverage Mapping
- Ch. 4 classification and evaluation
- Ch. 17 sequence labeling cues
- Ch. 25 dialog context effects on meaning
