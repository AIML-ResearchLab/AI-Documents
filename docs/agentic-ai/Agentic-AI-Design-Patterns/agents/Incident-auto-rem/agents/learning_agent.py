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
