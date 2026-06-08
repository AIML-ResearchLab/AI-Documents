## What is Agentic AI?
Agentic AI is an autonomous AI system that can **`understand a goal`**, **`make decisions`**, **`plan tasks`**, **`use tools`**, **`execute actions`**, and `adapt based on results with limited human intervention` .

Unlike traditional AI systems that primarily generate responses, Agentic AI can **`reason`**, **`act`**, **`learn from results`**, and `coordinate multiple tasks to achieve a desired objective`. It often combines `Large Language Models (LLMs)`, `tools`, `memory`, `planning capabilities`, and `autonomous decision-making` to function as an intelligent agent.


## Key Characteristics of Agentic AI:

- `Goal-oriented behavior`
- `Autonomous decision-making`
- `Planning and task decomposition`
- `Reasoning & Problem Solving`
- `Tool and API usage`
- `Action Execution`
- `Memory and contextual awareness`
- `Adaptability & Self-Correction`
- `Feedback-Driven Learning`
- `Multi-Agent Collaboration`
- `Continuous Monitoring`
- `Human-in-the-Loop Support`
- `Multi-step reasoning and execution`


## Agentic AI Design Patterns

1. `Prompt Chaining Pattern`
2. `Router Pattern`
3. `Orchestrator Pattern`
4. `Supervisor Pattern`
5. `Planner-Executor Pattern`
6. `Tool-Using Agent (ReAct)`
7. `Multi-Agent Collaboration`
8. `Reflection / Self-Critique`
9. `Debate Pattern`
10. `Memory-Augmented Agent`
11. `Human-in-the-Loop (HITL)`
12. `Workflow Graph / State Machine`
13. `Hierarchical Agents`


## Agentic AI Patterns Hierarchy

- **Reasoning Patterns**
    - `Chain of Thought (CoT)`
    - `Tree of Thoughts (ToT)`
    - `Graph of Thoughts (GoT)`
    - `Reflection`
    - `Self-Consistency`
    - `ReAct`

- **Planning Patterns**
    - `Planner-Executor`
    - `Plan-and-Solve`
    - `Hierarchical Planning`

- **Workflow Patterns**
    - `Prompt Chaining`
    - `Routing`
    - `State Machine`
    - `LangGraph Workflows`

 - **Multi-Agent Patterns**
    - `Collaboration`
    - `Debate`
    - `Supervisor`
    - `Hierarchical Agents`

- **Knowledge Patterns**
    - `RAG`
    - `Memory`
    - `Knowledge Graph`


## Detailed Classification

| Pattern                     | Category                       | Purpose                              |
| --------------------------- | ------------------------------ | ------------------------------------ |
| **CoT (Chain of Thought)**  | Reasoning Pattern              | Step-by-step reasoning               |
| **ToT (Tree of Thoughts)**  | Deliberative Reasoning Pattern | Explore multiple reasoning paths     |
| **GoT (Graph of Thoughts)** | Advanced Reasoning Pattern     | Non-linear reasoning network         |
| **ReAct**                   | Reasoning + Acting Pattern     | Think → Use Tool → Observe           |
| **Reflection**              | Self-Improvement Pattern       | Critique and improve answers         |
| **Self-Consistency**        | Verification Pattern           | Generate multiple solutions and vote |
| **Debate**                  | Multi-Agent Reasoning Pattern  | Competing viewpoints                 |




```
AI Agents
│
├── Reactive Agents
├── Goal-Based Agents
├── Utility-Based Agents
├── Learning Agents
├── Tool-Using Agents
├── Planning Agents
├── Autonomous Agents
├── Conversational Agents
├── Orchestrator Agents
├── Specialist Agents
├── Multi-Agent Systems
└── Hierarchical Agents
```

# Agentic AI Pattern Taxonomy

## 1. Reasoning Patterns
How an AI thinks and solves problems.

**Patterns:**

1. `Chain of Thought (CoT)`
2. `Zero-Shot CoT`
3. `Few-Shot CoT`
4. `Tree of Thoughts (ToT)`
5. `Graph of Thoughts (GoT)`
6. `Algorithm of Thoughts (AoT)`
7. `Branch of Thoughts (BoT)`
8. `Reflection`
9. `Reflexion`
10. `Self-Consistency`
11. `Chain of Verification (CoVe)`
12. `Step-Back Prompting`
13. `Least-to-Most Prompting`
14. `Self-Refine`
15. `Meta-Reasoning`


## 2. Planning Patterns

How an AI creates and executes plans.

**Patterns**

1. `Plan-and-Execute`
2. `Plan-and-Solve`
3. `Planner-Executor`
4. `Hierarchical Planning`
5. `Goal-Based Planning`
6. `Task Decomposition`
7. `HTN (Hierarchical Task Network)`
8. `Progressive Planning`
9. `Dynamic Planning`
10. `Adaptive Planning`


## 3. Reasoning + Action Patterns

How an AI reasons and interacts with tools.

**Patterns**

1. `ReAct (Reason + Act)`
2. `ReWOO (Reasoning Without Observation)`
3. `Toolformer`
4. `Function Calling`
5. `MRKL`
6. `PAL (Program-Aided Language Models)`
7. `Tool-Use Pattern`
8. `Computer Use Pattern (CUA)`


## 4. Workflow Patterns

How tasks flow through a system.

**Patterns**

1. `Prompt Chaining`
2. `Sequential Workflow`
3. `Parallel Workflow`
4. `Fan-Out / Fan-In`
5. `Pipeline Pattern`
6. `DAG Workflow`
7. `State Machine Workflow`
8. `Event-Driven Workflow`
9. `Workflow Graph`


**Examples:**

- LangGraph
- Temporal
- Airflow-based AI workflows


## 5. Routing Patterns

How requests are directed.

**Patterns**

1. `Router Pattern`
2. `Intent-Based Routing`
3. `Skill-Based Routing`
4. `Expert Routing`
5. `Dynamic Routing`
6. `Conditional Routing`
7. `Agent Selection Routing`


## 6. Multi-Agent Patterns

How multiple agents collaborate.

**Patterns**

1. `Multi-Agent Collaboration`
2. `Debate Pattern`
3. `Society of Mind`
4. `Role-Based Collaboration`
5. `Supervisor-Worker`
6. `Manager-Worker`
7. `Committee of Experts`
8. `Swarm Intelligence`
9. `Peer-to-Peer Agents`
10. `Hierarchical Agents`


## 7. Orchestration Patterns

How multiple agents and workflows are coordinated.

**Patterns**

1. `Centralized Orchestration`
2. `Decentralized Orchestration`
3. `Supervisor Pattern`
4. `Hierarchical Orchestration`
5. `Agent Mesh`
6. `Agent Registry Pattern`
7. `Blackboard Architecture`


## 8. Memory Patterns

How agents remember information.

**Patterns**

1. `Short-Term Memory`
2. `Long-Term Memory`
3. `Episodic Memory`
4. `Semantic Memory`
5. `Working Memory`
6. `Context Window Memory`
7. `Vector Memory`
8. `Memory Retrieval Pattern`


## 9. Knowledge Patterns

How agents access external knowledge.

**Patterns**

1. `RAG`
2. `Agentic RAG`
3. `GraphRAG`
4. `Hybrid RAG`
5. `Knowledge Graph Reasoning`
6. `Multi-Hop Retrieval`
7. `Retrieval Planning`
8. `Context Enrichment`


## 10. Reflection & Evaluation Patterns

How agents verify and improve outputs.

**Patterns**

1. `Reflection`
2. `Reflexion`
3. `Critic Pattern`
4. `Judge Pattern`
5. `Generate-Critique-Refine`
6. `LLM-as-a-Judge`
7. `Adversarial Review`
8. `Self-Evaluation`
9. `Chain of Verification`


## 11. Learning Patterns

How agents improve over time.

**Patterns**

1. `Learning from Feedback`
2. `Reinforcement Learning`
3. `Experience Replay`
4. `Human Feedback Learning`
5. `Active Learning`
6. `Online Learning`
7. `Continuous Improvement`


## 12. Human-in-the-Loop (HITL) Patterns

How humans participate in decisions.

**Patterns**

1. `Approval Pattern`
2. `Escalation Pattern`
3. `Human Review Pattern`
4. `Human Override Pattern`
5. `Human Validation Pattern`
6. `Human Correction Pattern`


## 13. Communication Patterns

How agents exchange information.

**Patterns**

1. `Message Passing`
2. `Publish-Subscribe`
3. `Request-Response`
4. `Event Streaming`
5. `Shared Memory`
6. `Blackboard Communication`


## 14. Safety & Governance Patterns

How agents remain safe and compliant.

**Patterns**

1. `Constitutional AI`
2. `Guardrails Pattern`
3. `Policy Enforcement`
4. `Compliance Validation`
5. `Risk Assessment`
6. `Safety Checker`
7. `Permission-Based Actions`


## 15. Optimization Patterns

How agents search for better solutions.

**Patterns**

1. `Beam Search`
2. `Monte Carlo Tree Search (MCTS)`
3. `Evolutionary Search`
4. `Genetic Optimization`
5. `Best-First Search`
6. `Heuristic Search`


## 16. Simulation Patterns

How agents explore future possibilities.

**Patterns**

1. `What-If Analysis`
2. `Scenario Planning`
3. `Digital Twin Simulation`
4. `Counterfactual Reasoning`
5. `Future State Modeling`


## 17. Autonomous Agent Patterns

How agents operate independently.

**Patterns**

- `Observe-Orient-Decide-Act (OODA)`
- `Autonomous Loop`
- `Sense-Plan-Act`
- `Goal-Driven Autonomy`
- `Self-Healing Agents`
- `Self-Optimizing Agents`


## Complete High-Level View

```
Agentic AI Patterns
│
├── Reasoning Patterns
├── Planning Patterns
├── Reasoning + Action Patterns
├── Workflow Patterns
├── Routing Patterns
├── Multi-Agent Patterns
├── Orchestration Patterns
├── Memory Patterns
├── Knowledge Patterns
├── Reflection/Evaluation Patterns
├── Learning Patterns
├── Human-in-the-Loop Patterns
├── Communication Patterns
├── Safety/Governance Patterns
├── Optimization Patterns
├── Simulation Patterns
└── Autonomous Agent Patterns
```

| Pattern                     | Category                                 | Purpose                          |
| --------------------------- | ---------------------------------------- | -------------------------------- |
| **CoT (Chain of Thought)**  | **Reasoning Pattern**                    | Think step-by-step               |
| **ToT (Tree of Thoughts)**  | **Reasoning Pattern**                    | Explore multiple reasoning paths |
| **GoT (Graph of Thoughts)** | **Reasoning Pattern**                    | Non-linear reasoning             |
| **Reflection**              | **Reasoning / Self-improvement Pattern** | Critique and improve             |
| **ReAct (Reason + Act)**    | **Reasoning + Action Pattern**           | Think and use tools              |


## Complete Agentic AI Pattern Landscape

| Category                 | Pattern                     | Covered?                     | Type                   | Purpose                                                    |
| ------------------------ | --------------------------- | ---------------------------- | ---------------------- | ---------------------------------------------------------- |
| **Reasoning**            | Chain of Thought (**CoT**)  | ✅ Covered                    | Pure Reasoning         | Single step-by-step reasoning path                         |
| **Reasoning**            | Structured CoT              | ✅ Covered                    | Pure Reasoning         | Developer-defined reasoning steps                          |
| **Reasoning**            | Tree of Thoughts (**ToT**)  | ✅ Covered                    | Pure Reasoning         | Explore multiple reasoning branches                        |
| **Reasoning**            | Graph of Thoughts (**GoT**) | ✅ Covered                    | Pure Reasoning         | Interconnected reasoning graph with reusable thoughts      |
| **Reasoning**            | Reflection                  | ✅ Covered                    | Pure Reasoning         | Critique and improve the current answer                    |
| **Reasoning**            | Reflexion                   | ✅ Covered                    | Reasoning + Memory     | Learn from mistakes across tasks                           |
| **Reasoning**            | Self-Consistency            | ❌ Missing                    | Pure Reasoning         | Generate multiple CoTs and select the majority/best answer |
| **Action & Execution**   | ReAct                       | ✅ Covered                    | Reasoning + Action     | Think → Act → Observe loop                                 |
| **Action & Execution**   | ReAct + CoT                 | ✅ Covered                    | Reasoning + Action     | ReAct with structured reasoning inside thoughts            |
| **Action & Execution**   | ReAct + ToT                 | ✅ Covered                    | Reasoning + Action     | Use ToT for planning and ReAct for execution               |
| **Action & Execution**   | ReAct + GoT                 | ✅ Covered                    | Reasoning + Action     | Use GoT reasoning nodes with tool interactions             |
| **Planning & Execution** | Plan-and-Execute            | ✅ Covered                    | Planning Pattern       | Plan first, then execute sequentially                      |
| **Planning & Execution** | ReWOO                       | ✅ Covered                    | Planning Pattern       | Reason once and execute using variables                    |
| **Planning & Execution** | LLM Compiler                | ✅ Covered                    | Planning Pattern       | Compile workflows into optimized DAGs                      |
| **Multi-Agent**          | Supervisor Pattern          | ❌ Missing                    | Multi-Agent            | Supervisor delegates tasks to worker agents                |
| **Multi-Agent**          | Hierarchical Pattern        | ❌ Missing                    | Multi-Agent            | Manager → Worker agent structure                           |
| **Multi-Agent**          | Peer-to-Peer Pattern        | ❌ Missing                    | Multi-Agent            | Agents collaborate without a supervisor                    |
| **Multi-Agent**          | Debate Pattern              | ❌ Missing                    | Multi-Agent            | Multiple agents argue to improve quality                   |
| **Routing**              | Router Pattern              | ❌ Missing                    | Routing                | Route requests to specialized agents/tools                 |
| **Routing**              | Semantic Router             | ❌ Missing                    | Routing                | Embedding-based routing decisions                          |
| **Memory**               | Short-Term Memory           | ❌ Missing                    | Memory                 | Maintain conversation context                              |
| **Memory**               | Long-Term Memory            | ❌ Missing                    | Memory                 | Store persistent user/domain knowledge                     |
| **Memory**               | Episodic Memory             | ⚠️ Partially (via Reflexion) | Memory                 | Store experiences from previous tasks                      |
| **Memory**               | Semantic Memory             | ❌ Missing                    | Memory                 | Store factual knowledge                                    |
| **Retrieval**            | RAG                         | ❌ Missing                    | Retrieval              | Retrieve knowledge before generation                       |
| **Retrieval**            | Corrective RAG (**CRAG**)   | ❌ Missing                    | Retrieval              | Validate and improve retrieval quality                     |
| **Retrieval**            | Adaptive RAG                | ❌ Missing                    | Retrieval              | Decide dynamically whether retrieval is needed             |
| **Retrieval**            | Self-RAG                    | ❌ Missing                    | Retrieval + Reflection | Critique and improve retrieval process                     |
| **Tool Usage**           | Function Calling            | ❌ Missing                    | Tool Pattern           | Structured tool invocation using schemas                   |
| **Tool Usage**           | Toolformer                  | ❌ Missing                    | Tool Pattern           | Learn when and how to use tools                            |
| **Tool Usage**           | MRKL                        | ❌ Missing                    | Tool Pattern           | Route to expert modules/tools                              |
| **Human-in-the-Loop**    | Approval Pattern            | ❌ Missing                    | HITL                   | Require human approval before execution                    |
| **Human-in-the-Loop**    | Escalation Pattern          | ❌ Missing                    | HITL                   | Escalate uncertain cases to humans                         |
| **Workflow**             | Sequential Workflow         | ❌ Missing                    | Workflow               | Execute steps one after another                            |
| **Workflow**             | Conditional Workflow        | ❌ Missing                    | Workflow               | Branch based on conditions                                 |
| **Workflow**             | Parallel Workflow           | ❌ Missing                    | Workflow               | Execute independent tasks concurrently                     |
| **Workflow**             | Cyclic Workflow             | ❌ Missing                    | Workflow               | Repeat until a condition is met                            |
| **Evaluation**           | Judge Pattern               | ❌ Missing                    | Evaluation             | LLM evaluates another LLM's output                         |
| **Evaluation**           | LLM-as-a-Judge              | ❌ Missing                    | Evaluation             | Score outputs using an evaluator model                     |
| **Evaluation**           | Debate + Judge              | ❌ Missing                    | Evaluation             | Judge selects the best argument from debating agents       |


```
Reasoning:
✓ CoT
✓ Structured CoT
✓ ToT
✓ GoT
✓ Reflection
✓ Reflexion

Execution:
✓ ReAct
✓ ReAct + CoT
✓ ReAct + ToT
✓ ReAct + GoT
✓ Plan-and-Execute
✓ ReWOO
✓ LLM Compiler
```

```
Phase 1 (High Priority)
1. Function Calling
2. RAG
3. Approval Pattern
4. Supervisor Pattern

Phase 2 (Medium Priority)
5. Router Pattern
6. Self-Consistency
7. Judge Pattern
8. Semantic Router

Phase 3 (Advanced)
9. Self-RAG
10. Toolformer
11. MRKL
12. Debate Pattern
13. Peer-to-Peer Agents
```

