# 12 - Structured Output, Schemas, and Validation

## 12.1 Structured Output Need
Schema-constrained output improves reliability for downstream systems.

## 12.2 Strategy Modes
Use provider-native structured output when available; fallback to tool-based strategies otherwise.

## 12.3 Validation Pipeline
Validate output types, required fields, and semantic constraints before execution.

## 12.4 Failure Recovery
Retry with corrective prompts or fallback schemas on validation failure.

## 12.5 Real-Time Example
Lead-qualification agent outputs strict JSON schema for CRM ingestion without manual cleanup.
