"""
TRUE Tree-of-Thoughts (ToT) Investment Agent
=============================================
Genuine multi-level ToT — branching + evaluation at EVERY depth level.

Tree Structure (3 levels deep, 3 branches each):
  Level 0: Root (ticker)
  Level 1: Research Angle     (Fundamental / Technical / Sentiment)
  Level 2: Sub-Strategy       (e.g., Fundamental → Revenue / Margins / Valuation)
  Level 3: Tool Execution     (e.g., Valuation → P/E / DCF / Peer Compare)

At each level:
  - Generate N child thoughts
  - Score each: sure / maybe / impossible
  - Prune impossible, expand sure/maybe (BFS)
  - Backtrack automatically by not adding bad nodes to frontier

Install:
    pip install langchain langchain-community langchain-openai openai duckduckgo-search

Run:
    export OPENAI_API_KEY="sk-..."
    python true_tot_agent.py
"""

import os
import json
from dataclasses import dataclass, field
from collections import deque
from langchain_openai import ChatOpenAI
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import tool
from langchain_core.messages import HumanMessage

# ─────────────────────────────────────────────────────────────
# CONFIG
# ─────────────────────────────────────────────────────────────
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "your-api-key-here")
MODEL          = "gpt-4o"
MAX_DEPTH      = 3       # tree depth (levels of reasoning)
BRANCH_N       = 3       # children per node
BEAM_WIDTH     = 2       # max nodes to expand per level (beam search)


# ─────────────────────────────────────────────────────────────
# DATA STRUCTURES
# ─────────────────────────────────────────────────────────────
@dataclass
class ThoughtNode:
    thought:   str
    depth:     int                        = 0
    score:     str                        = "unscored"   # sure/maybe/impossible
    parent:    "ThoughtNode | None"       = None
    children:  list                       = field(default_factory=list)
    findings:  str                        = ""           # tool output at leaf

    def path_from_root(self) -> list[str]:
        """Return list of thoughts from root → this node."""
        chain, node = [], self
        while node:
            chain.append(node.thought)
            node = node.parent
        return list(reversed(chain))

    def context_str(self) -> str:
        """Formatted reasoning path for prompts."""
        path = self.path_from_root()
        return "\n".join(f"  Level {i}: {t}" for i, t in enumerate(path))

    def __repr__(self):
        indent = "  " * self.depth
        icon = {"sure": "✅", "maybe": "⚠️ ", "impossible": "❌", "unscored": "❓"}
        return f"{indent}{icon.get(self.score,'❓')} [L{self.depth}] {self.thought[:80]}"


# ─────────────────────────────────────────────────────────────
# LLM INSTANCES
# ─────────────────────────────────────────────────────────────
llm       = ChatOpenAI(model=MODEL, temperature=0.7, api_key=OPENAI_API_KEY)
llm_eval  = ChatOpenAI(model=MODEL, temperature=0.0, api_key=OPENAI_API_KEY)


# ─────────────────────────────────────────────────────────────
# TOOLS
# ─────────────────────────────────────────────────────────────
_search = DuckDuckGoSearchRun()

@tool
def web_search(query: str) -> str:
    """Search the web for current financial data and news."""
    return _search.run(query)

@tool
def pe_ratio_analyzer(current_price: float, eps: float, industry_avg_pe: float) -> str:
    """Compute and interpret P/E ratio vs industry average."""
    if eps <= 0:
        return "EPS non-positive — company unprofitable, P/E not meaningful."
    pe    = current_price / eps
    delta = ((pe - industry_avg_pe) / industry_avg_pe) * 100
    verdict = ("OVERVALUED" if delta > 15 else
               "UNDERVALUED" if delta < -15 else "FAIRLY VALUED")
    return f"P/E: {pe:.1f} | Industry: {industry_avg_pe} | Δ {delta:+.1f}% → {verdict}"