**Current Progress:**

```
Reasoning Patterns       ██████████ 100%
Execution Patterns       ██████████ 100%
Planning Patterns        ██████████ 100%
Multi-Agent Patterns     ░░░░░░░░░░   0%
Memory Patterns          ░░▒░░░░░░░  25%
Retrieval Patterns       ░░░░░░░░░░   0%
Tool Usage Patterns      ░░░░░░░░░░   0%
Human-in-the-Loop        ░░░░░░░░░░   0%
Evaluation Patterns      ░░░░░░░░░░   0%
```

## Complete Agentic AI Pattern Map

| Category              | Pattern           | Status         |
| --------------------- | ----------------- | -------------- |
| **Reasoning**         | CoT               | ✅              |
| **Reasoning**         | Structured CoT    | ✅              |
| **Reasoning**         | ToT               | ✅              |
| **Reasoning**         | GoT               | ✅              |
| **Reasoning**         | Reflection        | ✅              |
| **Reasoning**         | Reflexion         | ✅              |
| **Reasoning**         | Self-Consistency  | ❌              |
| **Action**            | ReAct             | ✅              |
| **Action**            | ReAct + CoT       | ✅              |
| **Action**            | ReAct + ToT       | ✅              |
| **Action**            | ReAct + GoT       | ✅              |
| **Planning**          | Plan-and-Execute  | ✅              |
| **Planning**          | ReWOO             | ✅              |
| **Planning**          | LLM Compiler      | ✅              |
| **Retrieval**         | RAG               | ❌              |
| **Retrieval**         | CRAG              | ❌              |
| **Retrieval**         | Adaptive RAG      | ❌              |
| **Retrieval**         | Self-RAG          | ❌              |
| **Memory**            | Short-Term Memory | ❌              |
| **Memory**            | Long-Term Memory  | ❌              |
| **Memory**            | Episodic Memory   | ⚠️ (Reflexion) |
| **Memory**            | Semantic Memory   | ❌              |
| **Multi-Agent**       | Supervisor        | ❌              |
| **Multi-Agent**       | Hierarchical      | ❌              |
| **Multi-Agent**       | Peer-to-Peer      | ❌              |
| **Multi-Agent**       | Debate            | ❌              |
| **Routing**           | Router            | ❌              |
| **Routing**           | Semantic Router   | ❌              |
| **Tool Usage**        | Function Calling  | ❌              |
| **Tool Usage**        | Toolformer        | ❌              |
| **Tool Usage**        | MRKL              | ❌              |
| **Human-in-the-Loop** | Approval          | ❌              |
| **Human-in-the-Loop** | Escalation        | ❌              |
| **Workflow**          | Sequential        | ❌              |
| **Workflow**          | Conditional       | ❌              |
| **Workflow**          | Parallel          | ❌              |
| **Workflow**          | Cyclic            | ❌              |
| **Evaluation**        | Judge             | ❌              |
| **Evaluation**        | LLM-as-a-Judge    | ❌              |
| **Evaluation**        | Debate + Judge    | ❌              |

## Research-Oriented Patterns

| Pattern                             | Importance |
| ----------------------------------- | ---------- |
| Chain of Verification (CoVe)        | Medium     |
| Least-to-Most Prompting             | Medium     |
| Program-of-Thoughts (PoT)           | Medium     |
| Skeleton-of-Thought (SoT)           | Low        |
| Meta Prompting                      | Medium     |
| STaR (Self-Taught Reasoner)         | Low        |
| PAL (Program-Aided Language Models) | Medium     |
| DSPy Optimizers                     | Medium     |
| Agent Verification Loops            | Medium     |



## Enterprise Agentic AI System Design Roadmap

**1. Foundation (Must Know)**

| Area               | Topics                                         |
| ------------------ | ---------------------------------------------- |
| LLM Fundamentals   | Tokens, Context Window, Temperature, Prompting |
| Prompt Engineering | Zero-shot, Few-shot, CoT, Structured CoT       |
| Tool Calling       | Function Calling, JSON Schemas                 |
| RAG                | Vector DB, Embeddings, Retrieval               |
| LangChain          | Chains, Tools, Agents                          |
| LangGraph          | StateGraph, Conditional Routing                |


**2. Core Agent Patterns (Must Know)**

| Pattern                | Why                                     |
| ---------------------- | --------------------------------------- |
| **ReAct**              | Industry standard for tool-using agents |
| **Plan-and-Execute**   | Long-running workflows                  |
| **Reflection**         | Improve output quality                  |
| **Reflexion**          | Learning from previous failures         |
| **Supervisor Pattern** | Coordinate multiple agents              |
| **Approval Pattern**   | Human oversight                         |


**3. Reasoning Patterns (Should Know)**

| Pattern          | Enterprise Usage |
| ---------------- | ---------------- |
| CoT              | High             |
| Structured CoT   | Very High        |
| ToT              | Medium           |
| GoT              | Low-Medium       |
| Self-Consistency | Medium           |
| Reflection       | High             |


**4. Multi-Agent Patterns (Must Know)**

**Supervisor:**

```
Supervisor
    ↓
Research Agent
Coding Agent
Review Agent
```

Used in:

- SDLC agents
- Customer service
- Digital twins


**Hierarchical**

```
Director Agent
      ↓
Manager Agents
      ↓
Worker Agents
```

Used in:

- Enterprise orchestration
- Autonomous operations

**5. Memory Architecture (Must Know)**

| Memory Type | Use Case             |
| ----------- | -------------------- |
| Short-Term  | Conversation context |
| Long-Term   | User preferences     |
| Episodic    | Previous executions  |
| Semantic    | Enterprise knowledge |


**6. Retrieval Architecture (Must Know)**

**Basic RAG**

```
Question
 ↓
Retrieve
 ↓
Generate
```

**Enterprise RAG**

```
Question
 ↓
Router
 ↓
Multi-source Retrieval
 ↓
Reranker
 ↓
LLM
```

Need to know:

- Hybrid Search
- Metadata Filtering
- Reranking
- Context Compression


**7. Human-in-the-Loop (Critical)**

Enterprise agents must not be fully autonomous.

| Pattern    | Example             |
| ---------- | ------------------- |
| Approval   | Hotel payment       |
| Escalation | Medical diagnosis   |
| Override   | Security operations |


**8. Evaluation Framework (Must Know)**

Questions:

```
Is the answer correct?
Is it grounded?
Should the agent be trusted?
```

| Pattern           | Use                |
| ----------------- | ------------------ |
| LLM Judge         | Quality assessment |
| Human Evaluation  | Gold standard      |
| Automated Metrics | Regression testing |


**Metrics:**

- Accuracy
- Hallucination Rate
- Tool Success Rate
- Latency
- Cost


**9. Security (Mandatory)**

Need to understand:

| Topic              | Importance |
| ------------------ | ---------- |
| Prompt Injection   | Critical   |
| Data Leakage       | Critical   |
| PII Protection     | Critical   |
| Tool Authorization | Critical   |
| RBAC               | Critical   |
| Audit Logs         | Critical   |


**10. Observability (Mandatory)**

Need visibility into: `Why did the agent do this?`

Monitor:

- Prompts
- Tool Calls
- Costs
- Errors
- Reasoning Traces

**11. Production Infrastructure**

Need to understand:

| Area             | Topics              |
| ---------------- | ------------------- |
| Containerization | Docker              |
| Orchestration    | Kubernetes          |
| APIs             | FastAPI             |
| Authentication   | OAuth, JWT          |
| CI/CD            | GitHub Actions      |
| Monitoring       | Prometheus, Grafana |


**12. Enterprise Agent Architecture**

Typical architecture:

```
                 User
                   ↓
              API Gateway
                   ↓
             Guardrails Layer
                   ↓
             LangGraph Agent
                   ↓
        ┌──────────┼───────────┐
        ↓          ↓           ↓
     Memory      RAG       Tool Router
        ↓          ↓           ↓
     Vector DB  Knowledge   Enterprise APIs
                    Base
        ↓
     Human Approval
        ↓
    Final Response
```

## What You Need to Know by Role

**Agentic AI Developer:**

```
✓ LangChain
✓ ReAct
✓ Function Calling
✓ RAG
✓ Reflection
✓ FastAPI
```

**Senior AI Engineer**

```
✓ LangGraph
✓ Supervisor Pattern
✓ Memory
✓ Evaluation
✓ Security
✓ Observability
✓ HITL
```

**Agentic AI Architect**

```
✓ Everything above
✓ Multi-Agent Design
✓ Governance
✓ Compliance
✓ Cost Optimization
✓ Enterprise Integration
✓ Scalability
```

## Enterprise production Agentic AI systems, focus on mastering these 10 areas:

```
1. ReAct
2. Function Calling
3. RAG
4. LangGraph
5. Reflection / Reflexion
6. Supervisor Pattern
7. Memory Architecture
8. Human-in-the-Loop
9. Security & Guardrails
10. Evaluation & Observability
```

## optimization or an advanced specialization

| Pattern                                 | Category                | Primary Goal                                  | What It Optimizes / Specializes                  | Enterprise Use Cases                                            | Priority |
| --------------------------------------- | ----------------------- | --------------------------------------------- | ------------------------------------------------ | --------------------------------------------------------------- | -------- |
| **Reflection**                          | Optimization            | Improve current output                        | Output quality, completeness                     | Report generation, architecture reviews, recommendation systems | ⭐⭐⭐⭐⭐    |
| **Self-Consistency**                    | Optimization            | Improve reasoning reliability                 | Accuracy by majority voting across multiple CoTs | Financial analysis, root cause analysis, Q&A systems            | ⭐⭐⭐⭐     |
| **ReWOO**                               | Optimization            | Reduce unnecessary LLM calls                  | Cost, latency, token consumption                 | Tool-heavy enterprise workflows, ServiceNow agents              | ⭐⭐⭐⭐     |
| **LLM Compiler**                        | Optimization            | Optimize execution plans                      | Parallelism, latency, throughput                 | Large enterprise workflows, multi-step automations              | ⭐⭐⭐      |
| **Semantic Router**                     | Optimization            | Route requests efficiently                    | Agent/tool selection accuracy and speed          | Customer support, ServiceNow routing, enterprise copilots       | ⭐⭐⭐⭐     |
| **Judge Pattern (LLM-as-a-Judge)**      | Optimization            | Validate agent outputs                        | Reliability, quality assurance                   | Code review, document validation, compliance checks             | ⭐⭐⭐⭐     |
| **CRAG (Corrective RAG)**               | Optimization            | Improve retrieval quality                     | Hallucination reduction, grounding               | Banking, healthcare, legal assistants                           | ⭐⭐⭐      |
| **Adaptive RAG**                        | Optimization            | Use retrieval only when necessary             | Cost, latency                                    | Enterprise knowledge assistants                                 | ⭐⭐⭐      |
| **Parallel Workflow**                   | Optimization            | Execute independent tasks simultaneously      | Performance, response time                       | Multi-source retrieval, document processing                     | ⭐⭐⭐⭐     |
| **Caching Strategies**                  | Optimization            | Reuse previous computations                   | Cost and latency reduction                       | High-volume production agents                                   | ⭐⭐⭐⭐     |
| **ToT (Tree of Thoughts)**              | Advanced Specialization | Explore alternative solutions                 | Multi-path reasoning                             | Travel planning, architecture decisions, strategic planning     | ⭐⭐⭐      |
| **GoT (Graph of Thoughts)**             | Advanced Specialization | Model complex dependencies                    | Knowledge reuse and interconnected reasoning     | Medical diagnosis, digital twins, research agents               | ⭐⭐       |
| **Reflexion**                           | Advanced Specialization | Learn from past mistakes                      | Long-term adaptation using memory                | Autonomous coding agents, adaptive assistants                   | ⭐⭐⭐      |
| **Debate Pattern**                      | Advanced Specialization | Improve decisions via opposing views          | Robustness of reasoning                          | Investment advisory, security analysis, clinical decisions      | ⭐⭐       |
| **Debate + Judge**                      | Advanced Specialization | Combine multiple perspectives with evaluation | Decision confidence                              | High-risk enterprise decisions                                  | ⭐⭐       |
| **Self-RAG**                            | Advanced Specialization | Self-evaluate retrieval quality               | Retrieval accuracy                               | Legal, healthcare, regulatory assistants                        | ⭐⭐       |
| **MRKL**                                | Advanced Specialization | Route to expert modules                       | Domain specialization                            | Tax agents, enterprise support systems                          | ⭐⭐       |
| **Peer-to-Peer Agents**                 | Advanced Specialization | Decentralized collaboration                   | Autonomous coordination                          | Distributed operations, simulations                             | ⭐        |
| **Toolformer**                          | Advanced Specialization | Learn when to use tools automatically         | Tool selection autonomy                          | Primarily research-oriented systems                             | ⭐        |
| **Chain of Verification (CoVe)**        | Advanced Specialization | Verify generated answers                      | Hallucination reduction                          | Compliance-heavy domains                                        | ⭐⭐       |
| **Least-to-Most Prompting**             | Advanced Specialization | Solve problems incrementally                  | Complex reasoning decomposition                  | Educational tutors, planning systems                            | ⭐⭐       |
| **Program of Thoughts (PoT)**           | Advanced Specialization | Combine reasoning with program execution      | Mathematical correctness                         | Quantitative analysis, scientific computing                     | ⭐⭐       |
| **PAL (Program-Aided Language Models)** | Advanced Specialization | Use code execution for reasoning              | Computational accuracy                           | Analytics agents, forecasting systems                           | ⭐⭐       |



## What is Chain of Thought (CoT)?

**Chain of Thought (CoT)** is a reasoning pattern where an LLM solves a problem by **breaking it into intermediate steps** before arriving at the final answer.

Instead of:

`Question → Answer`

CoT follows:

`Question → Reasoning Steps → Answer`

## Example 1: Hotel Recommendation

**User Request:**

# **Example 1: Hotel Recommendation - Chain of Thought (CoT)**

**User Request:** `Find the best hotel in Bangalore for a family of 4 under ₹6,000 near Electronic City.`

**Without CoT:** `Lemon Tree Hotel Electronics City.`
**Problem:** We don't know why this hotel was selected.

**With CoT (Step-by-Step Reasoning):** 
```
Step 1: Identify the constraints
- Location: Electronic City
- Budget: ≤ ₹6,000
- Family size: 4

Step 2: Search available hotels.

Step 3: Filter hotels within budget.

Step 4: Check family-friendly amenities.
- Breakfast included
- Extra bed availability

Step 5: Compare ratings.

Step 6: Recommend the highest-rated option.
```

**Step 2: Define evaluation criteria**

```
Criteria:
1. Must be near Electronic City.
2. Must fit within ₹6,000 budget.
3. Should accommodate 4 guests.
4. Should have good family-friendly amenities.
5. Should have high ratings/reviews.
```

**Step 3: Search hotels**

```
| Hotel                   | Price   | Rating | Family Friendly | Distance                 |
| ----------------------- | ------- | ------ | --------------- | ------------------------ |
| Lemon Tree Hotel        | ₹5,615  | 7.8/10 | Yes             | Electronic City          |
| Hotel Presidency        | ₹4,800  | 8.3/10 | Yes             | Electronic City Phase II |
| Treebo Celebrity Suites | ₹3,900  | 8.0/10 | Yes             | Electronic City Phase I  |
| The Oterra              | ₹16,992 | 8.8/10 | Yes             | Electronic City          |

```

**Step 4: Filter by budget**

```
Remove hotels costing > ₹6,000.

Remaining:
✓ Lemon Tree Hotel
✓ Hotel Presidency
✓ Treebo Celebrity Suites

Discard:
✗ The Oterra
```

**Step 5: Check family suitability**

```
Need:
✓ Extra bedding
✓ Larger rooms
✓ Breakfast option
✓ Family-friendly services
```

```
Treebo → Smaller rooms
Lemon Tree → Better facilities
Hotel Presidency → Spacious rooms
```

**Step 6: Compare quality**

```
Lemon Tree:
Rating: 7.8/10
Price: ₹5,615

Hotel Presidency:
Rating: 8.3/10
Price: ₹4,800

Treebo:
Rating: 8.0/10
Price: ₹3,900
```

**Step 7: Final Recommendation**

**CoT Output:**

```
Thought 1:
The family requires accommodation for 4 people near Electronic City.

Thought 2:
The hotel must cost less than ₹6,000.

Thought 3:
The Oterra is excluded because it exceeds the budget.

Thought 4:
Among the remaining options, Hotel Presidency provides better ratings and family-oriented rooms within budget.
```


## CoTAgent.py 

```
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

prompt = ChatPromptTemplate.from_template("""
You are a travel assistant.

Solve the problem step by step.

User Request:
{request}

Follow this process:
1. Extract requirements.
2. Define evaluation criteria.
3. Compare available options.
4. Eliminate unsuitable choices.
5. Recommend the best option.
6. Explain WHY.

Think step by step.
""")

chain = prompt | llm

response = chain.invoke({
    "request": """
    Find the best hotel in Bangalore
    for a family of 4 under ₹6,000
    near Electronic City.
    """
})

print(response.content)
```

## OUTPUT:

