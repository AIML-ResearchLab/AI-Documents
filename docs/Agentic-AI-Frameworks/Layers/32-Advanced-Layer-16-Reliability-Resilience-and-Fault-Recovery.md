# 32 - Advanced Layer 16: Reliability, Resilience, and Fault Recovery

## 32.1 Purpose
Maintain service continuity under model, tool, and infrastructure failures.

## 32.2 Core Decisions
Design retries, circuit breakers, checkpoint resume, and compensation logic.

## 32.3 Design Artifacts
Failure mode catalog, resilience test suite, and recovery runbooks.

## 32.4 Failure Mode
No recovery orchestration causes prolonged outages and inconsistent state.

## 32.5 Real-Time Example
System fails over to fallback model tier during primary outage.