@tool
def growth_calculator(revenue_current: float, revenue_previous: float,
                       eps_current: float, eps_previous: float) -> str:
    """Calculate YoY revenue and EPS growth rates."""
    rev_growth = ((revenue_current - revenue_previous) / revenue_previous) * 100
    eps_growth = ((eps_current - eps_previous) / eps_previous) * 100 if eps_previous else 0
    return (f"Revenue Growth YoY: {rev_growth:+.1f}% | "
            f"EPS Growth YoY: {eps_growth:+.1f}%")

TOOL_MAP = {t.name: t for t in [web_search, pe_ratio_analyzer, growth_calculator]}


# ─────────────────────────────────────────────────────────────
# LEVEL DEFINITIONS
# Maps depth → what kind of thoughts to generate
# ─────────────────────────────────────────────────────────────
LEVEL_ROLES = {
    1: "research angle (e.g., Fundamental Analysis, Technical Analysis, Sentiment Analysis)",
    2: "sub-strategy within the chosen angle (e.g., Revenue Trends, Margin Analysis, Valuation)",
    3: "specific analysis task with a concrete tool action (web search / P/E check / growth calc)",
}

LEVEL_TOOL_HINT = {
    3: """At this level, each thought MUST specify:
- The exact tool to use: web_search / pe_ratio_analyzer / growth_calculator
- The exact inputs to pass
Format each thought as: "Use <tool>: <what to look up or calculate>"
"""
}


# ─────────────────────────────────────────────────────────────
# CORE TOT OPERATIONS
# ─────────────────────────────────────────────────────────────

def generate_children(ticker: str, parent: ThoughtNode, n: int = BRANCH_N) -> list[ThoughtNode]:
    """
    Generate N child thoughts for a given node.
    Thoughts are context-aware — they know the full path from root.
    """
    depth       = parent.depth + 1
    role        = LEVEL_ROLES.get(depth, "next reasoning step")
    tool_hint   = LEVEL_TOOL_HINT.get(depth, "")
    context     = parent.context_str()

    prompt = f"""
You are an investment research AI analyzing stock: {ticker}

Reasoning path so far:
{context}

Your task: Generate exactly {n} DISTINCT {role}s to explore next.
{tool_hint}
Rules:
- Each must be meaningfully different (not variations of the same idea)
- Each must logically follow from the path above
- Be specific to {ticker}

Respond ONLY with a JSON array of {n} strings.
Example: ["thought one", "thought two", "thought three"]
"""
    raw = llm.invoke([HumanMessage(content=prompt)]).content.strip()
    raw = _strip_json(raw)
    thoughts = json.loads(raw)

    children = [
        ThoughtNode(thought=t, depth=depth, parent=parent)
        for t in thoughts[:n]
    ]
    parent.children = children
    return children


def evaluate_children(ticker: str, parent: ThoughtNode,
                       children: list[ThoughtNode]) -> list[ThoughtNode]:
    """
    Score each child node: sure / maybe / impossible
    Evaluation is context-aware.
    """
    context    = parent.context_str()
    items      = "\n".join(f"{i+1}. {c.thought}" for i, c in enumerate(children))
    depth      = children[0].depth if children else 1
    role       = LEVEL_ROLES.get(depth, "reasoning step")

    prompt = f"""
You are a senior investment analyst evaluating research directions for {ticker}.

Reasoning path so far:
{context}

Candidate {role}s to evaluate:
{items}

Score each on research quality and likely yield of actionable insight:
- "sure"       → Strong direction, will produce clear signal
- "maybe"      → Reasonable but uncertain value
- "impossible" → Irrelevant, redundant, or won't work for {ticker}

Respond ONLY with a JSON array of scores in the same order.
Example: ["sure", "maybe", "impossible"]
"""
    raw    = llm_eval.invoke([HumanMessage(content=prompt)]).content.strip()
    raw    = _strip_json(raw)
    scores = json.loads(raw)

    for node, score in zip(children, scores):
        node.score = score

    return children


