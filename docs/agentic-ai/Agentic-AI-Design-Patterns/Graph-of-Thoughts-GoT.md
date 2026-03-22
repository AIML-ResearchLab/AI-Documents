# Graph-of-Thoughts (GoT) Agentic Pattern

## What It Is?

Graph-of-Thoughts is a reasoning framework where an LLM's thought process is modeled as a **directed graph** rather than a linear chain or tree. Each node represents a "thought" (a partial solution, hypothesis, or intermediate result), and edges represent the transformations or dependencies between them.

```
Chain-of-Thought:  A → B → C → Answer

Tree-of-Thoughts:       A
                       / \
                      B   C
                     /|   |
                    D E   F

Graph-of-Thoughts:  A → B → D
                    ↓   ↑   ↓
                    C ──┘   E → Answer
                    ↑_______|
```

## Core Concepts

| Concept        | Description                                                                  |
| -------------- | ---------------------------------------------------------------------------- |
| Thought Node   | A unit of information — a partial answer, sub-problem, or candidate solution |
| Transformation | An operation that generates, aggregates, refines, or scores nodes            |
| Aggregation    | Merging multiple thoughts into one (impossible in chains/trees)              |
| Backtracking   | Revisiting and improving earlier nodes via cycles or feedback edges          |
| Scoring        | Nodes are evaluated and ranked; low-scoring branches are pruned              |


## Key Operations

