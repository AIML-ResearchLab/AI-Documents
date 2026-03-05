# 23 - APIs, Microservices, and Contract-First AI Systems

## 23.1 API Design Principles
- explicit request/response schema
- deterministic error model
- backward-compatible versioning

## 23.2 FastAPI Patterns
- pydantic validation
- dependency injection
- typed response models

## 23.3 Service Boundaries
Separate:
- inference service
- feature service
- model registry service

## 23.4 Sync vs Async APIs
- sync for short CPU tasks
- async for I/O-heavy workflows and external integrations

## 23.5 Idempotency and Retries
Use idempotency keys for write-like operations and retried requests.

## 23.6 API Security Basics
- authN/authZ middleware
- rate limiting
- request signing for sensitive integrations

## 23.7 Real-Time Example
Support triage API:
- validates payload
- enriches with feature service
- calls model
- returns prediction + confidence + reason codes