def execute_leaf(ticker: str, node: ThoughtNode) -> str:
    """
    At MAX_DEPTH, execute the thought as a real tool call.
    Parse the thought to determine which tool to invoke.
    """
    thought = node.thought.lower()
    context = node.context_str()

    # Determine tool from thought text
    if "web_search" in thought or "search" in thought:
        # Extract what to search
        query_prompt = f"""
Given this research task: "{node.thought}"
And context: {context}
Write a precise 6-word web search query for {ticker}.
Respond with ONLY the query string, no quotes.
"""
        query  = llm_eval.invoke([HumanMessage(content=query_prompt)]).content.strip()
        result = web_search.invoke(query)

    elif "pe_ratio" in thought or "p/e" in thought or "valuation" in thought:
        # Ask LLM to estimate inputs (in real system, pull from API)
        est_prompt = f"""
For stock {ticker}, provide estimated values for P/E calculation.
Respond ONLY with JSON: {{"price": float, "eps": float, "industry_avg_pe": float}}
Use reasonable estimates based on your knowledge.
"""
        raw    = llm_eval.invoke([HumanMessage(content=est_prompt)]).content.strip()
        params = json.loads(_strip_json(raw))
        result = pe_ratio_analyzer.invoke(params)

    elif "growth" in thought or "revenue" in thought or "eps" in thought:
        est_prompt = f"""
For stock {ticker}, provide estimated values for growth calculation.
Respond ONLY with JSON: {{
  "revenue_current": float, "revenue_previous": float,
  "eps_current": float, "eps_previous": float
}}
Use reasonable estimates in billions for revenue.
"""
        raw    = llm_eval.invoke([HumanMessage(content=est_prompt)]).content.strip()
        params = json.loads(_strip_json(raw))
        result = growth_calculator.invoke(params)

    else:
        # Fallback: web search
        result = web_search.invoke(f"{ticker} {node.thought[:60]}")

    node.findings = result
    return result


# ─────────────────────────────────────────────────────────────
# BFS TREE SEARCH (TRUE TOT)
# ─────────────────────────────────────────────────────────────

def run_tot_bfs(ticker: str) -> list[ThoughtNode]:
    """
    True BFS Tree-of-Thoughts:
    - Expand frontier level by level
    - At each level: generate → evaluate → prune → select top BEAM_WIDTH
    - At MAX_DEPTH: execute real tools
    - Backtracking = automatic (pruned nodes never enter frontier)
    """
    root     = ThoughtNode(thought=f"Analyze {ticker} stock for investment decision", depth=0)
    frontier = deque([root])
    leaves   = []                    # completed paths with tool findings

    print(f"\n{'#'*65}")
    print(f"  TRUE ToT — BFS Search — {ticker.upper()}")
    print(f"  Max Depth: {MAX_DEPTH} | Branches: {BRANCH_N} | Beam: {BEAM_WIDTH}")
    print(f"{'#'*65}")

    while frontier:
        # Process all nodes at current depth (BFS level)
        level_nodes = []
        while frontier:
            level_nodes.append(frontier.popleft())

        current_depth = level_nodes[0].depth
        print(f"\n{'─'*65}")
        print(f"  LEVEL {current_depth} → generating children (depth {current_depth+1})")
        print(f"{'─'*65}")

        next_level_candidates = []

        for parent in level_nodes:
            print(f"\n  Expanding: [{parent.depth}] {parent.thought[:70]}")

            # ── Generate N children ──
            children = generate_children(ticker, parent, n=BRANCH_N)

            # ── Evaluate children ──
            children = evaluate_children(ticker, parent, children)

            # ── Print scored children ──
            for child in children:
                icon = {"sure":"✅","maybe":"⚠️ ","impossible":"❌"}.get(child.score,"❓")
                print(f"    {icon} [{child.score:>10}] {child.thought[:70]}")

            # ── Prune impossible, collect survivors ──
            survivors = [c for c in children if c.score != "impossible"]
            next_level_candidates.extend(survivors)

        # ── Beam selection: keep top BEAM_WIDTH per level ──
        priority = {"sure": 0, "maybe": 1}
        next_level_candidates.sort(key=lambda n: priority.get(n.score, 2))
        selected = next_level_candidates[:BEAM_WIDTH]

        print(f"\n  ✂️  Pruned to {len(selected)} node(s) via beam search (width={BEAM_WIDTH})")
        for s in selected:
            print(f"     → [L{s.depth}] {s.thought[:75]}")

        next_depth = current_depth + 1

        if next_depth >= MAX_DEPTH:
            # ── Leaf level: execute real tools ──
            print(f"\n{'─'*65}")
            print(f"  LEAF LEVEL {next_depth} — Executing Tools")
            print(f"{'─'*65}")

            # Generate leaf children and execute
            for parent in selected:
                leaf_children = generate_children(ticker, parent, n=BRANCH_N)
                leaf_children = evaluate_children(ticker, parent, leaf_children)
                survivors     = [c for c in leaf_children if c.score != "impossible"]

                for leaf in survivors[:BEAM_WIDTH]:
                    print(f"\n  🔧 Tool execution for: {leaf.thought[:70]}")
                    result = execute_leaf(ticker, leaf)
                    print(f"  📊 Result: {result[:200]}")
                    leaves.append(leaf)
        else:
            # Push selected to next BFS level
            for node in selected:
                frontier.append(node)

    return leaves


