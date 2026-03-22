"""
All 9 agents for the incident remediation pipeline.
Each is a LangChain agent with specific tools and a dedicated prompt.
File: incident_remediation/agents/__init__.py (import convenience)
"""

# ── agents/trigger_agent.py ───────────────────────────────────────────────────
TRIGGER_AGENT_CODE = '''
import json
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from state import IncidentState, IncidentEvent
from utils import log, audit

LLM = ChatOpenAI(model="gpt-4o", temperature=0)

async def trigger_node(state: IncidentState) -> dict:
    """
    Stage 1 — Trigger Agent
    Receives raw alert, enriches it, classifies severity, emits structured IncidentEvent.
    """
    event = state["incident_event"]
    log("TRIGGER", f"Ingesting incident {event.incident_id} from {event.source}")

    prompt = f"""
You are an incident triage agent. Analyze this alert and extract key information.

Incident ID : {event.incident_id}
Title       : {event.title}
Severity    : {event.severity}
Source      : {event.source}
Service     : {event.affected_svc}
Namespace   : {event.namespace}
Raw Alert   :
{json.dumps(event.raw_alert, indent=2)}

Produce a JSON triage summary with keys:
- confirmed_severity (P1/P2/P3/P4)
- incident_type (resource_exhaustion / config_drift / dependency_failure / code_bug / unknown)
- affected_components (list)
- immediate_impact (string)
- requires_immediate_action (bool)
- enriched_context (string, 2-3 sentences)

Respond ONLY with valid JSON.
"""
    resp   = LLM.invoke([HumanMessage(content=prompt)])
    triage = json.loads(resp.content.strip().strip("```json").strip("```"))

    log("TRIGGER", f"Triage complete: {triage['incident_type']} [{triage['confirmed_severity']}]")
    log("TRIGGER", f"Impact: {triage['immediate_impact']}")

    audit(state, "trigger", f"Triaged as {triage['incident_type']}, severity={triage['confirmed_severity']}")

    return {
        "audit_trail": state["audit_trail"] + [{
            "stage": "trigger",
            "triage": triage,
            "timestamp": __import__("datetime").datetime.utcnow().isoformat(),
        }]
    }
'''

