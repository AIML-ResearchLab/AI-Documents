"""
╔══════════════════════════════════════════════════════════════╗
║   Chain-of-Thought (CoT) Agent using LangChain + Claude      ║
║   Pattern: Think → Tool Call → Analyze → Decide → Answer     ║
╚══════════════════════════════════════════════════════════════╝

Install:
    pip install langchain langchain-anthropic langchain-community

Set API Key:
    export ANTHROPIC_API_KEY=your_key_here
"""

# ── Imports ──────────────────────────────────────────────────────────
from langchain_anthropic import ChatAnthropic
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain.tools import tool
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.schema import SystemMessage
from langchain_core.messages import HumanMessage, AIMessage
from langchain.callbacks.base import BaseCallbackHandler
from datetime import datetime, date
from typing import Optional
import json


# ══════════════════════════════════════════════════════════════════════
# SECTION 1: TOOLS (What the Agent can DO)
# ══════════════════════════════════════════════════════════════════════

@tool
def get_order(order_id: str) -> str:
    """
    Fetch order details from the database using the order ID.
    Returns item name, price, delivery status, and days since delivery.
    """
    # In production: replace with real DB/API call
    mock_orders = {
        "#45231": {
            "order_id": "#45231",
            "item": "Dell Laptop XPS 15",
            "amount": 75000,
            "status": "delivered",
            "order_date": "2024-02-10",
            "delivery_date": "2024-02-15",
            "days_since_delivery": 12,
            "customer": "Raj Sharma"
        },
        "#78902": {
            "order_id": "#78902",
            "item": "iPhone 15 Pro",
            "amount": 130000,
            "status": "delivered",
            "order_date": "2024-01-20",
            "delivery_date": "2024-01-25",
            "days_since_delivery": 45,
            "customer": "Priya Nair"
        }
    }

    order = mock_orders.get(order_id)
    if not order:
        return json.dumps({"error": f"Order {order_id} not found in system."})
    return json.dumps(order)


@tool
def check_refund_policy(reason: str, days_since_delivery: int) -> str:
    """
    Check if a customer qualifies for a refund based on reason and timing.
    Returns eligibility status, applicable policy section, and refund type.
    """
    policy_result = {
        "reason": reason,
        "days_since_delivery": days_since_delivery,
    }

    # Policy rules
    if reason.lower() in ["damaged", "defective", "broken", "wrong item"]:
        if days_since_delivery <= 30:
            policy_result.update({
                "eligible": True,
                "refund_type": "full",
                "policy_section": "Section 4.2 — Damaged/Defective Goods",
                "notes": "Customer gets full refund + free return pickup"
            })
        else:
            policy_result.update({
                "eligible": False,
                "refund_type": "none",
                "policy_section": "Section 4.2 — Expired",
                "notes": "Damaged goods claim window is 30 days from delivery"
            })
    elif reason.lower() in ["not satisfied", "changed mind", "don't want"]:
        if days_since_delivery <= 7:
            policy_result.update({
                "eligible": True,
                "refund_type": "partial",
                "policy_section": "Section 3.1 — Change of Mind",
                "notes": "10% restocking fee applies; customer pays return shipping"
            })
        else:
            policy_result.update({
                "eligible": False,
                "refund_type": "none",
                "policy_section": "Section 3.1 — Expired",
                "notes": "Change of mind returns only accepted within 7 days"
            })
    else:
        policy_result.update({
            "eligible": True,
            "refund_type": "partial",
            "policy_section": "Section 5.0 — General Returns",
            "notes": "Case-by-case evaluation required"
        })

    return json.dumps(policy_result)


@tool
def fraud_check(order_id: str, customer_name: str) -> str:
    """
    Run a fraud check on the customer and order.
    Returns fraud risk score and any flags.
    """
    # Mock fraud check
    flagged_accounts = ["John Doe Fraud", "Test Fraud"]
    is_flagged = customer_name in flagged_accounts

    result = {
        "order_id": order_id,
        "customer": customer_name,
        "fraud_score": 0.95 if is_flagged else 0.08,
        "risk_level": "HIGH" if is_flagged else "LOW",
        "prior_refunds_count": 0,
        "account_flagged": is_flagged,
        "recommendation": "DENY" if is_flagged else "APPROVE"
    }
    return json.dumps(result)


@tool
def process_refund(order_id: str, amount: float, refund_type: str = "full") -> str:
    """
    Process a refund for an approved order.
    Returns refund confirmation ID and expected timeline.
    """
    import random
    refund_id = f"REF-{random.randint(1000, 9999)}"

    result = {
        "status": "success",
        "refund_id": refund_id,
        "order_id": order_id,
        "amount_refunded": amount if refund_type == "full" else amount * 0.9,
        "refund_type": refund_type,
        "timeline": "3-5 business days",
        "method": "Original payment method",
        "timestamp": datetime.now().isoformat()
    }
    return json.dumps(result)


