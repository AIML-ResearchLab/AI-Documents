# 08 - Safety, Security, and Compliance

## 8.1 Threat Model
Common risks:
- Prompt injection
- Jailbreak attempts
- Data leakage
- Unsafe or policy-violating output
- Unauthorized tool usage

## 8.2 Prompt Injection Defenses
- Treat retrieved/user text as untrusted
- Delimit untrusted content clearly
- Instruct model to ignore instructions inside untrusted context
- Validate outputs before execution

## 8.3 Jailbreak Mitigation
- Layered policy prompts at highest instruction level
- Refusal and safe-completion templates
- External moderation and policy classifiers
- Block high-risk tool actions unless explicitly approved

## 8.4 Data Protection
- Redact PII before model calls where possible
- Avoid sending secrets in prompts
- Encrypt logs and enforce retention limits
- Use least-privilege for tool integrations

## 8.5 Compliance Controls
Map prompts and outputs to policy requirements:
- Privacy laws and internal data policies
- Regulated-domain constraints (health, finance, legal)
- Audit logging for high-impact decisions

## 8.6 Human-in-the-Loop
Require review for:
- financial approvals
- legal interpretations
- medical guidance
- account closure and irreversible operations

## 8.7 Safe Response Pattern
```text
If request is disallowed, do not comply.
Return:
- policy_decision: denied
- reason_code
- safe_alternative
```

## 8.8 Security Validation Checklist
- Injection tests included
- Red-team prompts included
- Tool permissions verified
- Output moderation enabled
- Incident response owner assigned

