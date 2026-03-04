# 12 - Glossary, Templates, and Checklists

## 12.1 Glossary
- Prompt: structured instructions to guide model output
- Context window: max tokens model can process
- Hallucination: unsupported generated content
- Grounding: linking claims to trusted evidence
- Few-shot: examples included in prompt
- RAG: retrieval-augmented generation
- Schema: strict output structure definition
- Tool calling: model-requested invocation of external functions
- Agent: orchestrated model workflow with goals and actions
- Regression test: repeatable benchmark to detect performance drop

## 12.2 Universal Production Prompt Template
```text
Role:
You are {{role}}.

Objective:
{{objective}}

Context:
{{trusted_context}}

Instructions:
1) {{instruction_1}}
2) {{instruction_2}}
3) {{instruction_3}}

Constraints:
- {{constraint_1}}
- {{constraint_2}}
- If unknown, return "unknown"

Output Format:
Return JSON only using this schema:
{{schema}}

Validation:
- Ensure all required fields exist
- No unsupported claims
- Respect policy constraints
```

## 12.3 Pre-Deployment Checklist
- Prompt has clear objective
- Output schema validated
- Failure behavior defined
- Evaluation suite passes threshold
- Safety tests pass
- Logging and monitoring enabled
- Rollback version prepared

## 12.4 Post-Deployment Checklist
- Daily quality sampling active
- Drift alerts configured
- Token cost monitored
- Incident runbook tested
- Prompt improvement backlog maintained

## 12.5 Review Template
Use this template during prompt reviews:
1. What task is this prompt solving?
2. What can fail and why?
3. Is schema strict enough for downstream systems?
4. Are safety constraints explicit?
5. Which metrics prove improvement?

## 12.6 Interview Questions (Prompt Engineer)
- How do you evaluate prompt quality?
- How do you design for unknown data?
- How do you defend against injection?
- How do you version and roll back prompts?
- How do you balance latency, cost, and accuracy?

