# Hierarchical Agents Pattern

**Core Idea**

Hierarchical Agents is a pattern where agents are organized into **layers of authority** — an Orchestrator at the top breaks down complex goals, delegates sub-tasks to Mid-level Manager agents, who further delegate atomic tasks to Specialist Worker agents at the bottom. No agent tries to do everything — each operates strictly within its domain.

```
┌─────────────────────────────────────────────────────────────┐
│                    ORCHESTRATOR AGENT                       │
│         "CEO — sets strategy, owns the final goal"         │
│   Decomposes goal → delegates to manager agents             │
└──────────┬──────────────┬──────────────┬────────────────────┘
           │              │              │
           ▼              ▼              ▼
    ┌──────────┐   ┌──────────┐   ┌──────────┐
    │ MANAGER  │   │ MANAGER  │   │ MANAGER  │
    │ Research │   │ Analysis │   │  Report  │
    │  Agent   │   │  Agent   │   │  Agent   │
    └────┬─────┘   └────┬─────┘   └────┬─────┘
         │              │              │
    ┌────┴────┐    ┌────┴────┐    ┌────┴────┐
    │WORKER   │    │WORKER   │    │WORKER   │
    │WORKER   │    │WORKER   │    │WORKER   │
    │WORKER   │    │WORKER   │    │WORKER   │
    └─────────┘    └─────────┘    └─────────┘
```


Each layer has a **different cognitive role:** strategy → coordination → execution.

## The Three Layers Explained

**Layer 1 — Orchestrator (CEO)** Receives the original goal. Decides what needs to happen at the highest level. Breaks it into major workstreams. Assigns each workstream to a Manager. Collects and synthesises all manager outputs into the final deliverable. Never touches tools directly.

**Layer 2 — Manager Agents (Department Heads)** Each Manager owns one workstream. Breaks its workstream into atomic tasks. Assigns tasks to specialist Workers. Collects worker outputs and synthesises them into a coherent workstream result. Reports only to the Orchestrator.

**Layer 3 — Worker Agents (Specialists)** Each Worker is a narrow expert with access to specific tools. Executes one atomic task. Returns a structured result to its Manager. Has no awareness of other workstreams or the broader goal.


## What Makes Hierarchical Agents Unique

| Concept                 | Description                                                                     |
| ----------------------- | ------------------------------------------------------------------------------- |
| Strict chain of command | Each agent only communicates with its direct superior and direct reports        |
| Separation of concerns  | Strategy, coordination, and execution are fully decoupled                       |
| Parallel execution      | Multiple managers and their workers run concurrently                            |
| Scope isolation         | A worker failure doesn't cascade — the manager handles it                       |
| Composable expertise    | New capabilities added by adding worker specialists, not modifying upper layers |



## How It Differs From Other Patterns

| Capability             | ReAct         | PAR       | GoT                  | Hierarchical Multi-agent |
| ---------------------- | ------------- | --------- | -------------------- | ------------------------ |
| Multi-agent            | ❌             | ✅ (flat)  | ❌                    | ✅ (layered)              |
| Parallel execution     | ❌             | ✅         | ✅                    | ✅                        |
| Chain of command       | ❌             | ❌         | ❌                    | ✅                        |
| Scope isolation        | ❌             | ❌         | ❌                    | ✅                        |
| Scales with complexity | ❌             | ❌         | ❌                    | ✅                        |
| Best for               | Live research | Workflows | Open-ended synthesis | Large complex tasks      |


## Real-Time Use Case: Automated M&A Due Diligence Platform

**Scenario:** A private equity firm asks — "Conduct full due diligence on TechCorp Inc. for a potential $200M acquisition — covering financials, technology, market position, legal risks, and team quality."

This is a perfect fit for Hierarchical Agents because:

- The task is **too large for one agent** — 5 distinct expert domains
- Each domain is **genuinely independent** — legal team doesn't need to wait for tech team
- **Parallel execution** slashes wall-clock time dramatically
- Different domains require **completely different tools and expertise**
- The final output requires **cross-domain synthesis** — only an Orchestrator can do this



## The Hierarchy for M&A Due Diligence

