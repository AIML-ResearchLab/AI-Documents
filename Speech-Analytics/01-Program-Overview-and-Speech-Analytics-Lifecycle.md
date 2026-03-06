# 01 - Program Overview and Speech Analytics Lifecycle

## Module Goal
Build a production-ready understanding of speech analytics from audio capture to business actions, grounded in SLP3 (Jurafsky & Martin, 2026).

## End-to-End Lifecycle
1. **Capture and ingest**: telephony, meeting, bot, and media streams.
2. **Preprocess**: resample, denoise, segment with VAD, normalize loudness.
3. **Transcribe and segment speakers**: ASR + diarization.
4. **Analyze**: intent, sentiment, emotion, compliance, conversation quality.
5. **Act**: alerts, agent assist, summaries, QA scoring, workflow triggers.
6. **Operate**: monitor drift, latency, costs, model quality, and incidents.

## Architecture Building Blocks
- Audio gateway and stream processor
- Feature/embedding service
- ASR + diarization services
- NLP analytics layer (classification, extraction, summarization)
- Serving APIs, dashboards, and case-management integrations

## Real-Time Example
A banking contact center streams live calls. Within 2 seconds, the system flags missing KYC statements, detects customer frustration, and recommends a compliant response script to the agent desktop.

## SLP3 Coverage Mapping
- Ch. 14: speech features and prosody foundations
- Ch. 15: ASR pipeline and WER
- Ch. 22: sentiment/affect lexicons
- Ch. 25: conversation structure

## What to Track from Day 1
- Quality: WER, DER, intent F1, sentiment calibration
- Reliability: p95 end-to-end latency, drop rate, retry rate
- Governance: PII redaction success, policy violations, access audit events
