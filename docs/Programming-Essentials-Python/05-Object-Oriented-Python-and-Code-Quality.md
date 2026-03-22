# 05 - Object-Oriented Python and Code Quality

## 5.1 OOP Essentials
- Classes and objects
- Encapsulation
- Inheritance
- Polymorphism

## 5.2 Dataclasses for AI Config
```python
from dataclasses import dataclass

@dataclass
class TrainConfig:
    lr: float = 0.001
    batch_size: int = 32
    epochs: int = 10
```

## 5.3 Composition Over Inheritance
Prefer composition for flexible model pipelines.

## 5.4 Type-Driven Development
Use type hints to catch integration mistakes early.

## 5.5 Clean Code Rules
- Keep functions short
- Name things by intent
- Remove dead code
- Centralize constants

## 5.6 Refactoring Signals
- Duplicate logic
- Long functions
- Too many parameters
- Hidden global state

## 5.7 Documentation Standard
Every module should include:
- purpose
- input and output contracts
- usage examples

