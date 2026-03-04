# 04 - Prompting Techniques

## 4.1 Zero-Shot Prompting
No examples provided. Works when task is clear and common.

Use for:
- Simple classification
- Basic summaries
- Standard transformations

## 4.2 Few-Shot Prompting
Provide high-quality examples to anchor behavior.

Rules:
- Use representative edge cases
- Keep example style aligned to expected output
- Prefer fewer, better examples over many noisy examples

## 4.3 Task Decomposition
Split complex tasks into subtasks:
1. Understand input
2. Extract facts
3. Reason over facts
4. Format output

This improves reliability and debugging.

## 4.4 Reflection and Critique Loops
Pattern:
1. Generate initial answer
2. Critique against rubric
3. Revise answer

Useful for long-form analysis and policy-sensitive tasks.

## 4.5 Reasoning Scaffolds
Instead of requesting hidden reasoning, ask for explicit structured analysis fields:
- assumptions
- evidence
- alternatives
- confidence

## 4.6 ReAct-Style Tool Use
When tools are available:
- ask model to decide whether tool use is required
- fetch evidence with tools
- synthesize final answer from tool results

## 4.7 Multi-Objective Prompting
If multiple objectives exist, define priority order:
1. Safety and policy compliance
2. Factual groundedness
3. Correct format
4. Style and tone

## 4.8 Domain-Specific Prompt Patterns
- Extraction: schema-first, temperature low
- Summarization: audience + format + constraints
- Planning: milestones + dependencies + risks
- Coding: acceptance tests + constraints + edge cases

## 4.9 Real-Time Mini Example
Baseline:
```text
Summarize this sales call.
```
Improved:
```text
You are a sales operations analyst.
Summarize the transcript into:
1) customer goals
2) objections
3) next steps with owner and due date
Return JSON only. Use "unknown" for missing owner/date.
```

