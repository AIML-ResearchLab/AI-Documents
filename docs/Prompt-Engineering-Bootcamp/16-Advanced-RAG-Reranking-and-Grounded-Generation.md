# 16 - Advanced RAG, Reranking, and Grounded Generation

## 16.1 Retrieval Architecture
Production RAG pipeline:
1. ingest and normalize docs
2. chunk with semantic boundaries
3. embed and index
4. retrieve
5. rerank
6. synthesize grounded answer

## 16.2 Hybrid Retrieval
Combine dense + keyword retrieval for better recall across lexical and semantic matches.

## 16.3 Reranking for Precision
Rerank top candidates with query-aware models to reduce irrelevant evidence.

## 16.4 Grounded Generation Contract
Require:
- claim-to-source mapping
- unknown when evidence missing
- citation completeness

## 16.5 Retrieval Evaluation
Track:
- recall@k
- MRR/NDCG
- citation accuracy
- unsupported claim rate

## 16.6 Real-Time Example
Refund policy assistant:
- retrieves latest policy sections
- reranks by intent and jurisdiction
- outputs answer with source ids and effective dates

## 16.7 Hallucination Controls
Use evidence-first prompting and reject generation when retrieval confidence is below threshold.

