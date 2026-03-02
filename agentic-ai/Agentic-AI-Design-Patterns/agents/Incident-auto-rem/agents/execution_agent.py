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
        "input": f"Execute these remediation steps in order:\n{steps_input}"
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
