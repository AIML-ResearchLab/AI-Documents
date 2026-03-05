# 07 - File I/O, Errors, Logging, and Config

## 7.1 File Handling
Always use context managers:
```python
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()
```

## 7.2 JSON and CSV
- JSON for nested data exchange
- CSV for tabular datasets

## 7.3 Exception Handling
```python
try:
    value = int(user_input)
except ValueError:
    value = None
```

Use specific exceptions; avoid broad `except Exception` unless logging and re-raising.

## 7.4 Logging
```python
import logging
logging.basicConfig(level=logging.INFO)
logging.info("training started")
```

Use logs for observability, not print statements in production.

## 7.5 Configuration Patterns
- Use environment variables for secrets
- Use config files for non-secret runtime options
- Validate config at startup

## 7.6 Real-Time Reliability Example
Input file missing during inference:
1. Catch `FileNotFoundError`
2. Log error with request id
3. Return safe fallback response
4. Trigger alert if threshold crossed