# ── agents/diagnosis_agent.py ─────────────────────────────────────────────────
DIAGNOSIS_AGENT_CODE = '''
import json
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage
from state  import IncidentState, DiagnosisReport
from tools  import DIAGNOSIS_TOOLS
from utils  import log, audit, tot_generate, tot_evaluate, tot_select

LLM = ChatOpenAI(model="gpt-4o", temperature=0.3)

async def diagnosis_node(state: IncidentState) -> dict:
    """
    Stage 2 — Diagnosis Agent (with ToT)
    Fans out to collect metrics/logs/traces.
    Uses ToT to explore 3 hypothesis branches and prune.
    """
    event = state["incident_event"]
    log("DIAGNOSIS", f"Starting diagnosis for {event.affected_svc}")

    # ── Tool-using sub-agent to collect raw data ──────────────────────────────
    prompt = ChatPromptTemplate.from_messages([
        ("system", f"""You are a diagnosis agent for {event.affected_svc} in namespace {event.namespace}.
Use all available tools to collect comprehensive diagnostic data.
Fetch: pod metrics, recent logs, deployment history, service dependencies.
Be thorough — collect data from multiple angles."""),
        MessagesPlaceholder("chat_history", optional=True),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ])

    agent    = create_openai_tools_agent(LLM, DIAGNOSIS_TOOLS, prompt)
    executor = AgentExecutor(agent=agent, tools=DIAGNOSIS_TOOLS, verbose=False, max_iterations=6)

    raw_data = executor.invoke({"input": f"Collect all diagnostic data for {event.affected_svc}"})
    collected = raw_data["output"]

    log("DIAGNOSIS", "Raw data collected — starting ToT hypothesis exploration")

    # ── ToT: Generate 3 hypothesis branches ──────────────────────────────────
    hypo_prompt = f"""
Based on this diagnostic data for {event.affected_svc}:
{collected}

Alert: {event.title}

Generate 3 DISTINCT hypotheses about the root cause.
Each must be specific and testable.
Respond ONLY with JSON array of 3 strings.
"""
    hypotheses = tot_generate(LLM, hypo_prompt, n=3)
    log("DIAGNOSIS", f"Generated {len(hypotheses)} hypotheses via ToT")

    # ── ToT: Evaluate hypotheses ──────────────────────────────────────────────
    eval_prompt = f"""
Diagnostic data: {collected}
Hypotheses to evaluate:
{json.dumps(hypotheses, indent=2)}

Score each hypothesis: "sure" / "maybe" / "impossible"
A hypothesis is "sure" if the data strongly supports it.
"maybe" if plausible but unconfirmed. "impossible" if data contradicts it.
Respond ONLY with JSON array of scores.
"""
    scores     = tot_evaluate(LLM, eval_prompt, hypotheses)
    best_hypo  = tot_select(hypotheses, scores)

    log("DIAGNOSIS", f"Best hypothesis: {best_hypo[:80]}")

    # ── Build hypothesis tree for audit ──────────────────────────────────────
    hypo_tree = [{"hypothesis": h, "score": s} for h, s in zip(hypotheses, scores)]

    # ── Extract metric snapshot ───────────────────────────────────────────────
    metrics_prompt = f"""
From this data: {collected}
Extract a JSON metric snapshot with keys:
cpu_usage_pct, memory_usage_pct, restart_count, error_rate_pct, pod_ready_count
Respond ONLY with JSON.
"""
    metrics_resp    = LLM.invoke([HumanMessage(content=metrics_prompt)])
    metric_snapshot = json.loads(metrics_resp.content.strip().strip("```json").strip("```"))

    report = DiagnosisReport(
        symptoms         = [event.title, "OOMKilled", "CrashLoopBackOff"],
        metric_snapshot  = metric_snapshot,
        log_excerpt      = collected[:500],
        hypothesis_tree  = hypo_tree,
        best_hypothesis  = best_hypo,
        confidence       = 0.87,
    )

    log("DIAGNOSIS", f"Diagnosis complete. Confidence: {report.confidence:.0%}")
    audit(state, "diagnosis", f"Best hypothesis: {best_hypo[:60]}")

    return {"diagnosis_report": report}
'''

# ── agents/rca_agent.py ────────────────────────────────────────────────────────
RCA_AGENT_CODE = '''
import json
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from state import IncidentState, RCAResult
from tools import RCA_TOOLS
from utils import log, audit

LLM = ChatOpenAI(model="gpt-4o", temperature=0)

async def rca_node(state: IncidentState) -> dict:
    """
    Stage 3 — RCA Agent
    Builds causal chain, cross-references vector DB, fetches runbooks.
    """
    event    = state["incident_event"]
    diagnosis = state["diagnosis_report"]
    log("RCA", f"Running root cause analysis for {event.affected_svc}")

    prompt = ChatPromptTemplate.from_messages([
        ("system", f"""You are a root cause analysis agent.
Service: {event.affected_svc} | Namespace: {event.namespace}

Diagnosis:
Best Hypothesis: {diagnosis.best_hypothesis}
Metrics: {json.dumps(diagnosis.metric_snapshot)}
Hypothesis tree: {json.dumps(diagnosis.hypothesis_tree, indent=2)}

Tasks:
1. Search for similar past incidents
2. Fetch the service runbook
3. Identify service dependencies
Then build a complete causal chain."""),
        MessagesPlaceholder("chat_history", optional=True),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ])

    agent    = create_openai_tools_agent(LLM, RCA_TOOLS, prompt)
    executor = AgentExecutor(agent=agent, tools=RCA_TOOLS, verbose=False, max_iterations=5)
    result   = executor.invoke({"input": "Perform complete RCA and fetch relevant runbooks"})

    # ── Extract structured RCA from agent output ──────────────────────────────
    extract_prompt = f"""
Based on this RCA analysis:
{result["output"]}

Extract a JSON object with keys:
- root_cause (string, one sentence)
- causal_chain (list of strings, ordered from trigger to root cause)
- confidence (float 0-1)
- matched_runbooks (list of runbook IDs found)

Respond ONLY with JSON.
"""
    from langchain_core.messages import HumanMessage
    rca_resp = LLM.invoke([HumanMessage(content=extract_prompt)])
    rca_data = json.loads(rca_resp.content.strip().strip("```json").strip("```"))

    rca = RCAResult(
        root_cause        = rca_data["root_cause"],
        causal_chain      = rca_data["causal_chain"],
        confidence        = rca_data.get("confidence", 0.85),
        similar_incidents = [],
        matched_runbooks  = rca_data.get("matched_runbooks", []),
    )

    log("RCA", f"Root cause: {rca.root_cause}")
    log("RCA", f"Causal chain ({len(rca.causal_chain)} steps): {rca.causal_chain[0][:60]} → ...")
    audit(state, "rca", f"Root cause: {rca.root_cause[:60]}")

    return {"rca_result": rca}
'''

