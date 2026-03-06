# 06 - Speaker Diarization and Speaker ID Basics

## Objective
Separate “who spoke when” and connect speech turns to speaker identities for analytics, QA, and compliance.

## Core Tasks
- **Diarization**: partition audio into speaker-homogeneous segments.
- **Speaker identification**: map voice to known identity set.
- **Speaker verification**: confirm claimed identity.

## Typical Pipeline
- VAD -> embedding extraction (x-vector/ECAPA style) -> clustering -> overlap handling -> resegmentation

## Operational Concerns
- Channel mismatch can hurt speaker embeddings.
- Overlapping speech inflates diarization error.
- Identity systems require strong consent and governance.

## Real-Time Example
A BPO QA platform uses diarization to isolate agent vs customer turns, enabling separate sentiment trajectories and accurate script-adherence scoring.

## SLP3 Coverage Mapping
- Ch. 15 ASR outputs as diarization input
- Ch. 25 turn-taking structure for speaker-change reasoning
