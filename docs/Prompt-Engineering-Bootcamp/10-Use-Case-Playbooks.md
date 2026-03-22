# 10 - Use Case Playbooks

## 10.1 Customer Support Triage
Goal: classify tickets, detect urgency, draft response.

Prompt pattern:
- Role: support triage assistant
- Output: category, priority, entities, reply, internal_actions
- Constraints: no hallucination, JSON only

## 10.2 Sales Call Intelligence
Goal: summarize calls into CRM-ready records.

Output schema:
- customer_needs
- objections
- buying_signals
- next_actions with owner/date

## 10.3 Marketing Content Workflow
Goal: generate campaign drafts aligned to brand rules.

Controls:
- audience profile
- messaging pillars
- banned claims
- required CTA format

## 10.4 Business Analytics Assistant
Goal: turn raw KPI notes into executive summaries.

Constraints:
- include numeric deltas
- classify risk level
- list top 3 actions

## 10.5 Engineering Copilot
Goal: produce safe code changes with tests.

Prompt requirements:
- specify language/runtime
- include acceptance tests
- require edge-case coverage
- request diff-style output where needed

## 10.6 Legal/Policy Summarization
Goal: summarize policy text with obligations and deadlines.

Guardrails:
- cite section references
- avoid legal advice framing if disallowed
- mark ambiguous clauses

## 10.7 HR Assistant
Goal: convert policy docs into employee-friendly Q&A.

Rules:
- neutral tone
- no confidential details
- include escalation contact

## 10.8 Finance Ops Assistant
Goal: classify expense anomalies.

Output:
- anomaly_type
- evidence
- recommended action
- confidence

