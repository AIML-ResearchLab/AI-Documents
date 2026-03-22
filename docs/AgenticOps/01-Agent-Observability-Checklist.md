# Agent Observability Checklist

Use this as a quick checklist when shipping agentic/LLM systems (especially tool-using, multi-step agents).

## What to capture (per run)

- Prompt + system instructions (with versions)
- Model name/config (temperature, top_p, etc.)
- Reasoning/step trace (plan → tool → reflect → next action)
- Tool calls (name, args, output, latency, errors)
- Retrieval context (query, top-k, doc ids/scores, chunk hashes)
- Memory access (reads/writes)
- Safety signals (moderation/guardrail decisions)
- Cost + token usage per step (prompt vs completion)
- Final output + outcome label (success/failure)

## What to monitor (metrics)

| Category | Examples |
| --- | --- |
| Cost | tokens, $/run, $/tool, $/session |
| Latency | LLM latency, tool latency, end-to-end latency |
| Reliability | tool error rate, retry rate, timeout rate |
| Quality | task success rate, eval score, hallucination rate |
| Safety | policy violations, jailbreak attempts, blocked outputs |
| Memory/RAG | retrieval hit-rate, low-score retrievals, stale context |

## Common alerts

- Sudden cost spikes (tokens/run or $/day)
- Tool failures or timeouts above threshold
- Latency regressions (p95/p99)
- Drop in success rate / eval score
- Increased safety/policy violations

## Related

- Full write-up: [Telemetry, Monitoring, and Observability for Agentic AI](README.md)

