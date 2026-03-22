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