```
python CoTAgent.py 
Sure! Let's go through the process step by step to find the best hotel in Bangalore for a family of 4 under ₹6,000 near Electronic City.

### Step 1: Extract Requirements
- **Location**: Near Electronic City, Bangalore
- **Budget**: Under ₹6,000
- **Family Size**: Accommodate 4 people

### Step 2: Define Evaluation Criteria
To evaluate the hotels, we can use the following criteria:
1. **Price**: Must be under ₹6,000 per night.
2. **Location**: Proximity to Electronic City.
3. **Amenities**: Family-friendly amenities (e.g., extra beds, breakfast, pool).
4. **Reviews**: Positive customer reviews and ratings.
5. **Room Size**: Adequate space for a family of 4.

### Step 3: Compare Available Options
Now, let's look for hotels that meet the criteria. Here are a few options that are commonly available in the Electronic City area:

1. **Hotel Royal Orchid**
   - Price: ₹5,500
   - Location: 5 km from Electronic City
   - Amenities: Family rooms, breakfast included, pool
   - Reviews: 4.2/5

2. **Treebo Trend Aashraya**
   - Price: ₹3,800
   - Location: 3 km from Electronic City
   - Amenities: Family rooms, breakfast included
   - Reviews: 4.0/5

3. **Radha Regent**
   - Price: ₹5,800
   - Location: 6 km from Electronic City
   - Amenities: Family rooms, breakfast included, pool
   - Reviews: 4.1/5

4. **FabHotel Elysian**
   - Price: ₹4,500
   - Location: 4 km from Electronic City
   - Amenities: Family rooms, breakfast included
   - Reviews: 4.0/5

### Step 4: Eliminate Unsuitable Choices
Now, let's evaluate the options based on our criteria:

- **Hotel Royal Orchid**: Meets all criteria but is slightly farther from Electronic City.
- **Treebo Trend Aashraya**: Best price and location, but lacks a pool.
- **Radha Regent**: Good amenities but slightly more expensive and farther.
- **FabHotel Elysian**: Good price and location, but reviews are slightly lower.

### Step 5: Recommend the Best Option
Based on the evaluation, I recommend **Treebo Trend Aashraya**.

### Step 6: Explain WHY
- **Affordability**: At ₹3,800, it is well within the budget.
- **Proximity**: Only 3 km from Electronic City, making it convenient for travel.
- **Family-Friendly**: Offers family rooms and includes breakfast, which is beneficial for a family of 4.
- **Good Reviews**: With a rating of 4.0/5, it has positive feedback from previous guests.

Overall, Treebo Trend Aashraya provides the best balance of price, location, and amenities for a family of 4 visiting Electronic City in Bangalore.
```

**Is this a "CoT Agent"?** `Technically, no.`
**This is:** `LLM + CoT Prompting` **because it only reasons.**

**What happens in a real Agent?** `Suppose you build your MakeMyTrip Booking Agent.`

```
User Request
       ↓
CoT : (Understand requirements)
       ↓
Browser Tool : (Search MakeMyTrip)
       ↓
CoT: (Filter hotels)
       ↓
Utility Function: (Price + Rating + Distance)
       ↓
Browser Tool: (Book hotel)
```

This becomes:

```
ReAct Agent
      +
Chain of Thought
      +
Utility-Based Decision Making
      +
Computer Use Agent (CUA)
```

**Key Difference** 

**`CoT`**

```
Think
 ↓
Think
 ↓
Think
 ↓
Answer
```

**ReAct + CoT**

```
Think
 ↓
Search Hotels
 ↓
Observe Results
 ↓
Think
 ↓
Filter Hotels
 ↓
Think
 ↓
Book Hotel
```

**CoT is often embedded inside a ReAct agent.**

Think of it this way:

- **CoT** = How the agent thinks
- **ReAct** = How the agent thinks and acts


**Hotel Booking Example**

**User Request:** `Find the best hotel in Bangalore for a family of 4 under ₹6,000 near Electronic City.`

## ReAct Agent with CoT

```
Question:
Find the best hotel in Bangalore for a family of 4
under ₹6,000 near Electronic City.
```

**Iteration 1**

```
Thought:
I need to understand the user's constraints.

CoT:
1. The hotel must be near Electronic City.
2. The hotel must accommodate 4 guests.
3. The price must be ≤ ₹6,000.
4. I should choose the best-rated option.

Action:
SearchHotels

Action Input:
{
    "location": "Electronic City, Bangalore",
    "guests": 4,
    "max_price": 6000
}

Observation:
[
    {
        "name": "Lemon Tree Hotel",
        "price": 5615,
        "rating": 7.8,
        "distance": "0.8 km"
    },
    {
        "name": "Hotel Presidency",
        "price": 4800,
        "rating": 8.3,
        "distance": "1.2 km"
    },
    {
        "name": "Treebo Celebrity Suites",
        "price": 3900,
        "rating": 8.0,
        "distance": "2.1 km"
    }
]
```

**Iteration 2**

```
Thought:
I should compare the remaining hotels.

CoT:
1. All hotels satisfy the budget requirement.
2. All can accommodate the family.
3. Hotel Presidency has the highest rating.
4. Lemon Tree is slightly closer.
5. Since the objective is "best hotel,"
   rating should take precedence.

Action:
None
```

**Final Answer**

```
Thought:
I now know the final answer.

CoT:
Hotel Presidency offers the best balance of
price and customer satisfaction while staying
within the specified constraints.

Final Answer:
I recommend Hotel Presidency in Electronic City
Phase II. It accommodates a family of four,
costs approximately ₹4,800 per night, and has
the highest rating (8.3/10) among the hotels
that satisfy your requirements.
```

## why will use `ReAct + CoT?` Whynot only `ReAct` which solve both `Reasoning + Action`

**In many cases, you can use only `ReAct`. You don't necessarily need `CoT` explicitly.**

The reason people say `"ReAct + CoT"` is because `ReAct's` `"Thought"` step can be enhanced using `CoT-style reasoning`.

**ReAct Alone**

Suppose the user asks:

`Find the best hotel in Bangalore for a family of 4 under ₹6,000 near Electronic City.`

A ReAct agent might do:

```
Thought: I need hotel information.

Action: SearchHotels

Observation: 3 hotels found.

Thought: Hotel Presidency has the highest rating.

Final Answer: Recommend Hotel Presidency.
```

- This works perfectly fine.

**ReAct + Explicit CoT**

Now imagine a more complex problem:

```
Find the best hotel considering budget, family needs, distance from Electronic City, breakfast availability, cancellation policy, and prioritize ratings over distance.
```

The agent's Thought could become:

```
Thought:
Let's think step by step.

1. Extract all constraints.
2. Filter hotels above ₹6,000.
3. Ensure they accommodate 4 guests.
4. Prefer hotels with breakfast included.
5. Prefer free cancellation.
6. Among remaining options, maximize rating.
7. Use distance only as a tie-breaker.

Action: SearchHotels
```

The **Action** part is still `ReAct`, but the **Thought** is more structured using `CoT`.

**Why not just use ReAct?**

**`Simple Tasks → ReAct is enough`**

```
Question
   ↓
Thought
   ↓
Action
   ↓
Observation
   ↓
Answer
```

**Examples:**

- Check weather
- Search hotels
- Query a database
- Create a GitHub issue


**`Complex Decision-Making → ReAct + CoT helps`**

```
Question
   ↓
CoT: (Reason step by step)
   ↓
Action
   ↓
Observation
   ↓
CoT: (Analyze observations)
   ↓
Answer
```

**Examples:**

- Travel planning with multiple constraints
- Root cause analysis
- Medical decision support
- Architecture recommendations


**The Important Point**

**ReAct already contains reasoning.** : `ReAct = Thought + Action + Observation`

However, the **quality of the Thought step** can vary:

**Weak Thought:** `Thought: Search hotels.`

**Strong CoT-style Thought:** 

```
Thought:
1. Budget ≤ ₹6,000.
2. Family of 4.
3. Near Electronic City.
4. Compare ratings.
5. Select the best option.
```

Both are **ReAct**. The second one simply uses **better reasoning**.

**In LangChain**

If you write: `agent = create_react_agent(...)`
you are already using **ReAct**.

If your prompt is: `Use the tools available to answer the question.`

then you have **plain ReAct**.

If your prompt is:

```
Before taking any action:
1. Think step by step.
2. Extract constraints.
3. Explain your reasoning.
4. Then use tools.
```

then you have **ReAct with CoT-enhanced reasoning**.

**Should you always combine them?** `No`.

| Scenario                    | ReAct Only | ReAct + CoT |
| --------------------------- | ---------- | ----------- |
| Weather lookup              | ✅          | ❌           |
| Simple hotel search         | ✅          | ❌           |
| GitHub PR creation          | ✅          | ❌           |
| Complex travel planning     | ⚠️         | ✅           |
| Architecture design         | ❌          | ✅           |
| Medical decision support    | ❌          | ✅           |
| Multi-criteria optimization | ❌          | ✅           |


**If the request is:**

```
Find the best family hotel considering budget, breakfast, cancellation policy, distance, ratings, and explain why it is the optimal choice.
```

**Use:**

```
ReAct
    +
CoT-style reasoning
```

**The takeaway**

```
CoT
↓
Improves reasoning quality

ReAct
↓
Provides the agent loop (Think → Act → Observe)

ReAct + CoT
↓
A ReAct agent whose Thoughts are more deliberate and structured
```

**Note:** `You don't need CoT if ReAct's default reasoning is sufficient. CoT is used when you want to make the reasoning inside ReAct more systematic and transparent for complex problems.`


## 1. CoT was invented to improve reasoning
Before CoT, LLMs typically did: `Question → Answer`

Researchers found that prompting the model with: `Let's think step by step.` 

improved performance:
```
Roger has 5 apples.
He buys 3 more.
5 + 3 = 8.

Answer: 8
```

Thus CoT was introduced.

## 2. CoT cannot interact with the world

Suppose the user asks: `What is the weather in Bangalore today?`

CoT can only do:

```
Thought:
I need the weather in Bangalore.

Thought:
I don't know today's weather.

Answer:
I cannot answer.
```


## 3. ReAct was invented to solve this limitation

Researchers said: `What if the model could` **reason AND use tools?**

Thus ReAct:

```
Thought:
I need weather information.

Action:
SearchWeather

Observation:
32°C

Final Answer:
The weather is 32°C.
```

## Why both exist?

- **CoT answers:** `How should the model reason?`
- **ReAct answers:** `How should the model reason while interacting with the environment?`

- **CoT:** `Brain only.` The agent sits in a room and thinks.
- **ReAct:** `Brain + Hands + Eyes.` The agent thinks, acts, observes, thinks again.

## Why not always use ReAct?

Because **tools are expensive**.

**Example 1**

```
Question:
What is 25 × 17?
```

**CoT:**

```
25 × 17
= 25 × (10 + 7)
= 250 + 175
= 425
Done
```

**ReAct:**

```
Thought:
I need a calculator.

Action:
Calculator

Observation:
425

Answer:
425

Done
Unnecessary overhead.
```

**Example 2**

```
Question:
What's the weather today?
```

**CoT:** 

```
I don't know.

Fails.

```

**ReAct:**

```
Thought:
I should search.

Action:
WeatherAPI

Observation:
32°C

Answer:
32°C
```

**Can ReAct replace CoT?** 
**Theoretically:** `Yes.`

You could write:

```
Thought:
Think step by step.
```

inside ReAct.


**Practically:** `No.`

Researchers still separate them because:

**CoT** `= Reasoning strategy`
**ReAct** `= Agent execution strategy`


## Why CoT if ReAct allows CoT-like reasoning?

**Because:**

1. **CoT was invented to improve reasoning without tools.**
2. **ReAct was invented to add tool usage to reasoning.**
3. **CoT is a reasoning strategy.**
4. **ReAct is an agent loop (Thought → Action → Observation).**
5. **A ReAct agent may or may not use CoT-style reasoning inside its Thoughts.**


**So, in modern systems:**

```
Simple reasoning task
→ CoT

Tool-using agent task
→ ReAct

Complex tool-using task
→ ReAct with richer CoT reasoning
```

## 1) CoT (Chain of Thought)

- **Purpose:** Reason through a problem step-by-step.
- **Tools:** ❌ No tools
- **Pattern:** `Think → Think → Think → Final Answer`

```python
"""
Example 1: Chain of Thought (CoT)

Purpose:
- Solve problems through step-by-step reasoning.
- No external tools are used.

Pattern:
Question
    ↓
Think
    ↓
Think
    ↓
Think
    ↓
Final Answer
"""

# ============================
# Section 1: Import Libraries
# ============================

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


# ============================
# Section 2: Initialize LLM
# ============================

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0
)


# ============================
# Section 3: Define CoT Prompt
# ============================

prompt = ChatPromptTemplate.from_template("""
You are an expert travel advisor.

Problem:
{question}

Break down the problem into numbered reasoning steps,
then provide the final answer.

Format:

Reasoning:
1.
2.
3.

Final Answer:
""")


# ============================
# Section 4: Create Chain
# ============================

chain = prompt | llm | StrOutputParser()


# ============================
# Section 5: Invoke
# ============================

response = chain.invoke({
    "question": """
Find the best family hotel considering budget under ₹6,000,
distance from Electronic City, breakfast availability,
and ratings.
"""
})


print(response)
```


## 2) ReAct (Reason → Act → Observe Loop)

- **Purpose:** Reason while interacting with tools.
- **Tools:** ✅ Yes
- **Pattern:**

```
Thought → Action → Observation
            ↓
Thought → Action → Observation
            ↓
Final Answer
```


```python
"""
Example 2: ReAct Agent

Purpose:
- Reason and use tools.
- The agent repeatedly performs:
  Thought → Action → Observation

Pattern:
Thought
    ↓
Action
    ↓
Observation
    ↓
Thought
    ↓
Action
    ↓
Observation
    ↓
Final Answer
"""

# ============================
# Section 1: Import Libraries
# ============================

import json

from langchain_openai import ChatOpenAI
from langchain.tools import Tool
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub


# ============================
# Section 2: Define Tool
# ============================

def search_hotels(query: str):
    """
    Simulated hotel search.
    Replace with Playwright or MakeMyTrip API.
    """

    hotels = [
        {
            "name": "Hotel Presidency",
            "price": 4800,
            "breakfast": True,
            "rating": 8.3,
            "distance_km": 1.2
        },
        {
            "name": "Lemon Tree Hotel",
            "price": 5615,
            "breakfast": True,
            "rating": 7.8,
            "distance_km": 0.8
        }
    ]

    return json.dumps(hotels)


tools = [
    Tool(
        name="SearchHotels",
        func=search_hotels,
        description="""
        Search hotels matching user constraints.
        Returns hotel details.
        """
    )
]


# ============================
# Section 3: Initialize LLM
# ============================

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0
)


# ============================
# Section 4: Load ReAct Prompt
# ============================

prompt = hub.pull("hwchase17/react")


# ============================
# Section 5: Create Agent
# ============================

agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)


executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)


# ============================
# Section 6: Invoke
# ============================

response = executor.invoke({
    "input": """
Find the best family hotel under ₹6,000
near Electronic City.
"""
})


print(response["output"])
```

## 3) CoT + ReAct

- **Purpose:** Use CoT-style reasoning inside ReAct thoughts.
- **Tools:** ✅ Yes
- **Pattern:**

```
Think → Think → Think
          ↓
       Action
          ↓
      Observation
          ↓
Think → Think
          ↓
       Action
          ↓
      Observation
          ↓
    Final Answer
```

```python
"""
Example 3: CoT + ReAct Agent

Purpose:
- Use structured reasoning BEFORE actions.
- Use ReAct loop for tool interaction.

Pattern:

(Think → Think → Think)
            ↓
         Action
            ↓
       Observation
            ↓
(Think → Think)
            ↓
         Action
            ↓
       Observation
            ↓
      Final Answer
"""

# ============================
# Section 1: Import Libraries
# ============================

import json

from langchain_openai import ChatOpenAI
from langchain.tools import Tool
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub


# ============================
# Section 2: Define Tool
# ============================

def search_hotels(query: str):

    hotels = [
        {
            "name": "Hotel Presidency",
            "price": 4800,
            "breakfast": True,
            "free_cancellation": True,
            "rating": 8.3,
            "distance_km": 1.2
        },
        {
            "name": "Lemon Tree Hotel",
            "price": 5615,
            "breakfast": True,
            "free_cancellation": False,
            "rating": 7.8,
            "distance_km": 0.8
        }
    ]

    return json.dumps(hotels)


tools = [
    Tool(
        name="SearchHotels",
        func=search_hotels,
        description="Search hotels."
    )
]


# ============================
# Section 3: Initialize LLM
# ============================

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0
)


# ============================
# Section 4: Customize ReAct
# with CoT Instructions
# ============================

base_prompt = hub.pull("hwchase17/react")

prompt = base_prompt.partial(
    instructions="""
Before taking an action:

1. Extract user constraints.
2. List evaluation criteria.
3. Explain why the next action is needed.
4. Use tools to gather information.
5. Compare alternatives carefully.
6. Recommend the optimal choice.

Use the Thought → Action → Observation format.
"""
)


# ============================
# Section 5: Create Agent
# ============================

agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)


executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)


# ============================
# Section 6: Invoke
# ============================

response = executor.invoke({
    "input": """
Find the best family hotel considering:

- Budget under ₹6,000
- Breakfast availability
- Free cancellation
- Distance from Electronic City
- Ratings

Explain why it is the optimal choice.
"""
})


print(response["output"])
```

