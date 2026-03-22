# 3) What this code implements (mapped to your “replace” table)

| Area                  | Implemented here                                                                                                                                                                                                                  |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Branch generation** | `llm_generate_branches()` uses **LLM + evidence + topology + deploy history**. If LLM unavailable, falls back to `deterministic_dynamic_branches()` which is still **dynamic** (uses signals + topology + deploy age).            |
| **Scoring**           | `score_plan()` includes **policy/autonomy hard checks** + soft scoring: **risk**, **blast radius**, **MTTR**, **cost**, **RCA confidence**, **evidence alignment**, and **memory success boost** (`MemoryStore.success_boost()`). |
| **Validation**        | `PolicyEngine` loads `policy.yaml` and enforces **RBAC + autonomy constraints + policy rules**; `validate_node()` uses same hard checks.                                                                                          |
| **Execution**         | `ToolGateway.call()` enforces **RBAC + budget** before tools; execution uses gateway for tool calls. (You can also enforce policy rules at execution as “defense in depth”.)                                                      |



## 4) How to run

```
pip install crewai langgraph pydantic pyyaml langchain-openai
export POLICY_YAML=policy.yaml
# Optional for LLM-based branch generation:
export OPENAI_API_KEY=your_key
python got_crewai_langgraph_incident.py
```

