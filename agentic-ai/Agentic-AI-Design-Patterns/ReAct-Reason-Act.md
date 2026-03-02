# ReAct (Reason + Act) Agentic Pattern

## Core Idea

ReAct interleaves **reasoning** (thinking about what to do) with **acting** (actually doing it),
then observing the result and reasoning again. It's a tight loop:

```
Thought → Action → Observation → Thought → Action → Observation → ... → Answer
```

Unlike Chain-of-Thought which only reasons, or tool-use which only acts, ReAct does both in alternation. The agent explains its reasoning before each action and updates its reasoning based on what it observes.

**The Loop in Detail**

```
┌─────────────────────────────────────────────────────────┐
│                     ReAct Loop                          │
│                                                         │
│   Question/Goal                                         │
│        │                                                │
│        ▼                                                │
│   ┌─ THOUGHT ──────────────────────────────────────┐   │
│   │  "I need to find X. The best way is to..."     │   │
│   └────────────────────────┬───────────────────────┘   │
│                            ▼                            │
│   ┌─ ACTION ───────────────────────────────────────┐   │
│   │  search("X"), calculate(Y), call_api(Z)...     │   │
│   └────────────────────────┬───────────────────────┘   │
│                            ▼                            │
│   ┌─ OBSERVATION ──────────────────────────────────┐   │
│   │  Raw result returned from the tool             │   │
│   └────────────────────────┬───────────────────────┘   │
│                            │                            │
│              ┌─────────────▼────────────┐              │
│              │  Done?                   │              │
│              │  Yes → Final Answer      │              │
│              │  No  → loop back         │              │
│              └──────────────────────────┘              │
└─────────────────────────────────────────────────────────┘
```

## Real-Time Use Case: AI-Powered Stock Research Assistant

**Scenario:** A user asks — "Should I be concerned about NVIDIA's debt levels given the current interest rate environment?"

This requires: fetching live financial data, fetching current interest rate data, reasoning about the relationship between them, and forming a judgment. A static LLM can't do this — ReAct can.

**Trace of the Agent's Reasoning**

```
User: "Should I be concerned about NVIDIA's debt levels 
       given the current interest rate environment?"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Thought 1:
  I need two pieces of information: NVIDIA's current debt 
  metrics and the current Fed interest rate. Let me get 
  NVIDIA's financials first.

Action 1:  get_financials(ticker="NVDA", metric="debt")
Observation 1:
  {
    "total_debt": "$8.5B",
    "debt_to_equity": 0.41,
    "interest_coverage_ratio": 47.2,
    "free_cash_flow": "$26.9B"
  }

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Thought 2:
  Interest coverage ratio of 47.2x is extremely high — they 
  can cover interest payments 47 times over. FCF of $26.9B 
  dwarfs the $8.5B debt. But I still need the current rate 
  environment to assess refinancing risk.

Action 2:  get_fed_rate()
Observation 2:
  {
    "federal_funds_rate": "4.75%",
    "10yr_treasury": "4.31%",
    "rate_trend": "holding_steady",
    "next_fed_meeting": "2025-03-19"
  }

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Thought 3:
  Rates are elevated but stable. I should check when NVIDIA's 
  debt matures — if it's short-term, refinancing at 4.75% 
  matters more than if it's long-dated.

Action 3:  get_debt_maturity(ticker="NVDA")
Observation 3:
  {
    "debt_schedule": {
      "2025": "$1.25B",
      "2026": "$1.00B",
      "2030+": "$6.25B"
    },
    "avg_coupon_rate": "3.25%",
    "weighted_avg_maturity": "9.2 years"
  }

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Thought 4:
  Only $2.25B matures in the next 2 years, against $26.9B 
  FCF. Even if refinanced at current rates (~4.75% vs their 
  3.25% coupon), the incremental interest cost is trivial.
  Long-dated debt at 9.2yr avg maturity is well-insulated.
  I have enough to answer.

Final Answer:
  NVIDIA's debt levels are NOT a concern in the current 
  rate environment. Here's why:
  - Coverage ratio of 47.2x means earnings cover interest 
    47 times — effectively zero debt stress
  - Only $2.25B of $8.5B matures before 2027, well covered 
    by $26.9B annual free cash flow
  - The bulk of debt (73%) is long-dated (2030+), insulated 
    from current high rates
  - Even worst-case refinancing adds <$35M in annual 
    interest — immaterial at NVIDIA's scale
```

