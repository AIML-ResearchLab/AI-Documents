# 19 - Multi-Stage RAG and Verifier Loop Pattern

## 19.1 Pattern Intent
Improve answer reliability with staged retrieval and verification loops.

## 19.2 Stage Design
Candidate retrieval -> reranking -> synthesis -> verification.

## 19.3 Verifier Role
Independent verifier checks factual grounding and citation adequacy.

## 19.4 Control Policies
Trigger re-retrieval when verifier confidence is below threshold.

## 19.5 Real-Time Example
Compliance assistant re-runs retrieval until citations cover all regulatory claims.
