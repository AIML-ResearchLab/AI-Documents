# 04 - Tasks, Outputs, Guardrails, and Human Input

## 4.1 Task Role
A task defines what must be done, by which agent, with expected output contract.

## 4.2 Output Modes
Task outputs can be raw text, JSON, or structured Pydantic outputs.

## 4.3 Guardrails
Single or chained guardrails validate and transform outputs before acceptance.

## 4.4 Human Review
`human_input` adds approval checkpoints for sensitive or high-impact decisions.

## 4.5 Real-Time Example
Compliance task blocks release until guardrail checks and human review both pass.
