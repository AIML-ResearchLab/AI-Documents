# 02 - Python Core Syntax and Types

## 2.1 Variables and Naming
- Use descriptive names
- Prefer snake_case for variables and functions
- Constants in UPPER_CASE

## 2.2 Core Data Types
- `int`, `float`, `bool`, `str`
- `list`, `tuple`, `dict`, `set`
- `NoneType`

## 2.3 Type Conversion
```python
age = int("25")
score = float("98.5")
text = str(42)
```

## 2.4 Operators
- Arithmetic: `+ - * / // % **`
- Comparison: `== != < <= > >=`
- Logical: `and or not`
- Membership: `in`, `not in`

## 2.5 Strings
Common operations:
- slicing: `s[0:5]`
- formatting: `f"value={x}"`
- cleanup: `strip()`, `lower()`, `replace()`

## 2.6 Mutable vs Immutable
- Immutable: `int`, `float`, `str`, `tuple`
- Mutable: `list`, `dict`, `set`

Understanding mutability avoids hidden side effects in AI pipelines.

## 2.7 Type Hints
```python
def normalize(score: float, max_score: float) -> float:
    return score / max_score
```

