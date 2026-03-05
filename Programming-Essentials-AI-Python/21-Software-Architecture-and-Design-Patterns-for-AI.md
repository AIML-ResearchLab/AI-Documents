# 21 - Software Architecture and Design Patterns for AI

## 21.1 Architecture Principles
- clear boundaries between data, modeling, and serving
- dependency inversion for testability
- explicit contracts between modules

## 21.2 Common Patterns
- Strategy pattern for interchangeable models
- Factory pattern for pipeline components
- Repository pattern for data access

## 21.3 Domain-Driven Interfaces
Model business concepts (ticket, session, prediction request) as explicit types.

## 21.4 Config-Driven Systems
Use config files and typed models to avoid hardcoded pipeline behavior.

## 21.5 Anti-Patterns
- monolithic notebook pipelines in production
- hidden global state
- tightly coupled training and serving code

## 21.6 Documentation Standards
Every module should include:
- purpose
- input/output schema
- failure behavior

## 21.7 Real-Time Example
Prediction service architecture:
- API layer
- validation layer
- feature layer
- model executor
- policy and audit layer

