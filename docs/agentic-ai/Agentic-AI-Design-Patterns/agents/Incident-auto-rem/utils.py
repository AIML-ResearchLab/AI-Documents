"""
Shared utilities: logging, ToT helpers, audit trail.
"""
import json
from datetime import datetime
from langchain_core.messages import HumanMessage


def log(agent: str, msg: str):
    ts = datetime.utcnow().strftime("%H:%M:%S")
    print(f"  [{ts}] [{agent:<14}] {msg}")


def audit(state: dict, stage: str, detail: str):
    entry = {
        "stage"    : stage,
        "detail"   : detail,
        "timestamp": datetime.utcnow().isoformat(),
    }
    state.setdefault("audit_trail", []).append(entry)


def banner():
    print("\n" + "═"*70)
    print("  INCIDENT AUTO-REMEDIATION — AGENTIC AI PIPELINE")
    print("  LangGraph + LangChain + ToT + Multi-Agent")
    print("═"*70 + "\n")


# ── ToT helpers ───────────────────────────────────────────────────────────────

def _strip_json(raw: str) -> str:
    raw = raw.strip()
    if raw.startswith("```"):
        parts = raw.split("```")
        raw = parts[1] if len(parts) > 1 else raw
        if raw.startswith("json"):
            raw = raw[4:]
    return raw.strip()


def tot_generate(llm, prompt: str, n: int = 3) -> list[str]:
    """Generate N thought branches from a prompt."""
    resp = llm.invoke([HumanMessage(content=prompt)])
    raw  = _strip_json(resp.content)
    items = json.loads(raw)
    return items[:n]


def tot_evaluate(llm, prompt: str, items: list[str]) -> list[str]:
    """Score a list of thoughts: sure / maybe / impossible."""
    resp   = llm.invoke([HumanMessage(content=prompt)])
    raw    = _strip_json(resp.content)
    scores = json.loads(raw)
    return scores[:len(items)]


def tot_select(items: list[str], scores: list[str]) -> str:
    """Select the best item by score priority."""
    priority = {"sure": 0, "maybe": 1, "impossible": 2}
    ranked   = sorted(zip(items, scores), key=lambda x: priority.get(x[1], 3))
    # Return best non-impossible
    for item, score in ranked:
        if score != "impossible":
            return item
    return items[0]  # fallback
