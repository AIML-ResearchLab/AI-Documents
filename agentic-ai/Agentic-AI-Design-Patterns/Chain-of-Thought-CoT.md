# Agentic AI Design Patterns

## 1. Chain-of-Thought (CoT)

**What is it?**
Chain-of-Thought is a reasoning pattern where an AI **breaks down a complex problem into a sequence of intermediate thinking steps** before arriving at a final answer — mimicking how a human "thinks out loud" to solve hard problems.

Instead of jumping straight to an answer, the model reasons step-by-step, where **each step builds on the previous one**.

**The Core Idea**

```
Input → Step 1 → Step 2 → Step 3 → ... → Final Answer
         (each step is visible reasoning, not a black box)
```

**Real-Time Example: E-Commerce Order Refund Agent**

Imagine you build an **AI-powered customer support agent** for an e-commerce platform. A customer sends:

```
"I ordered a laptop on Feb 10th, it arrived damaged on Feb 15th. I want a refund. My order ID is #45231."
```

❌ **Without CoT (Direct Answer — risky)**

`Agent → "Your refund has been approved."`

No reasoning. Could be wrong. No audit trail.

✅ **With Chain-of-Thought**

The agent reasons through it step by step:

**Step 1 — Parse the request**

```
"Customer wants a refund for order #45231. Reason: item arrived damaged. Order date: Feb 10. Delivery date: Feb 15."
```

**Step 2 — Fetch order details**

```
"Order #45231 confirmed. Item: Dell Laptop. Amount: ₹75,000. Status: Delivered. Payment: Completed."
```

**Step 3 — Check refund policy**

```
"Policy says: damaged items are eligible for full refund within 30 days of delivery. Today is Feb 27 — that's 12 days since delivery. ✅ Within window."
```

**Step 4 — Verify damage claim**

```
"Customer reported damage on delivery. No prior refund requests on this account. No fraud flags. ✅ Claim looks legitimate."
```

**Step 5 — Determine refund type**

```
"Since item is damaged (not just unwanted), customer qualifies for full refund + free return pickup under policy section 4.2."
```

**Step 6 — Final decision**

```
"Initiating full refund of ₹75,000 + scheduling return pickup for March 1st."
```

**Why CoT Makes This Agentic**

In an **agentic system**, CoT isn't just prompting — it drives **multi-step tool use**:

| Step    | Agent / Component          | Action Type     | Tool / API Called       | Purpose                                    | Output                                            |
| ------- | -------------------------- | --------------- | ----------------------- | ------------------------------------------ | ------------------------------------------------- |
| Step 1  | StepAgent                  | Receive request | —                       | Intake user refund request                 | Order ID, user context                            |
| Step 2  | StepAgent                  | Tool call       | `get_order()` API       | Fetch order details                        | Order data (status, items, payment, delivery)     |
| Step 3  | StepAgent                  | Tool call       | `check_policy()` tool   | Validate refund eligibility against policy | Eligibility result (approved / rejected + reason) |
| Step 4  | StepAgent                  | Service call    | `fraud_check()` service | Assess fraud risk score                    | Fraud score + risk flag                           |
| Step 5  | StepAgent (Reasoner)       | Decision        | —                       | Combine policy + fraud + order status      | Refund decision                                   |
| Step 6  | StepAgent                  | Action          | `initiate_refund()` API | Trigger refund process                     | Refund transaction ID                             |
| Step 7  | StepAgent                  | Action          | `schedule_pickup()` API | Arrange reverse logistics                  | Pickup confirmation ID                            |
| Step 8  | StepAgent                  | Update systems  | ITSM / DB               | Log workflow & audit trail                 | Case record updated                               |
| Step 9  | StepAgent                  | Notify user     | Email / SMS / App       | Send refund & pickup details               | User notification sent                            |
| Step 10 | Validator Agent (optional) | Post-check      | —                       | Verify refund + pickup scheduled           | Validation status                                 |


Each reasoning step **triggers a real-world action**. The chain of thought is what decides when and why to call each tool.


**Key Benefits**

- **Transparency —** You can audit why the agent made a decision, not just what it decided.
- **Accuracy —** Complex decisions with multiple conditions are far less error-prone when reasoned step by step.
- **Debuggability —?** If the agent refunds wrongly, you can trace exactly which step failed.
- **Trust —** Business stakeholders can review the reasoning chain and validate it.

## CoT vs. Standard Prompting at a Glance

| Capability                | Standard Prompting                 | Chain-of-Thought (CoT) Prompting   |
| ------------------------- | ---------------------------------- | ---------------------------------- |
| Reasoning visibility      | Hidden                             | Explicit, step-by-step             |
| Handling complex logic    | Struggles with multi-step problems | Strong at decomposition & planning |
| Tool orchestration        | Ad hoc, single call bias           | Structured multi-tool sequencing   |
| Task decomposition        | Implicit / often missing           | Explicit planning of subtasks      |
| Accuracy on complex tasks | Lower                              | Higher                             |
| Error tracing             | Hard to debug                      | Easy to trace failure step         |
| Auditability              | Low                                | High (reasoning trail)             |
| Explainability            | Minimal                            | Detailed reasoning path            |
| Determinism control       | Limited                            | Better with structured steps       |
| Multi-step workflows      | Weak                               | Native support                     |
| Agent planning            | Not suitable                       | Core mechanism                     |
| Policy enforcement points | Hard to insert                     | Can validate per step              |
| Observability             | Output only                        | Step-level telemetry possible      |
| RCA (root cause analysis) | Difficult                          | Natural fit                        |
| Memory integration        | Shallow                            | Can reference memory per step      |
| Human-in-the-loop gating  | Coarse                             | Fine-grained at each step          |

## When to Use CoT

