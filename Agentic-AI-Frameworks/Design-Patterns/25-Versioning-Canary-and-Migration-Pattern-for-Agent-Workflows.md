# 25 - Versioning, Canary, and Migration Pattern for Agent Workflows

## 25.1 Pattern Intent
Evolve workflows safely without breaking production behavior.

## 25.2 Version Strategy
Version prompts, tool schemas, and state contracts independently.

## 25.3 Canary Rollout
Expose new versions to small traffic slices before full release.

## 25.4 Migration Safety
Use dual-run and rollback checkpoints for critical flows.

## 25.5 Real-Time Example
Workflow v2 rolls back automatically after canary quality regression.
