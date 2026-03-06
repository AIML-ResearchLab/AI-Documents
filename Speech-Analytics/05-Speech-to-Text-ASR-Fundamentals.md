# 05 - Speech-to-Text (ASR) Fundamentals

## Objective
Understand modern ASR systems and how to make them useful for analytics at scale.

## ASR Pipeline
1. Acoustic front-end features
2. Acoustic/encoder model
3. Decoder (CTC, transducer, or seq2seq)
4. Language model integration
5. Text normalization and punctuation

## Key Error Drivers
- Accent and dialect mismatch
- Domain terminology and named entities
- Crosstalk and overlapping speech
- Low SNR and compression artifacts

## Quality Improvements
- Domain lexicon and phrase hints
- Fine-tuning on in-domain audio/transcripts
- Post-ASR normalization (numbers, acronyms, dates)
- Human-in-the-loop correction for high-risk workflows

## Real-Time Example
An insurance claims center adds policy/product phrase hints to streaming ASR. Proper noun recognition improves, reducing claim-routing errors and manual correction effort.

## SLP3 Coverage Mapping
- Ch. 15.1 ASR task definition
- Ch. 15.3 encoder-decoder ASR
- Ch. 15.5 CTC
- Ch. 15.6 WER evaluation
