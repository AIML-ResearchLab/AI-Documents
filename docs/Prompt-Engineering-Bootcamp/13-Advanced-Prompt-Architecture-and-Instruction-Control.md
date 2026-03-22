# 13 - Advanced Prompt Architecture and Instruction Control

## 13.1 Prompt as System Architecture
In production, prompts are part of a layered architecture:
1. Global policy/system constraints
2. Task-specific developer instructions
3. User request
4. Runtime context and tool outputs

## 13.2 Instruction Priority Design
Define strict instruction precedence and avoid ambiguous overlap.

Pattern:
- Policy first
- Safety second
- Task objectives third
- Style last

## 13.3 Prompt Segmentation
Use explicit sections with delimiters:
- `ROLE`
- `OBJECTIVE`
- `CONTEXT`
- `RULES`
- `OUTPUT_SCHEMA`

## 13.4 Conflict Resolution Rules
Include hard rules for conflicts:
- ignore lower-priority conflicting text
- report blocked requests with reason code

## 13.5 Contract-First Prompting
Design prompts backward from required output contract and downstream system requirements.

## 13.6 Real-Time Example
Customer support router:
- policy section blocks data leakage
- routing section selects queue
- response section returns structured JSON

## 13.7 Anti-Drift Rule
Freeze core instruction blocks and version each change with rationale and metric impact.

