# 16 - Advanced ASR Architectures and Adaptation

## Objective
Move beyond baseline ASR with architectures and adaptation methods tuned for production domains.

## Advanced Architectures
- Conformer/transformer encoders for robust speech modeling
- Encoder-decoder and transducer variants for streaming/offline tradeoffs
- Self-supervised pretraining (e.g., HuBERT-like approaches) for low-label settings

## Adaptation Levers
- Domain fine-tuning with curated in-domain audio
- Dynamic vocabulary injection and contextual biasing
- LM rescoring for domain terminology and phrase structure

## Real-Time Example
A legal-tech platform fine-tunes on courtroom audio and adds legal phrase biasing. Transcript fidelity for named entities rises enough to reduce manual review workload.

## SLP3 Coverage Mapping
- Ch. 15.3 encoder-decoder ASR
- Ch. 15.4 self-supervised speech models
- Ch. 15.5 CTC/decoding concepts