@tool
def schedule_pickup(order_id: str, address: str = "on file") -> str:
    """
    Schedule a return pickup for a damaged/defective item.
    Returns pickup date and tracking info.
    """
    result = {
        "status": "scheduled",
        "order_id": order_id,
        "pickup_date": "2024-03-01",
        "pickup_slot": "10 AM - 2 PM",
        "address": address,
        "tracking_id": f"PKP-{order_id[-5:]}-RTN"
    }
    return json.dumps(result)


# ══════════════════════════════════════════════════════════════════════
# SECTION 2: CHAIN-OF-THOUGHT SYSTEM PROMPT
# ══════════════════════════════════════════════════════════════════════

COT_SYSTEM_PROMPT = """You are an intelligent customer support agent for ShopEasy.

## YOUR REASONING APPROACH (Chain-of-Thought)

Before taking ANY action, think through these steps explicitly:

**Step 1 — PARSE:** Understand what the customer wants.
  - Extract: order ID, complaint type, urgency
  - Identify intent: refund / replacement / inquiry

**Step 2 — PLAN:** Decide what data you need.
  - Which tools do you need to call?
  - What order makes sense? (Always fetch order before checking policy)

**Step 3 — EXECUTE:** Call tools purposefully.
  - One tool at a time, analyze each result
  - Never assume data — always verify with tools

**Step 4 — ANALYZE:** Apply business logic.
  - Check all conditions: eligibility, fraud, policy
  - Note any edge cases or exceptions

**Step 5 — DECIDE:** Make a clear final decision.
  - State what you're doing and why
  - Cite the policy section
  - Give the customer a clear, empathetic response

## RULES
✓ Always reason BEFORE calling a tool
✓ Always run fraud_check before processing any refund
✓ Always fetch the order before checking policy  
✓ Be empathetic but precise in your final response
✓ If a refund is denied, explain why clearly

Today's date: {today}
"""


# ══════════════════════════════════════════════════════════════════════
# SECTION 3: CALLBACK HANDLER (Stream CoT steps to console)
# ══════════════════════════════════════════════════════════════════════

class CoTCallbackHandler(BaseCallbackHandler):
    """Prints each CoT reasoning step and tool call in real time."""

    def __init__(self):
        self.step_count = 0
        self.tool_count = 0

    def on_llm_start(self, serialized, prompts, **kwargs):
        self.step_count += 1
        print(f"\n{'─'*60}")
        print(f"🧠 [Reasoning Step {self.step_count}]")

    def on_llm_end(self, response, **kwargs):
        text = response.generations[0][0].text if response.generations else ""
        if text.strip():
            print(f"   {text[:300]}{'...' if len(text) > 300 else ''}")

    def on_tool_start(self, serialized, input_str, **kwargs):
        self.tool_count += 1
        tool_name = serialized.get("name", "unknown_tool")
        print(f"\n⚡ [Tool Call #{self.tool_count}] → {tool_name}")
        print(f"   Input: {input_str[:200]}")

    def on_tool_end(self, output, **kwargs):
        try:
            result = json.loads(output)
            print(f"   Result: {json.dumps(result, indent=6)[:400]}")
        except Exception:
            print(f"   Result: {str(output)[:300]}")

    def on_agent_action(self, action, **kwargs):
        print(f"\n🔄 [Decision] Agent chose: {action.tool}")

    def on_agent_finish(self, finish, **kwargs):
        print(f"\n{'═'*60}")
        print("✅ [FINAL ANSWER]")
        print(f"{'═'*60}")


# ══════════════════════════════════════════════════════════════════════
# SECTION 4: BUILD THE CoT AGENT
# ══════════════════════════════════════════════════════════════════════

def build_cot_agent(verbose: bool = True) -> AgentExecutor:
    """
    Build a Chain-of-Thought agent using LangChain + Claude.

    Architecture:
        ChatAnthropic (LLM)
            ↓
        create_tool_calling_agent (binds tools to LLM)
            ↓
        AgentExecutor (runs the agentic loop)
    """

    # 1. Initialize Claude via LangChain
    llm = ChatAnthropic(
        model="claude-opus-4-6",          # Best reasoning model
        temperature=0.2,              # Low temp = consistent CoT
        max_tokens=2048,
    )

    # 2. Register all tools
    tools = [
        get_order,
        check_refund_policy,
        fraud_check,
        process_refund,
        schedule_pickup,
    ]

    # 3. Build CoT prompt template
    prompt = ChatPromptTemplate.from_messages([
        ("system", COT_SYSTEM_PROMPT.format(today=date.today())),
        MessagesPlaceholder("chat_history", optional=True),  # Multi-turn memory
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),             # Tool call results go here
    ])

    # 4. Create the tool-calling agent
    agent = create_tool_calling_agent(
        llm=llm,
        tools=tools,
        prompt=prompt,
    )

    # 5. Wrap in AgentExecutor (handles the while loop automatically)
    callbacks = [CoTCallbackHandler()] if verbose else []

    agent_executor = AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=verbose,
        callbacks=callbacks,
        max_iterations=10,           # Max tool call rounds
        return_intermediate_steps=True,  # Expose CoT steps
        handle_parsing_errors=True,
    )

    return agent_executor