## Why ReAct is Ideal for This Use Case

| Requirement          | How ReAct Handles It                                                       |
| -------------------- | -------------------------------------------------------------------------- |
| Live data needed     | Actions call real APIs on each turn to fetch up-to-date information        |
| Multi-step reasoning | Each **Observation** updates the **Thought**, enabling iterative reasoning |
| Adaptive planning    | Agent decides what to fetch next based on what it just learned             |
| Explainability       | Every **Thought** is logged — you can audit why each action was taken      |
| Early termination    | Agent stops fetching once it has enough information to answer              |


A static prompt can't do this — it doesn't know NVIDIA's current debt maturity schedule at inference time. A pure tool-caller without reasoning would fetch data blindly without knowing which data matters. ReAct bridges both.


## The Pattern's Strength vs. Weakness

**Strengths:**

- Transparent — you can read exactly why the agent did what it did
- Adaptive — each action is informed by prior observations, not pre-planned
- Efficient — agent stops when it has enough, doesn't fetch everything upfront
- Easy to debug — the Thought→Action→Observation log is a full audit trail


**Weaknesses:**

- Sequential — actions happen one at a time (no parallelism, unlike GoT)
- Fragile loops — a bad observation can derail subsequent reasoning
- Latency — each loop iteration is a full LLM call + tool call
- Token cost — long traces eat context window quickly

## When to Use ReAct

| Good fit                                  | Poor fit                                 |
| ----------------------------------------- | ---------------------------------------- |
| Live data lookup tasks                    | Tasks needing parallel tool calls        |
| Research requiring adaptive data fetching | Simple single-step tool use              |
| Customer support with knowledge base      | Creative generation tasks                |
| Financial/medical Q&A with APIs           | High-throughput, low-latency pipelines   |
| Debugging / root cause analysis           | Tasks where reasoning trace isn't needed |


## Use Case — AI Stock Research Analyst

Ask natural-language investment questions and get data-backed answers with full reasoning trace.

```
"Should I be concerned about NVIDIA's debt levels given current interest rates?"
```

## 5 Live Data Tools (CrewAI BaseTool subclasses)

| Tool Source                  | Returns                             |
| ---------------------------- | ----------------------------------- |
| get_financials yfinance      | Debt, FCF, interest coverage, P/E   |
| get_debt_maturity yfinance   | Short-term vs long-term debt split  |
| get_interest_rate FRED API   | Fed funds rate, 10yr Treasury       |
| get_stock_price yfinance     | Price, 52wk range, beta, returns    |
| compare_competitors yfinance | Side-by-side metrics across tickers |


## LangGraph State Machine

```
START → react_loop → check_done ──(done)──→ finalize → END
            ↑             │
            └─(not done)──┘
```

- **react_loop** — runs the CrewAI analyst with a structured ReAct prompt
- **check_done** — safety valve, stops at `MAX_ITERATIONS = 8`
- **finalize** — formats and prints the final answer


## Key Design Points

**Clean separation:** LangGraph owns control flow, CrewAI owns reasoning + tool use. Neither knows about the other's internals.

**ReAct prompt engineering:** The task description explicitly instructs the agent to reason before acting and update its reasoning after each observation — enforcing the Thought→Action→Observation contract.

**Graceful fallback:** If FRED_API_KEY isn't set, interest rate data falls back to static representative values so the agent still works out of the box.

**Any question works** — swap the question in `DEMO_QUESTIONS` or call `ask_stock_analyst("your question")` directly for any ticker or macro topic.


ReAct = **Reason + Act:** the model alternates between **thinking about what to do next** and **taking an action via a tool**, then uses the tool result to decide the next step.


## What ReAct looks like (concept)