# ─────────────────────────────────────────────────────────────
# SYNTHESIS
# ─────────────────────────────────────────────────────────────

def synthesize(ticker: str, leaves: list[ThoughtNode]) -> str:
    """Synthesize all leaf findings into a final recommendation."""

    findings_text = ""
    for i, leaf in enumerate(leaves, 1):
        path = " → ".join(leaf.path_from_root())
        findings_text += f"\n--- Finding {i} ---\n"
        findings_text += f"Path: {path}\n"
        findings_text += f"Data: {leaf.findings}\n"

    prompt = f"""
You are a portfolio manager making a final investment decision on {ticker}.

Your research team explored multiple reasoning branches and gathered:
{findings_text}

Produce a structured final report:

RECOMMENDATION: BUY / HOLD / SELL
Confidence: X%

BULL CASE (2 points):
BEAR CASE (2 points):
KEY METRICS:
TIME HORIZON:
STOP LOSS LEVEL:
"""
    return llm_eval.invoke([HumanMessage(content=prompt)]).content


# ─────────────────────────────────────────────────────────────
# UTILITIES
# ─────────────────────────────────────────────────────────────

def _strip_json(raw: str) -> str:
    """Strip markdown code fences from LLM JSON output."""
    raw = raw.strip()
    if raw.startswith("```"):
        parts = raw.split("```")
        raw = parts[1] if len(parts) > 1 else raw
        if raw.startswith("json"):
            raw = raw[4:]
    return raw.strip()


def print_tree_summary(leaves: list[ThoughtNode]):
    """Print all explored paths."""
    print(f"\n{'='*65}")
    print(f"  EXPLORED PATHS SUMMARY")
    print(f"{'='*65}")
    for i, leaf in enumerate(leaves, 1):
        path = " → ".join(leaf.path_from_root())
        print(f"\n  Path {i}: {path}")
        print(f"  Finding: {leaf.findings[:150]}...")


# ─────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    ticker = "NVDA"

    # Run true multi-level ToT BFS
    leaves = run_tot_bfs(ticker)

    # Summary of all explored branches
    print_tree_summary(leaves)

    # Final synthesis
    print(f"\n{'='*65}")
    print(f"  FINAL RECOMMENDATION")
    print(f"{'='*65}")
    recommendation = synthesize(ticker, leaves)
    print(recommendation)

    # Save report
    out = f"{ticker}_true_tot_report.txt"
    with open(out, "w") as f:
        f.write(f"TRUE ToT INVESTMENT REPORT — {ticker}\n")
        f.write("="*65 + "\n\n")
        for i, leaf in enumerate(leaves, 1):
            f.write(f"Path {i}: {' → '.join(leaf.path_from_root())}\n")
            f.write(f"Finding: {leaf.findings}\n\n")
        f.write("="*65 + "\n")
        f.write("FINAL RECOMMENDATION\n")
        f.write("="*65 + "\n")
        f.write(recommendation)

    print(f"\n  Report saved → {out}")