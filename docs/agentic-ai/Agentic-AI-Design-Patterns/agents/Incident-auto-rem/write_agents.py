#!/usr/bin/env python3
"""Write all agent files to disk."""
import os, sys
sys.path.insert(0, '/Users/ganeshkinkargiri./Desktop/AI-Documents/agentic-ai/Agentic-AI-Design-Patterns/agents/Incident-auto-rem')
from agents_code import (TRIGGER_AGENT_CODE, DIAGNOSIS_AGENT_CODE, RCA_AGENT_CODE,
                          PLANNING_AGENT_CODE, PRE_VALIDATE_AGENT_CODE, EXECUTION_AGENT_CODE,
                          POST_VALIDATE_AGENT_CODE, LEARNING_AGENT_CODE, FEEDBACK_AGENT_CODE)

os.makedirs('/Users/ganeshkinkargiri./Desktop/AI-Documents/agentic-ai/Agentic-AI-Design-Patterns/agents/Incident-auto-rem/agents', exist_ok=True)

files = {
    'trigger_agent.py'      : TRIGGER_AGENT_CODE,
    'diagnosis_agent.py'    : DIAGNOSIS_AGENT_CODE,
    'rca_agent.py'          : RCA_AGENT_CODE,
    'planning_agent.py'     : PLANNING_AGENT_CODE,
    'pre_validate_agent.py' : PRE_VALIDATE_AGENT_CODE,
    'execution_agent.py'    : EXECUTION_AGENT_CODE,
    'post_validate_agent.py': POST_VALIDATE_AGENT_CODE,
    'learning_agent.py'     : LEARNING_AGENT_CODE,
    'feedback_agent.py'     : FEEDBACK_AGENT_CODE,
}

for fname, code in files.items():
    path = f'/Users/ganeshkinkargiri./Desktop/AI-Documents/agentic-ai/Agentic-AI-Design-Patterns/agents/Incident-auto-rem/agents/{fname}'
    # strip leading newline
    with open(path, 'w') as f:
        f.write(code.lstrip('\n'))
    print(f'  wrote {path}')

# write __init__.py
with open('/Users/ganeshkinkargiri./Desktop/AI-Documents/agentic-ai/Agentic-AI-Design-Patterns/agents/Incident-auto-rem/agents/__init__.py', 'w') as f:
    f.write('')
print('  wrote __init__.py')
print('Done.')
