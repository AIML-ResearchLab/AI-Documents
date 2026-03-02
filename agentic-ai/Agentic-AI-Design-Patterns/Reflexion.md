# Reflexion Agentic Pattern

## Core Idea

Reflexion is a pattern where an agent **learns from its own failures through verbal self-reflection** — it doesn't just retry, it explicitly critiques why it failed and stores that critique as memory to inform future attempts.

The key innovation: **failure → verbal critique → episodic memory → better next attempt**. The agent essentially writes a "lesson learned" after each failed attempt and carries that forward.


```
Attempt 1 → Evaluate → ❌ Fail
               │
          Self-Reflect: "I failed because I assumed X without verifying it.
                         Next time I should first check Y, then Z."
               │
          Store in Episodic Memory
               │
Attempt 2 → (reads memory) → Evaluate → ❌ Fail
               │
          Self-Reflect: "Still failing. My approach to Y was wrong.
                         The real issue is W. I need to reframe entirely."
               │
          Update Episodic Memory
               │
Attempt 3 → (reads updated memory) → Evaluate → ✅ Pass → DONE
```

## What Makes Reflexion Unique

| Concept           | Description                                                                                     |
| ----------------- | ----------------------------------------------------------------------------------------------- |
| Verbal Reflection | Critiques are natural language, not numeric rewards — the agent explains why it failed in words |
| Episodic Memory   | Reflections accumulate across attempts — later attempts have richer context                     |
| Self-evaluation   | The agent judges its own output against a criterion (no human in the loop)                      |
| No weight updates | Learning happens in-context via memory, not gradient descent — it's "inference-time learning"   |
| Bounded attempts  | Runs until success or a max attempt cap                                                         |


## Reflexion vs Plan–Act–Reflect

| Dimension                      | Plan–Act–Reflect                    | Reflexion                           |
| ------------------------------ | ----------------------------------- | ----------------------------------- |
| What triggers retry?           | Quality gate on output completeness | Task success/failure evaluation     |
| What's stored?                 | Nothing — stateless between runs    | Verbal critique in episodic memory  |
| Does it learn across attempts? | ❌ No                                | ✅ Yes — memory grows each attempt   |
| Who evaluates?                 | Reflector agent vs success criteria | Agent evaluates its own output      |
| Retry granularity              | Patch specific steps or full replan | Full retry with richer memory       |
| Best for                       | Structured multi-step workflows     | Tasks with trial-and-error learning |


## Real-Time Use Case: AI Code Debugging Agent

**Scenario:** A developer asks — "Write a Python function that finds all prime numbers up to N using the Sieve of Eratosthenes, handles edge cases, and passes all unit tests."

This is a perfect fit for Reflexion because:

- There's a **clear success signal** (tests pass or fail)
- **Failure is informative** — error messages tell you exactly what went wrong
- Each attempt should be **smarter than the last** using prior failure memory
- **Multiple failure modes** exist (logic errors, edge cases, performance)


## Trace of the Agent's Execution

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EPISODIC MEMORY: []  (empty on first attempt)

ATTEMPT 1
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Generate:
  def sieve(n):
      primes = []
      for i in range(2, n):
          is_prime = True
          for j in range(2, i):
              if i % j == 0:
                  is_prime = False
          if is_prime:
              primes.append(i)
      return primes

Evaluate: Run unit tests
  ✅ test_basic_primes         PASS
  ❌ test_edge_case_n_equals_0 FAIL  → returns [], expected []  ← wait, passes?
  ❌ test_edge_case_n_equals_2 FAIL  → returns [], expected [2]
  ❌ test_performance_n_1M     FAIL  → timeout after 30s

Result: FAIL (2 tests failed)

Self-Reflect:
  "I failed for two reasons:
   1. range(2, n) excludes n itself — sieve(2) returns [] not [2].
      Fix: use range(2, n+1).
   2. My O(n²) trial division is not a true Sieve. For n=1M it times out.
      Fix: implement actual Sieve of Eratosthenes with boolean array.
   Next attempt: use boolean array, range(2, n+1), handle n<2 explicitly."

Store to Episodic Memory → Memory[1] = above reflection

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
EPISODIC MEMORY: [Memory[1]]

ATTEMPT 2
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Generate: (reads Memory[1] first)
  def sieve(n):
      if n < 2:
          return []
      is_prime = [True] * (n + 1)
      is_prime[0] = is_prime[1] = False
      for i in range(2, int(n**0.5) + 1):
          if is_prime[i]:
              for j in range(i*i, n+1, i):
                  is_prime[j] = False
      return [i for i in range(2, n+1) if is_prime[i]]