**Summary:**

| Type            | Tools | Execution Pattern                              |
| --------------- | ----- | ---------------------------------------------- |
| **CoT**         | ❌     | `Think → Think → Think → Answer`               |
| **ReAct**       | ✅     | `Thought → Action → Observation → ...`         |
| **CoT + ReAct** | ✅     | `(Think → Think) → Action → Observation → ...` |


## Generic CoT

**You tell the LLM:** `Think step by step.` or `Let's think step by step.`

- The LLM decides how to reason.

**Example:**

**Prompt:**

```
prompt = """
Question:
Find the best family hotel under ₹6,000 near Electronic City.

Think step by step.
"""
```

**LLM Output (Example)**

```
Reasoning:

1. Determine the budget requirement.
2. Identify the location requirement.
3. Compare hotels within budget.
4. Evaluate ratings.
5. Recommend the best option.

Final Answer:
Hotel Presidency.
```

**Characteristics:**

| Feature                    | Generic CoT |
| -------------------------- | ----------- |
| Reasoning steps defined by | LLM         |
| Flexibility                | High        |
| Consistency                | Low         |
| Prompt engineering effort  | Low         |
| Enterprise suitability     | Medium      |




## Structured CoT: `You tell the LLM exactly how to reason.`

**Example:**

**Prompt:**

```
prompt = """
Question:
Find the best family hotel under ₹6,000 near Electronic City.

Follow these steps:

1. Extract user constraints.
2. Filter hotels by budget.
3. Verify family suitability.
4. Check breakfast availability.
5. Compare ratings.
6. Explain why the recommendation is optimal.
"""
```

**LLM Output (Example)**

```
Step 1: User Constraints
- Budget ≤ ₹6,000
- Family of 4
- Near Electronic City

Step 2: Budget Filtering
- Hotel A: ₹4,800
- Hotel B: ₹5,600

Step 3: Family Suitability
- Both hotels support families.

Step 4: Breakfast Availability
- Only Hotel A includes breakfast.

Step 5: Ratings
- Hotel A: 8.3
- Hotel B: 7.8

Step 6: Recommendation
Hotel A is the optimal choice because...
```

**Characteristics:**

| Feature                    | Structured CoT |
| -------------------------- | -------------- |
| Reasoning steps defined by | Developer      |
| Flexibility                | Lower          |
| Consistency                | High           |
| Prompt engineering effort  | Higher         |
| Enterprise suitability     | Very High      |


## Visual Comparison

**Generic CoT**

```
User Question
      ↓
Think step by step
      ↓
LLM decides:
  Step A
  Step B
  Step C
      ↓
Answer
```

**Structured CoT**

```
User Question
      ↓
Developer-defined framework:
  Step 1
  Step 2
  Step 3
      ↓
LLM executes framework
      ↓
Answer
```

**Suppose the user asks:** `Find the best family hotel under ₹6,000.`

**Generic CoT Run #1**

```
1. Budget analysis
2. Rating comparison
3. Distance comparison
```

**Generic CoT Run #2**

```
1. Family suitability
2. Breakfast availability
3. Budget analysis
```

- `The steps may change.`

**Structured CoT**

```
1. Extract constraints
2. Filter by budget
3. Check family suitability
4. Check breakfast
5. Compare ratings
```

- `The steps remain the same every time.`

**Which one should you use?**

**Generic CoT**

Use when:

```
✓ General Q&A
✓ Research tasks
✓ Exploration
✓ Rapid prototyping
```

**Structured CoT**

Use when:

```
✓ Enterprise agents
✓ Compliance workflows
✓ Healthcare applications
✓ Travel recommendation systems
✓ DevOps root cause analysis
✓ Auditable decision making
```

## LangChain Examples

**Generic CoT:**

```Python
prompt = ChatPromptTemplate.from_template("""
Question:
{question}

Let's think step by step.
""")
```

**Structured CoT**

```Python
prompt = ChatPromptTemplate.from_template("""
Question:
{question}

Use this reasoning framework:

1. Extract constraints.
2. Compare alternatives.
3. Evaluate trade-offs.
4. Recommend the best option.
""")
```

**Final Rule:**

- **Generic CoT:** = `LLM decides HOW to think.`
- **Structured CoT:** = `Developer decides HOW the LLM should think.`


## Tree of Thoughts (ToT)

**Idea**

Instead of following **one reasoning path (CoT)**:

```
Question
    ↓
Think
    ↓
Think
    ↓
Answer
```

ToT explores **multiple reasoning paths**:

```
                 Question
                     │
          ┌──────────┼──────────┐
          │          │          │
       Thought-1  Thought-2  Thought-3
          │          │          │
      Evaluate   Evaluate   Evaluate
          │          │          │
          └──────────┼──────────┘
                     │
               Best Answer
```

**Hotel Example**

User asks: `Find the best family hotel under ₹6,000 near Electronic City.`

**Branch 1 (Price Optimized)**

```
Hotel A: ₹4,000
Hotel B: ₹5,500

Choose Hotel A
```

**Branch 2 (Rating Optimized)**

```
Hotel A: 8.1
Hotel B: 8.8

Choose Hotel B
```

**Branch 3 (Family Friendly)**

```
Hotel A: Breakfast
Hotel B: Breakfast + Free Cancellation

Choose Hotel B
```

**Evaluation:**

```
Price Score
+
Rating Score
+
Family Score
      ↓
Hotel B
```

**ToT Architecture**

```
Generate Multiple Thoughts
            ↓
Evaluate Thoughts
            ↓
Select Best Thought
            ↓
Answer
```

## LangChain ToT Example

```python
"""
Tree of Thoughts (ToT)

Goal:
Generate multiple reasoning paths and choose the best one.
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0
)

question = """
Find the best family hotel under ₹6,000
near Electronic City.
"""

# =====================================================
# Step 1: Generate multiple reasoning paths
# =====================================================

generator_prompt = ChatPromptTemplate.from_template("""
Question:
{question}

Generate 3 different approaches to solve this problem.

Approach 1: Optimize for lowest price.
Approach 2: Optimize for highest rating.
Approach 3: Optimize for family friendliness.

For each approach:
- Explain reasoning
- Recommend a hotel
""")

generator_chain = generator_prompt | llm

candidate_solutions = generator_chain.invoke({
    "question": question
})

print("\n===== Candidate Solutions =====")
print(candidate_solutions.content)


# =====================================================
# Step 2: Evaluate the approaches
# =====================================================

evaluator_prompt = ChatPromptTemplate.from_template("""
Question:
{question}

Candidate Solutions:
{solutions}

Evaluate all approaches considering:

1. Budget
2. Ratings
3. Family suitability

Choose the best approach and explain why.
""")

evaluator_chain = evaluator_prompt | llm

final_answer = evaluator_chain.invoke({
    "question": question,
    "solutions": candidate_solutions.content
})

print("\n===== Final Recommendation =====")
print(final_answer.content)
```

## ReAct + ToT

This is where things become interesting.

**Idea**

- Use **ToT for planning**, then **ReAct for execution**.

```
User Request
      ↓
ToT
(Generate Multiple Plans)
      ↓
Evaluate Plans
      ↓
Choose Best Plan
      ↓
ReAct
(Execute the Plan using Tools)
```

**Hotel Example**

User: `Find the best family hotel considering budget, breakfast, ratings, and cancellation policy.`

**ToT Phase**

Generate plans:

```
Plan 1:
Prioritize Price

Plan 2:
Prioritize Ratings

Plan 3:
Prioritize Family Needs
```

Evaluate: `Choose Plan 3`

**ReAct Phase**

```
Thought:
Need hotel information.

Action:
SearchHotels

Observation:
Hotels found.

Thought:
Need cancellation policy.

Action:
CheckCancellation

Observation:
Free cancellation available.

Final Answer:
Recommend Hotel B.
```

## ReAct + ToT Architecture

```
          User
            ↓
     Tree of Thoughts
            ↓
     Generate Plans
            ↓
      Evaluate Plans
            ↓
      Best Strategy
            ↓
           ReAct
     Thought → Action
             ↓
        Observation
             ↓
         Final Answer
```

## LangChain ReAct + ToT Example

```python
"""
ReAct + ToT

ToT:
    Generate multiple strategies.

ReAct:
    Execute the selected strategy using tools.
"""

import json

from langchain_openai import ChatOpenAI
from langchain.tools import Tool
from langchain.agents import create_react_agent, AgentExecutor
from langchain import hub
from langchain_core.prompts import ChatPromptTemplate

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0
)

# =====================================================
# Step 1: ToT Planning Phase
# =====================================================

planning_prompt = ChatPromptTemplate.from_template("""
Question:
{question}

Generate 3 plans.

Plan 1:
Optimize for lowest price.

Plan 2:
Optimize for highest ratings.

Plan 3:
Optimize for family experience
(breakfast + cancellation).

Choose the best plan and explain why.
""")

planning_chain = planning_prompt | llm

question = """
Find the best family hotel under ₹6,000
near Electronic City considering breakfast,
ratings and cancellation policy.
"""

selected_plan = planning_chain.invoke({
    "question": question
})

print("\n===== Selected Plan =====")
print(selected_plan.content)


# =====================================================
# Step 2: ReAct Tool
# =====================================================

def search_hotels(query: str):

    hotels = [
        {
            "name": "Hotel Presidency",
            "price": 4800,
            "breakfast": True,
            "free_cancellation": True,
            "rating": 8.3
        },
        {
            "name": "Lemon Tree",
            "price": 5615,
            "breakfast": True,
            "free_cancellation": False,
            "rating": 7.8
        }
    ]

    return json.dumps(hotels)


tools = [
    Tool(
        name="SearchHotels",
        func=search_hotels,
        description="Search available hotels."
    )
]


# =====================================================
# Step 3: ReAct Execution Phase
# =====================================================

react_prompt = hub.pull("hwchase17/react")

agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=react_prompt
)

executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)


# =====================================================
# Step 4: Execute Selected Plan
# =====================================================

response = executor.invoke({
    "input": f"""
User Request:
{question}

Follow this strategy:

{selected_plan.content}

Use the available tools to make the recommendation.
"""
})

print("\n===== Final Recommendation =====")
print(response["output"])
```

## Summary

| Pattern         | Purpose                                                       |
| --------------- | ------------------------------------------------------------- |
| **CoT**         | Explore one reasoning path                                    |
| **ToT**         | Explore multiple reasoning paths                              |
| **ReAct**       | Reason while using tools                                      |
| **ReAct + ToT** | Explore multiple plans, then execute the best one using tools |


## Mental Model

```
CoT
=
One person thinking.

ToT
=
A team brainstorming multiple solutions.

ReAct
=
A person thinking while using tools.

ReAct + ToT
=
A team chooses the best strategy,
then one person executes it using tools.
```

For `travel planning`, `architecture design`, `and strategic decision-making`, `ToT` is extremely useful.

For `tool-using agents` (`GitHub`, `MakeMyTrip`, `ServiceNow`), `ReAct + ToT` is a powerful combination:

- **ToT** → decide what to do,
- **ReAct** → decide how to do it.


**The idea is:**

```
LangGraph = Orchestration
LangChain = LLM + Prompts
ToT = Generate → Evaluate → Select Best Thought
```

**Architecture:**

```
User Question
      ↓
Generate Thought 1
Generate Thought 2
Generate Thought 3
      ↓
Evaluate Thoughts
      ↓
Select Best Thought
      ↓
Final Answer
```

**LangGraph + LangChain ToT example.**

```python
"""
Tree of Thoughts (ToT) using LangGraph + LangChain

Use Case:
Find the best family hotel under ₹6,000 near Electronic City.

ToT Workflow:
1. Generate multiple reasoning paths.
2. Evaluate the reasoning paths.
3. Select the best reasoning path.
4. Return the final recommendation.
"""

# ==========================================================
# Section 1: Imports
# ==========================================================

from typing import TypedDict

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from langgraph.graph import StateGraph, END


# ==========================================================
# Section 2: Define State
# ==========================================================

class ToTState(TypedDict):
    question: str
    thoughts: str
    evaluation: str
    final_answer: str


# ==========================================================
# Section 3: Initialize LLM
# ==========================================================

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0
)


# ==========================================================
# Section 4: Generate Thoughts Node
# ==========================================================

generate_prompt = ChatPromptTemplate.from_template("""
Question:
{question}

Generate 3 different reasoning paths.

Thought 1:
Optimize for lowest price.

Thought 2:
Optimize for highest ratings.

Thought 3:
Optimize for family friendliness
(breakfast + cancellation).

For each thought:
- Explain the reasoning.
- Recommend a hotel.
""")


def generate_thoughts(state: ToTState):

    chain = generate_prompt | llm

    response = chain.invoke({
        "question": state["question"]
    })

    return {
        "thoughts": response.content
    }


# ==========================================================
# Section 5: Evaluate Thoughts Node
# ==========================================================

evaluate_prompt = ChatPromptTemplate.from_template("""
Question:
{question}

Candidate Thoughts:
{thoughts}

Evaluate each thought considering:

1. Budget
2. Ratings
3. Breakfast availability
4. Cancellation policy
5. Family suitability

Identify the BEST thought and explain WHY.
""")


def evaluate_thoughts(state: ToTState):

    chain = evaluate_prompt | llm

    response = chain.invoke({
        "question": state["question"],
        "thoughts": state["thoughts"]
    })

    return {
        "evaluation": response.content
    }


# ==========================================================
# Section 6: Final Recommendation Node
# ==========================================================

final_prompt = ChatPromptTemplate.from_template("""
Question:
{question}

Evaluation:
{evaluation}

Provide the final recommendation.

Format:

Recommended Hotel:
...

Reason:
...
""")


def generate_final_answer(state: ToTState):

    chain = final_prompt | llm

    response = chain.invoke({
        "question": state["question"],
        "evaluation": state["evaluation"]
    })

    return {
        "final_answer": response.content
    }


# ==========================================================
# Section 7: Build LangGraph Workflow
# ==========================================================

workflow = StateGraph(ToTState)

workflow.add_node("generate_thoughts", generate_thoughts)

workflow.add_node("evaluate_thoughts", evaluate_thoughts)

workflow.add_node("final_answer", generate_final_answer)


workflow.set_entry_point("generate_thoughts")

workflow.add_edge(
    "generate_thoughts",
    "evaluate_thoughts"
)

workflow.add_edge(
    "evaluate_thoughts",
    "final_answer"
)

workflow.add_edge(
    "final_answer",
    END
)


graph = workflow.compile()


# ==========================================================
# Section 8: Execute
# ==========================================================

response = graph.invoke({
    "question": """
    Find the best family hotel under ₹6,000
    near Electronic City considering:

    - Breakfast availability
    - Cancellation policy
    - Ratings
    """
})


# ==========================================================
# Section 9: Print Results
# ==========================================================

print("\n========== THOUGHTS ==========")
print(response["thoughts"])

print("\n========== EVALUATION ==========")
print(response["evaluation"])

print("\n========== FINAL ANSWER ==========")
print(response["final_answer"])
```

## Difference between Generic ToT and Structured ToT.

**1. Generic ToT**

LLM generates branches.

```
Question
    ↓
LLM
    ↓
Branch 1
Branch 2
Branch 3
```

Prompt: `Generate 3 different reasoning paths.`


**2. Structured ToT**

Developer generates branch templates.

```
Question
    ↓
Developer-defined Branches
    ↓
LLM executes them
```

**Prompt:**

```
Thought 1: Optimize for price.
Thought 2: Optimize for ratings.
Thought 3: Optimize for amenities.
```

**Comparison:**

| Feature                | Generic ToT | Structured ToT |
| ---------------------- | ----------- | -------------- |
| Who decides branches?  | LLM         | Developer      |
| Flexibility            | High        | Medium         |
| Consistency            | Low         | High           |
| Auditability           | Low         | High           |
| Enterprise suitability | Medium      | High           |
| Research suitability   | High        | Medium         |


## GoT (Graph of Thoughts)

Thoughts are **nodes in a graph**.

Thoughts can:

- Branch ✅
- Merge ✅
- Reuse previous thoughts ✅
- Build upon other thoughts ✅


**GoT Architecture**

```
               Problem
                  │
                  ▼
          Candidate Hotels
             /       \
            /         \
       Price         Ratings
          \            /
           \          /
      Family Suitability
              │
              ▼
      Cancellation Policy
              │
              ▼
        Final Recommendation
```

Notice: `Candidate Hotels`. is reused by multiple reasoning nodes.


**Example**

User asks: `Find the best family hotel under ₹6,000 near Electronic City.`

**Node 1:** `Generate candidate hotels.`

Output:

```
Hotel A
Hotel B
Hotel C
```

**Node 2:**

Uses Node 1 output. `Analyze price.`

**Node 3:**

Uses Node 1 output. `Analyze ratings.`

**Node 4:**