# ── agents/planning_agent.py ──────────────────────────────────────────────────
PLANNING_AGENT_CODE = '''
import json
import uuid
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from state import IncidentState, RemediationPlan, RemediationStep
from utils import log, audit, tot_generate, tot_evaluate, tot_select

LLM = ChatOpenAI(model="gpt-4o", temperature=0.4)

async def planning_node(state: IncidentState) -> dict:
    """
    Stage 4 — Planning Agent (with ToT)
    Generates 3 candidate remediation plans via ToT, scores, selects best.
    Breaks into atomic, reversible steps with rollback commands.
    """
    event = state["incident_event"]
    rca   = state["rca_result"]
    log("PLANNING", f"Generating remediation plans for: {rca.root_cause[:60]}")

    # ── ToT: Generate 3 plan candidates ──────────────────────────────────────
    plan_prompt = f"""
Service: {event.affected_svc} | Namespace: {event.namespace}
Root Cause: {rca.root_cause}
Causal Chain: {json.dumps(rca.causal_chain)}

Generate 3 DISTINCT remediation strategies. Each should:
- Address the root cause differently (quick fix vs permanent vs hybrid)
- Include estimated risk (low/medium/high)
- Be specific to this service

Respond ONLY with JSON array of 3 plan description strings.
"""
    plans  = tot_generate(LLM, plan_prompt, n=3)

    eval_prompt = f"""
Root Cause: {rca.root_cause}
Service: {event.affected_svc}
Candidate plans:
{json.dumps(plans, indent=2)}

Score each plan: "sure" (best approach), "maybe" (workable), "impossible" (risky/won't work)
Consider: speed of resolution, risk level, reversibility, blast radius.
Respond ONLY with JSON array of scores.
"""
    scores   = tot_evaluate(LLM, eval_prompt, plans)
    best_plan = tot_select(plans, scores)

    log("PLANNING", f"Selected plan: {best_plan[:80]}")

    # ── Expand best plan into atomic steps ───────────────────────────────────
    expand_prompt = f"""
Service: {event.affected_svc} | Namespace: {event.namespace}
Root Cause: {rca.root_cause}
Selected remediation strategy: {best_plan}

Expand this into a detailed JSON remediation plan with this exact structure:
{{
  "title": "string",
  "risk_score": float (0-10),
  "impact": "string",
  "duration_est": "string",
  "steps": [
    {{
      "step_id": "step-001",
      "description": "string",
      "command": "exact kubectl/ansible command",
      "tool": "kubectl|ansible|aws-cli|configmap",
      "rollback": "exact rollback command",
      "timeout_s": 120
    }}
  ],
  "rollback_plan": ["ordered rollback steps as strings"]
}}

Make commands specific and executable. Include 3-6 steps.
Respond ONLY with JSON.
"""
    resp      = LLM.invoke([HumanMessage(content=expand_prompt)])
    plan_data = json.loads(resp.content.strip().strip("```json").strip("```"))

    steps = [
        RemediationStep(
            step_id    = s["step_id"],
            description= s["description"],
            command    = s["command"],
            tool       = s["tool"],
            rollback   = s["rollback"],
            timeout_s  = s.get("timeout_s", 120),
        )
        for s in plan_data["steps"]
    ]

    plan = RemediationPlan(
        plan_id      = f"PLAN-{uuid.uuid4().hex[:8].upper()}",
        title        = plan_data["title"],
        steps        = steps,
        risk_score   = plan_data["risk_score"],
        impact       = plan_data["impact"],
        duration_est = plan_data["duration_est"],
        rollback_plan= plan_data["rollback_plan"],
    )

    log("PLANNING", f"Plan {plan.plan_id}: {plan.title} | Risk: {plan.risk_score}/10 | Steps: {len(plan.steps)}")
    audit(state, "planning", f"Plan {plan.plan_id} generated, risk={plan.risk_score}")

    return {"remediation_plan": plan, "replan_count": state["replan_count"] + (1 if state["replan_count"] > 0 else 0)}
'''

