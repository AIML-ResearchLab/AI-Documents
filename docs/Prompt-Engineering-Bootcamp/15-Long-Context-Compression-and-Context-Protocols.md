# 15 - Long Context, Compression, and Context Protocols

## 15.1 Long-Context Risks
More context does not always improve quality. Noise and contradictions can reduce accuracy.

## 15.2 Context Protocol Design
Define context layers:
- mandatory policy context
- task-critical context
- optional supplemental context

## 15.3 Compression Strategies
- map-reduce summarization
- relevance filtering
- duplicate removal
- contradiction flagging

## 15.4 Context Budgeting
Reserve token budget explicitly for:
- instructions
- retrieved evidence
- output

## 15.5 Context Provenance
Every context block should include metadata:
- source id
- timestamp
- trust level

## 15.6 Real-Time Example
Incident report assistant:
- compresses 200 logs into 12 critical events
- preserves source ids
- outputs confidence by evidence density

## 15.7 Protocol Checklist
- no untrusted instruction mixing
- no stale context without timestamp check
- no context block without source metadata

