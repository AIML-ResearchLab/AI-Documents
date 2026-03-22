# 18 - Agent Frameworks, Memory, and Orchestration

## 18.1 Agent Roles
Common roles:
- planner
- executor
- verifier
- policy checker

## 18.2 Memory Types
- session memory (current thread)
- workflow memory (task state)
- long-term memory (approved facts/preferences)

## 18.3 Memory Governance
- store only needed information
- attach provenance and expiry
- redact sensitive content

## 18.4 Orchestration Models
- state machine workflows
- graph-based task orchestration
- event-driven agent triggers

## 18.5 Stopping Criteria
Agents need explicit stop rules:
- maximum steps
- confidence gate
- timeout and fallback

## 18.6 Real-Time Example
Research assistant:
1. planner creates query plan
2. retriever fetches evidence
3. writer drafts summary
4. verifier checks citation coverage

## 18.7 Reliability Rules
Never allow autonomous side-effect actions without policy and confirmation checks.