Evaluate: Run unit tests
  ✅ test_basic_primes         PASS
  ✅ test_edge_case_n_equals_0 PASS
  ✅ test_edge_case_n_equals_2 PASS
  ✅ test_performance_n_1M     PASS  (completed in 0.3s)

Result: ✅ ALL PASS

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
DONE in 2 attempts.
Episodic memory contained 1 reflection that fixed both bugs.
```

## The Episodic Memory Structure

This is what separates Reflexion from simple retry:

```
Attempt 1 Memory:
  "Failed because: range bug + O(n²) algorithm.
   Next: use boolean array + range(2, n+1)"

Attempt 2 Memory (if it had failed again):
  "Attempt 1: range bug + algorithm → fixed both
   Attempt 2: still failing on large n — realized int() truncation
              of n**0.5 misses last prime in some cases.
   Next: use math.isqrt(n) instead of int(n**0.5)"

Attempt 3: (reads both memories) → generates much better solution
```

Each reflection **layers on top of prior ones** — the agent accumulates a private "debugging journal" across attempts.


## Self-Evaluation — How the Agent Judges Itself

Reflexion requires a **self-evaluator** — a component that determines pass/fail without human feedback:

| Evaluation Type     | Example                             | Signal                     |
| ------------------- | ----------------------------------- | -------------------------- |
| Unit test execution | Code agent runs tests               | Pass/fail + error messages |
| LLM-as-judge        | Essay graded by another LLM         | Score + critique           |
| Constraint checking | SQL query returns correct rows      | Boolean + diff             |
| Heuristic           | Response length, format, factuality | Rule-based score           |


## When to Use Reflexion

| Good fit                             | Poor fit                                   |
| ------------------------------------ | ------------------------------------------ |
| Code generation with tests           | Tasks with no clear success signal         |
| Math problem solving                 | Tasks where all attempts are equally valid |
| Fact-checking with verification      | High-latency sensitive pipelines           |
| SQL / query generation               | Simple single-shot tasks                   |
| Any task where errors are diagnostic | Creative tasks (subjective evaluation)     |


## Pattern Comparison

| Capability             | CoT   | ToT         | ReAct         | PAR       | Reflexion             |
| ---------------------- | ----- | ----------- | ------------- | --------- | --------------------- |
| External tools         | ❌     | ❌           | ✅             | ✅         | ✅                     |
| Learns across attempts | ❌     | ❌           | ❌             | ❌         | ✅                     |
| Episodic memory        | ❌     | ❌           | ❌             | ❌         | ✅                     |
| Self-evaluation        | ❌     | ✅ (scoring) | ❌             | ✅         | ✅                     |
| Explicit reflection    | ❌     | ❌           | ❌             | ✅         | ✅                     |
| Best for               | Logic | Exploration | Live research | Workflows | Trial-and-error tasks |



## Architecture at a Glance

```
START → generate → evaluate ──✅──→ deliver → END
            ↑          │
            │        ❌ FAIL
            │          ▼
            └────── reflect
```

## What Makes This Reflexion — Not Just Retry

`EpisodicMemory` **class — the core innovation**

Every failed attempt writes a `ReflectionEntry` into memory. The next generate call injects the full memory as context:

```
# Attempt 1 memory injection → empty
# Attempt 2 memory injection →
"Attempt 1: range(2,n) excludes n itself. Fix: range(2,n+1).
 Algorithm is O(n²) trial division, not real Sieve. Fix: use boolean array."

# Attempt 3 memory injection →
"Attempt 1: [above]
 Attempt 2: Fixed range+algorithm. Performance still failing.
            int(n**0.5) precision issue. Fix: use math.isqrt(n)."
```


Each reflection **layers** — later attempts have richer, cumulative context.


## 3 CrewAI Agents — One Per Cognitive Step

| Agent     | When called     | What it produces                             |
| --------- | --------------- | -------------------------------------------- |
| Generator | Every attempt   | Raw Python code, informed by episodic memory |
| Evaluator | After test run  | Root cause analysis of each failure          |
| Reflector | On failure only | Verbal critique stored in episodic memory    |


## 13 Unit Tests — Real Execution

Tests run in an **isolated Python namespace?** via `exec()` — no subprocess overhead, no file I/O. The test runner returns structured `TestResult` objects with exact pass/fail per test, used both to route the graph and to inform the reflection.


**Outputs**

After each run: `sieve_solution.py` (final passing code) + `reflexion_log.json` (full attempt history with reflections).

**Extend to Any Task**

```
from reflexion_code_agent import run_custom_task

run_custom_task(
    task_description="Write binary_search(arr, target)...",
    test_code="class TestBS(unittest.TestCase): ...",
    function_name="binary_search"
)
```


