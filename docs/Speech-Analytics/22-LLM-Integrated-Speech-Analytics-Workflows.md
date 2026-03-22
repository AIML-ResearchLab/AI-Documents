# 22 - LLM-Integrated Speech Analytics Workflows

## Objective
Use LLMs to add reasoning, summarization, extraction, and policy interpretation on top of speech pipelines.

## Integration Patterns
- Transcript cleanup and structure normalization
- Intent/entity extraction with chain-of-thought hidden from users
- Policy-aware response recommendations
- Multi-turn summarization and action item extraction

## Guardrails
- Constrain output with schemas and validators
- Ground critical outputs in transcript spans
- Route uncertain outputs for human review
- Enforce prompt/version management for reproducibility

## Real-Time Example
An enterprise helpdesk uses LLM post-processing to generate structured “issue, root cause, next action” cards during calls, reducing wrap-up time.

## SLP3 Coverage Mapping
- Ch. 7 LLM fundamentals
- Ch. 8 transformer foundations
- Ch. 10 post-training and alignment concepts
