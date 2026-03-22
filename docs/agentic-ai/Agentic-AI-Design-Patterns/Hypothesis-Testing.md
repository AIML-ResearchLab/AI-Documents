# Hypothesis Testing Agentic Pattern

## Core Idea

Hypothesis Testing is a pattern where an agent **forms explicit hypotheses about a problem, designs experiments to test them, observes results, and updates its beliefs** — mimicking the scientific method. Unlike Reflexion (which learns from failure) or ReAct (which acts on observations), Hypothesis Testing is fundamentally about **structured belief updating under uncertainty**.

```
┌─────────────────────────────────────────────────────────────┐
│              Hypothesis Testing Loop                        │
│                                                             │
│   Problem                                                   │
│      │                                                      │
│      ▼                                                      │
│   HYPOTHESIZE ── form ranked hypotheses H1, H2, H3...      │
│      │                                                      │
│      ▼                                                      │
│   DESIGN ──── design experiment to falsify top hypothesis   │
│      │                                                      │
│      ▼                                                      │
│   EXPERIMENT ── run the experiment, collect evidence        │
│      │                                                      │
│      ▼                                                      │
│   UPDATE ───── confirm / reject / refine hypotheses         │
│      │                                                      │
│      ├── Hypothesis confirmed + sufficient evidence → CONCLUDE
│      │                                                      │
│      └── Still uncertain → loop back to DESIGN             │
└─────────────────────────────────────────────────────────────┘
```

The key principle: **hypotheses are falsifiable, ranked by confidence, and updated with evidence** — not just guesses.


## What Makes Hypothesis Testing Unique

| Concept               | Description                                                                       |
| --------------------- | --------------------------------------------------------------------------------- |
| Ranked Hypothesis Set | Multiple competing explanations maintained simultaneously with confidence scores  |
| Falsifiability        | Each experiment is designed to disprove the leading hypothesis, not confirm it    |
| Belief Updating       | Confidence scores shift based on evidence — Bayesian-style reasoning              |
| Experiment Design     | The agent decides what test would best discriminate between hypotheses            |
| Termination Criteria  | Stops when one hypothesis reaches sufficient confidence OR evidence is exhaustive |


## How It Differs From Other Patterns

| Capability                                | ReAct         | Reflexion      | PAR                  | Hypothesis Testing              |
| ----------------------------------------- | ------------- | -------------- | -------------------- | ------------------------------- |
| Maintains multiple competing explanations | ❌             | ❌              | ❌                    | ✅                               |
| Designs experiments to falsify            | ❌             | ❌              | ❌                    | ✅                               |
| Updates confidence scores                 | ❌             | ❌              | ❌                    | ✅                               |
| Learns from failure                       | ❌             | ✅              | ✅                    | ✅                               |
| Scientific method structure               | ❌             | ❌              | ❌                    | ✅                               |
| Best for                                  | Live research | Code debugging | Structured workflows | Diagnosis & root cause analysis |


## Real-Time Use Case: Automated Production Incident Diagnosis

**Scenario:** A site reliability engineer gets paged at 2am — "API error rate spiked from 0.1% to 34% at 02:14 UTC. P1 incident. Find root cause."

This is a perfect fit for Hypothesis Testing because:

- **Multiple competi  ng causes** exist (database, network, deployment, traffic spike, etc.)
- **Each check is costly** — you want to test the most likely cause first
- **Evidence accumulates** — each check either rules out or narrows candidates
- **Confidence matters** — you need to be sure before rolling back a deployment


## Trace of the Agent's Execution

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

HYPOTHESIZE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Forming hypotheses for: API error rate 0.1% → 34% at 02:14 UTC

H1: Bad deployment at 02:12 UTC caused regression     [confidence: 0.40]
H2: Database connection pool exhausted                [confidence: 0.30]
H3: Upstream dependency (payment API) is down         [confidence: 0.15]
H4: Traffic spike overwhelming application servers    [confidence: 0.10]
H5: Network partition in us-east-1b                   [confidence: 0.05]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EXPERIMENT 1 — Testing H1 (deployment regression)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Experiment Design:
  "If H1 is true, there should be a deployment at ~02:12.
   Check deployment logs. If no deployment → H1 falsified.
   If deployment found → check which services were affected."

