# Plan–Act–Reflect Agentic Pattern

## Core Idea

Unlike ReAct which reasons just-in-time before each action, Plan–Act–Reflect separates the agent's cognition into three distinct, explicit phases:

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│    PLAN     │───▶│     ACT     │───▶│   REFLECT   │
│             │    │             │    │             │
│ Decompose   │    │ Execute all │    │ Evaluate    │
│ the goal    │    │ planned     │    │ results,    │
│ into steps  │    │ steps       │    │ revise plan │
│ upfront     │    │             │    │ if needed   │
└─────────────┘    └─────────────┘    └──────┬──────┘
       ▲                                      │
       └──────────────────────────────────────┘
                    (loop if needed)
```

The key insight: **planning is separated from execution**. The agent thinks holistically about the whole task before touching any tools, then reflects on whether the outcome matched the intent.

## The Three Phases in Detail

**PLAN** — The agent receives a goal and produces a structured execution plan: ordered steps, which tools to use, what success looks like, and what could go wrong. This happens once (or is revised after reflection).

**ACT** — The agent executes each planned step sequentially (or in parallel where possible), collecting results. Unlike ReAct, there's no mid-execution replanning — the agent commits to the plan.

**REFLECT** — After all steps are done, the agent evaluates: Did the results answer the goal? Were any steps wrong or incomplete? Should the plan be revised and re-run?

## How It Differs from ReAct

| Dimension                  | ReAct                           | Plan–Act–Reflect              |
| -------------------------- | ------------------------------- | ----------------------------- |
| When does planning happen? | Just-in-time before each action | Upfront, all at once          |
| Mid-execution replanning?  | ✅ Continuous                    | ❌ Commits to plan             |
| Reflection?                | ❌ No explicit reflection        | ✅ Dedicated phase             |
| Good for                   | Exploratory, uncertain tasks    | Well-scoped, multi-step tasks |
| Plan quality               | Reactive, local                 | Global, structured            |


## Real-Time Use Case: Automated Competitive Intelligence Report

**Scenario:** A product manager asks — "Generate a competitive intelligence report comparing our SaaS product against HubSpot, Salesforce, and Zoho — covering pricing, features, customer sentiment, and market positioning."

This is a perfect fit for Plan–Act–Reflect because:

- The goal is **well-scoped** (known competitors, known dimensions)
- It requires **many parallel actions** (scraping, API calls, sentiment analysis)
- The output must be **coherent and complete** — partial answers aren't useful
- **Quality reflection** matters — a bad section should trigger a re-run


## Trace of the Agent's Execution

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 1: PLAN
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Goal: Competitive intelligence report on HubSpot, Salesforce, Zoho

Execution Plan:
  Step 1 → scrape_pricing(HubSpot, Salesforce, Zoho)
  Step 2 → fetch_feature_matrix(HubSpot, Salesforce, Zoho)
  Step 3 → scrape_reviews(G2, Capterra) for each competitor
  Step 4 → run_sentiment_analysis(reviews)
  Step 5 → fetch_market_share_data()
  Step 6 → synthesise_report(all results)

Success criteria:
  - All 3 competitors covered on all 4 dimensions
  - Sentiment score has ≥ 50 reviews per competitor
  - Report has actionable positioning recommendations

Risk flags:
  - Salesforce pricing page may be gated
  - G2 may rate-limit scraping

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 2: ACT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Step 1 → scrape_pricing()
  HubSpot:    Starter $20/mo, Pro $890/mo, Enterprise $3,600/mo
  Salesforce: Essentials $25/mo, Pro $75/mo, Enterprise $150/mo
  Zoho:       Standard $14/mo, Pro $23/mo, Enterprise $40/mo

Step 2 → fetch_feature_matrix()
  [matrix of 24 features × 3 competitors returned]

Step 3 → scrape_reviews()
  HubSpot:    312 reviews fetched  ✓
  Salesforce: 428 reviews fetched  ✓
  Zoho:       89 reviews fetched   ✓

Step 4 → run_sentiment_analysis()
  HubSpot:    +0.72 (strong positive, ease-of-use praised)
  Salesforce: +0.48 (moderate, complexity complaints)
  Zoho:       +0.61 (positive, value-for-money highlighted)

Step 5 → fetch_market_share_data()
  Salesforce: 23.8% CRM market share
  HubSpot:    6.1%
  Zoho:       3.2%

Step 6 → synthesise_report()
  [Full markdown report generated]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
PHASE 3: REFLECT
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Evaluating against success criteria:

  ✅ All 3 competitors covered on all 4 dimensions
  ✅ Sentiment has ≥ 50 reviews per competitor (89, 312, 428)
  ⚠️  Salesforce Enterprise pricing was estimated — page was gated
  ❌  Report lacks positioning recommendations (Step 6 too generic)

Reflection decision: PARTIAL REPLAN
  → Re-run Step 6 with explicit instruction to add
    3 actionable positioning recommendations
  → Flag Salesforce pricing as estimated in report

[Step 6 re-executed with corrected prompt]

✅ All criteria now met → FINAL REPORT DELIVERED
```

