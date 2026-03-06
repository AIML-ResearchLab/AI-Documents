# 17 - Multilingual Speech Processing and Code-Switching

## Objective
Build speech analytics that work across languages and mixed-language conversations.

## Core Challenges
- Language identification in short turns
- Intra-sentence code-switching
- Non-uniform lexicons and transliteration
- Accent and dialect variability

## Practical Patterns
- Multi-stage pipeline: LID -> multilingual ASR -> language-aware NLP
- Shared multilingual embeddings with locale-specific adaptation
- Separate evaluation slices by language pair and switch frequency

## Real-Time Example
A global support desk handling Hindi-English calls uses dynamic language routing per turn, reducing transcription errors in mixed-language escalation calls.

## SLP3 Coverage Mapping
- Ch. 15 ASR generalization limits
- Ch. 2 tokenization/Unicode foundations for multilingual text