| Operation  | Description                                                                 |
| ---------- | --------------------------------------------------------------------------- |
| Generate   | Expand a node into multiple new thought nodes (like ToT branching)          |
| Aggregate  | Merge several nodes into a single, synthesized thought (GoT's unique power) |
| Refine     | Loop a node back through the LLM to improve it                              |
| Score/Rank | Evaluate nodes for quality, relevance, or correctness                       |


## Why GoT > Chain/Tree

**Problem with CoT:** Purely linear — one wrong step poisons everything downstream.

**Problem with ToT:** Tree structure can't merge insights from separate branches. Two branches that each discover something useful can't combine their knowledge.

**GoT solves this** by allowing:

- **Cross-branch synthesis** — combine the best of multiple reasoning paths
- **Iterative refinement loops** — a node can be improved multiple times
- **Non-hierarchical dependencies** — thought B can depend on both A and C, even if C came "later"


## Example: Writing a Complex Report

```
[Gather Facts A] ──┐
                   ├──→ [Synthesize Section 1] ──┐
[Gather Facts B] ──┘                             ├──→ [Final Draft] → [Refine] → Answer
                                                 │
[Gather Facts C] ──→ [Draft Section 2] ──────────┘
        ↑                    |
        └────[Critique]──────┘  ← feedback loop
```

Multiple parallel research threads feed into synthesis nodes, with critique loops refining earlier nodes — impossible in a tree.


## Architecture Overview

```
LangGraph (orchestrator / state machine)
    │
    ├── node_generate  ──→  CrewAI Generator Agent
    ├── node_score     ──→  CrewAI Scorer Agent
    ├── node_prune     ──→  (pure logic, no LLM)
    ├── node_aggregate ──→  CrewAI Aggregator Agent
    ├── node_refine    ──→  CrewAI Refiner Agent
    └── node_finalize  ──→  CrewAI Refiner Agent (concluding mode)
```

- **GoT (Graph of Thoughts) reasoning agent** implemented using **CrewAI Agents/Tasks**
- **LangGraph** acts as the **orchestrator/state-machine**
- GoT core loop: **generate thoughts → build dependency graph → transform (aggregate/refine) → select best**


## How this uses GoT (quick mapping)

| Part          | What it does                                                                                                                    |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `GoTReasoner` | Generates multiple “thoughts” (nodes), adds edges (dependencies), runs transformations (aggregate/refine), then picks best plan |
| CrewAI Agent  | Executes the GoTReasoner as a “brain” agent (structured role + goal)                                                            |
| LangGraph     | Orchestrates end-to-end nodes: `intake → got_plan → validate → execute → end`                                                   |


## Complete Python code (CrewAI + LangGraph + GoT)

```
Install (typical):
pip install crewai langgraph pydantic
(LLM provider packages depend on what you use)
```

```
from __future__ import annotations

import json
import uuid
from dataclasses import dataclass
from typing import Any, Dict, List, Literal, Optional, Tuple

from pydantic import BaseModel, Field

# LangGraph
from langgraph.graph import StateGraph, END

# CrewAI
from crewai import Agent, Task, Crew, Process

# -----------------------------
# 1) State + schemas
# -----------------------------

Severity = Literal["SEV1", "SEV2", "SEV3", "SEV4"]

class Incident(BaseModel):
    incident_id: str
    title: str
    severity: Severity
    service: str
    environment: str = "prod"
    raw_event: Dict[str, Any] = Field(default_factory=dict)

class ActionStep(BaseModel):
    step_id: str
    action: str
    tool: str
    parameters: Dict[str, Any] = Field(default_factory=dict)
    risk: Literal["LOW", "MEDIUM", "HIGH"] = "LOW"

class RemediationPlan(BaseModel):
    plan_id: str
    goal: str
    steps: List[ActionStep]
    got_score: float = 0.0
    rationale: str = ""

class ValidationResult(BaseModel):
    ok: bool
    reason: str
    violations: List[str] = Field(default_factory=list)

class ExecutionResult(BaseModel):
    ok: bool
    executed_steps: List[str] = Field(default_factory=list)
    error: Optional[str] = None

class AgentState(BaseModel):
    incident: Incident
    evidence: Dict[str, Any] = Field(default_factory=dict)

    plan: Optional[RemediationPlan] = None
    validation: Optional[ValidationResult] = None
    execution: Optional[ExecutionResult] = None

    attempts: int = 0
    max_attempts: int = 2
    errors: List[str] = Field(default_factory=list)


# -----------------------------
# 2) Tools (mock; replace later)
# -----------------------------

def tool_metrics_query(service: str) -> Dict[str, Any]:
    # Replace with Prometheus/Datadog/CloudWatch
    return {"p95_latency_ms": 1800, "error_rate": 0.12, "cpu_pct": 90, "service": service}

def tool_logs_query(service: str) -> List[str]:
    # Replace with Loki/Splunk/ELK
    return ["ERROR: DB timeout", "WARN: pool exhausted", "ERROR: retry budget exceeded"]

TOOL_REGISTRY = {
    "metrics_query": tool_metrics_query,
    "logs_query": tool_logs_query,
    # "k8s_restart": ..., "k8s_scale": ..., "itsm_update": ...
}

# -----------------------------
# 3) GoT (Graph of Thoughts) core
#    - thoughts are nodes
#    - edges are dependencies
#    - transformations: aggregate/refine/select
# -----------------------------

@dataclass
class ThoughtNode:
    node_id: str
    kind: Literal["HYPOTHESIS", "PLAN", "EVAL", "AGGREGATE", "REFINE"]
    content: str
    score: float = 0.0
    meta: Dict[str, Any] = None

class ThoughtGraph:
    def __init__(self):
        self.nodes: Dict[str, ThoughtNode] = {}
        self.edges: List[Tuple[str, str, str]] = []  # (src, dst, label)

    def add_node(self, kind: str, content: str, score: float = 0.0, meta: Optional[Dict[str, Any]] = None) -> str:
        nid = str(uuid.uuid4())
        self.nodes[nid] = ThoughtNode(node_id=nid, kind=kind, content=content, score=score, meta=meta or {})
        return nid

    def add_edge(self, src: str, dst: str, label: str) -> None:
        self.edges.append((src, dst, label))

    def top_nodes(self, kind: str, k: int = 3) -> List[ThoughtNode]:
        cand = [n for n in self.nodes.values() if n.kind == kind]
        cand.sort(key=lambda x: x.score, reverse=True)
        return cand[:k]

class GoTReasoner:
    """
    Minimal GoT engine:
      1) Generate candidate plans (PLAN nodes)
      2) Evaluate each (EVAL nodes)
      3) Aggregate best signals (AGGREGATE node)
      4) Refine best plan (REFINE node)
      5) Select final plan
    """
    def __init__(self, beam_width: int = 3):
        self.beam_width = beam_width

    def generate_plan_thoughts(self, g: ThoughtGraph, incident: Incident, evidence: Dict[str, Any]) -> List[str]:
        svc = incident.service
        # Dynamic branching (you can make this LLM-driven later)
        candidates = [
            {
                "plan_id": "restart_deploy",
                "goal": "Fast recovery by restarting workload",
                "steps": [{"action": f"Restart deployment {svc}", "tool": "k8s_restart", "risk": "LOW"}],
                "rationale": "Often clears stuck connections / transient issues",
            },
            {
                "plan_id": "scale_deploy_6",
                "goal": "Reduce load per pod by scaling out",
                "steps": [{"action": f"Scale deployment {svc} to 6", "tool": "k8s_scale", "risk": "MEDIUM", "replicas": 6}],
                "rationale": "Handles traffic spikes; reduces contention",
            },
            {
                "plan_id": "rollback_last_release",
                "goal": "Undo suspected bad deploy",
                "steps": [{"action": f"Rollback {svc} to previous version", "tool": "k8s_rollback", "risk": "MEDIUM"}],
                "rationale": "If errors started after deploy, rollback is effective",
            },
        ]

        plan_node_ids = []
        for c in candidates:
            nid = g.add_node(kind="PLAN", content=json.dumps(c), score=0.0, meta={"plan_id": c["plan_id"]})
            plan_node_ids.append(nid)
        return plan_node_ids

    def score_plan(self, plan_obj: Dict[str, Any], evidence: Dict[str, Any]) -> float:
        """
        Replace with your real scoring:
          - policy compliance
          - risk
          - cost
          - time-to-recover
          - match to evidence
          - historical success (memory)
        """
        p95 = evidence.get("metrics", {}).get("p95_latency_ms", 0)
        err = evidence.get("metrics", {}).get("error_rate", 0.0)
        logs = " ".join(evidence.get("logs", []))

        base = 5.0
        if p95 > 1500: base += 1.5
        if err > 0.1: base += 1.0
        if "DB timeout" in logs and plan_obj["plan_id"] == "restart_deploy": base += 0.8
        if plan_obj["plan_id"] == "rollback_last_release" and "deploy" not in logs.lower(): base -= 0.5

        # risk penalty
        risk = plan_obj["steps"][0].get("risk", "LOW")
        rp = {"LOW": 0.5, "MEDIUM": 1.5, "HIGH": 3.0}[risk]
        return base - rp

    def evaluate_and_prune(self, g: ThoughtGraph, plan_node_ids: List[str], evidence: Dict[str, Any]) -> List[str]:
        """
        Creates EVAL nodes + scores, then prunes to beam_width best PLAN nodes.
        """
        for pid in plan_node_ids:
            plan_obj = json.loads(g.nodes[pid].content)
            score = self.score_plan(plan_obj, evidence)
            g.nodes[pid].score = score

            eid = g.add_node(kind="EVAL", content=f"score={score}", score=score, meta={"plan_id": plan_obj["plan_id"]})
            g.add_edge(pid, eid, "evaluated_by")

        # prune
        survivors = sorted(plan_node_ids, key=lambda nid: g.nodes[nid].score, reverse=True)[: self.beam_width]
        return survivors

    def aggregate(self, g: ThoughtGraph, survivors: List[str]) -> str:
        best = g.nodes[survivors[0]]
        agg_content = f"Top plan candidates: {[g.nodes[s].meta.get('plan_id') for s in survivors]}; best={best.meta.get('plan_id')}"
        aid = g.add_node(kind="AGGREGATE", content=agg_content, score=best.score)
        for s in survivors:
            g.add_edge(s, aid, "contributes_to")
        return aid

    def refine(self, g: ThoughtGraph, best_plan_id: str, aggregate_id: str) -> str:
        """
        Adds a REFINE node to improve the selected plan (e.g., add validation steps, rollback, safety checks).
        """
        plan_obj = json.loads(g.nodes[best_plan_id].content)
        # Example refinement: add a "post-check" note
        plan_obj["rationale"] += " | Refined: add post-validate SLO check + rollback if needed"
        rid = g.add_node(kind="REFINE", content=json.dumps(plan_obj), score=g.nodes[best_plan_id].score + 0.2, meta={"plan_id": plan_obj["plan_id"]})
        g.add_edge(aggregate_id, rid, "refines")
        g.add_edge(best_plan_id, rid, "refines_from")
        return rid

    def run(self, incident: Incident, evidence: Dict[str, Any]) -> RemediationPlan:
        g = ThoughtGraph()

        plan_nodes = self.generate_plan_thoughts(g, incident, evidence)
        survivors = self.evaluate_and_prune(g, plan_nodes, evidence)
        agg = self.aggregate(g, survivors)
        best = survivors[0]
        refined = self.refine(g, best, agg)

        final_obj = json.loads(g.nodes[refined].content)
        steps = []
        for i, s in enumerate(final_obj["steps"], start=1):
            params = {}
            if "replicas" in s:
                params["replicas"] = s["replicas"]
            steps.append(ActionStep(step_id=str(i), action=s["action"], tool=s["tool"], parameters=params, risk=s["risk"]))

        return RemediationPlan(
            plan_id=final_obj["plan_id"],
            goal=final_obj["goal"],
            steps=steps,
            got_score=g.nodes[refined].score,
            rationale=final_obj["rationale"],
        )


# -----------------------------
# 4) CrewAI GoT Agent wrapper
# -----------------------------

def run_crewai_got_planner(incident: Incident, evidence: Dict[str, Any]) -> RemediationPlan:
    """
    We *use CrewAI* to host the GoT reasoning as an "Agent".
    In real usage, you can make the Agent call an LLM to generate candidate branches,
    but here we keep logic deterministic and production-safe.
    """
    got = GoTReasoner(beam_width=3)

    got_agent = Agent(
        role="GoT Planning Agent",
        goal="Generate the best safe remediation plan using Graph-of-Thoughts branching, scoring, pruning, refinement.",
        backstory="You model candidate plans as a graph of dependent thoughts and select the best plan.",
        allow_delegation=False,
        verbose=False,
    )

    task = Task(
        description=(
            "Use GoT to produce a remediation plan. "
            "Inputs are incident and evidence. "
            "Return a JSON plan with plan_id, goal, steps, score, rationale."
        ),
        agent=got_agent,
        expected_output="A JSON object representing the best remediation plan.",
    )

    crew = Crew(
        agents=[got_agent],
        tasks=[task],
        process=Process.sequential,
        verbose=False,
    )

    # We *run* the crew (keeps you aligned with CrewAI framework usage),
    # but the plan itself is produced by GoTReasoner (graph algorithm).
    _ = crew.kickoff(inputs={"incident": incident.model_dump(), "evidence": evidence})

    return got.run(incident, evidence)


# -----------------------------
# 5) LangGraph Orchestrator nodes
# -----------------------------

def intake_node(state: AgentState) -> AgentState:
    # Collect basic telemetry (mock)
    svc = state.incident.service
    metrics = TOOL_REGISTRY["metrics_query"](svc)
    logs = TOOL_REGISTRY["logs_query"](svc)
    state.evidence = {"metrics": metrics, "logs": logs}
    return state

def got_plan_node(state: AgentState) -> AgentState:
    state.plan = run_crewai_got_planner(state.incident, state.evidence)
    return state

def validate_node(state: AgentState) -> AgentState:
    # Minimal validator; replace with your YAML policy engine
    violations = []
    if not state.plan:
        state.validation = ValidationResult(ok=False, reason="No plan", violations=["missing_plan"])
        return state

    # Example guardrail: block HIGH risk in AUTO
    high_risk = any(s.risk == "HIGH" for s in state.plan.steps)
    if high_risk:
        violations.append("AUTO policy denies HIGH risk action")

    state.validation = ValidationResult(ok=(len(violations) == 0), reason=("ok" if not violations else "violations"), violations=violations)
    return state

def execute_node(state: AgentState) -> AgentState:
    if not state.plan or not state.validation or not state.validation.ok:
        state.execution = ExecutionResult(ok=False, error="Cannot execute: plan invalid or missing")
        return state

    executed = []
    try:
        for step in state.plan.steps:
            # Replace with real tool calls (k8s/cloud/itsm)
            # Here we just simulate execution
            executed.append(step.step_id)
        state.execution = ExecutionResult(ok=True, executed_steps=executed)
    except Exception as e:
        state.execution = ExecutionResult(ok=False, executed_steps=executed, error=str(e))
    return state

def router_after_validate(state: AgentState) -> str:
    if state.validation and state.validation.ok:
        return "execute"
    state.attempts += 1
    if state.attempts > state.max_attempts:
        return "end"
    return "got_plan"  # backtrack to GoT to pick next best branch (or re-generate)

def end_node(state: AgentState) -> AgentState:
    return state


def build_orchestrator():
    g = StateGraph(AgentState)

    g.add_node("intake", intake_node)
    g.add_node("got_plan", got_plan_node)
    g.add_node("validate", validate_node)
    g.add_node("execute", execute_node)
    g.add_node("end", end_node)

    g.set_entry_point("intake")
    g.add_edge("intake", "got_plan")
    g.add_edge("got_plan", "validate")
    g.add_conditional_edges("validate", router_after_validate, {"execute": "execute", "got_plan": "got_plan", "end": "end"})
    g.add_edge("execute", "end")
    g.add_edge("end", END)

    return g.compile()


# -----------------------------
# 6) Demo runner
# -----------------------------

if __name__ == "__main__":
    incident = Incident(
        incident_id="INC-2026-0007",
        title="Checkout latency spike",
        severity="SEV1",
        service="checkout",
        environment="prod",
        raw_event={"source": "prometheus", "alert": "HighLatency"},
    )

    state = AgentState(incident=incident, max_attempts=2)
    app = build_orchestrator()
    final = app.invoke(state)

    print("\n=== FINAL ===")
    print("Incident:", final.incident.incident_id)
    print("Evidence:", final.evidence)
    print("Plan:", final.plan.model_dump() if final.plan else None)
    print("Validation:", final.validation)
    print("Execution:", final.execution)
```




# Clauda explanation based on example script

## Overall Architecture — How the Pieces Fit Together

Here's the big picture of what's happening when you call `solve_with_got("your problem")`:

The Three Layers

```
┌─────────────────────────────────────────────────┐
│  Layer 1: YOU                                   │
│  solve_with_got("Reduce SaaS churn by 30%")     │
└───────────────────┬─────────────────────────────┘
                    │
┌───────────────────▼─────────────────────────────┐
│  Layer 2: LANGGRAPH  (the orchestrator)         │
│  Manages WHAT happens and IN WHAT ORDER         │
│  Holds shared state (GoTGraph, problem, etc.)   │
│  Makes routing decisions (loop vs. finalize)    │
└───────────────────┬─────────────────────────────┘
                    │  delegates each operation to ↓
┌───────────────────▼─────────────────────────────┐
│  Layer 3: CREWAI  (the workers)                 │
│  Specialist agents that do the actual LLM work  │
│  Generator / Scorer / Aggregator / Refiner      │
└─────────────────────────────────────────────────┘
```

LangGraph knows nothing about LLMs directly. It only knows about nodes, edges, and state. CrewAI knows nothing about graph structure. It just receives a text prompt and returns a text result. The two are cleanly separated.


**The State Object — The Glue**

Everything flows through a single `GoTState` dict that LangGraph passes from node to node:


```
GoTState = {
    "problem"      : "Reduce SaaS churn by 30%",   # never changes
    "graph"        : GoTGraph(...),                 # grows as thoughts are added
    "current_ids"  : ["a1b2", "c3d4"],              # which thoughts are "in focus" now
    "operation"    : "prune",                       # last operation performed
    "iteration"    : 3,                             # loop counter
    "final_answer" : None,                          # filled at the end
}
```

`current_ids` is particularly important — it acts like a cursor, telling each node *which subset of thoughts* to work on. It narrows and expands as the graph evolves.

---

### The Full Execution Flow
```
solve_with_got("problem")
        │
        │  LangGraph starts with root ThoughtNode seeded in GoTGraph
        │
        ▼
┌─── GENERATE ──────────────────────────────────────────┐
│  For each current_id, call CrewAI Generator Agent     │
│  → produces 3 child ThoughtNodes                      │
│  → adds them to GoTGraph with parent edges            │
│  → current_ids = new child IDs                        │
└───────────────────────┬───────────────────────────────┘
                        ▼
┌─── SCORE ─────────────────────────────────────────────┐
│  For each current_id, call CrewAI Scorer Agent        │
│  → returns {"score": 0.82, "rationale": "..."}        │
│  → sets node.score on each ThoughtNode                │
└───────────────────────┬───────────────────────────────┘
                        ▼
┌─── PRUNE ─────────────────────────────────────────────┐
│  Pure logic — no LLM call                             │
│  → nodes with score < 0.6 → status = PRUNED           │
│  → current_ids = only survivors                       │
└───────────────────────┬───────────────────────────────┘
                        │
              ┌─────────▼──────────┐
              │  Routing decision  │
              │  (conditional edge)│
              └──┬──────────────┬──┘
          survivors?          no survivors
              │                    │
              ▼                    ▼
┌─── AGGREGATE ────────┐      FINALIZE
│  CrewAI Aggregator   │
│  merges survivors    │
│  into 1 new node     │
└──────────┬───────────┘
           ▼
┌─── REFINE ────────────────────────────────────────────┐
│  CrewAI Refiner improves the aggregated thought       │
│  → node.content updated in-place                     │
│  → node.refine_count++                               │
└───────────────────────┬───────────────────────────────┘
                        │
              ┌─────────▼──────────┐
              │  Routing decision  │
              └──┬──────────────┬──┘
          can expand?        at depth limit?
              │                    │
              ▼                    ▼
          GENERATE             FINALIZE ──→ END
          (loop back)
```

## How CrewAI Fits In — The Worker Pattern

Each LangGraph node calls a helper like `crewai_generate()`, `crewai_score()`, etc. These all follow the same pattern:

```
def crewai_generate(parent_content, problem, n=3):
    task = Task(description="...", agent=AGENTS["generator"])
    crew = Crew(agents=[agent], tasks=[task], process=Process.sequential)
    result = crew.kickoff()          # ← this is the actual LLM call
    return parse(result)             # ← extract structured output
```

So CrewAI is being used in **single-agent, single-task mode** — not for multi-agent coordination. Its value here is the agent abstraction: each agent has a distinct `role, goal, and backstory` that shapes how the LLM responds, without you having to manually craft system prompts each time.


## How GoTGraph Fits In — Persistent Memory

Unlike a chain or tree where you just pass text forward, here the entire reasoning history is stored in `GoTGraph`. Every `ThoughtNode` records:

- its content (the actual thought)
- who its parents are (where it came from)
- who its children are (where it led)
- its score, status, depth

## Why This Split Works Well

| Concern                        | Handled by                  |
| ------------------------------ | --------------------------- |
| Control flow & looping         | LangGraph                   |
| State persistence across steps | LangGraph (GoTState)        |
| Routing / branching logic      | LangGraph conditional edges |
| LLM prompt specialization      | CrewAI agent roles          |
| Thought history & lineage      | GoTGraph + ThoughtNode      |
| Structured LLM output parsing  | Helper functions (crewai_*) |
