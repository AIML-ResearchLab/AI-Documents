# 20 - Structured Outputs, Contracts, and Validator Design

## 20.1 Output Contracts
Every machine-consumed response should have a strict schema with required fields and enums.

## 20.2 Validation Layers
- syntactic validation (JSON/schema)
- semantic validation (cross-field logic)
- policy validation (allowed content)

## 20.3 Unknown and Null Policy
Define explicit handling:
- use `unknown` when evidence missing
- never infer prohibited fields

## 20.4 Repair and Retry Flow
If validation fails:
1. return validation errors
2. re-prompt with error context
3. retry with bounded attempts

## 20.5 Schema Evolution
Version schemas and maintain backward compatibility for consuming services.

## 20.6 Real-Time Example
Lead scoring API contract:
- strict enum for lead_tier
- confidence range 0-1
- reasons array with max length

## 20.7 Governance Rule
No production deploy without schema tests in CI.

