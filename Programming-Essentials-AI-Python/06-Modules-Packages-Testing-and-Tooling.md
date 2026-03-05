# 06 - Modules, Packages, Testing, and Tooling

## 6.1 Modules and Imports
- One file = one module
- Avoid circular imports
- Prefer explicit imports for readability

## 6.2 Package Layout
```text
src/my_ai_app/
  __init__.py
  data.py
  features.py
  model.py
  evaluate.py
```

## 6.3 Dependency Management
Use `requirements.txt` or `pyproject.toml` for reproducibility.

## 6.4 Unit Testing with pytest
```python
def add(a: int, b: int) -> int:
    return a + b

def test_add():
    assert add(2, 3) == 5
```

## 6.5 Linting and Formatting
- `ruff` for linting
- `black` for formatting

## 6.6 Pre-Commit Quality Gate
Run before push:
```bash
pytest
ruff check .
black --check .
```

## 6.7 CI Fundamentals
Automate tests and style checks in every pull request.