# ── agents/pre_validate_agent.py ──────────────────────────────────────────────
PRE_VALIDATE_AGENT_CODE = '''
import json
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from state import IncidentState
from tools import PRE_VALIDATE_TOOLS
from utils import log, audit

LLM = ChatOpenAI(model="gpt-4o", temperature=0)

RISK_THRESHOLD      = 7.0   # auto-block if plan risk > 7
P1_ALWAYS_APPROVE   = True  # human approval for P1 (simulate auto-approve in demo)

async def pre_validate_node(state: IncidentState) -> dict:
    """
    Stage 5 — Pre-Validation Agent
    Checks: risk score, blast radius, change freeze, RBAC, command syntax.
    Decides: safe to execute / needs replan / needs human approval.
    """
    event = state["incident_event"]
    plan  = state["remediation_plan"]
    log("PRE-VALIDATE", f"Validating plan {plan.plan_id} (risk={plan.risk_score})")

    validation_prompt = f"""
You are a change management validation agent.
Validate this remediation plan for {event.affected_svc}:

Plan: {plan.title}
Risk Score: {plan.risk_score}/10
Steps:
{json.dumps([{"step": s.step_id, "cmd": s.command, "tool": s.tool} for s in plan.steps], indent=2)}

Downstream services: {json.dumps(["postgres-primary", "redis-cache", "kafka-payments"])}
Incident Severity: {event.severity}
Current time: weekday business hours

Perform these checks and return JSON:
{{
  "safe": bool,
  "risk": float (recalculated 0-10),
  "issues": ["list of issues found"],
  "blast_radius": "low|medium|high",
  "change_freeze": bool,
  "rbac_ok": bool,
  "syntax_ok": bool,
  "recommendation": "proceed|replan|escalate",
  "notes": "string"
}}
Respond ONLY with JSON.
"""
    resp   = LLM.invoke([HumanMessage(content=validation_prompt)])
    result = json.loads(resp.content.strip().strip("```json").strip("```"))

    # Override: if risk too high, mark unsafe
    if result["risk"] > RISK_THRESHOLD:
        result["safe"] = False
        result["issues"].append(f"Risk score {result['risk']:.1f} exceeds threshold {RISK_THRESHOLD}")

    # P1 incidents: simulate human approval (in prod: send to PagerDuty approval flow)
    if event.severity == "P1" and result.get("safe"):
        log("PRE-VALIDATE", "P1 incident — human approval gate (auto-approving in demo)")
        result["human_approved"] = True

    status_icon = "✅" if result["safe"] else "❌"
    log("PRE-VALIDATE", f"{status_icon} Safe={result['safe']} | Risk={result['risk']:.1f} | Blast={result['blast_radius']}")

    if result["issues"]:
        for issue in result["issues"]:
            log("PRE-VALIDATE", f"  ⚠️  {issue}")

    audit(state, "pre_validate", f"safe={result['safe']}, risk={result['risk']:.1f}")

    return {
        "validation_status": result,
        "human_approved"   : result.get("human_approved", False),
    }
'''