| Step | What the agent does                                             | Output                                |
| ---- | --------------------------------------------------------------- | ------------------------------------- |
| 1    | **Reason**: interpret the user goal + decide which tool to call | “I should query metrics first.”       |
| 2    | **Act**: call a tool                                            | `metrics_query(service=checkout)`     |
| 3    | **Observe**: read tool output                                   | latency=1800ms, errors=0.14           |
| 4    | **Reason**: decide next best action                             | “Need logs to confirm DB timeouts.”   |
| 5    | **Act**: call another tool                                      | `logs_query(service=checkout)`        |
| 6    | **Observe**                                                     | “DB timeout / pool exhausted”         |
| 7    | **Reason**: pick remediation plan                               | “Restart pods, then scale if needed.” |
| 8    | **Act**: execute steps                                          | `k8s_restart(...)`                    |
| 9    | **Observe**                                                     | success/failure                       |
| 10   | **Reason**: validate outcome & finish/backtrack                 | “SLO recovered → close incident.”     |


## ReAct vs Chain-of-Thought vs Tree-of-Thoughts

| Dimension              | Chain-of-Thought (CoT)            | Tree-of-Thoughts (ToT)                          | ReAct                                       |
| ---------------------- | --------------------------------- | ----------------------------------------------- | ------------------------------------------- |
| Core idea              | Reason linearly, step by step     | Explore multiple reasoning branches in parallel | Alternate reasoning with real-world actions |
| Structure              | A → B → C → Answer                | Tree with branching + pruning                   | Thought → Action → Observation loop         |
| Uses external tools?   | ❌ No                              | ❌ No                                            | ✅ Yes (APIs, search, DBs)                   |
| Live / real-time data? | ❌ No                              | ❌ No                                            | ✅ Yes                                       |
| Handles uncertainty?   | ❌ One path, no backtracking       | ✅ Explores alternatives                         | ✅ Adapts based on observations              |
| Parallelism            | ❌ Sequential only                 | ✅ Parallel branches                             | ❌ Sequential only                           |
| Self-correction        | ❌ Can't recover from wrong step   | ✅ Prunes bad branches                           | ✅ Updates reasoning after each observation  |
| Explainability         | ✅ Full reasoning trace            | ⚠️ Complex tree is harder to follow             | ✅ Clear T→A→O audit trail                   |
| LLM calls per query    | Low (1–2)                         | High (many branches × scoring)                  | Medium (1 per loop iteration)               |
| Latency                | 🟢 Fast                           | 🔴 Slow                                         | 🟡 Medium                                   |
| Cost                   | 🟢 Cheap                          | 🔴 Expensive                                    | 🟡 Moderate                                 |
| Best for               | Math, logic, summarisation        | Complex planning, open-ended problems           | Research, Q&A needing live data             |
| Fails when             | One wrong step derails everything | Problem doesn't benefit from exploration        | Tool returns bad/incomplete data            |
| Example use case       | "Solve this algebra problem"      | "Design a product launch strategy"              | "What is NVIDIA's debt risk today?"         |


## At a Glance

```
Complexity of reasoning needed
        │
  High  │                          GoT ●
        │               ToT ●
        │                        ReAct ●
   Low  │    CoT ●
        └─────────────────────────────────→
              No tools              Live tools needed
```

## If you need...

| Need                                              | Best method |
| ------------------------------------------------- | ----------- |
| Fast, cheap, explainable reasoning on static data | CoT         |
| Exploring many solutions to find the best one     | ToT         |
| Live data + adaptive multi-step research          | ReAct       |
| Parallel reasoning + synthesis across branches    | GoT         |


## Why ReAct is powerful in incident remediation

Because incidents require interactive evidence gathering:

```
metrics → logs → traces → topology → deploy history → choose action → validate → repeat
```

ReAct naturally fits this pattern.

## A tiny ReAct-style pseudo-flow for your incident use case

```
Reason: latency high → fetch metrics
Act: metrics_query(checkout)
Observe: p95=1800ms, errors=0.14
Reason: need cause → fetch logs
Act: logs_query(checkout)
Observe: "DB timeout", "pool exhausted"
Reason: choose low-risk fix first → restart pods
Act: k8s_restart(checkout)
Observe: restarted ok
Reason: validate SLO
Act: metrics_query(checkout)
Observe: p95 still high
Reason: escalate fix → scale replicas
Act: k8s_scale(checkout, replicas=6)
Observe: scaled ok
Reason: validate again → close ticket
```