CoT is most valuable when your agent faces **multi-condition decisions** (like eligibility checks), **sequential dependencies** (step B needs step A's output), **high-stakes actions** (financial transactions, medical triage), or **compliance-sensitive workflows** (where you need an audit trail).
It's the foundation that most other agentic patterns (ReAct, Plan-and-Execute, Self-Reflection) are built on top of.


## Cloud / SRE / Platform Engineering

| #  | Use Case                                | Why CoT is Required                       |
| -- | --------------------------------------- | ----------------------------------------- |
| 1  | K8s pod crash auto-remediation          | Detect → RCA → safe restart decision      |
| 2  | Multi-cluster failover                  | Health → quorum → traffic shift plan      |
| 3  | Auto-scaling with cost guardrails       | Load → forecast → budget check → scale    |
| 4  | Noisy alert deduplication & correlation | Multi-signal reasoning                    |
| 5  | Service dependency impact analysis      | Graph traversal before action             |
| 6  | Blue-green deployment validation        | Metrics → error rate → rollback logic     |
| 7  | Capacity planning simulation            | Forecast → scenario compare               |
| 8  | SLA breach prediction                   | Trend → risk score → proactive ticket     |
| 9  | Storage tier optimization               | Access pattern → cost vs latency decision |
| 10 | Network latency RCA                     | Trace → hop analysis → bottleneck detect  |

## 💰 FinOps / Cost Optimization

| #  | Use Case                          | Why CoT is Required                     |
| -- | --------------------------------- | --------------------------------------- |
| 1  | Idle resource detection & cleanup | Usage → policy → approval → delete      |
| 2  | Rightsizing recommendations       | Metrics → instance match → savings calc |
| 3  | RI/Savings Plan planning          | Historical usage → commit strategy      |
| 4  | Budget breach prevention          | Forecast → throttle policy              |
| 5  | Cost anomaly investigation        | Billing → tags → workload mapping       |
| 6  | Multi-cloud cost comparison       | Normalize pricing → TCO decision        |
| 7  | Chargeback allocation             | Tag validation → split logic            |
| 8  | Spot vs on-demand switching       | Risk → SLA → cost tradeoff              |
| 9  | Storage lifecycle optimization    | Access freq → tier move                 |
| 10 | FinOps policy enforcement agent   | Spend → policy → auto action            |


## 🛠️ ITSM / IT Operations

| #  | Use Case                      | Why CoT is Required                |
| -- | ----------------------------- | ---------------------------------- |
| 1  | Ticket triage & routing       | NLP → CMDB → resolver mapping      |
| 2  | Major incident coordination   | Timeline → dependency → comms plan |
| 3  | Change risk scoring           | CI impact → blast radius           |
| 4  | Auto-runbook execution        | Step sequencing + validation       |
| 5  | SLA-aware prioritization      | Business impact → queue reorder    |
| 6  | Knowledge article suggestion  | Context → similarity → rank        |
| 7  | Problem management clustering | Pattern detection across incidents |
| 8  | CMDB drift detection          | State compare → reconcile          |
| 9  | Auto-closure validation       | Metrics → service health check     |
| 10 | Escalation decisioning        | SLA + severity + customer tier     |

## 🔐 Security / GRC

| #  | Use Case                           | Why CoT is Required                       |
| -- | ---------------------------------- | ----------------------------------------- |
| 1  | Security incident response         | Detect → enrich → contain → recover       |
| 2  | IAM toxic access detection         | Role graph reasoning                      |
| 3  | Vulnerability prioritization       | CVSS + exploitability + asset criticality |
| 4  | Compliance evidence collection     | Control → artifact mapping                |
| 5  | Threat hunting workflows           | IOC → log pivot → pattern match           |
| 6  | SOAR playbook orchestration        | Multi-tool sequencing                     |
| 7  | Data exfiltration RCA              | Network → identity → storage correlation  |
| 8  | Zero trust access validation       | Contextual policy evaluation              |
| 9  | Third-party risk scoring           | Multi-factor aggregation                  |
| 10 | Security posture drift remediation | Baseline → diff → fix plan                |


## 🧾 Finance / ERP

| #  | Use Case                   | Why CoT is Required                |
| -- | -------------------------- | ---------------------------------- |
| 1  | Financial close automation | Reconcile → adjust → validate      |
| 2  | Invoice exception handling | Match → discrepancy → route        |
| 3  | Fraud detection workflow   | Transaction → pattern → risk score |
| 4  | Revenue recognition rules  | Contract → schedule → posting      |
| 5  | Multi-entity consolidation | FX → intercompany elimination      |
| 6  | Expense policy enforcement | Claim → policy → approval          |
| 7  | Audit trail reconstruction | Journal → source → evidence        |
| 8  | Cash flow forecasting      | Historical → scenario modeling     |
| 9  | Tax rule application       | Jurisdiction → rate → exemption    |
| 10 | Payment run optimization   | Due date → liquidity → priority    |

## 🏭 Supply Chain / Operations

| #  | Use Case                       | Why CoT is Required                |
| -- | ------------------------------ | ---------------------------------- |
| 1  | Shipment delay mitigation      | Detect → alternate route plan      |
| 2  | Inventory optimization         | Demand → safety stock → reorder    |
| 3  | Supplier risk scoring          | Performance → financial → geo risk |
| 4  | Production bottleneck RCA      | Throughput → stage analysis        |
| 5  | Demand forecasting             | Multi-signal time series reasoning |
| 6  | Backorder allocation           | Priority → margin → SLA            |
| 7  | Warehouse slot optimization    | SKU velocity → layout plan         |
| 8  | Recall impact analysis         | Batch → distribution graph         |
| 9  | Multi-modal logistics planning | Cost vs time tradeoff              |
| 10 | Cold chain failure response    | Sensor → threshold → reroute       |


## 🧠 Data / AI / MLOps

| #  | Use Case                      | Why CoT is Required          |
| -- | ----------------------------- | ---------------------------- |
| 1  | Data pipeline failure RCA     | Stage → dependency → replay  |
| 2  | Feature drift detection       | Baseline → statistical test  |
| 3  | Model deployment gating       | Metrics → bias → policy      |
| 4  | Auto-retraining decision      | Performance → data freshness |
| 5  | Experiment result analysis    | Multi-metric comparison      |
| 6  | Dataset lineage tracing       | Source → transform → output  |
| 7  | Data quality remediation      | Rule → anomaly → fix         |
| 8  | Hyperparameter tuning planner | Search → evaluate → select   |
| 9  | Model rollback decision       | KPI → threshold → action     |
| 10 | LLM evaluation workflow       | Benchmark → score → approve  |


## 🏥 Healthcare Ops (Non-clinical workflow automation)

| #  | Use Case                       | Why CoT is Required                 |
| -- | ------------------------------ | ----------------------------------- |
| 1  | Insurance claim processing     | Policy → eligibility → payout       |
| 2  | Appointment no-show mitigation | Pattern → reminder → reschedule     |
| 3  | Resource scheduling            | Staff → room → equipment match      |
| 4  | Billing code validation        | Procedure → CPT mapping             |
| 5  | Prior authorization workflow   | Criteria → documentation → decision |
| 6  | Bed allocation optimization    | Capacity → acuity → turnover        |
| 7  | Supply usage anomaly           | Consumption → threshold → audit     |
| 8  | Referral routing               | Specialty → availability → SLA      |
| 9  | Denial management              | Reason → appeal path                |
| 10 | Discharge planning workflow    | Criteria → checklist → follow-up    |


## 🧑‍💼 Customer Support / CX

| #  | Use Case                        | Why CoT is Required             |
| -- | ------------------------------- | ------------------------------- |
| 1  | Refund with fraud check         | Policy → risk → action          |
| 2  | Escalation decisioning          | Sentiment → SLA → tier          |
| 3  | Multi-product troubleshooting   | Symptom → product → fix path    |
| 4  | Warranty validation             | Purchase → coverage → approve   |
| 5  | Order exception handling        | Inventory → shipment → reroute  |
| 6  | Proactive churn mitigation      | Usage → risk score → offer      |
| 7  | SLA-aware response planning     | Queue → priority → agent assign |
| 8  | Knowledge synthesis             | Case → KB → resolution steps    |
| 9  | Field service dispatch planning | Skill → location → ETA          |
| 10 | Voice-of-customer RCA           | Theme → product → action        |


## 🧭 Summary Rule

| Condition                 | Needed |
| ------------------------- | ------ |
| Multiple tools            | ✅      |
| Policy gates              | ✅      |
| Branching decisions       | ✅      |
| Financial/security impact | ✅      |
| Audit trail required      | ✅      |
| Autonomous execution      | ✅      |


# Role mapping of CoT use cases → Planner / Executor / Validator agents.

## 🧠 Role Definitions

| Role            | Responsibility                                                            |
| --------------- | ------------------------------------------------------------------------- |
| Planner Agent   | Decompose goal, select tools, create step plan, insert policy checkpoints |
| Executor Agent  | Call APIs/tools, run workflows, perform remediation actions               |
| Validator Agent | Verify outcomes, enforce guardrails, rollback or approve                  |


## ☁️ Cloud / SRE

| Use Case                  | Planner                 | Executor                | Validator                 |
| ------------------------- | ----------------------- | ----------------------- | ------------------------- |
| K8s pod auto-remediation  | RCA plan                | kubectl restart         | Check metrics recovery    |
| Multi-cluster failover    | Failover strategy       | Shift traffic           | Health + quorum check     |
| Auto-scaling with budget  | Scale decision          | Apply HPA               | Cost + performance check  |
| Alert correlation         | Signal grouping plan    | Query logs/metrics      | Validate incident created |
| Blue-green validation     | Rollout plan            | Switch service          | Error rate check          |
| Capacity planning         | Forecast plan           | Generate recommendation | Compare vs thresholds     |
| SLA breach prediction     | Risk model selection    | Create proactive ticket | SLA timer validation      |
| Storage tier optimization | Tier move plan          | Change storage class    | Latency + cost check      |
| Network RCA               | Trace path plan         | Run trace tools         | Bottleneck confirmed      |
| Dependency impact         | Service graph traversal | Query CMDB              | Blast radius validated    |


## 💰 FinOps

| Use Case            | Planner              | Executor              | Validator            |
| ------------------- | -------------------- | --------------------- | -------------------- |
| Idle cleanup        | Identify candidates  | Stop/delete resources | Savings confirmed    |
| Rightsizing         | Instance match plan  | Modify instance       | Performance ok       |
| RI planning         | Commitment strategy  | Purchase RI           | Utilization tracked  |
| Budget prevention   | Throttle policy      | Apply quota           | Spend within limit   |
| Cost anomaly RCA    | Cost drill-down plan | Fetch billing data    | Root cause confirmed |
| Multi-cloud TCO     | Comparison model     | Aggregate pricing     | Recommendation valid |
| Chargeback          | Tag mapping plan     | Allocate cost         | Totals reconcile     |
| Spot switching      | Risk model           | Replace instance      | SLA maintained       |
| Lifecycle tiering   | Move objects plan    | Change tier           | Access latency ok    |
| FinOps policy agent | Policy steps         | Enforce limits        | Compliance report    |


## 🛠️ ITSM

| Use Case            | Planner             | Executor         | Validator           |
| ------------------- | ------------------- | ---------------- | ------------------- |
| Ticket triage       | Classification plan | Route ticket     | Correct group check |
| Major incident      | Comms + action plan | Trigger runbooks | Timeline validated  |
| Change risk scoring | Impact plan         | Fetch CI data    | Risk score verified |
| Runbook automation  | Step sequence       | Execute steps    | Outcome validated   |
| SLA prioritization  | Queue reorder plan  | Update priority  | SLA met             |
| Problem clustering  | Pattern plan        | Query incidents  | Cluster accuracy    |
| CMDB drift          | Compare states      | Update CMDB      | Drift resolved      |
| Auto-closure        | Health check plan   | Close ticket     | Service healthy     |
| Escalation logic    | Tier decision       | Notify L3        | Response time ok    |
| KB suggestion       | Context plan        | Retrieve KB      | Relevance score     |


## 🔐 Security / GRC

| Use Case              | Planner            | Executor          | Validator             |
| --------------------- | ------------------ | ----------------- | --------------------- |
| Incident response     | Containment plan   | Isolate host      | Threat removed        |
| IAM toxic access      | Role graph plan    | Revoke access     | Least privilege check |
| Vuln prioritization   | Risk model         | Patch system      | CVE resolved          |
| Compliance evidence   | Control map        | Collect artifacts | Control satisfied     |
| Threat hunting        | IOC pivot plan     | Query SIEM        | Findings validated    |
| SOAR playbook         | Action sequence    | Run playbook      | Outcome confirmed     |
| Data exfiltration RCA | Flow analysis plan | Query logs        | Source confirmed      |
| Zero trust validation | Context policy     | Enforce access    | Policy compliance     |
| Third-party risk      | Scoring model      | Aggregate data    | Risk level accurate   |
| Posture drift fix     | Baseline diff plan | Apply config      | Baseline restored     |


## 🧾 Finance / ERP

| Use Case             | Planner               | Executor           | Validator            |
| -------------------- | --------------------- | ------------------ | -------------------- |
| Financial close      | Reconciliation plan   | Post entries       | Balance matched      |
| Invoice exception    | Match rules           | Route for approval | Discrepancy cleared  |
| Fraud workflow       | Pattern plan          | Block transaction  | False positive check |
| Revenue recognition  | Schedule plan         | Post revenue       | GAAP compliance      |
| Consolidation        | FX + elimination plan | Run consolidation  | Totals reconcile     |
| Expense policy       | Rule check plan       | Approve/reject     | Policy compliance    |
| Audit trail          | Evidence plan         | Fetch journals     | Trace complete       |
| Cash forecast        | Model selection       | Run forecast       | Accuracy vs actual   |
| Tax rules            | Jurisdiction plan     | Apply tax          | Correct rate         |
| Payment optimization | Priority plan         | Execute payments   | Liquidity safe       |


## 🏭 Supply Chain

| Use Case               | Planner             | Executor         | Validator            |
| ---------------------- | ------------------- | ---------------- | -------------------- |
| Delay mitigation       | Reroute plan        | Change shipment  | ETA improved         |
| Inventory optimization | Reorder model       | Place PO         | Stock within target  |
| Supplier risk          | Scoring plan        | Fetch metrics    | Risk tier correct    |
| Bottleneck RCA         | Stage analysis plan | Query MES        | Root cause validated |
| Demand forecast        | Model plan          | Run forecast     | Error within limit   |
| Backorder allocation   | Priority logic      | Allocate stock   | SLA met              |
| Warehouse slotting     | Layout plan         | Update slots     | Pick time reduced    |
| Recall impact          | Batch trace plan    | Notify nodes     | Coverage complete    |
| Multi-modal logistics  | Cost/time plan      | Book carrier     | Target met           |
| Cold chain response    | Threshold plan      | Reroute shipment | Temp restored        |


## 🧠 Data / MLOps

| Use Case            | Planner          | Executor       | Validator            |
| ------------------- | ---------------- | -------------- | -------------------- |
| Pipeline RCA        | Stage trace plan | Replay job     | Data complete        |
| Feature drift       | Test selection   | Run stats      | Drift confirmed      |
| Model gating        | Eval plan        | Run tests      | Metrics pass         |
| Auto-retrain        | Trigger logic    | Start training | Performance improved |
| Experiment analysis | Metric plan      | Compare runs   | Winner valid         |
| Lineage trace       | Graph plan       | Query catalog  | Path correct         |
| Data quality fix    | Rule plan        | Clean data     | Quality score ok     |
| HPO planner         | Search strategy  | Run trials     | Best params verified |
| Rollback decision   | KPI plan         | Revert model   | Service stable       |
| LLM eval            | Benchmark plan   | Run eval       | Threshold met        |


## 🧑‍💼 Customer Support

| Use Case         | Planner          | Executor         | Validator             |
| ---------------- | ---------------- | ---------------- | --------------------- |
| Refund + fraud   | Policy plan      | Issue refund     | Fraud risk acceptable |
| Escalation       | Tier logic       | Assign agent     | SLA met               |
| Troubleshooting  | Decision tree    | Run diagnostics  | Issue resolved        |
| Warranty check   | Coverage plan    | Approve claim    | Policy matched        |
| Order exception  | Resolution plan  | Reroute order    | Delivery confirmed    |
| Churn mitigation | Offer strategy   | Apply offer      | Retention improved    |
| SLA response     | Queue plan       | Reassign ticket  | SLA met               |
| KB synthesis     | Retrieval plan   | Fetch articles   | Relevance validated   |
| Field dispatch   | Skill match plan | Schedule tech    | ETA met               |
| VoC RCA          | Theme plan       | Analyze feedback | Root cause valid      |


## 🔁 Universal Agent Flow

```
Planner → creates step plan + tool list + guardrails
Executor → performs tool calls + actions
Validator → checks outcome + enforces policy + rollback if needed
```

## 🧱 Where Each Role Runs in Your Architecture

| Layer                          | Role      |
| ------------------------------ | --------- |
| Agent Core                     | Planner   |
| Tool Gateway / Execution Layer | Executor  |
| Guardrails + Observability     | Validator |




# 🧠 CoT Usage Across Agent Roles (Examples)

| Use Case                       | Planner (CoT – Plan Steps)                                                                   | Executor (CoT – Actions)                                                                            | Validator (CoT – Verify Steps)                                           |
| ------------------------------ | -------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| Refund with fraud check        | Step 1: Fetch order → Step 2: Check policy → Step 3: Run fraud score → Step 4: Decide refund | Call `get_order()` → `check_policy()` → `fraud_check()` → `initiate_refund()` → `schedule_pickup()` | Verify refund ID exists → Fraud score below threshold → Pickup scheduled |
| K8s pod auto-remediation       | Detect high CPU → Correlate logs → Identify memory leak → Plan safe restart                  | Query metrics → Fetch logs → `kubectl rollout restart`                                              | CPU normalized → Pod healthy → No error spike                            |
| Idle resource cleanup (FinOps) | Identify idle > 7 days → Check owner tag → Check policy approval → Plan stop                 | Call billing API → Stop instance → Update CMDB                                                      | Instance stopped → Cost reduced → Tag compliance logged                  |
| ITSM ticket routing            | Classify ticket → Map to CI → Select resolver group → Set priority                           | NLP classify → Query CMDB → Assign group                                                            | Correct group → SLA timer valid → No reassignment needed                 |
| Security incident response     | Enrich alert → Validate IOC → Identify affected host → Plan isolation                        | Query SIEM → Call EDR isolate host → Disable user                                                   | Host isolated → IOC blocked → No lateral movement                        |
| Change risk scoring            | Fetch impacted services → Calculate blast radius → Assign risk score                         | Query CMDB → Build dependency graph → Update change record                                          | Risk score matches policy → Approval required if high                    |
| Blue-green deployment          | Monitor new version → Compare error rate → Decide switch or rollback                         | Shift traffic to green → Monitor metrics                                                            | Error rate < threshold → Rollback if violated                            |
| Data pipeline RCA              | Detect failed stage → Trace upstream dependency → Plan replay                                | Query Airflow → Re-run failed task                                                                  | Data completeness restored → No duplicates                               |
| IAM toxic access removal       | Detect role conflict → Plan revoke least-privilege                                           | Fetch IAM roles → Remove conflicting role                                                           | User retains required access → Toxic combo removed                       |
| Capacity planning              | Forecast demand → Simulate scenarios → Recommend scale plan                                  | Run forecast model → Generate report                                                                | Forecast error within tolerance → Plan approved                          |


# 🔍 CoT Structure Inside Each Role

## Planner CoT (example)

```
Goal: Process refund safely
Step 1: Retrieve order details
Step 2: Validate refund eligibility policy
Step 3: Run fraud risk scoring
Step 4: If eligible AND risk < threshold → approve
Step 5: Initiate refund and schedule pickup
```

## Executor CoT (tool sequencing)

```
Call get_order()
Call check_policy()
Call fraud_check()
If approved → call initiate_refund()
Call schedule_pickup()
```

## Validator CoT (post-conditions)

```
Check refund transaction created
Check fraud score below threshold
Check pickup confirmation exists
Log audit trail
```

## 🧱 CoT Control Points

| Stage     | What CoT Enables                             |
| --------- | -------------------------------------------- |
| Planner   | Task decomposition + policy insertion        |
| Executor  | Ordered tool orchestration                   |
| Validator | Post-condition verification + rollback logic |


**Note:** `No free-text CoT exposed — only structured reasoning trace.`

- Planner node → generates CoT plan (JSON steps)
- Executor node → executes steps sequentially
- Validator node → checks success criteria

# Universal Guardrailed Chain-of-Thought (CoT) JSON Schema

This schema:

✅ Supports Planner → Executor → Validator
✅ Adds policy checkpoints
✅ Enables audit + observability
✅ Avoids storing raw LLM hidden CoT
✅ Uses structured reasoning steps

## 🧠 Universal CoT JSON Schema

```
{
  "task_id": "string",
  "goal": "string",
  "context": {
    "user_id": "string",
    "session_id": "string",
    "source": "ui | api | event",
    "priority": "low | medium | high",
    "timestamp": "ISO-8601"
  },
  "inputs": {
    "entities": [],
    "parameters": {},
    "artifacts": []
  },
  "plan": {
    "planner_agent": "string",
    "steps": [
      {
        "step_id": "1",
        "description": "Fetch order details",
        "type": "data_retrieval | policy_check | analysis | action | validation",
        "tool": "get_order",
        "preconditions": [],
        "expected_output": "Order object",
        "policy_checks": ["refund_policy_v2"],
        "risk_level": "low | medium | high"
      }
    ],
    "decision_logic": {
      "conditions": [
        {
          "if": "fraud_score < 0.7 AND eligible == true",
          "then": "approve_refund",
          "else": "reject_refund"
        }
      ]
    }
  },
  "execution": {
    "executor_agent": "string",
    "step_results": [
      {
        "step_id": "1",
        "status": "pending | success | failed | skipped",
        "tool_called": "get_order",
        "input": {},
        "output": {},
        "error": null,
        "start_time": "ISO-8601",
        "end_time": "ISO-8601",
        "duration_ms": 0,
        "retry_count": 0
      }
    ]
  },
  "validation": {
    "validator_agent": "string",
    "checks": [
      {
        "check_id": "refund_created",
        "description": "Refund transaction exists",
        "status": "pass | fail",
        "evidence": {},
        "policy_reference": "refund_policy_v2"
      }
    ],
    "final_status": "approved | rejected | rollback_required"
  },
  "guardrails": {
    "rbac": {
      "role": "string",
      "permissions": []
    },
    "budget_limit": {
      "max_cost": 0,
      "currency": "USD",
      "status": "within_limit | exceeded"
    },
    "autonomy_mode": "read_only | suggest | auto_with_approval | full_auto",
    "human_in_the_loop": {
      "required": true,
      "approver_role": "manager",
      "approval_status": "pending | approved | rejected"
    }
  },
  "observability": {
    "logs": [],
    "metrics": {
      "total_duration_ms": 0,
      "tool_calls": 0,
      "success_rate": 1.0
    },
    "traces": [
      {
        "span_id": "string",
        "step_id": "string",
        "latency_ms": 0
      }
    ],
    "cost": {
      "llm_tokens": 0,
      "tool_cost": 0,
      "total_cost": 0
    }
  },
  "memory_updates": {
    "short_term": [],
    "long_term": [],
    "knowledge_graph_edges": []
  },
  "audit": {
    "created_by": "agent_id",
    "created_at": "ISO-8601",
    "approved_by": "string",
    "approval_time": "ISO-8601",
    "change_log": []
  }
}
```

# Universal CoT JSON schema in Python + LangChain, with Planner → Executor → Validator.

It uses:

- **Pydantic models** for the schema
- **Structured output** for the planner
- **LangChain tools** for execution
- A **validator** that checks post-conditions and updates the trace


## 1) Define the Universal CoT Schema (Pydantic)

```
from __future__ import annotations

from typing import Any, Dict, List, Literal, Optional
from pydantic import BaseModel, Field


# ---------- Core schema types ----------

StepType = Literal["data_retrieval", "policy_check", "analysis", "action", "validation"]
RiskLevel = Literal["low", "medium", "high"]
StepStatus = Literal["pending", "success", "failed", "skipped"]

AutonomyMode = Literal["read_only", "suggest", "auto_with_approval", "full_auto"]


class Context(BaseModel):
    user_id: str
    session_id: str
    source: Literal["ui", "api", "event"] = "api"
    priority: Literal["low", "medium", "high"] = "medium"
    timestamp: str  # ISO-8601 string


class PlanStep(BaseModel):
    step_id: str
    description: str
    type: StepType
    tool: Optional[str] = None
    preconditions: List[str] = Field(default_factory=list)
    expected_output: Optional[str] = None
    policy_checks: List[str] = Field(default_factory=list)
    risk_level: RiskLevel = "low"


class DecisionCondition(BaseModel):
    if_: str = Field(alias="if")
    then: str
    else_: str = Field(alias="else")


class DecisionLogic(BaseModel):
    conditions: List[DecisionCondition] = Field(default_factory=list)


class Plan(BaseModel):
    planner_agent: str
    steps: List[PlanStep]
    decision_logic: DecisionLogic = Field(default_factory=DecisionLogic)


class StepResult(BaseModel):
    step_id: str
    status: StepStatus = "pending"
    tool_called: Optional[str] = None
    input: Dict[str, Any] = Field(default_factory=dict)
    output: Dict[str, Any] = Field(default_factory=dict)
    error: Optional[str] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    duration_ms: Optional[int] = None
    retry_count: int = 0


class Execution(BaseModel):
    executor_agent: str
    step_results: List[StepResult] = Field(default_factory=list)


class ValidationCheck(BaseModel):
    check_id: str
    description: str
    status: Literal["pass", "fail"]
    evidence: Dict[str, Any] = Field(default_factory=dict)
    policy_reference: Optional[str] = None


class Validation(BaseModel):
    validator_agent: str
    checks: List[ValidationCheck] = Field(default_factory=list)
    final_status: Literal["approved", "rejected", "rollback_required"] = "approved"


class Guardrails(BaseModel):
    autonomy_mode: AutonomyMode = "suggest"
    human_in_the_loop_required: bool = False
    # add RBAC/budget etc. as needed


class CoTTrace(BaseModel):
    task_id: str
    goal: str
    context: Context
    inputs: Dict[str, Any] = Field(default_factory=dict)
    plan: Optional[Plan] = None
    execution: Execution
    validation: Optional[Validation] = None
    guardrails: Guardrails = Field(default_factory=Guardrails)
```

## 2) Define Tools (LangChain Tooling)

Here’s a simple example flow like refund scenario:

- `get_order()`
- `check_policy()`
- `fraud_check()`
- `initiate_refund()`
- `schedule_pickup()`

```
from langchain_core.tools import tool

@tool
def get_order(order_id: str) -> dict:
    # Replace with real API call
    return {"order_id": order_id, "status": "delivered", "amount": 1200, "days_since_delivery": 2}

@tool
def check_policy(order: dict) -> dict:
    eligible = (order["status"] == "delivered") and (order["days_since_delivery"] <= 7)
    return {"eligible": eligible, "policy": "refund_policy_v2", "reason": None if eligible else "outside_window"}

@tool
def fraud_check(order: dict) -> dict:
    # Replace with real fraud service
    return {"fraud_score": 0.22, "threshold": 0.70, "flag": False}

@tool
def initiate_refund(order_id: str, amount: float) -> dict:
    return {"refund_id": f"rf_{order_id}", "status": "initiated", "amount": amount}

@tool
def schedule_pickup(order_id: str) -> dict:
    return {"pickup_id": f"pk_{order_id}", "status": "scheduled", "eta_days": 2}
```


## 3) Planner: Produce a Structured Plan (LLM → Pydantic)

This uses LangChain’s **structured output** to ensure the planner returns valid JSON matching `Plan`.

```
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)

planner_prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are a Planner Agent. Return a step-by-step plan as JSON that matches the Plan schema. "
     "Use available tools only when needed."),
    ("user",
     "Goal: {goal}\n"
     "Inputs: {inputs}\n"
     "Available tools: get_order, check_policy, fraud_check, initiate_refund, schedule_pickup.\n"
     "Create a safe plan with policy checkpoints.")
])

PlannerStructured = llm.with_structured_output(Plan)

def plan(goal: str, inputs: dict) -> Plan:
    return PlannerStructured.invoke(planner_prompt.format_messages(goal=goal, inputs=inputs))
```

## 4) Executor: Run Steps and Record StepResults

You can execute tools directly (simple) or via an agent runner. Below is a **deterministic executor** that follows the planner’s steps in order and logs every call.

```
import time
from datetime import datetime, timezone

TOOLS = {
    "get_order": get_order,
    "check_policy": check_policy,
    "fraud_check": fraud_check,
    "initiate_refund": initiate_refund,
    "schedule_pickup": schedule_pickup
}

def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()

def execute_plan(trace: CoTTrace) -> CoTTrace:
    if not trace.plan:
        raise ValueError("trace.plan is required before execution")

    # Scratchpad between steps (shared working memory)
    state: dict = {"inputs": trace.inputs.copy()}

    for step in trace.plan.steps:
        result = StepResult(step_id=step.step_id, status="pending", tool_called=step.tool)
        result.start_time = now_iso()
        t0 = time.time()

        try:
            # Decide tool inputs from state
            if step.tool == "get_order":
                order_id = state["inputs"]["order_id"]
                result.input = {"order_id": order_id}
                out = TOOLS["get_order"].invoke(result.input)

                state["order"] = out
                result.output = out
                result.status = "success"

            elif step.tool == "check_policy":
                result.input = {"order": state["order"]}
                out = TOOLS["check_policy"].invoke(result.input)

                state["policy"] = out
                result.output = out
                result.status = "success"

                # Guardrail example: stop if not eligible
                if not out.get("eligible", False):
                    # Mark remaining as skipped
                    trace.execution.step_results.append(result)
                    _skip_remaining(trace, after_step_id=step.step_id)
                    return trace

            elif step.tool == "fraud_check":
                result.input = {"order": state["order"]}
                out = TOOLS["fraud_check"].invoke(result.input)

                state["fraud"] = out
                result.output = out
                result.status = "success"

                # Guardrail example: stop if fraud flagged
                if out.get("fraud_score", 1.0) >= out.get("threshold", 0.7):
                    trace.execution.step_results.append(result)
                    _skip_remaining(trace, after_step_id=step.step_id)
                    return trace

            elif step.tool == "initiate_refund":
                order = state["order"]
                result.input = {"order_id": order["order_id"], "amount": float(order["amount"])}
                out = TOOLS["initiate_refund"].invoke(result.input)

                state["refund"] = out
                result.output = out
                result.status = "success"

            elif step.tool == "schedule_pickup":
                order = state["order"]
                result.input = {"order_id": order["order_id"]}
                out = TOOLS["schedule_pickup"].invoke(result.input)

                state["pickup"] = out
                result.output = out
                result.status = "success"

            else:
                # Non-tool step: treat as no-op success
                result.status = "success"

        except Exception as e:
            result.status = "failed"
            result.error = str(e)

        finally:
            result.end_time = now_iso()
            result.duration_ms = int((time.time() - t0) * 1000)
            trace.execution.step_results.append(result)

            if result.status == "failed":
                _skip_remaining(trace, after_step_id=step.step_id)
                return trace

    # Store state for validator (optional)
    trace.inputs["__state__"] = state
    return trace


def _skip_remaining(trace: CoTTrace, after_step_id: str) -> None:
    # Mark planned steps after failure/gate as skipped in execution (optional)
    planned_ids = [s.step_id for s in trace.plan.steps] if trace.plan else []
    try:
        idx = planned_ids.index(after_step_id)
    except ValueError:
        return
    for sid in planned_ids[idx + 1:]:
        trace.execution.step_results.append(
            StepResult(step_id=sid, status="skipped", tool_called=None)
        )
```


## 5) Validator: Post-Conditions + Final Status

Validator uses the trace outputs to assert correctness.

```
def validate(trace: CoTTrace) -> CoTTrace:
    state = trace.inputs.get("__state__", {})
    order = state.get("order")
    policy = state.get("policy")
    fraud = state.get("fraud")
    refund = state.get("refund")
    pickup = state.get("pickup")

    checks = []

    # Policy must pass
    if policy:
        checks.append(ValidationCheck(
            check_id="policy_eligibility",
            description="Refund policy eligibility passed",
            status="pass" if policy.get("eligible") else "fail",
            evidence=policy,
            policy_reference=policy.get("policy")
        ))

    # Fraud must be below threshold
    if fraud:
        ok = fraud.get("fraud_score", 1.0) < fraud.get("threshold", 0.7)
        checks.append(ValidationCheck(
            check_id="fraud_threshold",
            description="Fraud score below threshold",
            status="pass" if ok else "fail",
            evidence=fraud,
            policy_reference="fraud_threshold"
        ))

    # If we executed refund step, refund_id must exist
    if any(r.tool_called == "initiate_refund" and r.status == "success" for r in trace.execution.step_results):
        checks.append(ValidationCheck(
            check_id="refund_created",
            description="Refund transaction created",
            status="pass" if (refund and refund.get("refund_id")) else "fail",
            evidence=refund or {}
        ))

    # If we executed pickup step, pickup_id must exist
    if any(r.tool_called == "schedule_pickup" and r.status == "success" for r in trace.execution.step_results):
        checks.append(ValidationCheck(
            check_id="pickup_scheduled",
            description="Pickup scheduled",
            status="pass" if (pickup and pickup.get("pickup_id")) else "fail",
            evidence=pickup or {}
        ))

    final = "approved"
    if any(c.status == "fail" for c in checks):
        final = "rejected"

    trace.validation = Validation(
        validator_agent="validator_v1",
        checks=checks,
        final_status=final
    )
    return trace
```

## 6) End-to-End Run (Planner → Executor → Validator)

```
def run_refund_flow(order_id: str) -> CoTTrace:
    trace = CoTTrace(
        task_id=f"refund_{order_id}",
        goal="Process refund safely",
        context=Context(
            user_id="u_123",
            session_id="s_abc",
            source="api",
            priority="high",
            timestamp=now_iso(),
        ),
        inputs={"order_id": order_id},
        execution=Execution(executor_agent="executor_v1"),
        guardrails=Guardrails(autonomy_mode="auto_with_approval", human_in_the_loop_required=False),
    )

    # 1) Plan
    trace.plan = plan(goal=trace.goal, inputs=trace.inputs)

    # 2) Execute
    trace = execute_plan(trace)

    # 3) Validate
    trace = validate(trace)

    return trace


if __name__ == "__main__":
    trace = run_refund_flow("12345")
    print(trace.model_dump_json(indent=2))
```


## What you get from this pattern

- The **Planner** returns a valid **Plan** (strict JSON via Pydantic)
- The **Executor** runs tools in order and writes **step_results**
- The **Validator** produces **checks + final_status**
- Complete **audit trace** that is easy to store (Postgres JSONB), query, and debug


Here is the **same Universal CoT flow implemented using LangGraph**
with a **state machine: plan → execute → validate → end.**


✅ Pydantic state (CoT trace)
✅ Deterministic executor
✅ Validator node
✅ LangGraph transitions


## 🧠 1. Install (if needed)

```
pip install langgraph langchain langchain-openai pydantic
```

## 🧱 2. Define Graph State (CoT Trace)

LangGraph requires a **state object** that flows between nodes.

```
from typing import Optional
from pydantic import BaseModel
from datetime import datetime, timezone

from typing import Dict, Any
from pydantic import Field


def now_iso():
    return datetime.now(timezone.utc).isoformat()


class GraphState(BaseModel):
    task_id: str
    goal: str
    inputs: Dict[str, Any] = Field(default_factory=dict)

    plan: Optional[dict] = None
    execution: Dict[str, Any] = Field(default_factory=dict)
    validation: Optional[dict] = None

    status: str = "planning"   # planning → executing → validating → done
```

## 🧠 3. Planner Node (Structured Plan)

```
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(model="gpt-4.1-mini", temperature=0)

planner_prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are a Planner Agent. Output a JSON plan with ordered steps using tools: "
     "get_order, check_policy, fraud_check, initiate_refund, schedule_pickup."),
    ("user", "Goal: {goal}\nInputs: {inputs}")
])

def planner_node(state: GraphState):
    plan = llm.invoke(
        planner_prompt.format_messages(
            goal=state.goal,
            inputs=state.inputs
        )
    ).content

    state.plan = plan  # In prod: parse to JSON/Pydantic
    state.status = "executing"
    return state
```

👉 In production replace with **structured output → Pydantic Plan model**

## 🛠️ 4. Tool Functions (same as before)

```
def get_order(order_id: str):
    return {"order_id": order_id, "status": "delivered", "amount": 1200, "days_since_delivery": 2}

def check_policy(order: dict):
    eligible = order["days_since_delivery"] <= 7
    return {"eligible": eligible}

def fraud_check(order: dict):
    return {"fraud_score": 0.2, "threshold": 0.7}

def initiate_refund(order_id: str, amount: float):
    return {"refund_id": f"rf_{order_id}"}

def schedule_pickup(order_id: str):
    return {"pickup_id": f"pk_{order_id}"}
```

## ⚙️ 5. Executor Node

Deterministic execution with step logging.

```
def executor_node(state: GraphState):
    order_id = state.inputs["order_id"]

    execution_log = []

    # Step 1: get_order
    order = get_order(order_id)
    execution_log.append({"step": "get_order", "output": order})

    # Step 2: policy
    policy = check_policy(order)
    execution_log.append({"step": "check_policy", "output": policy})

    if not policy["eligible"]:
        state.execution = execution_log
        state.status = "validating"
        return state

    # Step 3: fraud
    fraud = fraud_check(order)
    execution_log.append({"step": "fraud_check", "output": fraud})

    if fraud["fraud_score"] >= fraud["threshold"]:
        state.execution = execution_log
        state.status = "validating"
        return state

    # Step 4: refund
    refund = initiate_refund(order_id, order["amount"])
    execution_log.append({"step": "initiate_refund", "output": refund})

    # Step 5: pickup
    pickup = schedule_pickup(order_id)
    execution_log.append({"step": "schedule_pickup", "output": pickup})

    state.execution = execution_log
    state.status = "validating"
    return state
```

## ✅ 6. Validator Node

```
def validator_node(state: GraphState):
    checks = []

    steps = {s["step"]: s["output"] for s in state.execution}

    if "check_policy" in steps:
        checks.append({
            "check": "policy_pass",
            "status": "pass" if steps["check_policy"]["eligible"] else "fail"
        })

    if "fraud_check" in steps:
        fraud = steps["fraud_check"]
        checks.append({
            "check": "fraud_threshold",
            "status": "pass" if fraud["fraud_score"] < fraud["threshold"] else "fail"
        })

    if "initiate_refund" in steps:
        checks.append({
            "check": "refund_created",
            "status": "pass" if "refund_id" in steps["initiate_refund"] else "fail"
        })

    state.validation = {
        "checks": checks,
        "final_status": "approved" if all(c["status"] == "pass" for c in checks) else "rejected"
    }

    state.status = "done"
    return state
```

## 🔀 7. Build LangGraph State Machine

```
from langgraph.graph import StateGraph, END

workflow = StateGraph(GraphState)

workflow.add_node("plan", planner_node)
workflow.add_node("execute", executor_node)
workflow.add_node("validate", validator_node)

workflow.set_entry_point("plan")

workflow.add_edge("plan", "execute")
workflow.add_edge("execute", "validate")
workflow.add_edge("validate", END)

graph = workflow.compile()
```

## ▶️ 8. Run the Graph

```
initial_state = GraphState(
    task_id="refund_123",
    goal="Process refund safely",
    inputs={"order_id": "123"}
)

result = graph.invoke(initial_state)

print(result)
```

## 🧠 Execution Flow

```
plan → execute → validate → end
```

LangGraph handles:

- State passing between nodes
- Deterministic transitions
- Long-running workflows (with persistence if enabled)


## 🔐 Where Guardrails Fit

Add a **guardrail node** between execute → validate or before execute:

```
plan → guardrail_check → execute → validate → end
```

Guardrail node can:

- Enforce RBAC
- Check budget
- Require HITL approval


## 📊 Observability Integration

Inside each node:

- Emit logs
- Track latency
- Count tool calls
- Store cost metrics


## 🚀 Production Extensions

Next steps for platform:

- Use **structured planner output → Pydantic Plan model**
- Add **Tool Gateway node**
- Add **HITL approval node**
- Persist state in **Postgres / Redis**
- Enable **parallel branches** for multi-agent flows

# Tool Gateway wrapper for LangGraph / LangChain that enforces:

✅ RBAC
✅ Budget limits (FinOps)
✅ Policy checks per tool
✅ Audit logging
✅ Observability hooks


before any tool is executed.

This sits between **Executor → Tools**.

## 🧠 1. Design

```
Executor → ToolGateway → Guardrails (RBAC/Budget/Policy) → Tool → Result
```

The gateway:

- Blocks unauthorized tool calls
- Enforces spend limits
- Logs every action
- Attaches telemetry


## 🧱 2. Tool Gateway Config Models

```
from typing import Dict, List, Callable, Any
from pydantic import BaseModel, Field


class RBACConfig(BaseModel):
    role: str
    allowed_tools: List[str]


class BudgetConfig(BaseModel):
    max_cost: float
    current_cost: float = 0.0
    currency: str = "USD"


class PolicyConfig(BaseModel):
    tool_policies: Dict[str, Dict[str, Any]] = Field(default_factory=dict)
```

## 🛠️ 3. Tool Gateway Wrapper

```
import time
from datetime import datetime, timezone


def now_iso():
    return datetime.now(timezone.utc).isoformat()


class ToolGateway:
    def __init__(
        self,
        tools: Dict[str, Callable],
        rbac: RBACConfig,
        budget: BudgetConfig,
        policies: PolicyConfig,
    ):
        self.tools = tools
        self.rbac = rbac
        self.budget = budget
        self.policies = policies

        self.audit_log = []

    # ---------- Guardrail checks ----------

    def _check_rbac(self, tool_name: str):
        if tool_name not in self.rbac.allowed_tools:
            raise PermissionError(f"RBAC: tool '{tool_name}' not allowed for role '{self.rbac.role}'")

    def _check_budget(self, estimated_cost: float):
        if self.budget.current_cost + estimated_cost > self.budget.max_cost:
            raise RuntimeError("Budget exceeded")

    def _check_policy(self, tool_name: str, kwargs: dict):
        policy = self.policies.tool_policies.get(tool_name)
        if not policy:
            return

        # Example: refund amount limit
        if tool_name == "initiate_refund":
            max_amount = policy.get("max_refund_amount")
            if max_amount and kwargs.get("amount", 0) > max_amount:
                raise RuntimeError("Policy violation: refund amount exceeds limit")

    # ---------- Execution ----------

    def call_tool(self, tool_name: str, **kwargs):
        start = time.time()

        # Guardrails
        self._check_rbac(tool_name)
        self._check_policy(tool_name, kwargs)

        estimated_cost = 0.01  # example flat cost per tool
        self._check_budget(estimated_cost)

        # Execute tool
        tool_fn = self.tools[tool_name]
        result = tool_fn(**kwargs)

        # Update budget
        self.budget.current_cost += estimated_cost

        # Audit log
        self.audit_log.append({
            "timestamp": now_iso(),
            "tool": tool_name,
            "input": kwargs,
            "output": result,
            "cost": estimated_cost,
            "role": self.rbac.role,
            "latency_ms": int((time.time() - start) * 1000)
        })

        return result
```

## 🔐 4. Configure RBAC / Budget / Policy

```
rbac = RBACConfig(
    role="refund_agent",
    allowed_tools=["get_order", "check_policy", "fraud_check", "initiate_refund", "schedule_pickup"]
)

budget = BudgetConfig(max_cost=1.00)

policies = PolicyConfig(
    tool_policies={
        "initiate_refund": {
            "max_refund_amount": 5000
        }
    }
)

gateway = ToolGateway(
    tools={
        "get_order": get_order,
        "check_policy": check_policy,
        "fraud_check": fraud_check,
        "initiate_refund": initiate_refund,
        "schedule_pickup": schedule_pickup
    },
    rbac=rbac,
    budget=budget,
    policies=policies
)
```

## ⚙️ 5. Use Gateway Inside Executor Node (LangGraph)

Replace direct tool calls with gateway calls.

```
def executor_node(state: GraphState):
    order_id = state.inputs["order_id"]
    execution_log = []

    order = gateway.call_tool("get_order", order_id=order_id)
    execution_log.append({"step": "get_order", "output": order})

    policy = gateway.call_tool("check_policy", order=order)
    execution_log.append({"step": "check_policy", "output": policy})

    if not policy["eligible"]:
        state.execution = execution_log
        state.status = "validating"
        return state

    fraud = gateway.call_tool("fraud_check", order=order)
    execution_log.append({"step": "fraud_check", "output": fraud})

    if fraud["fraud_score"] >= fraud["threshold"]:
        state.execution = execution_log
        state.status = "validating"
        return state

    refund = gateway.call_tool("initiate_refund", order_id=order_id, amount=order["amount"])
    execution_log.append({"step": "initiate_refund", "output": refund})

    pickup = gateway.call_tool("schedule_pickup", order_id=order_id)
    execution_log.append({"step": "schedule_pickup", "output": pickup})

    state.execution = execution_log
    state.status = "validating"
    return state
```

## 📊 6. Observability Output

After execution:

```
print(gateway.audit_log)
print("Budget used:", gateway.budget.current_cost)
```

Example audit entry:

```
{
  "timestamp": "2026-02-27T10:00:00Z",
  "tool": "initiate_refund",
  "input": {"order_id": "123", "amount": 1200},
  "output": {"refund_id": "rf_123"},
  "cost": 0.01,
  "role": "refund_agent",
  "latency_ms": 42
}
```

## 🧠 What This Gives You

| Feature                  | Benefit                       |
| ------------------------ | ----------------------------- |
| RBAC enforcement         | Prevents unauthorized actions |
| Budget guardrail         | FinOps control                |
| Policy validation        | Safe automation               |
| Audit log                | Compliance & debugging        |
| Telemetry                | Observability ready           |
| Deterministic tool calls | No hallucinated actions       |


## 🔁 Where It Sits in Your Architecture

```
Agent Core → Executor Node → Tool Gateway → Guardrails → Tools
                               ↓
                           Audit Log
                               ↓
                         Observability
```


**1. Pydantic v2 JSON Schema export** (for your Universal CoT trace)
**2. OpenTelemetry trace mapping** (Graph run → node spans → tool spans → validation spans)


# 1) Pydantic v2 JSON Schema export

## A. Define models (Pydantic v2 style)

```
from __future__ import annotations

from typing import Any, Dict, List, Literal, Optional
from pydantic import BaseModel, Field, ConfigDict


StepType = Literal["data_retrieval", "policy_check", "analysis", "action", "validation"]
RiskLevel = Literal["low", "medium", "high"]
StepStatus = Literal["pending", "success", "failed", "skipped"]
AutonomyMode = Literal["read_only", "suggest", "auto_with_approval", "full_auto"]


class Context(BaseModel):
    model_config = ConfigDict(extra="forbid")
    user_id: str
    session_id: str
    source: Literal["ui", "api", "event"] = "api"
    priority: Literal["low", "medium", "high"] = "medium"
    timestamp: str  # ISO-8601


class PlanStep(BaseModel):
    model_config = ConfigDict(extra="forbid")
    step_id: str
    description: str
    type: StepType
    tool: Optional[str] = None
    preconditions: List[str] = Field(default_factory=list)
    expected_output: Optional[str] = None
    policy_checks: List[str] = Field(default_factory=list)
    risk_level: RiskLevel = "low"


class Plan(BaseModel):
    model_config = ConfigDict(extra="forbid")
    planner_agent: str
    steps: List[PlanStep]


class StepResult(BaseModel):
    model_config = ConfigDict(extra="forbid")
    step_id: str
    status: StepStatus = "pending"
    tool_called: Optional[str] = None
    input: Dict[str, Any] = Field(default_factory=dict)
    output: Dict[str, Any] = Field(default_factory=dict)
    error: Optional[str] = None
    start_time: Optional[str] = None
    end_time: Optional[str] = None
    duration_ms: Optional[int] = None
    retry_count: int = 0


class Execution(BaseModel):
    model_config = ConfigDict(extra="forbid")
    executor_agent: str
    step_results: List[StepResult] = Field(default_factory=list)


class ValidationCheck(BaseModel):
    model_config = ConfigDict(extra="forbid")
    check_id: str
    description: str
    status: Literal["pass", "fail"]
    evidence: Dict[str, Any] = Field(default_factory=dict)
    policy_reference: Optional[str] = None


class Validation(BaseModel):
    model_config = ConfigDict(extra="forbid")
    validator_agent: str
    checks: List[ValidationCheck] = Field(default_factory=list)
    final_status: Literal["approved", "rejected", "rollback_required"]


class Guardrails(BaseModel):
    model_config = ConfigDict(extra="forbid")
    autonomy_mode: AutonomyMode = "suggest"
    human_in_the_loop_required: bool = False
    budget_max_cost: Optional[float] = None
    budget_currency: str = "USD"


class CoTTrace(BaseModel):
    model_config = ConfigDict(extra="forbid")
    task_id: str
    goal: str
    context: Context
    inputs: Dict[str, Any] = Field(default_factory=dict)
    plan: Optional[Plan] = None
    execution: Execution
    validation: Optional[Validation] = None
    guardrails: Guardrails = Field(default_factory=Guardrails)
```


## B. Export JSON Schema (Pydantic v2)

```
import json
from pathlib import Path

schema = CoTTrace.model_json_schema()  # dict
Path("cot_trace.schema.json").write_text(json.dumps(schema, indent=2), encoding="utf-8")

print("Wrote schema: cot_trace.schema.json")
```

**Output file:** `cot_trace.schema.json (use it for validation, contracts, governance, UI forms, etc.)`

# 2) OpenTelemetry trace mapping

## A. What to map (recommended span hierarchy)

**Trace = one agent run** (task_id)

- **Span 1:** agent.run (root)
   - **Span:** graph.node.plan
   - **Span:** graph.node.execute
     - **Span(s):** tool.call.<tool_name> (one per tool call)
   - **Span:** graph.node.validate  
     - **Span(s):** validation.check.<check_id>


This gives you perfect observability:

- latency per node
- latency per tool
- failures at exact step
- attributes for cost / policy / RBAC


## B. Minimal OpenTelemetry setup (SDK + Console exporter)

```
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor, ConsoleSpanExporter

resource = Resource.create({
    "service.name": "agentic-ai",
    "service.version": "1.0.0"
})

provider = TracerProvider(resource=resource)
provider.add_span_processor(SimpleSpanProcessor(ConsoleSpanExporter()))
trace.set_tracer_provider(provider)

tracer = trace.get_tracer("agentic-ai.tracer")
```

Swap `ConsoleSpanExporter()` with OTLP exporter to send to Jaeger/Grafana Tempo/Datadog/etc.

## C. Attribute mapping (what to put on spans)

**Root span** (`agent.run`) **attributes**

- `task.id` = trace.task_id
- `agent.goal` = trace.goal
- `user.id` = trace.context.user_id
- `session.id` = trace.context.session_id

- `autonomy.mode` = trace.guardrails.autonomy_mode

**Tool span** (tool.call.<name>) **attributes**

- `tool.name`
- `step.id`
- `policy.checks` (comma list)
- `risk.level`
- `budget.max_cost`
- `budget.currency`
- `tool.status` (success/failed)
- `error.type`, `error.message` if failed


## D. Instrumented ToolGateway (spans + events)

```
from typing import Callable, Dict, Any, List, Optional
from datetime import datetime, timezone
import time


def now_iso():
    return datetime.now(timezone.utc).isoformat()


class ToolGateway:
    def __init__(
        self,
        tools: Dict[str, Callable[..., Any]],
        allowed_tools: List[str],
        role: str,
        budget_max_cost: float = 1.0,
        currency: str = "USD",
        tool_costs: Optional[Dict[str, float]] = None
    ):
        self.tools = tools
        self.allowed_tools = set(allowed_tools)
        self.role = role
        self.budget_max_cost = budget_max_cost
        self.currency = currency
        self.current_cost = 0.0
        self.tool_costs = tool_costs or {}
        self.audit_log: List[dict] = []

    def _rbac(self, tool_name: str):
        if tool_name not in self.allowed_tools:
            raise PermissionError(f"RBAC deny: {tool_name} for role={self.role}")

    def _budget(self, cost: float):
        if self.current_cost + cost > self.budget_max_cost:
            raise RuntimeError("Budget exceeded")

    def call_tool(
        self,
        tool_name: str,
        *,
        step_id: str,
        policy_checks: List[str],
        risk_level: str,
        **kwargs
    ):
        tool_cost = float(self.tool_costs.get(tool_name, 0.01))

        with tracer.start_as_current_span(f"tool.call.{tool_name}") as span:
            span.set_attribute("tool.name", tool_name)
            span.set_attribute("step.id", step_id)
            span.set_attribute("risk.level", risk_level)
            span.set_attribute("policy.checks", ",".join(policy_checks))
            span.set_attribute("rbac.role", self.role)
            span.set_attribute("budget.max_cost", self.budget_max_cost)
            span.set_attribute("budget.currency", self.currency)
            span.set_attribute("tool.estimated_cost", tool_cost)

            t0 = time.time()
            start = now_iso()
            try:
                # Guardrails
                self._rbac(tool_name)
                self._budget(tool_cost)

                # Execute
                out = self.tools[tool_name](**kwargs)

                # Update budget
                self.current_cost += tool_cost

                span.set_attribute("tool.status", "success")
                span.set_attribute("budget.current_cost", self.current_cost)

                # Optional: event for audit trail (avoid huge payloads)
                span.add_event("tool.executed", {
                    "timestamp": start,
                    "input.keys": ",".join(kwargs.keys()),
                })

                return out

            except Exception as e:
                span.record_exception(e)
                span.set_status(trace.Status(trace.StatusCode.ERROR, str(e)))
                span.set_attribute("tool.status", "failed")
                raise

            finally:
                latency_ms = int((time.time() - t0) * 1000)
                end = now_iso()

                self.audit_log.append({
                    "timestamp": start,
                    "tool": tool_name,
                    "step_id": step_id,
                    "policy_checks": policy_checks,
                    "risk_level": risk_level,
                    "role": self.role,
                    "latency_ms": latency_ms,
                    "budget_current_cost": self.current_cost,
                    "budget_max_cost": self.budget_max_cost,
                    "currency": self.currency,
                    "end_time": end,
                })
```


## E. LangGraph node spans (plan → execute → validate)
Use spans inside each node:

```
# Example node wrappers
def plan_node(state):
    with tracer.start_as_current_span("graph.node.plan") as span:
        span.set_attribute("task.id", state.task_id)
        span.set_attribute("agent.goal", state.goal)
        # ... planner logic ...
        return state

def execute_node(state):
    with tracer.start_as_current_span("graph.node.execute") as span:
        span.set_attribute("task.id", state.task_id)
        # ... executor uses ToolGateway.call_tool(...) ...
        return state

def validate_node(state):
    with tracer.start_as_current_span("graph.node.validate") as span:
        span.set_attribute("task.id", state.task_id)
        # ... validation checks ...
        # For each check you can create sub-spans:
        # with tracer.start_as_current_span(f"validation.check.{check_id}"): ...
        return state
```

## And wrap the entire run:

```
def run_graph(graph, initial_state):
    with tracer.start_as_current_span("agent.run") as span:
        span.set_attribute("task.id", initial_state.task_id)
        span.set_attribute("agent.goal", initial_state.goal)
        span.set_attribute("user.id", getattr(initial_state, "user_id", "unknown"))
        return graph.invoke(initial_state)
```


## Quick mapping reference

| CoT Schema field                  | Span / Attribute                                     |
| --------------------------------- | ---------------------------------------------------- |
| `task_id`                         | root span `agent.run` attr `task.id`                 |
| `plan.steps[].step_id`            | tool span attr `step.id`                             |
| `plan.steps[].tool`               | tool span name `tool.call.<tool>` + attr `tool.name` |
| `plan.steps[].policy_checks`      | tool span attr `policy.checks`                       |
| `plan.steps[].risk_level`         | tool span attr `risk.level`                          |
| `execution.step_results[].status` | tool span attr `tool.status`                         |
| `guardrails.autonomy_mode`        | root span attr `autonomy.mode`                       |
| `validation.checks[]`             | `validation.check.<id>` spans + pass/fail attrs      |


## OTLP exporter config (Tempo/Jaeger)

**OpenTelemetry OTLP exporter config for:**

✅ Grafana Tempo
✅ Jaeger (OTLP)
with **Python + LangGraph agents?**


This will send:

- `agent.run traces`
- `node spans (plan/execute/validate)`
- `tool spans`
- `validation spans`


## 🧠 1. Install OpenTelemetry OTLP packages

```
pip install opentelemetry-sdk opentelemetry-exporter-otlp
```

## 🧱 2. OTLP Exporter – Grafana Tempo (HTTP)

**Tempo OTLP endpoint (typical)**

```
http://tempo:4318/v1/traces
```

**Python config**

```
from opentelemetry import trace
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter

resource = Resource.create({
    "service.name": "agentic-ai",
    "service.version": "1.0.0",
    "deployment.environment": "dev"
})

provider = TracerProvider(resource=resource)

otlp_exporter = OTLPSpanExporter(
    endpoint="http://tempo:4318/v1/traces",
    headers={}
)

span_processor = BatchSpanProcessor(otlp_exporter)

provider.add_span_processor(span_processor)
trace.set_tracer_provider(provider)

tracer = trace.get_tracer("agentic-ai.tracer")
```

## 🧱 3. OTLP Exporter – Jaeger (OTLP gRPC)

Jaeger OTLP gRPC default:

```
http://jaeger:4317
```

**Python config**

```
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

otlp_exporter = OTLPSpanExporter(
    endpoint="http://jaeger:4317",
    insecure=True
)

span_processor = BatchSpanProcessor(otlp_exporter)
provider.add_span_processor(span_processor)
```

## 🔀 4. Switch Tempo vs Jaeger via ENV

```
import os

backend = os.getenv("OTEL_BACKEND", "tempo")

if backend == "tempo":
    from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
    exporter = OTLPSpanExporter(endpoint=os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT"))
else:
    from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
    exporter = OTLPSpanExporter(
        endpoint=os.getenv("OTEL_EXPORTER_OTLP_ENDPOINT"),
        insecure=True
    )
```

ENV example:

```
export OTEL_BACKEND=tempo
export OTEL_EXPORTER_OTLP_ENDPOINT=http://tempo:4318/v1/traces
```

or

```
export OTEL_BACKEND=jaeger
export OTEL_EXPORTER_OTLP_ENDPOINT=http://jaeger:4317
```

## 🧠 5. LangGraph Trace Example

```
def run_agent(graph, initial_state):
    with tracer.start_as_current_span("agent.run") as span:
        span.set_attribute("task.id", initial_state.task_id)
        span.set_attribute("agent.goal", initial_state.goal)

        result = graph.invoke(initial_state)

        span.set_attribute("agent.final_status", result.validation["final_status"])
        return result
```

## 🛠️ 6. Tool Span Example (inside ToolGateway)

```
with tracer.start_as_current_span(f"tool.call.{tool_name}") as span:
    span.set_attribute("tool.name", tool_name)
    span.set_attribute("step.id", step_id)
    span.set_attribute("risk.level", risk_level)
    span.set_attribute("policy.checks", ",".join(policy_checks))
    span.set_attribute("budget.current_cost", self.current_cost)
```

## 📊 7. Recommended Span Attributes

**Root span** (`agent.run`)

| Attribute     | Value          |
| ------------- | -------------- |
| task.id       | CoT trace ID   |
| agent.goal    | Task goal      |
| user.id       | Context user   |
| session.id    | Session        |
| autonomy.mode | Guardrail mode |


## Node spans

| Span name           | Attributes  |
| ------------------- | ----------- |
| graph.node.plan     | step_count  |
| graph.node.execute  | tool_calls  |
| graph.node.validate | check_count |


## Tool spans

| Attribute     | Example          |
| ------------- | ---------------- |
| tool.name     | initiate_refund  |
| step.id       | 4                |
| risk.level    | medium           |
| policy.checks | refund_policy_v2 |
| tool.status   | success          |


## 🐳 8. Docker Compose – Tempo + Jaeger (Dev)

```
version: "3.8"

services:

  tempo:
    image: grafana/tempo:latest
    command: ["-config.file=/etc/tempo.yaml"]
    ports:
      - "4318:4318"
      - "3200:3200"

  jaeger:
    image: jaegertracing/all-in-one:latest
    ports:
      - "4317:4317"
      - "16686:16686"
```

UI:

- Tempo → via Grafana
- Jaeger → http://localhost:16686

## 🔐 9. Production Best Practices

| Area         | Recommendation                            |
| ------------ | ----------------------------------------- |
| Sampling     | Use parent-based + 10–20% sampling        |
| PII          | Do NOT log full tool inputs (mask)        |
| Payload size | Log keys only, not full JSON              |
| Batching     | Use BatchSpanProcessor (already used)     |
| Multi-tenant | Add tenant.id attribute                   |
| Cost         | Add llm.token_cost + tool_cost attributes |



# Multi-agent LangGraph (Planner, Telemetry, Remediation, Validator as separate nodes)

Below is a **multi-agent LangGraph** example with **separate nodes**:

- **Planner Agent**
- **Telemetry Agent**
- **Remediation Agent**
- **Validator Agent**

It follows a typical SRE/self-healing flow:

`plan → telemetry → remediation → validate → (loop if needed) → end`


## 2) Define State (shared across agents)

```
from __future__ import annotations
from typing import Any, Dict, List, Literal, Optional
from pydantic import BaseModel, Field

Severity = Literal["low", "medium", "high"]
Status = Literal["ok", "degraded", "failed"]

class PlanStep(BaseModel):
    step_id: str
    description: str
    tool: Optional[str] = None
    risk_level: Severity = "low"
    policy_checks: List[str] = Field(default_factory=list)

class AgentState(BaseModel):
    # Identity / request
    task_id: str
    goal: str
    inputs: Dict[str, Any] = Field(default_factory=dict)

    # Planner outputs
    plan: List[PlanStep] = Field(default_factory=list)
    current_step_index: int = 0

    # Telemetry outputs
    telemetry: Dict[str, Any] = Field(default_factory=dict)
    diagnosis: Dict[str, Any] = Field(default_factory=dict)

    # Remediation outputs
    actions_taken: List[Dict[str, Any]] = Field(default_factory=list)
    remediation_result: Dict[str, Any] = Field(default_factory=dict)

    # Validator outputs
    validation: Dict[str, Any] = Field(default_factory=dict)

    # Control
    attempt: int = 0
    max_attempts: int = 2
    status: Status = "degraded"
    done: bool = False
```

## 3) Tools (mocked) + optional ToolGateway hook

Replace these with real APIs (Prometheus, Loki, Kubernetes, ITSM, etc.).

```
import random
from datetime import datetime, timezone

def now_iso():
    return datetime.now(timezone.utc).isoformat()

# --- Telemetry tools ---
def get_metrics(service: str) -> dict:
    # mock
    return {"service": service, "cpu": random.randint(40, 95), "error_rate": round(random.random() * 0.2, 3)}

def get_logs(service: str) -> dict:
    # mock
    return {"service": service, "last_errors": ["OOMKilled" if random.random() < 0.4 else "None"]}

# --- Remediation tools ---
def kubectl_rollout_restart(service: str) -> dict:
    return {"service": service, "action": "rollout_restart", "result": "initiated"}

def scale_deployment(service: str, replicas: int) -> dict:
    return {"service": service, "action": "scale", "replicas": replicas, "result": "applied"}
```


If you already have the **ToolGateway wrapper** (RBAC/budget/policy), call tools via:
`gateway.call_tool("get_metrics", step_id="...", policy_checks=[...], risk_level="...", service=...)`

## 4) Node 1 — Planner Agent
Creates a minimal plan: gather telemetry → decide remediation → validate.

```
def planner_node(state: AgentState) -> AgentState:
    state.attempt += 1
    service = state.inputs.get("service", "checkout")

    state.plan = [
        PlanStep(step_id="1", description="Fetch metrics", tool="get_metrics", risk_level="low"),
        PlanStep(step_id="2", description="Fetch logs", tool="get_logs", risk_level="low"),
        PlanStep(step_id="3", description="Choose remediation", tool=None, risk_level="medium", policy_checks=["sre_remediation_policy_v1"]),
        PlanStep(step_id="4", description="Execute remediation", tool="remediate", risk_level="high", policy_checks=["rbac", "budget"]),
        PlanStep(step_id="5", description="Validate service health", tool="validate", risk_level="low"),
    ]
    state.current_step_index = 0
    return state
```

## 5) Node 2 — Telemetry Agent

Collects metrics/logs and produces a diagnosis.

```
def telemetry_node(state: AgentState) -> AgentState:
    service = state.inputs.get("service", "checkout")

    metrics = get_metrics(service)
    logs = get_logs(service)

    state.telemetry = {"metrics": metrics, "logs": logs, "ts": now_iso()}

    # simple diagnosis logic
    cpu = metrics["cpu"]
    err = metrics["error_rate"]
    oom = "OOMKilled" in logs["last_errors"]

    state.diagnosis = {
        "cpu_hot": cpu >= 80,
        "high_error_rate": err >= 0.05,
        "oom_suspected": oom,
        "summary": f"cpu={cpu} err={err} oom={oom}"
    }
    return state
```

## 6) Node 3 — Remediation Agent

Chooses and executes the remediation action based on diagnosis.

```
def remediation_node(state: AgentState) -> AgentState:
    service = state.inputs.get("service", "checkout")
    d = state.diagnosis

    # decision: pick action
    if d.get("oom_suspected"):
        action = kubectl_rollout_restart(service)
    elif d.get("cpu_hot") and d.get("high_error_rate"):
        action = scale_deployment(service, replicas=3)
    elif d.get("high_error_rate"):
        action = kubectl_rollout_restart(service)
    else:
        action = {"service": service, "action": "none", "result": "no-op"}

    state.actions_taken.append({"ts": now_iso(), **action})
    state.remediation_result = action
    return state
```

## 7) Node 4 — Validator Agent
Checks post-conditions (simulated) and decides if we’re done or should loop.

```
def validator_node(state: AgentState) -> AgentState:
    service = state.inputs.get("service", "checkout")

    # post-check: re-check telemetry (in real life, wait/poll)
    metrics = get_metrics(service)
    healthy = (metrics["error_rate"] < 0.03) and (metrics["cpu"] < 80)

    state.validation = {
        "service": service,
        "post_metrics": metrics,
        "healthy": healthy,
        "attempt": state.attempt,
    }

    state.status = "ok" if healthy else "degraded"
    state.done = healthy or (state.attempt >= state.max_attempts)
    return state
```

## 8) Build LangGraph with a loop

Routing:

- **Always:** plan → telemetry → remediation → validate

- **After validate:**

- if `done=True` → END
- else → telemetry again (loop)

```
from langgraph.graph import StateGraph, END

def route_after_validate(state: AgentState) -> str:
    return END if state.done else "telemetry"

graph = StateGraph(AgentState)

graph.add_node("plan", planner_node)
graph.add_node("telemetry", telemetry_node)
graph.add_node("remediation", remediation_node)
graph.add_node("validate", validator_node)

graph.set_entry_point("plan")

graph.add_edge("plan", "telemetry")
graph.add_edge("telemetry", "remediation")
graph.add_edge("remediation", "validate")

graph.add_conditional_edges("validate", route_after_validate)

app = graph.compile()
```

## 9) Run
```
initial = AgentState(
    task_id="inc_1001",
    goal="Restore service health",
    inputs={"service": "checkout"},
    max_attempts=2
)

result = app.invoke(initial)
print(result.model_dump_json(indent=2))
```