## Why Plan–Act–Reflect is Ideal Here

| Requirement               | How P–A–R handles it                                        |
| ------------------------- | ----------------------------------------------------------- |
| Many steps needed upfront | PLAN phase lays out all 6 steps before touching any tool    |
| Coherent final output     | ACT phase collects everything before synthesis              |
| Quality gate              | REFLECT catches the missing recommendations before delivery |
| Partial failure recovery  | REFLECT triggers targeted re-runs, not full restart         |
| Auditability              | Plan is a first-class artifact — stakeholders can review it |


## The Reflection Decision Tree

After the ACT phase, the REFLECT phase makes one of four decisions:

```
REFLECT evaluates results
        │
        ├── ✅ All criteria met         → DELIVER final output
        │
        ├── ⚠️  Minor gaps              → PATCH (re-run specific steps only)
        │
        ├── ❌  Major failure           → REPLAN (generate new plan, re-ACT)
        │
        └── 🔁  New information found   → EXPAND (add new steps to plan)
```

## When to Use Plan–Act–Reflect

| Good fit                              | Poor fit                                             |
| ------------------------------------- | ---------------------------------------------------- |
| Multi-step tasks with known structure | Highly exploratory, open-ended tasks                 |
| Report generation & synthesis         | Tasks where the next step depends on the last result |
| Workflows with quality gates          | Simple single-tool lookups                           |
| Long-horizon tasks (research, audits) | Real-time streaming responses                        |
| When the plan itself is a deliverable | Tasks needing sub-second latency                     |


## Pattern Comparison Update

| Capability          | CoT   | ToT         | ReAct         | Plan–Act–Reflect     |
| ------------------- | ----- | ----------- | ------------- | -------------------- |
| Upfront planning    | ❌     | ❌           | ❌             | ✅                    |
| External tools      | ❌     | ❌           | ✅             | ✅                    |
| Explicit reflection | ❌     | ❌           | ❌             | ✅                    |
| Parallel execution  | ❌     | ✅           | ❌             | ✅                    |
| Self-correction     | ❌     | ✅           | ✅             | ✅ (post-hoc)         |
| Best for            | Logic | Exploration | Live research | Structured workflows |


## 3 CrewAI Specialist Agents

| Agent     | Role                                | Responsibility                                                          |
| --------- | ----------------------------------- | ----------------------------------------------------------------------- |
| Planner   | Strategic Research Planner          | Decomposes goal → structured JSON plan with steps, criteria, risk flags |
| Executor  | Competitive Intelligence Researcher | Runs all 6 tools step-by-step, resolves data dependencies               |
| Reflector | QA & Research Director              | Evaluates results, returns DELIVER / PATCH / REPLAN / EXPAND            |


## 6 Research Tools (CrewAI BaseTool)

All use realistic simulated data out of the box — swap `_run()` bodies with real scrapers for production:

```
scrape_pricing → fetch_feature_matrix → scrape_reviews
    → run_sentiment_analysis → fetch_market_share → synthesise_report
```

## LangGraph State Machine — 7 Nodes

```
START → plan → act → reflect ──DELIVER──→ deliver → END
                        │
                     PATCH → patch → reflect
                     REPLAN → replan → act → reflect  
                     EXPAND → expand → act → reflect
```

## Key Design Patterns

**Step dependency resolution** — Args like `__FROM_STEP_3__` are automatically resolved at execution time, so `run_sentiment_analysis` always receives the live output of `scrape_reviews`, not a hardcoded value.

**Safety valves** — `MAX_REPLAN_LOOPS = 2` and `MAX_PATCH_LOOPS = 3` prevent infinite loops, forcing delivery after N attempts.

**Reflection decision tree** — The Reflector agent scores each success criterion independently and returns a structured JSON decision, not free-form text, making routing deterministic.