Action: query_deployment_logs(start="02:00", end="02:20")

Result:
  {
    "deployments": [],
    "last_deployment": "2024-03-01 18:45 UTC",
    "status": "No deployments in window"
  }

Update:
  H1: Bad deployment          [0.40 → 0.05]  ← FALSIFIED (no deployment)
  H2: DB connection pool      [0.30 → 0.45]  ← promoted to top
  H3: Upstream dependency     [0.15 → 0.22]  ← slightly promoted
  H4: Traffic spike           [0.10 → 0.18]  ← slightly promoted
  H5: Network partition       [0.05 → 0.10]  ← slightly promoted

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EXPERIMENT 2 — Testing H2 (DB connection pool)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Experiment Design:
  "If H2 is true, DB connection metrics should show pool
   exhaustion near 02:14. Check DB connection count vs limit.
   Also check query latency — pool exhaustion causes queuing."

Action: query_db_metrics(metric="connections", window="02:00-02:30")
Action: query_db_metrics(metric="query_latency_p99", window="02:00-02:30")

Result:
  {
    "max_connections": 100,
    "connections_at_02:14": 98,
    "connections_at_02:20": 100,
    "wait_queue_at_02:14": 47,
    "p99_latency_ms": {"02:10": 45, "02:14": 4200, "02:20": 8900}
  }

Update:
  H2: DB connection pool      [0.45 → 0.78]  ← STRONG EVIDENCE
  H3: Upstream dependency     [0.22 → 0.10]  ← demoted (DB issue more likely)
  H4: Traffic spike           [0.18 → 0.09]  ← demoted
  H5: Network partition       [0.10 → 0.03]  ← demoted

Confidence threshold (0.75) reached for H2!
But — what caused the connection pool to exhaust?
Expanding H2 into sub-hypotheses:

  H2a: Slow queries holding connections (query leak)  [0.50]
  H2b: Connection leak in application code            [0.35]
  H2c: Sudden traffic surge to DB-heavy endpoints     [0.15]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

EXPERIMENT 3 — Testing H2a (slow query leak)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Action: query_slow_query_log(threshold_ms=1000, window="02:10-02:20")

Result:
  {
    "slow_queries": [
      {
        "query": "SELECT * FROM orders JOIN users ON ... WHERE created_at > ?",
        "count": 8420,
        "avg_duration_ms": 4100,
        "started_at": "02:13:47"
      }
    ],
    "missing_index": "orders.created_at"
  }

Update:
  H2a: Slow query leak         [0.50 → 0.92]  ← ROOT CAUSE CONFIRMED

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

CONCLUDE
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Root Cause (confidence: 0.92):
  A missing index on orders.created_at caused full table scans
  on a high-frequency query starting at 02:13:47. Each query
  held a DB connection for ~4.1 seconds, exhausting the 100-connection
  pool and causing cascading API timeouts.

Evidence Chain:
  ✅ No deployment found → ruled out H1
  ✅ DB connections at 98/100 with 47-request queue → confirmed H2
  ✅ 8,420 slow queries averaging 4.1s on missing-index table scan → confirmed H2a

Immediate Action:
  1. Add index: CREATE INDEX CONCURRENTLY ON orders(created_at)
  2. Kill long-running queries to drain connection queue
  3. Scale connection pool temporarily while index builds