```
┌──────────────────────────────────────────────────────────────┐
│           ORCHESTRATOR: M&A Strategy Director                │
│   "Coordinate full due diligence on TechCorp Inc. $200M"    │
└──────┬───────────┬───────────┬───────────┬──────────────────┘
       │           │           │           │           │
       ▼           ▼           ▼           ▼           ▼
  ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐ ┌─────────┐
  │Financial│ │  Tech   │ │ Market  │ │  Legal  │ │  Team   │
  │ Manager │ │ Manager │ │ Manager │ │ Manager │ │ Manager │
  └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘ └────┬────┘
       │           │           │           │           │
  ┌────┴──┐   ┌────┴──┐   ┌────┴──┐   ┌────┴──┐   ┌────┴──┐
  │Revenue│   │ Tech  │   │Market │   │Patent │   │Founder│
  │Worker │   │ Debt  │   │ Size  │   │Worker │   │Worker │
  │ Cash  │   │Worker │   │Worker │   │Contract│  │Team   │
  │ Flow  │   │ Arch  │   │Compet │   │Worker │   │Worker │
  │Worker │   │Worker │   │Worker │   │Litigation│ │Culture│
  │ Debt  │   │ Sec   │   │Growth │   │Worker │   │Worker │
  │Worker │   │Worker │   │Worker │   │       │   │       │
  └───────┘   └───────┘   └───────┘   └───────┘   └───────┘
  ```


  ## Execution Trace

  ```
  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
ORCHESTRATOR receives goal
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Goal: "Full due diligence on TechCorp Inc. for $200M acquisition"

Orchestrator decomposes into 5 workstreams:
  → Financial DD   (Manager 1)
  → Technology DD  (Manager 2)
  → Market DD      (Manager 3)
  → Legal DD       (Manager 4)
  → Team DD        (Manager 5)

[All 5 Managers launch in parallel]

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MANAGER 1: Financial DD  [running in parallel]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Manager decomposes into worker tasks:
  → Revenue Worker: fetch_revenue_data() → $18.4M ARR, 94% YoY
  → Cash Flow Worker: analyze_cash_flow() → FCF positive $2.1M
  → Debt Worker: check_debt_obligations() → $4.2M debt, manageable

Manager synthesises: "Strong financials. ARR growth exceptional.
  Debt/revenue ratio healthy at 0.23. FCF positive 3 quarters.
  ⚠️ Customer concentration risk: top 3 clients = 61% of revenue"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
MANAGER 2: Technology DD  [running in parallel]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  → Tech Debt Worker: scan_codebase()  → Tech debt score 6.2/10
  → Architecture Worker: review_arch() → Microservices, cloud-native ✓
  → Security Worker: run_sec_scan()    → 2 critical CVEs unpatched ⚠️

Manager synthesises: "Modern architecture, good scalability.
  Tech debt manageable. ⚠️ 2 critical unpatched CVEs in auth service
  require immediate attention post-acquisition."

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
[Managers 3, 4, 5 complete in parallel...]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

ORCHESTRATOR receives all 5 manager reports
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Synthesises cross-domain findings:

  ✅ STRENGTHS: 94% ARR growth, cloud-native tech, TAM $4.2B
  ⚠️ RISKS: Customer concentration, 2 CVEs, 1 key-man dependency
  💰 VALUATION: $200M is 10.9x ARR — justified given growth rate
  📋 CONDITIONS: Security remediation clause, retention packages

FINAL RECOMMENDATION: PROCEED WITH CONDITIONS
```

## Communication Protocol — The Chain of Command

```
ALLOWED:                           FORBIDDEN:
Orchestrator ↔ Manager ✅          Worker → Orchestrator ❌
Manager ↔ Worker        ✅          Worker → Worker (diff team) ❌
                                   Orchestrator → Worker ❌
```


This strict protocol is what makes the system **scalable and debuggable** — failures are always contained within one manager's domain.

**Why Parallelism Matters**

Without hierarchical agents (sequential):

```
Financial (15min) → Tech (12min) → Market (10min) → Legal (18min) → Team (8min)
Total: 63 minutes
```

With hierarchical agents (parallel):

```
Financial │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│ 15min
Tech      │▓▓▓▓▓▓▓▓▓▓▓▓│    12min   → All run simultaneously
Market    │▓▓▓▓▓▓▓▓▓▓│      10min
Legal     │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│ 18min
Team      │▓▓▓▓▓▓▓▓│          8min
          └──────────────────────→ 18min + synthesis
```

## Termination and Failure Handling

```
Worker fails
    │
    ▼
Manager catches failure
    ├── Retry worker? → yes if transient
    ├── Use partial result? → yes if non-critical
    └── Report gap to Orchestrator → "Legal section incomplete: patent data unavailable"

Orchestrator receives partial results
    ├── Still synthesise available sections
    └── Flag missing sections in final report
```