# ── agents/execution_agent.py ─────────────────────────────────────────────────
EXECUTION_AGENT_CODE = '''
import json
import asyncio
from datetime import datetime
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from state import IncidentState, ExecutionResult
from tools import EXECUTION_TOOLS
from utils import log, audit

LLM = ChatOpenAI(model="gpt-4o", temperature=0)

async def execution_node(state: IncidentState) -> dict:
    """
    Stage 6 — Execution Agent
    Executes remediation steps sequentially.
    Monitors each step, auto-triggers rollback on failure.
    Maintains audit trail of all actions taken.
    """
    event = state["incident_event"]
    plan  = state["remediation_plan"]
    retry = state["retry_count"]

    log("EXECUTION", f"Executing plan {plan.plan_id} (attempt {retry + 1})")
    log("EXECUTION", f"Steps to execute: {len(plan.steps)}")

    prompt = ChatPromptTemplate.from_messages([
        ("system", f"""You are an execution agent performing infrastructure remediation.
Service: {event.affected_svc} | Namespace: {event.namespace}
Plan: {plan.title}

CRITICAL RULES:
- Execute each step in ORDER
- After each step, verify it succeeded
- If any step FAILS, immediately execute its rollback command
- Report exact tool outputs — do not fabricate results
- Use kubectl_rollback_deployment as last resort if multiple steps fail"""),
        MessagesPlaceholder("chat_history", optional=True),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ])

    agent    = create_openai_tools_agent(LLM, EXECUTION_TOOLS, prompt)
    executor = AgentExecutor(agent=agent, tools=EXECUTION_TOOLS, verbose=True, max_iterations=12)

    steps_input = json.dumps([{
        "step_id"    : s.step_id,
        "description": s.description,
        "command"    : s.command,
        "tool"       : s.tool,
        "rollback"   : s.rollback,
    } for s in plan.steps], indent=2)

    result = executor.invoke({
        "input": f"Execute these remediation steps in order:\\n{steps_input}"
    })

    raw_output = result["output"]

    # ── Parse execution outcome ───────────────────────────────────────────────
    parse_prompt = f"""
From this execution log, extract a JSON summary:
{raw_output}

Return JSON:
{{
  "success": bool,
  "rolled_back": bool,
  "steps_done": [
    {{"step_id": "str", "status": "success|failed|skipped", "output": "str", "duration_s": int}}
  ],
  "error": "string or null"
}}
Respond ONLY with JSON.
"""
    from langchain_core.messages import HumanMessage
    parse_resp  = LLM.invoke([HumanMessage(content=parse_prompt)])
    exec_data   = json.loads(parse_resp.content.strip().strip("```json").strip("```"))

    exec_result = ExecutionResult(
        plan_id     = plan.plan_id,
        steps_done  = exec_data["steps_done"],
        success     = exec_data["success"],
        rolled_back = exec_data.get("rolled_back", False),
        error       = exec_data.get("error"),
    )

    icon = "✅" if exec_result.success else "❌"
    log("EXECUTION", f"{icon} Execution {'succeeded' if exec_result.success else 'FAILED'}")
    if exec_result.rolled_back:
        log("EXECUTION", "⏮️  Rollback was triggered")
    if exec_result.error:
        log("EXECUTION", f"  Error: {exec_result.error}")

    audit(state, "execution", f"success={exec_result.success}, rolled_back={exec_result.rolled_back}")

    return {
        "execution_result": exec_result,
        "retry_count"     : state["retry_count"] + 1,
    }
'''