Time to diagnosis: 3 experiments, ~4 minutes
```


## The Hypothesis Ranking System

The agent maintains a live scoreboard updated after each experiment:

```
Initial State:          After Exp 1:            After Exp 2:
H1: deploy  [0.40]      H1: deploy  [0.05] ✗    H2: db pool [0.78] ★
H2: db pool [0.30]  →   H2: db pool [0.45] ★ →  H2a: slow q [0.50]
H3: upstream[0.15]      H3: upstream[0.22]       H2b: conn lk[0.35]
H4: traffic [0.10]      H4: traffic [0.18]       H3: upstream[0.10]
H5: network [0.05]      H5: network [0.10]       H4: traffic [0.09]
```

## Termination Conditions

The loop stops when any of these are met:

```
1. CONFIDENCE THRESHOLD  — any hypothesis reaches ≥ 0.85 confidence
2. FALSIFICATION COMPLETE— all but one hypothesis falsified
3. EVIDENCE EXHAUSTION   — no more useful experiments can be designed
4. MAX EXPERIMENTS       — hard cap on experiment count (cost control)
```

## When to Use Hypothesis Testing

| Good fit                       | Poor fit                            |
| ------------------------------ | ----------------------------------- |
| Production incident diagnosis  | Tasks with a single obvious cause   |
| Medical / clinical reasoning   | Creative generation                 |
| Security threat investigation  | Simple data lookup                  |
| A/B test result interpretation | Tasks needing real-time speed       |
| Scientific data analysis       | Well-defined procedural tasks       |
| Customer churn root cause      | Tasks where all paths cost the same |


## Pattern Comparison — Full Updated Table

| Capability                      | CoT   | ToT         | ReAct         | PAR       | Reflexion | Hyp. Testing |
| ------------------------------- | ----- | ----------- | ------------- | --------- | --------- | ------------ |
| Multiple competing explanations | ❌     | ✅           | ❌             | ❌         | ❌         | ✅            |
| Confidence scoring              | ❌     | ✅           | ❌             | ❌         | ❌         | ✅            |
| Experiment design               | ❌     | ❌           | ❌             | ❌         | ❌         | ✅            |
| Falsification logic             | ❌     | ❌           | ❌             | ❌         | ❌         | ✅            |
| Learns from failure             | ❌     | ❌           | ❌             | ✅         | ✅         | ✅            |
| External tools                  | ❌     | ❌           | ✅             | ✅         | ✅         | ✅            |
| Best for                        | Logic | Exploration | Live research | Workflows | Debugging | Diagnosis    |


## Architecture

```
START → hypothesize → design_experiment → update_beliefs
                              ↑                  │
                              └────(loop)─────────┤
                                                  │
                                        confidence ≥ 0.85?
                                                  │
                                              conclude → END
```

## How Google ADK Is Integrated

Unlike CrewAI, Google ADK uses Gemini's native function calling — the agent model itself decides which tools to call and in what order:

```
class ADKAgent:
    def __init__(self, name, system_instruction, use_tools=False):
        self.model = GenerativeModel(
            model_name="gemini-1.5-pro",
            system_instruction=system_instruction,
            tools=[ADK_TOOLS] if use_tools else None,
        )

    def run(self, prompt, execute_tools=False):
        # Gemini autonomously calls tools via function_call parts
        # Agent handles the tool→result→continuation loop internally
```


The `ExperimentDesignerAgent` has `use_tools=True` — it autonomously decides which of the 9 observability tools to call, executes them, reads results, and continues reasoning.


## Four ADK Agents — One Per Phase

| Agent                   | Phase       | ADK Feature Used               |
| ----------------------- | ----------- | ------------------------------ |
| HypothesizerAgent       | HYPOTHESIZE | Structured JSON output         |
| ExperimentDesignerAgent | DESIGN+RUN  | Gemini native function calling |
| BeliefUpdaterAgent      | UPDATE      | Bayesian JSON reasoning        |
| ConcluderAgent          | CONCLUDE    | Long-form structured report    |


## 9 Real Observability Tools

All declared as `FunctionDeclaration` schemas (Gemini's native tool format), mapped to Python callables via `TOOL_REGISTRY`. In production, replace the simulated return values with real Datadog / CloudWatch / Prometheus calls.

## Three Output Files

`incident_report.md` — full post-mortem with remediation steps, `experiment_log.json` — every experiment with tools called, `hypothesis_scores.json` — final confidence scores for all hypotheses.
