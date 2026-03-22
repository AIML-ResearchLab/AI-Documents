# 21 - Real-Time Streaming Speech Analytics Systems

## Objective
Design low-latency systems that transform speech streams into actionable insights while calls are in progress.

## Streaming Reference Architecture
- Ingestion (SIP/WebRTC/Kafka)
- Chunking and VAD
- Incremental ASR + diarization
- Online analytics (intent, compliance, sentiment)
- Event router and agent-assist UI/webhook output

## Latency Budgeting
- Audio chunking: 200–500 ms
- ASR incremental decode: sub-second
- Analytics + action dispatch: sub-second
- End-to-end target: typically < 2–3 s for live assistance

## Reliability Patterns
- Backpressure-aware queues
- Graceful degradation (disable heavy models first)
- Idempotent event publication
- Regional failover

## Real-Time Example
A card-services center streams live calls and triggers PCI warning prompts within 1.5 seconds when card-number disclosure risk is detected.

## SLP3 Coverage Mapping
- Ch. 15 ASR as real-time foundation
- Ch. 25 turn-taking and dialog timing
