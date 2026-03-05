# 03 - Planner-Executor Pattern

## 3.1 Pattern Intent
Split task decomposition from action execution for clarity and control.

## 3.2 Planner Responsibilities
Generate ordered action plans with confidence and dependency metadata.

## 3.3 Executor Responsibilities
Run actions deterministically and report verifiable outcomes.

## 3.4 Tradeoffs
Improves auditability but adds orchestration complexity.

## 3.5 Real-Time Example
Incident planner sequences diagnostics while executors run probes and collect evidence.