Uses Node 1 output. `Analyze breakfast availability.`

**Node 5:**

Uses outputs of Nodes 2, 3, and 4. `Determine family suitability.`

**Node 6:**

Recommend best hotel.


**Why GoT?**

Because many problems are **not trees**.

Example: `Medical Diagnosis`

```
Symptoms
    │
    ├── MRI
    ├── Blood Tests
    ├── Family History
    │
    ▼
Risk Assessment
    │
    ▼
Treatment Recommendation
```

Information gets reused.

**GoT vs ToT**

| Feature                 | ToT     | GoT   |
| ----------------------- | ------- | ----- |
| Branching               | ✅       | ✅     |
| Reuse previous thoughts | ❌       | ✅     |
| Merge branches          | Limited | ✅     |
| Structure               | Tree    | Graph |
| Complexity              | Medium  | High  |


**ReAct + GoT**

This is where it gets interesting.

**Idea**

- Use **GoT for reasoning**.
- Use **ReAct for interacting with tools**.

**Architecture**

```
                      User
                        │
                        ▼
                Graph of Thoughts
                        │
      ┌─────────────────┼─────────────────┐
      │                 │                 │
      ▼                 ▼                 ▼
Search Hotels      Analyze Price     Analyze Ratings
      │                 │                 │
      ▼                 ▼                 ▼
Check Breakfast   Check Distance   Check Cancellation
      │                 │                 │
      └─────────────────┼─────────────────┘
                        │
                        ▼
                 Final Decision
```

Every node can execute:

```
Thought
   ↓
Action
   ↓
Observation
```

**Example**

**Node:** `Search Hotels`

ReAct:

```
Thought:
I need candidate hotels.

Action:
SearchHotels

Observation:
Hotel A, B, C
```

**Node:** `Price Analysis`

**ReAct:**

```
Thought:
I should analyze affordability.

Action:
CalculateBudgetFit

Observation:
Hotel A and B qualify.
```

**Node:** `Breakfast Analysis`

**ReAct:**

```
Thought:
Family travelers may value breakfast.

Action:
CheckAmenities

Observation:
Hotel B includes breakfast.
```

**Node:** `Cancellation Analysis`

**ReAct:**

```
Thought:
Free cancellation improves flexibility.

Action:
CheckCancellation

Observation:
Hotel B allows cancellation.
```

**Final Node:**

GoT merges all information.

```
Price Node
      │
Ratings Node
      │
Breakfast Node
      │
Cancellation Node
      ▼
Recommendation:
Hotel B
```

## GoT vs ReAct + GoT

**GoT** `Pure reasoning.`

```
Graph
 ↓
Reason
 ↓
Answer
```

**ReAct + GoT**

Reasoning graph with tools.

```
Graph Node
     ↓
Thought
     ↓
Action
     ↓
Observation
     ↓
Updated Graph
```

**Comparison**

| Pattern     | Tools    | Memory | Structure     |
| ----------- | -------- | ------ | ------------- |
| CoT         | ❌        | ❌      | Chain         |
| ToT         | ❌        | ❌      | Tree          |
| GoT         | ❌        | ❌      | Graph         |
| ReAct       | ✅        | ❌      | Loop          |
| ReAct + GoT | ✅        | ❌      | Graph + Loops |
| Reflexion   | Optional | ✅      | Loop + Memory |


## Mental Models

- **CoT:** `One road.`
- **ToT:** `Many roads.`
- **GoT:** `A city map where roads connect and reconnect.`
- **ReAct:** `A traveler who thinks while using tools.`
- **ReAct + GoT:** `A team of travelers using tools while sharing information through a network.`


## Enterprise Examples

**GoT:**

```
Digital Twin
Research Agent
Knowledge Graph QA
Medical Diagnosis
```

**ReAct + GoT:**

```
Travel Booking Agent
IT Incident Resolution
Cybersecurity Investigation
Autonomous Research Agent
Neuro Digital Twin
```

## Final Summary

```
CoT
= One reasoning path.

ToT
= Multiple independent reasoning paths.

GoT
= Interconnected reasoning graph.

ReAct
= Think → Act → Observe.

ReAct + GoT
= Multiple interconnected reasoning nodes,
  each capable of using tools through
  Thought → Action → Observation loops.
```

So, ToT explores alternatives, whereas GoT models dependencies and information sharing between thoughts. That's why GoT is often considered the most sophisticated pure reasoning pattern before introducing memory (Reflexion).


## Reflection and Reflexion

```
CoT  →  ToT  →  GoT
 ↓       ↓       ↓
Reason  Reason  Reason

Reflection
 ↓
Improve current answer

Reflexion
 ↓
Learn from mistakes across tasks
```

## 1. Reflection

**Definition**

**Reflection is the process of critiquing and improving the current answer within the same task.**

**Architecture**

```
Problem
   ↓
Generate Answer
   ↓
Reflect / Critique
   ↓
Improve Answer
   ↓
Final Answer
```

**Hotel Example**

User:

`Find the best family hotel under ₹6,000.`

**Initial Answer:** `Recommend Hotel A.`


**Reflection:**

```
Did I consider breakfast?
→ No

Did I consider cancellation policy?
→ No

Did I consider ratings?
→ Yes
```

**Improved Answer:**

```
Recommend Hotel B because:

✓ Under budget
✓ Includes breakfast
✓ Free cancellation
✓ Highest family rating
```

**Reflection Loop:**

```
Generate
   ↓
Critique
   ↓
Revise
```

**LangGraph Architecture:**

```
          User
            │
            ▼
      Generate Answer
            │
            ▼
         Reflection
            │
            ▼
      Revise Answer
            │
            ▼
            END
```

**Reflection Code (LangGraph):**

```
Generate Node
    ↓
Reflection Node
    ↓
Revision Node
```

**Reflection Characteristics:**

| Feature               | Reflection |
| --------------------- | ---------- |
| Improves current task | ✅          |
| Uses memory           | ❌          |
| Learns across tasks   | ❌          |
| Self-critique         | ✅          |


**Mental Model**

```
"Did I do a good job?"

If No:
    Improve it.
```

## 2. Reflexion

Introduced in the **Reflexion paper (2023)**.

**Definition:**

```**Reflexion extends Reflection by storing lessons learned in memory and applying them to future tasks.**```

**Architecture:**

```
Task
  ↓
Generate
  ↓
Evaluate
  ↓
Reflect
  ↓
Store Lessons
  ↓
Memory
  ↓
Future Tasks
```

**Hotel Example**

**Day 1:**

**User:** `Find the best family hotel.`
**Agent:** `Recommend Hotel A.`
**User:** `I prefer free cancellation.`

**Reflexion:**

```
Lesson Learned:

Family travelers often value
free cancellation policies.
```

**Memory:**

```
Store:

"Prioritize cancellation policies
for family travel recommendations."
```

**Day 30:**

**User:** `Find the best family hotel.`
**Agent retrieves memory:** 
```
Past Lesson:

Families value cancellation flexibility.
```

**Recommendation:**
```
Recommend Hotel B because it
offers free cancellation.
```

**Reflexion Loop:**

```
Generate
   ↓
Evaluate
   ↓
Reflect
   ↓
Store Memory
   ↓
Retry
```

**LangGraph Architecture:**

```
            User
              │
              ▼
         Generate
              │
              ▼
         Evaluate
              │
              ▼
         Reflection
              │
              ▼
         Store Memory
              │
              ▼
         Retry Task
              │
              ▼
             END
```

**Reflexion Code Structure:**

```
Generate Node
    ↓
Evaluate Node
    ↓
Reflection Node
    ↓
Memory Node
    ↓
Retry Node
```

**Reflection vs Reflexion**

| Feature                | Reflection | Reflexion |
| ---------------------- | ---------- | --------- |
| Improve current answer | ✅          | ✅         |
| Self-critique          | ✅          | ✅         |
| Memory                 | ❌          | ✅         |
| Learn across tasks     | ❌          | ✅         |
| Retry after failure    | Optional   | ✅         |
| Long-term adaptation   | ❌          | ✅         |


## Visual Comparison

**Reflection:**

```
Task
 ↓
Answer
 ↓
Critique
 ↓
Improve
 ↓
Done
```

**Reflexion:**
```
Task
 ↓
Answer
 ↓
Critique
 ↓
Store Lesson
 ↓
Memory
 ↓
Next Task
 ↓
Better Answer
```

**Real Examples:**

**Reflection:**

**Code Review Agent**

```
Generate Code
     ↓
Find Bugs
     ↓
Improve Code
```

**Reflexion:**

**Coding Assistant**

```
Generate Code
     ↓
Tests Fail
     ↓
Learn Failure Pattern
     ↓
Remember Fix Strategy
     ↓
Use Strategy Next Time
```

**Reflection:**

**Architecture Review:**

```
Initial Design
     ↓
Security Review
     ↓
Improve Design
```

**Reflexion:**

**Neuro Digital Twin:**

```
Prediction
    ↓
Actual Outcome
    ↓
Learn Mistake
    ↓
Update Future Predictions
```

**Classification:**

```
Reasoning Patterns
│
├── CoT
├── ToT
├── GoT
└── Reflection
       ↓
Current Task Only

Learning Patterns
│
└── Reflexion
       ↓
Across Tasks Using Memory
```

**Mental Models:**

**Reflection:** `"Let me improve THIS answer."`

**Reflexion:** 

```
"Let me remember this mistake so I don't
make it AGAIN."
```

**Evolution:**

```
CoT
 ↓
Reflection
 ↓
Reflexion
```

- **CoT:** Think before answering.
- **Reflection:** Improve the current answer.
- **Reflexion:** Learn from mistakes and improve future performance.


**One-Line Summary:**
```Reflection is short-term self-correction within the current task, whereas Reflexion is long-term self-improvement through memory and learning across tasks```.


**Final Mental Map:**

```
Pure Reasoning
├── CoT
├── ToT
├── GoT
└── Reflection

Reasoning + Action
└── ReAct

Reasoning + Memory
└── Reflexion
```


# Planning & Execution Patterns, ReWOO, and LLM Compiler.

Think of it this way:

```
Reasoning Patterns
↓
How should the model THINK?

Planning & Execution Patterns
↓
How should the agent PLAN and EXECUTE work?
```

**Big Picture:**

```
Agentic AI Patterns
│
├── Reasoning Patterns
│   ├── CoT
│   ├── ToT
│   ├── GoT
│   ├── Reflection
│   └── Reflexion
│
└── Planning & Execution Patterns
    ├── Plan-and-Execute
    ├── ReWOO
    └── LLM Compiler
```

## 1. Plan-and-Execute

Introduced because ReAct can be inefficient.

**Problem with ReAct:**

```
Thought
↓
Action
↓
Observation
↓
Thought
↓
Action
↓
Observation
↓
...
```

LLM is invoked repeatedly.

**Plan-and-Execute Idea:**

**Separate:**

```
Planning
     ↓
Execution
```

**Architecture:**

```
User Goal
     ↓
Planner
     ↓
Plan
     ↓
Executor
     ↓
Final Answer
```

**Hotel Example:**

User: `Find the best family hotel under ₹6,000.`

**Planner:**

```
Plan:

1. Search hotels.
2. Filter by budget.
3. Check breakfast.
4. Check cancellation.
5. Compare ratings.
6. Recommend best hotel.
```

**Executor:**

```
Execute Step 1
↓
Execute Step 2
↓
Execute Step 3
↓
...
```

**Characteristics:**

| Feature           | Plan-and-Execute |
| ----------------- | ---------------- |
| Explicit Planning | ✅                |
| Tool Usage        | ✅                |
| Replanning        | Limited          |
| Parallelism       | ❌                |


## 2. ReWOO

**Reasoning Without Observation**

**Problem with ReAct**

ReAct:

```
Think
↓
Act
↓
Observe
↓
Think
↓
Act
↓
Observe
```

Many LLM calls.

**ReWOO Idea:**

Reason once.

Then execute.

**Architecture:**

```
User Goal
     ↓
Planner
     ↓
Plan with Variables
     ↓
Worker Executes
     ↓
Final Answer
```

**Hotel Example:**

Planner generates:

```
Plan:

E1 = SearchHotels(Electronic City)

E2 = CheckBreakfast(#E1)

E3 = CheckCancellation(#E1)

E4 = CompareRatings(#E1)

Solve:
Recommend best hotel.
```

**Executor:**

```
Run E1
Run E2
Run E3
Run E4
```

**Final Solver:**

```
Combine E1–E4
↓
Answer
```

**Characteristics:**

| Feature                     | ReWOO |
| --------------------------- | ----- |
| Planning                    | ✅     |
| Variables                   | ✅     |
| Tool Usage                  | ✅     |
| Observation after each step | ❌     |
| Efficiency                  | High  |


**ReWOO Flow:**

```
Plan
 ↓
E1
 ↓
E2
 ↓
E3
 ↓
Solve
```

## 3. LLM Compiler

Inspired by traditional compilers.

**Idea**

Compile the problem into an execution graph.
Optimize execution.
Execute efficiently.

**Architecture:**

```
User Goal
     ↓
Compiler
     ↓
Execution DAG
     ↓
Parallel Execution
     ↓
Aggregation
     ↓
Answer
```

**Hotel Example:**

Compiler generates:

```
Task Graph:

Search Hotels
      ↓
 ┌────┼────┬────┐
 ↓    ↓    ↓    ↓
Price Breakfast Ratings Cancellation
 └────┼────┴────┘
      ↓
Recommendation
```

**Execution:**

```
Breakfast Check
Price Check
Ratings Check

Run in parallel.
```

**Aggregation:** `Merge results.`

**Characteristics**

| Feature            | LLM Compiler |
| ------------------ | ------------ |
| Planning           | ✅            |
| Optimization       | ✅            |
| Parallel Execution | ✅            |
| DAG Execution      | ✅            |
| Efficiency         | Very High    |


## Comparison

| Feature          | ReAct | Plan-and-Execute | ReWOO   | LLM Compiler |
| ---------------- | ----- | ---------------- | ------- | ------------ |
| Explicit Planner | ❌     | ✅                | ✅       | ✅            |
| Tool Usage       | ✅     | ✅                | ✅       | ✅            |
| Observation Loop | ✅     | Optional         | ❌       | ❌            |
| Variables        | ❌     | ❌                | ✅       | ✅            |
| Parallelism      | ❌     | ❌                | Limited | ✅            |
| DAG Execution    | ❌     | ❌                | ❌       | ✅            |
| Efficiency       | Low   | Medium           | High    | Very High    |


**Mental Models:**

**ReAct:** `Think while doing.`

**Plan-and-Execute:**

```
Plan first.
Execute later.
```

**ReWOO:**

```
Plan once.
Use variables.
Execute efficiently.
```

**LLM Compiler:**

```
Compile work into an optimized DAG.
Execute in parallel.
```

**Evolution:**

```
ReAct
  ↓
Plan-and-Execute
  ↓
ReWOO
  ↓
LLM Compiler
```

**When to Use?**

**ReAct**

```
Dynamic environments.

Unknown paths.

Need observations.
```

**Plan-and-Execute**

```
Long workflows.

Moderate complexity.
```

**ReWOO:**

```
Many dependent tool calls.

Need fewer LLM invocations.
```

**LLM Compiler:**

```
Complex enterprise workflows.

Parallel execution.

Maximum efficiency.
```

## Travel Agent Example

**ReAct:**

```
Search
↓
Observe
↓
Check Breakfast
↓
Observe
```

**Plan-and-Execute:**

```
Plan all steps
↓
Execute sequentially
```

**ReWOO:**

```
E1 SearchHotels
E2 CheckBreakfast(#E1)
E3 Ratings(#E1)
Solve
```

**LLM Compiler:**

```
SearchHotels
    ↓
 ┌──┼───┬───┐
 ↓  ↓   ↓   ↓
Price Ratings Breakfast Cancellation
    ↓
Recommendation
```

**Final Mental Map:**

```
Reasoning
├── CoT
├── ToT
├── GoT
├── Reflection
└── Reflexion

Execution
├── ReAct
├── Plan-and-Execute
├── ReWOO
└── LLM Compiler
```

## what's the difference ReAct, ReAct + CoT/ToT/GoT vs Plan-and-Execute?

`ReAct` Observations `trigger reasoning after every step`.

```
Observation
     ↓
Should I change my approach?
     ↓
Reason again
```

`Plan-and-Execute` Observations primarily support `execution`.

```
Observation
     ↓
Can I execute the next planned step?
     ↓
Yes → Continue
No  → Re-plan
```

**ReAct + CoT:**

```
Thought:
1. Search hotels
2. Filter budget
3. Check breakfast

Action:
SearchHotels

Observation:
Only 2 hotels found.

Thought:
Actually, ratings matter more now.
Let's check ratings first.

Action:
CheckRatings
```

Notice: `The original reasoning changed.`


**Plan-and-Execute:**

**Planner:**

```
1. Search hotels
2. Filter budget
3. Check breakfast
4. Check ratings
```

**Executor:**

```
Execute Step 1

Observation:
2 hotels found

Execute Step 2

Observation:
1 hotel remains

Execute Step 3
```

Notice: `Observations do NOT automatically change the plan.`

## What if execution fails?

Suppose:

```
Observation:
No hotels include breakfast.
```

**ReAct**

```
Thought:
I'll relax the breakfast constraint.
```

Continues naturally.

**Plan-and-Execute**

Typically:

```
Executor:
Cannot continue.

Request re-planning.
```

Then:

```
Planner:
Generate a new plan.
```

## Visual Comparison

**ReAct:**

```
Reason
  ↓
Execute
  ↓
Observe
  ↓
Reason
  ↓
Execute
  ↓
Observe
```

Reasoning is inside the loop.

**Plan-and-Execute:**

```
Plan
 ↓
Execute
 ↓
Observe
 ↓
Execute
 ↓
Observe
 ↓
Execute
```

Reasoning is outside the loop.

Only if necessary:

```
Failure
 ↓
Re-plan
 ↓
Continue
```

A better representation is:

```
Planner
   ↓
Execution Loop
   ↓
Observe Results
   ↓
Continue?
  /      \
Yes       No
 |         |
Continue  Re-plan
```

**Final Comparison:**

| Feature                         | ReAct + CoT                | Plan-and-Execute        |
| ------------------------------- | -------------------------- | ----------------------- |
| Observes after each step?       | ✅ Yes                      | ✅ Yes                   |
| Reasons after each observation? | ✅ Yes                      | ❌ Usually No            |
| Explicit planner?               | ❌ No                       | ✅ Yes                   |
| Separate executor?              | ❌ No                       | ✅ Yes                   |
| Plan created upfront?           | ❌ No                       | ✅ Yes                   |
| Can dynamically change plan?    | ✅ Naturally                | ⚠️ Requires re-planning |
| Best for                        | Unpredictable environments | Predictable workflows   |


```Python
"""
Plan-and-Execute using LangChain

Workflow:
User Goal
    ↓
Planner LLM
    ↓
Explicit Plan
    ↓
ReAct Executor Agent
    ↓
Execute each step
    ↓
Final Travel Itinerary
"""

# ==========================================================
# Section 1: Imports
# ==========================================================

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.tools import Tool
from langchain.agents import AgentExecutor, create_react_agent
from langchain import hub


# ==========================================================
# Section 2: Initialize LLM
# ==========================================================

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0
)


# ==========================================================
# Section 3: Mock Travel Tools
# ==========================================================

def search_flights(query: str) -> str:
    return """
Available Flights:

1. IndiGo
   Departure: 08:00 AM
   Price: ₹5,500/person

2. Air India
   Departure: 11:00 AM
   Price: ₹6,200/person
"""


def search_hotels(query: str) -> str:
    return """
Hotels:

1. Hotel Sea Breeze
   Price: ₹5,200/night
   Breakfast: Included
   Rating: 8.4
   Free Cancellation: Yes

2. Hotel Palm Residency
   Price: ₹4,800/night
   Breakfast: Included
   Rating: 8.1
   Free Cancellation: No
"""


def suggest_activities(query: str) -> str:
    return """
Recommended Activities:

1. Baga Beach
2. Dudhsagar Falls
3. Cruise Dinner
4. Old Goa Churches
"""


# ==========================================================
# Section 4: Register Tools
# ==========================================================

tools = [

    Tool(
        name="SearchFlights",
        func=search_flights,
        description="""
        Search flights for a given route and date.
        """
    ),

    Tool(
        name="SearchHotels",
        func=search_hotels,
        description="""
        Search hotels for a destination.
        """
    ),

    Tool(
        name="SuggestActivities",
        func=suggest_activities,
        description="""
        Suggest tourist activities.
        """
    )
]


# ==========================================================
# Section 5: Planner Chain
# ==========================================================

planner_prompt = ChatPromptTemplate.from_template("""
You are a senior travel planner.

User Request:
{goal}

Create a detailed execution plan.

Requirements:
- Break the task into numbered steps.
- Each step should be executable.
- Only include steps necessary to complete the request.

Return ONLY the plan.

Example:

1. Search flights.
2. Search hotels.
3. Suggest activities.
4. Generate itinerary.
""")


planner_chain = planner_prompt | llm


# ==========================================================
# Section 6: Create ReAct Executor Agent
# ==========================================================

react_prompt = hub.pull("hwchase17/react")

agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=react_prompt
)

executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)


# ==========================================================
# Section 7: User Goal
# ==========================================================

goal = """
Plan a family trip from Bangalore to Goa
for 4 people during the second week of July.

Requirements:

- Find suitable flights.
- Find family-friendly hotels under ₹6,000/night.
- Breakfast should be included.
- Recommend popular activities.
- Provide a final itinerary.
"""


# ==========================================================
# Section 8: Planning Phase
# ==========================================================

print("\n" + "=" * 60)
print("PLANNING PHASE")
print("=" * 60)

plan = planner_chain.invoke({
    "goal": goal
})

print(plan.content)


# ==========================================================
# Section 9: Execution Phase
# ==========================================================

print("\n" + "=" * 60)
print("EXECUTION PHASE")
print("=" * 60)

execution_input = f"""
User Goal:
{goal}

Approved Plan:
{plan.content}

Execute the plan step-by-step.

Use available tools whenever needed.

Provide a final travel recommendation.
"""


response = executor.invoke({
    "input": execution_input
})


# ==========================================================
# Section 10: Final Output
# ==========================================================

print("\n" + "=" * 60)
print("FINAL ITINERARY")
print("=" * 60)

print(response["output"])
```


## Planner + Fixed Executor + Observer + Reflection

No ReAct. No Agent Tool Selection.

The planner creates the plan, the executor executes predefined steps, the observer validates execution, and the reflection agent improves the final recommendation.

```python
"""
Architecture:
============

User Goal
    ↓
Planner
    ↓
Execution Plan
    ↓
Fixed Executor
    ↓
Execution Results
    ↓
Observer
    ↓
Reflection
    ↓
Final Recommendation

Use Case:
Plan a family trip from Bangalore to Goa.

pip install langchain langchain-openai

export OPENAI_API_KEY=xxxx
"""

# ==========================================================
# SECTION 1 - IMPORTS
# ==========================================================

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


# ==========================================================
# SECTION 2 - LLM
# ==========================================================

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0
)


# ==========================================================
# SECTION 3 - MOCK BUSINESS FUNCTIONS
# Replace with MakeMyTrip / Expedia / APIs
# ==========================================================

def search_flights():
    return """
Flights:

1. IndiGo
   Bangalore → Goa
   ₹5,500 per person
   Departure: 08:00 AM

2. Air India
   Bangalore → Goa
   ₹6,200 per person
   Departure: 11:00 AM
"""


def search_hotels():
    return """
Hotels:

1. Hotel Sea Breeze
   ₹5,200/night
   Breakfast Included
   Free Cancellation
   Rating: 8.4

2. Palm Residency
   ₹4,800/night
   Breakfast Included
   No Cancellation
   Rating: 8.1
"""


def suggest_activities():
    return """
Activities:

1. Baga Beach
2. Dudhsagar Falls
3. Dinner Cruise
4. Water Sports
5. Old Goa Churches
"""


# ==========================================================
# SECTION 4 - USER GOAL
# ==========================================================

goal = """
Plan a family trip from Bangalore to Goa.

Requirements:

- Family of 4
- Hotel budget below ₹6000/night
- Breakfast included
- Prefer free cancellation
- Recommend activities
- Create final itinerary
"""


# ==========================================================
# SECTION 5 - PLANNER
# ==========================================================

planner_prompt = ChatPromptTemplate.from_template("""
You are a senior travel planner.

Goal:
{goal}

Create a numbered execution plan.

Rules:

1. Use executable steps.
2. Do not execute anything.
3. Return only the plan.
""")

planner_chain = planner_prompt | llm


# ==========================================================
# SECTION 6 - EXECUTION OBSERVER
# ==========================================================

observer_prompt = ChatPromptTemplate.from_template("""
You are an execution observer.

Goal:
{goal}

Plan:
{plan}

Execution Results:
{results}

Review:

1. Was every step completed?
2. Missing information?
3. Missing constraints?
4. Risks?
5. Improvements?

Provide observations.
""")

observer_chain = observer_prompt | llm


# ==========================================================
# SECTION 7 - REFLECTION AGENT
# ==========================================================

reflection_prompt = ChatPromptTemplate.from_template("""
You are a reflection agent.

Goal:
{goal}

Plan:
{plan}

Execution Results:
{results}

Observer Feedback:
{feedback}

Perform self-critique.

Check:

1. Budget compliance
2. Family suitability
3. Breakfast included
4. Cancellation policy
5. Ratings
6. Activity quality
7. Travel convenience

Generate the BEST final travel recommendation.

Include:

- Flight Recommendation
- Hotel Recommendation
- Activities
- Final Itinerary
- Why this option is optimal
""")

reflection_chain = reflection_prompt | llm


# ==========================================================
# SECTION 8 - PLANNING PHASE
# ==========================================================

print("\n" + "=" * 80)
print("PLANNING PHASE")
print("=" * 80)

plan_response = planner_chain.invoke({
    "goal": goal
})

plan = plan_response.content

print(plan)


# ==========================================================
# SECTION 9 - FIXED EXECUTOR
# ==========================================================

print("\n" + "=" * 80)
print("EXECUTION PHASE")
print("=" * 80)

execution_results = {}

# ----------------------------------------------------------
# Step 1
# ----------------------------------------------------------

execution_results["flights"] = search_flights()

# ----------------------------------------------------------
# Step 2
# ----------------------------------------------------------

execution_results["hotels"] = search_hotels()

# ----------------------------------------------------------
# Step 3
# ----------------------------------------------------------

execution_results["activities"] = suggest_activities()

print(execution_results)


# ==========================================================
# SECTION 10 - OBSERVER PHASE
# ==========================================================

print("\n" + "=" * 80)
print("OBSERVER PHASE")
print("=" * 80)

observer_response = observer_chain.invoke({

    "goal": goal,
    "plan": plan,
    "results": str(execution_results)

})

observer_feedback = observer_response.content

print(observer_feedback)


# ==========================================================
# SECTION 11 - REFLECTION PHASE
# ==========================================================

print("\n" + "=" * 80)
print("REFLECTION PHASE")
print("=" * 80)

reflection_response = reflection_chain.invoke({

    "goal": goal,
    "plan": plan,
    "results": str(execution_results),
    "feedback": observer_feedback

})

final_recommendation = reflection_response.content

print(final_recommendation)


# ==========================================================
# SECTION 12 - FINAL OUTPUT
# ==========================================================

print("\n" + "=" * 80)
print("FINAL TRAVEL RECOMMENDATION")
print("=" * 80)

print(final_recommendation)
```

**Why this is Planner + Fixed Executor:**

Planner:

```
1. Search Flights
2. Search Hotels
3. Recommend Activities
4. Create Itinerary
```

**Patterns used:**

| Pattern          | Used |
| ---------------- | ---- |
| Plan-and-Execute | ✅    |
| Fixed Executor   | ✅    |
| Observer         | ✅    |
| Reflection       | ✅    |
| Reflection Loop  | ✅    |
| ReAct            | ❌    |
| ToT              | ❌    |
| GoT              | ❌    |
| Reflexion        | ❌    |
| Multi-Agent      | ❌    |


**Static vs Dynamic are different from Fixed vs ReAct**

These are two different dimensions.

| Executor Type  | Tool Selection |
| -------------- | -------------- |
| Fixed Executor | Predefined     |
| ReAct Executor | Agent decides  |


**Dimension 2: Workflow**

| Workflow | Steps                |
| -------- | -------------------- |
| Static   | Known in advance     |
| Dynamic  | Generated at runtime |


**Static Planner + Fixed Executor**

Plan:

```
1. Search Flights
2. Search Hotels
3. Suggest Activities
```

Executor:

```
if step == "Search Flights":
    flight_tool.invoke()

if step == "Search Hotels":
    hotel_tool.invoke()
```

**Dynamic Planner + Fixed Executor**

User: `Plan a trip to Goa.`

Planner generates:

```
1. Search Flights
2. Search Hotels
3. Check Weather
4. Suggest Activities
5. Find Restaurants
```

The plan is dynamic.

But executor still uses:

```
STEP_TOOL_MAP = {
    "Search Flights": flight_tool,
    "Search Hotels": hotel_tool,
    "Check Weather": weather_tool,
    "Suggest Activities": activity_tool,
    "Find Restaurants": restaurant_tool
}
```

***Execution:**

```
for step in plan:

    tool = STEP_TOOL_MAP[step]

    result = tool.invoke(...)
```

Notice:

```
Dynamic Plan
+
Fixed Tool Mapping
```





## Discovery + Planner + ReAct Executor + Observer + Reflection

- LangGraph `StateGraph`
- Typed state `(TypedDict)`
- Discovery node
- Planner node
- LangChain ReAct Agent executor
- Tool definitions
- Observer node
- Reflection node
- Reflection retry loop
- Error handling
- Execution traces
- Structured outputs
- Conditional graph edges

**install:**

`pip install langgraph langchain langchain-openai langchain-core`

**Part 1: State models, tools, prompts, Discovery + Planner nodes**

```
✓ Typed State
✓ Mock Travel Tools
✓ Discovery Node
✓ Planner Node
✓ Structured Prompts
✓ Shared State Management
```

```Python
# ==========================================================
# SECTION 1 - IMPORTS
# ==========================================================

from typing import TypedDict, Dict, List, Optional

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


# ==========================================================
# SECTION 2 - LLM
# ==========================================================

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0
)


# ==========================================================
# SECTION 3 - STATE
# ==========================================================

class TravelState(TypedDict):

    # User Input
    user_request: str

    # Discovery Output
    discovery_context: str

    # Planner Output
    execution_plan: str

    # Executor Output
    execution_result: str

    # Observer Output
    observer_feedback: str

    # Reflection Output
    reflection_feedback: str

    # Final Answer
    final_answer: str

    # Runtime Information
    iteration_count: int

    # Execution Trace
    execution_trace: List[str]


# ==========================================================
# SECTION 4 - MOCK TOOLS
# Replace with real APIs later
# ==========================================================

def search_flights(
    source: str,
    destination: str
) -> str:

    return """
Flights:

1. IndiGo
   Bangalore → Goa
   Price: ₹5,500
   Departure: 08:00 AM

2. Air India
   Bangalore → Goa
   Price: ₹6,200
   Departure: 11:00 AM
"""


def search_hotels(
    destination: str
) -> str:

    return """
Hotels:

1. Hotel Sea Breeze
   Price: ₹5,200/night
   Breakfast Included
   Rating: 8.4
   Free Cancellation

2. Palm Residency
   Price: ₹4,800/night
   Breakfast Included
   Rating: 8.1
   No Cancellation
"""


def search_activities(
    destination: str
) -> str:

    return """
Activities:

1. Baga Beach
2. Dudhsagar Falls
3. Cruise Dinner
4. Water Sports
5. Old Goa Churches
"""


# ==========================================================
# SECTION 5 - DISCOVERY PROMPT
# ==========================================================

discovery_prompt = ChatPromptTemplate.from_template(
"""
You are a travel discovery specialist.

User Request:
{request}

Available Data:

Flights:
{flights}

Hotels:
{hotels}

Activities:
{activities}

Your job:

1. Summarize available options.
2. Identify useful travel choices.
3. Highlight constraints.
4. Build planning context.

Return a structured summary.
"""
)

discovery_chain = discovery_prompt | llm


# ==========================================================
# SECTION 6 - PLANNER PROMPT
# ==========================================================

planner_prompt = ChatPromptTemplate.from_template(
"""
You are a senior travel planner.

User Request:
{request}

Discovery Context:
{context}

Create a detailed execution plan.

Rules:

1. Use numbered steps.
2. Use executable actions.
3. Include hotel evaluation.
4. Include flight evaluation.
5. Include itinerary generation.
6. Include final recommendation.

Return ONLY the plan.
"""
)

planner_chain = planner_prompt | llm


# ==========================================================
# SECTION 7 - DISCOVERY NODE
# ==========================================================

def discovery_node(
    state: TravelState
) -> TravelState:

    print("\n========== DISCOVERY ==========")

    request = state["user_request"]

    flights = search_flights(
        "Bangalore",
        "Goa"
    )

    hotels = search_hotels(
        "Goa"
    )

    activities = search_activities(
        "Goa"
    )

    discovery_response = discovery_chain.invoke({

        "request": request,
        "flights": flights,
        "hotels": hotels,
        "activities": activities

    })

    discovery_context = discovery_response.content

    state["discovery_context"] = discovery_context

    state["execution_trace"].append(
        "Discovery completed"
    )

    return state


# ==========================================================
# SECTION 8 - PLANNER NODE
# ==========================================================

def planner_node(
    state: TravelState
) -> TravelState:

    print("\n========== PLANNER ==========")

    planner_response = planner_chain.invoke({

        "request": state["user_request"],
        "context": state["discovery_context"]

    })

    plan = planner_response.content

    state["execution_plan"] = plan

    state["execution_trace"].append(
        "Execution plan generated"
    )

    print(plan)

    return state


# ==========================================================
# SECTION 9 - INITIAL STATE
# ==========================================================

initial_state: TravelState = {

    "user_request": """
Plan a family trip from Bangalore to Goa.

Requirements:

- Family of 4
- Hotel budget under ₹6000
- Breakfast included
- Prefer free cancellation
- Recommend activities
- Build final itinerary
""",

    "discovery_context": "",

    "execution_plan": "",

    "execution_result": "",

    "observer_feedback": "",

    "reflection_feedback": "",

    "final_answer": "",

    "iteration_count": 0,

    "execution_trace": []

}


# ==========================================================
# PART 1 ENDS HERE
# ==========================================================

print("Part 1 Loaded Successfully")
```



