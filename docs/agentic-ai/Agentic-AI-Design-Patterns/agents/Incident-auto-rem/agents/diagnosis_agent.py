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
