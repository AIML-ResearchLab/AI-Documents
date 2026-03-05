# 06 - Persistence, Checkpointing, and Durable Execution

## 6.1 Persistence Purpose
Checkpointing allows workflow resumption after failures or pauses.

## 6.2 Checkpoint Stores
Use durable backing stores for production-grade recoverability.

## 6.3 Resume Semantics
Restart from last consistent checkpoint instead of replaying full workflow.

## 6.4 Operational Controls
Design retention and cleanup policies for checkpoint storage.

## 6.5 Real-Time Example
Long-running compliance flow resumes after restart without losing approval history.
