# 03 - Base Protocol: JSON-RPC Messages and Schemas

## 3.1 Message Types
- requests
- responses (result or error)
- notifications

## 3.2 Request/Response Rules
Request IDs must be unique within session and must not be null.

## 3.3 Notifications
One-way messages with no response expected.

## 3.4 Schema Usage
MCP relies on JSON Schema (default 2020-12) for tool/resource/prompt contracts.