## When to Use Hierarchical Agents

| Good fit                                 | Poor fit                                    |
| ---------------------------------------- | ------------------------------------------- |
| Multi-domain research tasks              | Simple single-tool lookups                  |
| Large document processing                | Tasks requiring shared state across domains |
| Enterprise workflow automation           | Low-latency requirements                    |
| Tasks with truly independent workstreams | Creative tasks (holistic, not decomposable) |
| When domain expertise isolation matters  | Small tasks where overhead isn't worth it   |


## Termination and Failure Handling

```
Worker fails
    │
    ▼
Manager catches failure
    ├── Retry worker? → yes if transient
    ├── Use partial result? → yes if non-critical
    └── Report gap to Orchestrator → "Legal section incomplete: patent data unavailable"

Orchestrator receives partial results
    ├── Still synthesise available sections
    └── Flag missing sections in final report
```


## When to Use Hierarchical Agents

| Good fit                                 | Poor fit                                    |
| ---------------------------------------- | ------------------------------------------- |
| Multi-domain research tasks              | Simple single-tool lookups                  |
| Large document processing                | Tasks requiring shared state across domains |
| Enterprise workflow automation           | Low-latency requirements                    |
| Tasks with truly independent workstreams | Creative tasks (holistic, not decomposable) |
| When domain expertise isolation matters  | Small tasks where overhead isn't worth it   |


## Full Pattern Comparison

| Capability            | CoT   | ReAct    | PAR       | Reflexion | Hyp. Test | Hierarchical Multi-agent |
| --------------------- | ----- | -------- | --------- | --------- | --------- | ------------------------ |
| Multi-agent           | ❌     | ❌        | ❌         | ❌         | ❌         | ✅                        |
| Parallel execution    | ❌     | ❌        | ✅         | ❌         | ❌         | ✅                        |
| Chain of command      | ❌     | ❌        | ❌         | ❌         | ❌         | ✅                        |
| Domain isolation      | ❌     | ❌        | ❌         | ❌         | ❌         | ✅                        |
| Scales with task size | ❌     | ❌        | ❌         | ❌         | ❌         | ✅                        |
| Best for              | Logic | Research | Workflows | Debugging | Diagnosis | Complex multi-domain     |


# Full Hierarchy — 21 Agents Total

```
Orchestrator (1)
├── FinancialManager  → RevenueAnalyst, CashFlowAnalyst, DebtAnalyst
├── TechnologyManager → TechDebtAnalyst, ArchAnalyst, SecurityAnalyst
├── MarketManager     → MarketAnalyst, CompAnalyst, GrowthAnalyst
├── LegalManager      → PatentAnalyst, ContractAnalyst, LitigationAnalyst
└── TeamManager       → FounderAnalyst, TeamAnalyst, CultureAnalyst
```

## LangGraph State Machine — 3 Nodes Only

```
START → parallel_workstreams → orchestrate → deliver → END
```

The magic is inside `parallel_workstreams —` a single LangGraph node that uses `ThreadPoolExecutor(max_workers=5)` to run all 5 manager workstreams simultaneously, then waits for all to complete before passing results to orchestrate.


## Key Design Decisions

**Strict chain of command —** Workers only know their domain tool. Managers only know their 3 workers. Orchestrator only sees manager reports. Zero cross-talk between workstreams — this is what makes it debuggable and extensible.

**GeminiAgent base class —** `All 21 agents` inherit from one base class with run() and run_json(). Google ADK's GenerativeModel is instantiated per agent with unique system_instruction that defines its role, authority, and reporting line.

**WorkerResult and ManagerReport dataclasses —** Structured typed contracts between layers. A worker never returns raw text — always a WorkerResult. A manager never returns raw text — always a ManagerReport. This is what makes the Orchestrator synthesis reliable.


**Temperature tuning by layer —** Workers use 0.2 (precise, analytical), Orchestrator uses 0.1 (ultra-precise for $200M recommendation).

**Three Output Files**


ma_dd_report.md — board-level DD report, domain_scorecards.json — score + recommendation + risks per domain, worker_findings.json — all 15 worker-level findings for full audit trail.


## Extending in 3 Lines

Adding a new domain (e.g. ESG) requires only: new worker tools + `WorkerAgent instances + one ManagerAgent — LangGraph picks it up automatically in the parallel executor.

