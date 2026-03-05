# 04 - Lifecycle: Initialization, Version, and Capability Negotiation

## 4.1 Lifecycle Phases
1. initialization
2. operation
3. shutdown

## 4.2 Initialization
Client sends `initialize`; server responds with negotiated version and capabilities; client sends `notifications/initialized`.

## 4.3 Capability Negotiation
Define which features are active for the session (tools/resources/prompts/roots/sampling/elicitation/etc.).

## 4.4 Versioning
Protocol uses date-based versions (for example, `2025-11-25`).