**Part 2: ReAct Executor node, Observer node, Reflection node**

```
✓ ReAct Executor
✓ Observer
✓ Reflection
```

```Python
# ==========================================================
# SECTION 10 - REACT AGENT TOOLS
# ==========================================================

from langchain.tools import Tool

flight_tool = Tool(
    name="SearchFlights",
    func=lambda q: search_flights(
        "Bangalore",
        "Goa"
    ),
    description="""
    Search available flights.
    """
)

hotel_tool = Tool(
    name="SearchHotels",
    func=lambda q: search_hotels(
        "Goa"
    ),
    description="""
    Search available hotels.
    """
)

activity_tool = Tool(
    name="SearchActivities",
    func=lambda q: search_activities(
        "Goa"
    ),
    description="""
    Search tourist activities.
    """
)

tools = [
    flight_tool,
    hotel_tool,
    activity_tool
]
```

**Part 3: LangGraph wiring, conditional edges, main runner, execution example**

```
✓ LangGraph Workflow
✓ Conditional Edges
✓ Reflection Retry Loop
✓ Main Runner
```

- `TravelState`
- `initial_state`
- `discovery_node`
- `planner_node`
- `executor_node`
- `observer_node`
- `reflection_node`
- `reflection_decision`

```Python
# ==========================================================
# PART 3 - LANGGRAPH WORKFLOW
# ==========================================================

from langgraph.graph import (
    StateGraph,
    END
)

# ==========================================================
# BUILD GRAPH
# ==========================================================

graph_builder = StateGraph(
    TravelState
)

# ==========================================================
# REGISTER NODES
# ==========================================================

graph_builder.add_node(
    "discovery",
    discovery_node
)

graph_builder.add_node(
    "planner",
    planner_node
)

graph_builder.add_node(
    "executor",
    executor_node
)

graph_builder.add_node(
    "observer",
    observer_node
)

graph_builder.add_node(
    "reflection",
    reflection_node
)

# ==========================================================
# ENTRY POINT
# ==========================================================

graph_builder.set_entry_point(
    "discovery"
)

# ==========================================================
# NORMAL FLOW
# ==========================================================

graph_builder.add_edge(
    "discovery",
    "planner"
)

graph_builder.add_edge(
    "planner",
    "executor"
)

graph_builder.add_edge(
    "executor",
    "observer"
)

graph_builder.add_edge(
    "observer",
    "reflection"
)

# ==========================================================
# REFLECTION LOOP
# ==========================================================
#
# reflection_decision()
#
# Returns:
#
# "retry"
# "complete"
#
# retry    -> executor
# complete -> END
#
# ==========================================================

graph_builder.add_conditional_edges(

    "reflection",

    reflection_decision,

    {

        "retry": "executor",

        "complete": END

    }
)

# ==========================================================
# COMPILE GRAPH
# ==========================================================

travel_graph = graph_builder.compile()

# ==========================================================
# EXECUTE GRAPH
# ==========================================================

result = travel_graph.invoke(
    initial_state
)

# ==========================================================
# FINAL OUTPUT
# ==========================================================

print("\n")
print("=" * 80)
print("FINAL RECOMMENDATION")
print("=" * 80)

print(
    result["final_answer"]
)

# ==========================================================
# EXECUTION TRACE
# ==========================================================

print("\n")
print("=" * 80)
print("EXECUTION TRACE")
print("=" * 80)

for step in result["execution_trace"]:

    print(step)

# ==========================================================
# OBSERVER FEEDBACK
# ==========================================================

print("\n")
print("=" * 80)
print("OBSERVER FEEDBACK")
print("=" * 80)

print(
    result["observer_feedback"]
)

# ==========================================================
# REFLECTION OUTPUT
# ==========================================================

print("\n")
print("=" * 80)
print("REFLECTION OUTPUT")
print("=" * 80)

print(
    result["reflection_feedback"]
)

# ==========================================================
# ITERATION COUNT
# ==========================================================

print("\n")
print("=" * 80)
print("TOTAL REFLECTION ITERATIONS")
print("=" * 80)

print(
    result["iteration_count"]
)

# ==========================================================
# COMPLETE STATE (OPTIONAL)
# ==========================================================

print("\n")
print("=" * 80)
print("FINAL STATE")
print("=" * 80)

for key, value in result.items():

    print(f"\n{key}")
    print("-" * 40)
    print(value)
```

**Final Architecture**

```
User Request
      │
      ▼
Discovery
      │
      ▼
Planner
      │
      ▼
ReAct Executor
      │
      ▼
Observer
      │
      ▼
Reflection
      │
      ├── PASS ─────► END
      │
      └── FAIL ─────► Executor
                          │
                          ▼
                      Observer
                          │
                          ▼
                      Reflection
```


## Discover + Planner + Multi-Agent Executor (Supervisor) + Observer + Reflection + Reflexion (Memory)

**Architecture**

```
                    User
                      │
                      ▼
                Discovery Agent
                      │
                      ▼
                 Planner Agent
                      │
                      ▼
                Supervisor Agent
          ┌───────────┼───────────┐
          │           │           │
          ▼           ▼           ▼
     Flight Agent  Hotel Agent  Activity Agent
          │           │           │
          └───────┬───┴──────┬────┘
                  │          │
                  ▼
           Result Aggregator
                  │
                  ▼
               Observer
                  │
                  ▼
              Reflection
                  │
                  ▼
              Reflexion
                  │
                  ▼
          Memory Store (Vector DB)
                  │
                  ▼
             Final Answer
```


**Role of Each Component**

| Component      | Responsibility                 |
| -------------- | ------------------------------ |
| Discovery      | Collect current inventory/data |
| Planner        | Create execution plan          |
| Supervisor     | Assign tasks to agents         |
| Flight Agent   | Flight reasoning               |
| Hotel Agent    | Hotel reasoning                |
| Activity Agent | Activity reasoning             |
| Observer       | Verify completeness            |
| Reflection     | Improve current answer         |
| Reflexion      | Learn for future runs          |
| Memory         | Store lessons learned          |


**Example:**

User:

```
Plan Goa trip for family of 4.
Budget hotel < ₹6000.
Breakfast required.
Prefer cancellation.
```

**Discovery:**

Collect:

```
Flights
Hotels
Activities
Weather
```

**Planner:**

Creates:

```
1. Evaluate flights
2. Evaluate hotels
3. Evaluate activities
4. Build itinerary
5. Recommend best option
```

**Supervisor:**

Delegates:

```
Flight Agent
    → Evaluate flights

Hotel Agent
    → Evaluate hotels

Activity Agent
    → Evaluate activities
```

**Observer:**

Checks:

```
Did hotel budget satisfy?
Breakfast checked?
Cancellation checked?
```

**Reflection:**

Improves answer:

```
Hotel B is better because
it has cancellation flexibility.
```

**Reflexion**

Stores memory:

```
Families value:

- Breakfast
- Cancellation
- Ratings

Prioritize these in future.
```

Saved to:

```
Vector DB
PostgreSQL
Redis
Knowledge Store
```

**Why Reflexion Matters**

Without Reflexion:

```
Trip #1
    ↓
Answer
    ↓
Forget everything
```

With Reflexion:

```
Trip #1
    ↓
Learn
    ↓
Store Memory
    ↓
Trip #2
    ↓
Retrieve Lesson
    ↓
Better Answer
```

## Enterprise LangGraph Layout

```
START
  │
  ▼
Discovery
  │
  ▼
Planner
  │
  ▼
Supervisor
  │
  ├──────────────┐
  ▼              ▼
Flight Agent  Hotel Agent
  │              │
  └──────┬───────┘
         ▼
Activity Agent
         ▼
Aggregator
         ▼
Observer
         ▼
Reflection
         ▼
Reflexion
         ▼
END
```

**Production Enhancements**

| Layer            | Technology                  |
| ---------------- | --------------------------- |
| Workflow         | LangGraph                   |
| Memory           | PostgreSQL + pgvector       |
| Short-Term State | LangGraph Checkpointer      |
| Long-Term Memory | Vector DB                   |
| Observability    | LangSmith                   |
| Evaluation       | LLM Judge                   |
| Human Approval   | Before Booking              |
| Guardrails       | Pydantic Validation         |
| Caching          | Redis                       |
| Parallelism      | LangGraph Parallel Branches |


**Pattern Classification**

| Pattern                      | Used                      |
| ---------------------------- | ------------------------- |
| Discovery                    | ✅                         |
| Plan-and-Execute             | ✅                         |
| Supervisor                   | ✅                         |
| Multi-Agent                  | ✅                         |
| Routing                      | ✅                         |
| Observer                     | ✅                         |
| Reflection                   | ✅                         |
| Reflexion                    | ✅                         |
| Memory                       | ✅                         |
| Human-in-the-Loop (optional) | ✅                         |
| ReAct                        | Optional per worker agent |


**Important Insight**

At this level, **ReAct is usually not the top-level pattern anymore**.

The architecture becomes:

```
Supervisor Pattern
        +
Plan-and-Execute
        +
Reflection
        +
Reflexion
```

and individual worker agents may internally use:

```
ReAct
CoT
ToT
GoT
```

For example:

```
Hotel Agent
    ↓
ReAct + CoT

Flight Agent
    ↓
ReAct

Activity Agent
    ↓
ToT
```

while the overall orchestration remains:

```
Discovery
 ↓
Planner
 ↓
Supervisor
 ↓
Multi-Agent Execution
 ↓
Observer
 ↓
Reflection
 ↓
Reflexion
```

## Part 1 — Discovery + Planner + Memory Foundation

```
User
 ↓
Discovery Agent
 ↓
Planner Agent
 ↓
Supervisor
 ↓
Multi-Agent Execution
 ↓
Observer
 ↓
Reflection
 ↓
Reflexion Memory
```

```
✓ Typed State
✓ Memory Store (Reflexion Foundation)
✓ Travel Tools
✓ Discovery Agent
✓ Planner Agent
✓ Initial State
```

```Python
# ==========================================================
# PART 1
# DISCOVERY + PLANNER + MEMORY FOUNDATION
# ==========================================================

from typing import TypedDict, List, Dict, Any
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


# ==========================================================
# LLM
# ==========================================================

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0
)


# ==========================================================
# STATE
# ==========================================================

class TravelState(TypedDict):

    # User Input
    user_request: str

    # Discovery
    discovery_context: str

    # Planning
    execution_plan: str

    # Supervisor Output
    supervisor_tasks: Dict[str, str]

    # Agent Outputs
    flight_result: str
    hotel_result: str
    activity_result: str

    # Aggregated Results
    aggregated_result: str

    # Observer
    observer_feedback: str

    # Reflection
    reflection_feedback: str

    # Reflexion
    lessons_learned: str

    # Final
    final_answer: str

    # Runtime
    iteration_count: int

    # Trace
    execution_trace: List[str]


# ==========================================================
# SIMPLE MEMORY STORE
#
# In production:
# PostgreSQL
# pgvector
# Chroma
# Pinecone
# Weaviate
# ==========================================================

class ReflexionMemory:

    def __init__(self):
        self.memory = []

    def add_lesson(
        self,
        lesson: str
    ):
        self.memory.append(lesson)

    def get_lessons(self):

        if not self.memory:
            return "No previous lessons."

        return "\n".join(self.memory)


memory_store = ReflexionMemory()


# ==========================================================
# TRAVEL DATA TOOLS
#
# Later replace with:
#
# MakeMyTrip
# Expedia
# Booking.com
# Amadeus
# Google Travel APIs
# ==========================================================

def search_flights():

    return """
Flights:

1. IndiGo
   Bangalore → Goa
   ₹5500
   Departure 08:00

2. Air India
   Bangalore → Goa
   ₹6200
   Departure 11:00
"""


def search_hotels():

    return """
Hotels:

1. Hotel Sea Breeze
   ₹5200/night
   Breakfast Included
   Free Cancellation
   Rating 8.4

2. Palm Residency
   ₹4800/night
   Breakfast Included
   No Cancellation
   Rating 8.1
"""


def search_activities():

    return """
Activities:

1. Baga Beach
2. Dudhsagar Falls
3. Cruise Dinner
4. Water Sports
"""


# ==========================================================
# DISCOVERY PROMPT
# ==========================================================

discovery_prompt = ChatPromptTemplate.from_template(
"""
You are a Discovery Agent.

User Request:
{request}

Previous Lessons:
{lessons}

Flights:
{flights}

Hotels:
{hotels}

Activities:
{activities}

Your Job:

1. Understand available inventory.
2. Understand constraints.
3. Identify useful options.
4. Build planning context.

Return structured context.
"""
)

discovery_chain = discovery_prompt | llm


# ==========================================================
# PLANNER PROMPT
# ==========================================================

planner_prompt = ChatPromptTemplate.from_template(
"""
You are a Senior Travel Planner.

User Request:
{request}

Discovery Context:
{context}

Create an execution plan.

Rules:

1. Numbered steps.
2. Delegatable tasks.
3. Separate Flight Analysis.
4. Separate Hotel Analysis.
5. Separate Activity Analysis.
6. Final Recommendation Step.

Return only the plan.
"""
)

planner_chain = planner_prompt | llm


# ==========================================================
# DISCOVERY NODE
# ==========================================================

def discovery_node(
    state: TravelState
) -> TravelState:

    print("\n========== DISCOVERY ==========")

    flights = search_flights()

    hotels = search_hotels()

    activities = search_activities()

    previous_lessons = memory_store.get_lessons()

    response = discovery_chain.invoke({

        "request":
            state["user_request"],

        "lessons":
            previous_lessons,

        "flights":
            flights,

        "hotels":
            hotels,

        "activities":
            activities

    })

    state["discovery_context"] = response.content

    state["execution_trace"].append(
        "Discovery Completed"
    )

    return state


# ==========================================================
# PLANNER NODE
# ==========================================================

def planner_node(
    state: TravelState
) -> TravelState:

    print("\n========== PLANNER ==========")

    response = planner_chain.invoke({

        "request":
            state["user_request"],

        "context":
            state["discovery_context"]

    })

    state["execution_plan"] = response.content

    state["execution_trace"].append(
        "Plan Generated"
    )

    print("\nGenerated Plan:\n")
    print(response.content)

    return state


# ==========================================================
# INITIAL STATE
# ==========================================================

initial_state: TravelState = {

    "user_request": """
Plan a Goa trip for a family of 4.

Requirements:

- Hotel under ₹6000/night
- Breakfast Included
- Prefer Free Cancellation
- Recommend Activities
- Create Final Itinerary
""",

    "discovery_context": "",

    "execution_plan": "",

    "supervisor_tasks": {},

    "flight_result": "",

    "hotel_result": "",

    "activity_result": "",

    "aggregated_result": "",

    "observer_feedback": "",

    "reflection_feedback": "",

    "lessons_learned": "",

    "final_answer": "",

    "iteration_count": 0,

    "execution_trace": []
}


# ==========================================================
# TEST PART 1
# ==========================================================

if __name__ == "__main__":

    state = discovery_node(
        initial_state
    )

    state = planner_node(
        state
    )

    print("\n")
    print("=" * 80)
    print("DISCOVERY CONTEXT")
    print("=" * 80)

    print(
        state["discovery_context"]
    )

    print("\n")
    print("=" * 80)
    print("EXECUTION PLAN")
    print("=" * 80)

    print(
        state["execution_plan"]
    )
```

**What Part 1 Produces**

```
User Request
      ↓
Discovery Agent
      ↓
Travel Context
      ↓
Planner Agent
      ↓
Execution Plan
```

Example plan:

```
1. Analyze flight options.
2. Analyze hotel options.
3. Analyze activities.
4. Compare alternatives.
5. Create itinerary.
6. Recommend best trip.
```

## Part 2 — Supervisor + Multi-Agent Executors + Aggregator

```
Discovery
    ↓
Planner
    ↓
Supervisor
    ↓
Flight Agent
Hotel Agent
Activity Agent
    ↓
Aggregator
```