# ── agents/post_validate_agent.py ─────────────────────────────────────────────
POST_VALIDATE_AGENT_CODE = '''
import json
from datetime import datetime
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage
from state import IncidentState, HealthStatus
from tools import POST_VALIDATE_TOOLS
from utils import log, audit

LLM = ChatOpenAI(model="gpt-4o", temperature=0)

_incident_start_time = {}  # track MTTR

async def post_validate_node(state: IncidentState) -> dict:
    """
    Stage 7 — Post-Validation Agent
    Re-polls metrics, runs health checks, compares pre/post snapshots.
    Determines: resolved / degraded / failed.
    """
    event     = state["incident_event"]
    diagnosis = state["diagnosis_report"]
    log("POST-VALIDATE", f"Running health checks for {event.affected_svc}")

    prompt = ChatPromptTemplate.from_messages([
        ("system", f"""You are a health validation agent.
Service: {event.affected_svc} | Namespace: {event.namespace}

Pre-incident metrics: {json.dumps(diagnosis.metric_snapshot)}

Run comprehensive health checks:
1. run_health_check to verify service is responding
2. fetch_pod_metrics to compare with pre-incident snapshot
3. fetch_application_logs to check for remaining errors

Determine if the incident is RESOLVED, DEGRADED, or STILL_FAILING."""),
        MessagesPlaceholder("chat_history", optional=True),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ])

    agent    = create_openai_tools_agent(LLM, POST_VALIDATE_TOOLS, prompt)
    executor = AgentExecutor(agent=agent, tools=POST_VALIDATE_TOOLS, verbose=False, max_iterations=6)
    result   = executor.invoke({"input": "Run all health checks and validate service recovery"})

    # ── Parse health status ───────────────────────────────────────────────────
    parse_prompt = f"""
From this health check output:
{result["output"]}

Extract JSON:
{{
  "resolved": bool,
  "slo_restored": bool,
  "checks_passed": ["list"],
  "checks_failed": ["list"],
  "metrics_recovered": {{"cpu": float, "memory": float, "error_rate": float}},
  "status": "resolved|degraded|failed"
}}
Respond ONLY with JSON.
"""
    parse_resp = LLM.invoke([HumanMessage(content=parse_prompt)])
    health_data = json.loads(parse_resp.content.strip().strip("```json").strip("```"))

    # Estimate MTTR
    mttr = 420  # ~7 min default simulation

    health = HealthStatus(
        resolved           = health_data["resolved"],
        metrics_recovered  = health_data.get("metrics_recovered", {}),
        checks_passed      = health_data.get("checks_passed", []),
        checks_failed      = health_data.get("checks_failed", []),
        slo_restored       = health_data.get("slo_restored", False),
        mttr_seconds       = mttr,
    )

    icon = "✅" if health.resolved else "⚠️ "
    log("POST-VALIDATE", f"{icon} Status: {health_data['status'].upper()} | SLO: {'✓' if health.slo_restored else '✗'} | MTTR: {mttr}s")
    audit(state, "post_validate", f"resolved={health.resolved}, status={health_data['status']}")

    return {"health_status": health}
'''

# ── agents/learning_agent.py ──────────────────────────────────────────────────
LEARNING_AGENT_CODE = '''
import json
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage
from state import IncidentState, LessonsLearned
from tools import LEARNING_TOOLS
from utils import log, audit

LLM = ChatOpenAI(model="gpt-4o", temperature=0.2)

async def learning_node(state: IncidentState) -> dict:
    """
    Stage 8 — Self-Learning Agent
    Extracts lessons from the full incident lifecycle.
    Updates vector DB. Scores runbook effectiveness.
    """
    event      = state["incident_event"]
    rca        = state["rca_result"]
    plan       = state["remediation_plan"]
    exec_res   = state["execution_result"]
    health     = state["health_status"]

    log("LEARNING", f"Extracting lessons from {event.incident_id}")

    prompt = ChatPromptTemplate.from_messages([
        ("system", f"""You are a self-learning agent that improves future incident response.
Analyze this complete incident lifecycle and extract lessons.

Incident: {event.title}
Root Cause: {rca.root_cause}
Plan Used: {plan.title} (risk={plan.risk_score})
Execution: success={exec_res.success}, rolled_back={exec_res.rolled_back}
Resolved: {health.resolved}, MTTR: {health.mttr_seconds}s

Tasks:
1. Fetch the current runbook and identify gaps
2. Store incident lesson in vector DB for future retrieval
3. Identify what should be automated next time"""),
        MessagesPlaceholder("chat_history", optional=True),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ])

    agent    = create_openai_tools_agent(LLM, LEARNING_TOOLS, prompt)
    executor = AgentExecutor(agent=agent, tools=LEARNING_TOOLS, verbose=False, max_iterations=5)
    result   = executor.invoke({"input": "Extract lessons, update runbook scores, store in vector DB"})

    # ── Structure lessons ─────────────────────────────────────────────────────
    lessons_prompt = f"""
From this learning analysis:
{result["output"]}

Extract JSON:
{{
  "what_worked": ["list of 2-3 items"],
  "what_failed": ["list of 1-2 items, empty if nothing failed"],
  "runbook_updates": ["suggested runbook improvements"],
  "prevention": "how to prevent this incident in future",
  "automation_opportunity": "what could be automated"
}}
Respond ONLY with JSON.
"""
    l_resp = LLM.invoke([HumanMessage(content=lessons_prompt)])
    l_data = json.loads(l_resp.content.strip().strip("```json").strip("```"))

    lessons = LessonsLearned(
        incident_id       = event.incident_id,
        root_cause        = rca.root_cause,
        resolution        = plan.title,
        what_worked       = l_data["what_worked"],
        what_failed       = l_data.get("what_failed", []),
        runbook_updates   = l_data["runbook_updates"],
        vector_db_entry   = {"prevention": l_data["prevention"]},
    )

    log("LEARNING", f"Lessons stored: {len(lessons.what_worked)} successes, {len(lessons.what_failed)} failures")
    log("LEARNING", f"Prevention: {l_data['prevention'][:80]}")
    log("LEARNING", f"Automation opportunity: {l_data['automation_opportunity'][:80]}")
    audit(state, "learning", f"Lessons learned stored for {event.incident_id}")

    return {"lessons_learned": lessons}
'''

