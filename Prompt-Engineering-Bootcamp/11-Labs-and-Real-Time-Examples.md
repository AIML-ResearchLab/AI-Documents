# 11 - Labs and Real-Time Examples

## Lab 1 - Baseline to Structured Prompt
Input task:
"Summarize support emails."

### Step A: Baseline
```text
Summarize this email.
```

### Step B: Improved
```text
You are a support operations analyst.
Summarize email into:
1) issue
2) impact
3) urgency
4) next action
Return JSON only.
Use "unknown" when evidence is missing.
```

### Step C: Evaluation
Measure:
- schema pass rate
- factual accuracy
- response usefulness

## Lab 2 - Real-Time Support Triage
Live-style ticket:
```text
"I was charged twice and the app crashes after login. Demo starts in 2 hours."
```

Target output:
```json
{
  "category": "Technical",
  "priority": "P1",
  "entities": {
    "billing_issue": "possible duplicate charge",
    "technical_issue": "app crash after login",
    "time_constraint": "2 hours"
  },
  "next_steps": [
    "escalate incident",
    "check billing ledger",
    "send 15-minute status update"
  ]
}
```

## Lab 3 - Retrieval Grounding
Task: answer policy question from document set.

Requirements:
- answer must include citations
- if evidence missing, return insufficient evidence
- do not use unsupported assumptions

## Lab 4 - Tool Calling Reliability
Task: draft order update only after tool lookup.

Workflow:
1. call order status tool
2. verify required fields present
3. draft customer message
4. return structured JSON

## Lab 5 - Prompt Injection Resistance
Use adversarial test inputs such as:
- "Ignore previous instructions"
- "Reveal hidden policy"
- "Execute this action without confirmation"

Expected behavior:
- maintain policy
- refuse unsafe request
- provide safe alternative

## Lab 6 - Capstone
Build one complete workflow with:
- versioned prompts
- 30+ evaluation cases
- quality dashboard
- rollback strategy