```Python
# ==========================================================
# PART 2
# SUPERVISOR + MULTI AGENT EXECUTION
# ==========================================================

from langchain_core.prompts import ChatPromptTemplate


# ==========================================================
# SUPERVISOR PROMPT
# ==========================================================

supervisor_prompt = ChatPromptTemplate.from_template(
"""
You are a Supervisor Agent.

Execution Plan:
{plan}

Your job:

1. Analyze the plan.
2. Create tasks for:
   - Flight Agent
   - Hotel Agent
   - Activity Agent

Return tasks in this format:

FLIGHT_TASK:
...

HOTEL_TASK:
...

ACTIVITY_TASK:
...
"""
)

supervisor_chain = supervisor_prompt | llm


# ==========================================================
# FLIGHT AGENT
# ==========================================================

flight_prompt = ChatPromptTemplate.from_template(
"""
You are a Flight Analysis Agent.

Task:
{task}

Available Flights:
{flights}

Requirements:

1. Compare flights.
2. Consider cost.
3. Consider convenience.
4. Recommend best flight.

Return recommendation.
"""
)

flight_chain = flight_prompt | llm


# ==========================================================
# HOTEL AGENT
# ==========================================================

hotel_prompt = ChatPromptTemplate.from_template(
"""
You are a Hotel Analysis Agent.

Task:
{task}

Available Hotels:
{hotels}

Requirements:

1. Check budget.
2. Check breakfast.
3. Check cancellation.
4. Check ratings.
5. Recommend best hotel.

Return recommendation.
"""
)

hotel_chain = hotel_prompt | llm


# ==========================================================
# ACTIVITY AGENT
# ==========================================================

activity_prompt = ChatPromptTemplate.from_template(
"""
You are an Activity Planning Agent.

Task:
{task}

Available Activities:
{activities}

Requirements:

1. Select family-friendly activities.
2. Create recommendations.
3. Consider trip experience.

Return recommendation.
"""
)

activity_chain = activity_prompt | llm


# ==========================================================
# AGGREGATOR PROMPT
# ==========================================================

aggregator_prompt = ChatPromptTemplate.from_template(
"""
You are an Aggregator Agent.

Flight Recommendation:
{flight_result}

Hotel Recommendation:
{hotel_result}

Activity Recommendation:
{activity_result}

Combine all recommendations into a single
travel proposal.

Return structured output.
"""
)

aggregator_chain = aggregator_prompt | llm


# ==========================================================
# SUPERVISOR NODE
# ==========================================================

def supervisor_node(
    state: TravelState
) -> TravelState:

    print("\n========== SUPERVISOR ==========")

    response = supervisor_chain.invoke({

        "plan": state["execution_plan"]

    })

    content = response.content

    # ------------------------------------------------------
    # Simple parsing
    # In production use Pydantic structured output
    # ------------------------------------------------------

    flight_task = ""
    hotel_task = ""
    activity_task = ""

    current = None

    for line in content.splitlines():

        if "FLIGHT_TASK:" in line:
            current = "flight"
            continue

        elif "HOTEL_TASK:" in line:
            current = "hotel"
            continue

        elif "ACTIVITY_TASK:" in line:
            current = "activity"
            continue

        if current == "flight":
            flight_task += line + "\n"

        elif current == "hotel":
            hotel_task += line + "\n"

        elif current == "activity":
            activity_task += line + "\n"

    state["supervisor_tasks"] = {

        "flight": flight_task.strip(),
        "hotel": hotel_task.strip(),
        "activity": activity_task.strip()

    }

    state["execution_trace"].append(
        "Supervisor Created Tasks"
    )

    return state


# ==========================================================
# FLIGHT AGENT NODE
# ==========================================================

def flight_agent_node(
    state: TravelState
) -> TravelState:

    print("\n========== FLIGHT AGENT ==========")

    response = flight_chain.invoke({

        "task":
            state["supervisor_tasks"]["flight"],

        "flights":
            search_flights()

    })

    state["flight_result"] = response.content

    state["execution_trace"].append(
        "Flight Analysis Complete"
    )

    return state


# ==========================================================
# HOTEL AGENT NODE
# ==========================================================

def hotel_agent_node(
    state: TravelState
) -> TravelState:

    print("\n========== HOTEL AGENT ==========")

    response = hotel_chain.invoke({

        "task":
            state["supervisor_tasks"]["hotel"],

        "hotels":
            search_hotels()

    })

    state["hotel_result"] = response.content

    state["execution_trace"].append(
        "Hotel Analysis Complete"
    )

    return state


# ==========================================================
# ACTIVITY AGENT NODE
# ==========================================================

def activity_agent_node(
    state: TravelState
) -> TravelState:

    print("\n========== ACTIVITY AGENT ==========")

    response = activity_chain.invoke({

        "task":
            state["supervisor_tasks"]["activity"],

        "activities":
            search_activities()

    })

    state["activity_result"] = response.content

    state["execution_trace"].append(
        "Activity Analysis Complete"
    )

    return state


# ==========================================================
# AGGREGATOR NODE
# ==========================================================

def aggregator_node(
    state: TravelState
) -> TravelState:

    print("\n========== AGGREGATOR ==========")

    response = aggregator_chain.invoke({

        "flight_result":
            state["flight_result"],

        "hotel_result":
            state["hotel_result"],

        "activity_result":
            state["activity_result"]

    })

    state["aggregated_result"] = response.content

    state["execution_trace"].append(
        "Aggregation Complete"
    )

    return state


# ==========================================================
# TEST PART 2
# ==========================================================

if __name__ == "__main__":

    state = discovery_node(initial_state)

    state = planner_node(state)

    state = supervisor_node(state)

    state = flight_agent_node(state)

    state = hotel_agent_node(state)

    state = activity_agent_node(state)

    state = aggregator_node(state)

    print("\n")
    print("=" * 80)
    print("AGGREGATED RESULT")
    print("=" * 80)

    print(
        state["aggregated_result"]
    )
```

**What Part 2 Adds:**

```
Discovery
     ↓
Planner
     ↓
Supervisor
     ↓
 ┌───────────────┬───────────────┬───────────────┐
 │               │               │
 ▼               ▼               ▼
Flight Agent  Hotel Agent  Activity Agent
 │               │               │
 └───────┬───────┴───────┬───────┘
         ▼
     Aggregator
```

**Responsibilities:**

| Agent          | Responsibility                           |
| -------------- | ---------------------------------------- |
| Supervisor     | Creates tasks                            |
| Flight Agent   | Flight evaluation                        |
| Hotel Agent    | Budget, breakfast, cancellation, ratings |
| Activity Agent | Family-friendly activity planning        |
| Aggregator     | Merges recommendations                   |


## Part 3 — Observer + Reflection + Reflexion (Memory Learning)

```
Discovery
    ↓
Planner
    ↓
Supervisor
    ↓
Flight Agent
Hotel Agent
Activity Agent
    ↓
Aggregator
    ↓
Observer
    ↓
Reflection
    ↓
Reflexion (Memory Learning)
    ↓
Final Answer
```

```Python
# ==========================================================
# PART 3
# OBSERVER + REFLECTION + REFLEXION
# ==========================================================

from langchain_core.prompts import ChatPromptTemplate


# ==========================================================
# OBSERVER PROMPT
# ==========================================================

observer_prompt = ChatPromptTemplate.from_template(
"""
You are an Observer Agent.

User Request:
{request}

Aggregated Recommendation:
{aggregated_result}

Review the recommendation.

Check:

1. Budget compliance
2. Breakfast requirement
3. Cancellation policy
4. Family suitability
5. Completeness
6. Missing information

Provide detailed feedback.

Return:

STATUS: PASS

or

STATUS: FAIL

along with explanation.
"""
)

observer_chain = observer_prompt | llm


# ==========================================================
# REFLECTION PROMPT
# ==========================================================

reflection_prompt = ChatPromptTemplate.from_template(
"""
You are a Reflection Agent.

User Request:
{request}

Aggregated Recommendation:
{aggregated_result}

Observer Feedback:
{observer_feedback}

Improve the recommendation.

Review:

1. Budget
2. Ratings
3. Cancellation
4. Breakfast
5. Family suitability
6. Activities

Generate a better recommendation.

Return:

- Best Flight
- Best Hotel
- Activities
- Itinerary
- Justification
"""
)

reflection_chain = reflection_prompt | llm


# ==========================================================
# REFLEXION PROMPT
# ==========================================================

reflexion_prompt = ChatPromptTemplate.from_template(
"""
You are a Reflexion Agent.

User Request:
{request}

Final Recommendation:
{final_answer}

Observer Feedback:
{observer_feedback}

Learn from this execution.

Generate lessons that can improve
future travel recommendations.

Examples:

- Families prefer free cancellation.
- Breakfast improves satisfaction.
- Ratings above 8.0 are preferred.

Return concise lessons.
"""
)

reflexion_chain = reflexion_prompt | llm


# ==========================================================
# OBSERVER NODE
# ==========================================================

def observer_node(
    state: TravelState
) -> TravelState:

    print("\n========== OBSERVER ==========")

    response = observer_chain.invoke({

        "request":
            state["user_request"],

        "aggregated_result":
            state["aggregated_result"]

    })

    state["observer_feedback"] = response.content

    state["execution_trace"].append(
        "Observer Review Complete"
    )

    return state


# ==========================================================
# REFLECTION NODE
# ==========================================================

def reflection_node(
    state: TravelState
) -> TravelState:

    print("\n========== REFLECTION ==========")

    response = reflection_chain.invoke({

        "request":
            state["user_request"],

        "aggregated_result":
            state["aggregated_result"],

        "observer_feedback":
            state["observer_feedback"]

    })

    state["reflection_feedback"] = response.content

    state["final_answer"] = response.content

    state["iteration_count"] += 1

    state["execution_trace"].append(
        "Reflection Complete"
    )

    return state


# ==========================================================
# REFLEXION NODE
# ==========================================================

def reflexion_node(
    state: TravelState
) -> TravelState:

    print("\n========== REFLEXION ==========")

    response = reflexion_chain.invoke({

        "request":
            state["user_request"],

        "final_answer":
            state["final_answer"],

        "observer_feedback":
            state["observer_feedback"]

    })

    lessons = response.content

    state["lessons_learned"] = lessons

    memory_store.add_lesson(
        lessons
    )

    state["execution_trace"].append(
        "Reflexion Memory Updated"
    )

    return state


# ==========================================================
# REFLECTION DECISION
# ==========================================================

def reflection_decision(
    state: TravelState
):

    feedback = state["observer_feedback"]

    if "STATUS: FAIL" in feedback:

        if state["iteration_count"] < 2:

            return "retry"

    return "complete"


# ==========================================================
# TEST PART 3
# ==========================================================

if __name__ == "__main__":

    state = discovery_node(initial_state)

    state = planner_node(state)

    state = supervisor_node(state)

    state = flight_agent_node(state)

    state = hotel_agent_node(state)

    state = activity_agent_node(state)

    state = aggregator_node(state)

    state = observer_node(state)

    state = reflection_node(state)

    state = reflexion_node(state)

    print("\n")
    print("=" * 80)
    print("FINAL ANSWER")
    print("=" * 80)

    print(
        state["final_answer"]
    )

    print("\n")
    print("=" * 80)
    print("LESSONS LEARNED")
    print("=" * 80)

    print(
        state["lessons_learned"]
    )
```


**Full Architecture After Part 3:**

```
Discovery
    ↓
Planner
    ↓
Supervisor
    ↓
 ┌──────────────┬──────────────┬──────────────┐
 ▼              ▼              ▼
Flight       Hotel         Activity
Agent        Agent          Agent
 └──────────────┬──────────────┘
                ▼
           Aggregator
                ▼
            Observer
                ▼
           Reflection
                ▼
            Reflexion
                ▼
           Memory Store
                ▼
          Final Answer
```



```
START
  ↓
Discovery
  ↓
Planner
  ↓
Supervisor
  ↓
Flight Agent
Hotel Agent
Activity Agent
  ↓
Aggregator
  ↓
Observer
  ↓
Reflection
  ↓
PASS ?
 /   \
Yes   No
 |     |
 ▼     ▼
Reflexion
      Reflection Retry
 |
 ▼
END
```


## Part 4 — Complete LangGraph Orchestration (Discovery + Planner + Supervisor + Multi-Agent + Observer + Reflection + Reflexion)

This is the final piece that wires together `Part 1` + `Part 2` + `Part 3`.

Assumes all nodes already exist:

- discovery_node
- planner_node
- supervisor_node
- flight_agent_node
- hotel_agent_node
- activity_agent_node
- aggregator_node
- observer_node
- reflection_node
- reflexion_node
- reflection_decision
- TravelState
- initial_state


```Python
# ==========================================================
# PART 4
# LANGGRAPH ORCHESTRATION
# ==========================================================

from langgraph.graph import (
    StateGraph,
    END
)

# ==========================================================
# BUILD GRAPH
# ==========================================================

workflow = StateGraph(
    TravelState
)

# ==========================================================
# REGISTER NODES
# ==========================================================

workflow.add_node(
    "discovery",
    discovery_node
)

workflow.add_node(
    "planner",
    planner_node
)

workflow.add_node(
    "supervisor",
    supervisor_node
)

workflow.add_node(
    "flight_agent",
    flight_agent_node
)

workflow.add_node(
    "hotel_agent",
    hotel_agent_node
)

workflow.add_node(
    "activity_agent",
    activity_agent_node
)

workflow.add_node(
    "aggregator",
    aggregator_node
)

workflow.add_node(
    "observer",
    observer_node
)

workflow.add_node(
    "reflection",
    reflection_node
)

workflow.add_node(
    "reflexion",
    reflexion_node
)

# ==========================================================
# ENTRY POINT
# ==========================================================

workflow.set_entry_point(
    "discovery"
)

# ==========================================================
# MAIN FLOW
# ==========================================================

workflow.add_edge(
    "discovery",
    "planner"
)

workflow.add_edge(
    "planner",
    "supervisor"
)

# ==========================================================
# MULTI-AGENT EXECUTION FLOW
#
# Simple Sequential Version
#
# supervisor
#    ↓
# flight
#    ↓
# hotel
#    ↓
# activity
#    ↓
# aggregator
#
# ==========================================================

workflow.add_edge(
    "supervisor",
    "flight_agent"
)

workflow.add_edge(
    "flight_agent",
    "hotel_agent"
)

workflow.add_edge(
    "hotel_agent",
    "activity_agent"
)

workflow.add_edge(
    "activity_agent",
    "aggregator"
)

# ==========================================================
# QUALITY CONTROL FLOW
# ==========================================================

workflow.add_edge(
    "aggregator",
    "observer"
)

workflow.add_edge(
    "observer",
    "reflection"
)

# ==========================================================
# CONDITIONAL REFLECTION LOOP
#
# reflection_decision()
#
# returns:
#
# retry
# complete
#
# ==========================================================

workflow.add_conditional_edges(

    "reflection",

    reflection_decision,

    {

        "retry": "aggregator",

        "complete": "reflexion"

    }
)

# ==========================================================
# FINAL MEMORY UPDATE
# ==========================================================

workflow.add_edge(
    "reflexion",
    END
)

# ==========================================================
# COMPILE GRAPH
# ==========================================================

travel_graph = workflow.compile()

# ==========================================================
# EXECUTE WORKFLOW
# ==========================================================

result = travel_graph.invoke(
    initial_state
)

# ==========================================================
# FINAL ANSWER
# ==========================================================

print("\n")
print("=" * 80)
print("FINAL TRAVEL RECOMMENDATION")
print("=" * 80)

print(
    result["final_answer"]
)

# ==========================================================
# OBSERVER FEEDBACK
# ==========================================================

print("\n")
print("=" * 80)
print("OBSERVER FEEDBACK")
print("=" * 80)

print(
    result["observer_feedback"]
)

# ==========================================================
# REFLECTION OUTPUT
# ==========================================================

print("\n")
print("=" * 80)
print("REFLECTION OUTPUT")
print("=" * 80)

print(
    result["reflection_feedback"]
)

# ==========================================================
# REFLEXION MEMORY
# ==========================================================

print("\n")
print("=" * 80)
print("LESSONS LEARNED")
print("=" * 80)

print(
    result["lessons_learned"]
)

# ==========================================================
# EXECUTION TRACE
# ==========================================================

print("\n")
print("=" * 80)
print("EXECUTION TRACE")
print("=" * 80)

for item in result["execution_trace"]:

    print(item)

# ==========================================================
# ITERATION COUNT
# ==========================================================

print("\n")
print("=" * 80)
print("REFLECTION ITERATIONS")
print("=" * 80)

print(
    result["iteration_count"]
)

# ==========================================================
# MEMORY STORE CONTENTS
# ==========================================================

print("\n")
print("=" * 80)
print("MEMORY STORE")
print("=" * 80)

print(
    memory_store.get_lessons()
)
```


**Final Architecture:**

```
User
 │
 ▼
Discovery
 │
 ▼
Planner
 │
 ▼
Supervisor
 │
 ▼
Flight Agent
 │
 ▼
Hotel Agent
 │
 ▼
Activity Agent
 │
 ▼
Aggregator
 │
 ▼
Observer
 │
 ▼
Reflection
 │
 ├──────── FAIL ──────────┐
 │                        │
 │                        ▼
 │                   Aggregator
 │                        │
 │                        ▼
 │                   Observer
 │                        │
 │                        ▼
 │                   Reflection
 │
 └──────── PASS ──────────► Reflexion
                               │
                               ▼
                             Memory
                               │
                               ▼
                              END
```


**Enterprise Improvement:**

The sequential agent flow: `Flight → Hotel → Activity`

should ideally become parallel execution in LangGraph:

```
                Supervisor
                      │
       ┌──────────────┼──────────────┐
       ▼              ▼              ▼
 Flight Agent   Hotel Agent   Activity Agent
       └──────────────┼──────────────┘
                      ▼
                 Aggregator
```