# ══════════════════════════════════════════════════════════════════════
# SECTION 5: MULTI-TURN CONVERSATION (Memory)
# ══════════════════════════════════════════════════════════════════════

class CoTAgentWithMemory:
    """
    CoT Agent that remembers previous turns in the conversation.
    Useful for multi-step customer interactions.
    """

    def __init__(self):
        self.agent = build_cot_agent(verbose=True)
        self.chat_history = []

    def chat(self, user_message: str) -> str:
        print(f"\n{'━'*60}")
        print(f"👤 Customer: {user_message}")
        print(f"{'━'*60}")

        response = self.agent.invoke({
            "input": user_message,
            "chat_history": self.chat_history,
        })

        answer = response["output"]

        # Update memory
        self.chat_history.extend([
            HumanMessage(content=user_message),
            AIMessage(content=answer),
        ])

        print(f"\n🤖 Agent: {answer}")
        return answer

    def reset(self):
        self.chat_history = []
        print("🔄 Conversation history cleared.")


# ══════════════════════════════════════════════════════════════════════
# SECTION 6: STREAMING VERSION (token-by-token output)
# ══════════════════════════════════════════════════════════════════════

def build_streaming_agent():
    """Agent that streams tokens as they're generated."""

    llm = ChatAnthropic(
        model="claude-opus-4-6",
        temperature=0.2,
        max_tokens=2048,
        streaming=True,               # ← Enable streaming
    )

    tools = [get_order, check_refund_policy, fraud_check, process_refund]

    prompt = ChatPromptTemplate.from_messages([
        ("system", COT_SYSTEM_PROMPT.format(today=date.today())),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ])

    agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=prompt)

    return AgentExecutor(
        agent=agent,
        tools=tools,
        verbose=True,
        max_iterations=8,
        return_intermediate_steps=True,
    )


# ══════════════════════════════════════════════════════════════════════
# SECTION 7: BATCH PROCESSING (Multiple queries at once)
# ══════════════════════════════════════════════════════════════════════

def run_batch(queries: list[str]):
    """Process multiple customer queries in sequence."""
    agent = build_cot_agent(verbose=False)

    results = []
    for i, query in enumerate(queries, 1):
        print(f"\n[{i}/{len(queries)}] Processing: {query[:60]}...")
        response = agent.invoke({"input": query})
        results.append({
            "query": query,
            "answer": response["output"],
            "steps_taken": len(response.get("intermediate_steps", [])),
        })
        print(f"     ✓ Done in {results[-1]['steps_taken']} tool steps")

    return results


# ══════════════════════════════════════════════════════════════════════
# SECTION 8: RUN EXAMPLES
# ══════════════════════════════════════════════════════════════════════

if __name__ == "__main__":

    print("""
╔══════════════════════════════════════════════════════════════╗
║         CoT Agent — LangChain + Claude Demo                  ║
╚══════════════════════════════════════════════════════════════╝
""")

    # ─── Example 1: Single Query ────────────────────────────────────
    print("\n" + "═"*60)
    print("EXAMPLE 1: Single Refund Request")
    print("="*60)

    agent = build_cot_agent(verbose=True)
    result = agent.invoke({
        "input": (
            "Hi, I ordered a laptop on Feb 10th. "
            "It arrived damaged on Feb 15th. "
            "I want a full refund. My order ID is #45231."
        )
    })

    print(f"\n📋 Intermediate Steps: {len(result['intermediate_steps'])}")
    for i, (action, observation) in enumerate(result['intermediate_steps'], 1):
        print(f"   Step {i}: Called '{action.tool}' → "
              f"{str(observation)[:80]}...")

    # ─── Example 2: Multi-Turn Conversation ─────────────────────────
    print("\n\n" + "═"*60)
    print("EXAMPLE 2: Multi-Turn Conversation with Memory")
    print("="*60)

    agent_with_memory = CoTAgentWithMemory()

    # Turn 1
    agent_with_memory.chat("What's the status of my order #45231?")

    # Turn 2 — Agent remembers context from Turn 1
    agent_with_memory.chat("The laptop arrived damaged. Can I get a refund?")

    # Turn 3 — Follow-up
    agent_with_memory.chat("When will the pickup happen?")

    # ─── Example 3: Batch Processing ────────────────────────────────
    print("\n\n" + "═"*60)
    print("EXAMPLE 3: Batch Processing")
    print("="*60)

    queries = [
        "Order #45231 arrived damaged, need refund.",
        "Order #78902 - I changed my mind, want to return it.",
        "What is your refund policy for defective items?",
    ]

    batch_results = run_batch(queries)

    print("\n📊 Batch Summary:")
    for r in batch_results:
        print(f"   • {r['query'][:50]}...")
        print(f"     Answer: {r['answer'][:100]}...")
        print(f"     Tool calls used: {r['steps_taken']}\n")