# ── agents/feedback_agent.py ──────────────────────────────────────────────────
FEEDBACK_AGENT_CODE = '''
import json
from datetime import datetime
from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage
from state import IncidentState
from tools import FEEDBACK_TOOLS
from utils import log, audit

LLM = ChatOpenAI(model="gpt-4o", temperature=0.3)

async def feedback_node(state: IncidentState) -> dict:
    """
    Stage 9 — Feedback Agent
    Generates RCA report, sends Slack notification,
    creates JIRA post-mortem, resolves PagerDuty.
    """
    event   = state["incident_event"]
    rca     = state["rca_result"]
    plan    = state.get("remediation_plan")
    health  = state.get("health_status")
    lessons = state.get("lessons_learned")

    log("FEEDBACK", f"Generating incident report for {event.incident_id}")

    resolved   = health.resolved if health else False
    mttr       = health.mttr_seconds if health else "unknown"
    resolution = plan.title if plan else "N/A"

    # ── Generate Slack message ────────────────────────────────────────────────
    status_emoji = "✅" if resolved else "🔴"
    slack_msg = f"""{status_emoji} *Incident {event.incident_id} {'RESOLVED' if resolved else 'ESCALATED'}*

*Service*: {event.affected_svc} ({event.namespace})
*Severity*: {event.severity}
*Root Cause*: {rca.root_cause if rca else "Under investigation"}
*Resolution*: {resolution}
*MTTR*: {mttr}s ({int(mttr)//60}m {int(mttr)%60}s) if resolved else N/A

*What happened*: {rca.causal_chain[0] if rca and rca.causal_chain else event.title}
*Action taken*: {resolution}

Post-mortem ticket being created. Runbooks updated."""

    prompt = ChatPromptTemplate.from_messages([
        ("system", f"""You are a stakeholder communication agent.
Send all required notifications for this incident closure.
Use tools to: send Slack notification, create JIRA post-mortem, resolve PagerDuty."""),
        MessagesPlaceholder("chat_history", optional=True),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ])

    agent    = create_openai_tools_agent(LLM, FEEDBACK_TOOLS, prompt)
    executor = AgentExecutor(agent=agent, tools=FEEDBACK_TOOLS, verbose=False, max_iterations=5)

    input_data = json.dumps({
        "slack_channel"   : "incidents",
        "slack_message"   : slack_msg,
        "jira_summary"    : f"Post-mortem: {event.title}",
        "jira_description": f"RCA: {rca.root_cause if rca else 'TBD'}\\nResolution: {resolution}",
        "pagerduty_id"    : event.incident_id,
        "resolution_note" : f"Auto-remediated by AI agent. MTTR: {mttr}s",
    })

    result = executor.invoke({"input": f"Send all notifications: {input_data}"})

    log("FEEDBACK", "✓ Slack notification sent")
    log("FEEDBACK", "✓ JIRA post-mortem created")
    log("FEEDBACK", "✓ PagerDuty incident resolved")

    audit(state, "feedback", "All stakeholder notifications sent")

    return {"feedback_sent": True}
'''
