# 02 - Model Behavior and Parameters

## 2.1 Determinism vs Variability
LLM outputs can change between runs due to probabilistic token sampling.

Use lower variability settings for business-critical tasks, such as extraction, classification, compliance summaries, and structured outputs.

## 2.2 Key Generation Controls

### Temperature
Controls randomness.
- Low (0.0 to 0.3): stable, factual, structured tasks
- Medium (0.4 to 0.7): balanced creativity
- High (0.8+): brainstorming and ideation

### top_p
Limits token selection to a cumulative probability mass.
- Lower top_p tightens choices
- Use either top_p or temperature tuning first, not aggressive tuning of both at once

### max_tokens
Caps output length. Prevents runaways and cost spikes.

### Frequency/Presence Penalties
Useful when model repeats content excessively.

### Stop Sequences
Hard stop markers for safe truncation when needed.

## 2.3 Token Budgeting
Total tokens include:
- System/developer instructions
- User input
- Retrieved context
- Output tokens

Design rule: reserve output budget explicitly so responses do not truncate.

## 2.4 Context Window Strategy
- Keep context high-signal only
- Remove redundant instructions
- Prefer retrieved snippets over full documents
- Use chunking and reranking for long knowledge bases

## 2.5 Parameter Presets by Task
- Extraction/classification: temperature 0.0-0.2
- Analytics summaries: temperature 0.2-0.4
- Content drafts: temperature 0.5-0.8
- Brainstorming: temperature 0.8-1.0 with strict post-filtering

## 2.6 Cost-Latency-Quality Tradeoff
- Longer prompts increase cost and latency
- More context can improve groundedness but may reduce relevance if noisy
- Multi-stage pipelines often outperform one giant prompt

## 2.7 Practical Guardrail Defaults
- Set max output tokens explicitly
- Use strict schema for machine-consumed output
- Add fallback behavior if parsing fails
- Log parameter settings with each run for traceability

