# 03 - Prompt Design Principles

## 3.1 Prompt Anatomy
A production-grade prompt normally includes:
1. Role
2. Objective
3. Input context
4. Constraints
5. Output format
6. Validation instructions

## 3.2 Design Frameworks

### RTF
- Role
- Task
- Format

### TAG
- Task
- Action
- Goal

### BROKE
- Background
- Role
- Objective
- Key Result
- Evolution

Use frameworks as scaffolding, then refine with domain constraints.

## 3.3 Clarity and Specificity Rules
- Replace vague verbs: use classify, extract, compare, generate, validate
- Add measurable constraints: word count, section count, schema fields
- State allowed and disallowed behaviors

## 3.4 Output Contracting
For machine workflows:
- Request JSON only
- Provide fixed field names
- Define enums
- Define unknown/null handling
- Define validation requirements

## 3.5 Prompt Anti-Patterns
- Ambiguous objective
- Conflicting instructions
- Missing schema
- Overly long irrelevant context
- No unknown handling
- No failure behavior

## 3.6 Failure-Mode-Driven Prompting
Include explicit failure behavior:
- "If evidence is missing, return unknown"
- "If request violates policy, decline with reason code"
- "If schema cannot be satisfied, return error object"

## 3.7 Quality Rubric
Score each prompt 1-5:
- Clarity
- Grounding
- Structure
- Reliability
- Actionability

## 3.8 Prompt Versioning Standard
Keep version notes:
- v1 baseline
- v2 constraints added
- v3 schema hardened
- v4 safety/policy integrated

Include before/after metric deltas for each change.

