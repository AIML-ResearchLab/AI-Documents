# 01 - Foundations

## 1.1 What Is Prompt Engineering
Prompt engineering is the discipline of designing inputs, context, constraints, and output contracts so LLM behavior is reliable, useful, and measurable.

It is not only writing one clever prompt. It is a lifecycle:
1. Define task and success criteria
2. Design prompt and output schema
3. Test on representative data
4. Evaluate and iterate
5. Deploy with monitoring and guardrails

## 1.2 Why Prompt Engineering Matters
- LLM outputs are probabilistic, not guaranteed
- Small instruction changes can produce large behavior shifts
- Business workflows require repeatability and traceability

## 1.3 Core Terms
- Prompt: Instructions and context given to model
- Completion/Response: Model output
- Context window: Maximum tokens model can process
- Hallucination: Unsupported or fabricated content
- Grounding: Tying output to trusted sources
- Schema: Enforced output structure

## 1.4 Instruction Hierarchy
Models follow instruction priority levels. In practical systems:
1. System-level constraints (global behavior)
2. Developer/application instructions
3. User instructions
4. Tool outputs and retrieved context

Design rule: higher-priority safety and policy constraints must remain explicit and always-on.

## 1.5 Prompt Lifecycle
- Discovery: understand user intent and business process
- Design: create role, objective, constraints, output schema
- Validation: run against sample set, record failures
- Hardening: add guardrails, retries, fallback behavior
- Production: monitor quality, latency, and cost

## 1.6 Common Misconceptions
- "Better wording always solves it": false, context quality and schema control matter more
- "One prompt fits all": false, domain-specific prompts perform better
- "High temperature is always creative and better": false, can reduce reliability

## 1.7 Baseline Prompt Pattern
Use this minimal production skeleton:

```text
Role: You are {{assistant_role}}.
Objective: {{clear_goal}}.
Context: {{trusted_context}}.
Constraints:
- {{rules}}
Output Format:
{{strict_schema_or_template}}
Quality Checks:
- No unsupported claims
- Mark unknowns explicitly
```

## 1.8 Foundation Quality Rules
- Be explicit about task and boundaries
- Separate instructions from context using delimiters
- Define acceptance criteria before testing
- Never deploy without evaluation dataset

