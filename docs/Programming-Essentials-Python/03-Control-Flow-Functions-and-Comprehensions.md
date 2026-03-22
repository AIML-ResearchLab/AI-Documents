# 03 - Control Flow, Functions, and Comprehensions

## 3.1 Conditionals
```python
if accuracy >= 0.9:
    status = "promote"
elif accuracy >= 0.8:
    status = "improve"
else:
    status = "retrain"
```

## 3.2 Loops
- `for` loops for iteration
- `while` loops for condition-driven repetition
- `break`, `continue`, and loop `else`

## 3.3 Functions
Design principles:
- Single responsibility
- Clear input/output types
- Minimal side effects

```python
def f1_score(precision: float, recall: float) -> float:
    if precision + recall == 0:
        return 0.0
    return 2 * (precision * recall) / (precision + recall)
```

## 3.4 Scope and Closures
- Local scope
- Global scope
- `nonlocal` for nested functions

## 3.5 Comprehensions
```python
squared = [x * x for x in range(10)]
valid = {k: v for k, v in scores.items() if v >= 0.8}
```

## 3.6 Iterators and Generators
Generators reduce memory usage for large data streams.

```python
def stream_lines(path: str):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()
```

## 3.7 Lambda and Higher-Order Functions
Use sparingly for readability.

