# 05 - Context Engineering and RAG

## 5.1 Why Context Engineering
Model quality is constrained by context quality. Better retrieval and context selection usually improve results more than prompt wording changes.

## 5.2 RAG Pipeline
1. Ingest source data
2. Clean and chunk documents
3. Generate embeddings
4. Store with metadata
5. Retrieve top candidates
6. Rerank for relevance
7. Build grounded prompt with citations
8. Validate output against retrieved evidence

## 5.3 Chunking Strategies
- Fixed-size chunks for uniformity
- Semantic chunks for topic boundaries
- Overlap chunks to preserve continuity

Chunk design rules:
- Keep chunks self-contained
- Preserve source identifiers
- Avoid excessive overlap that increases noise

## 5.4 Retrieval Strategies
- Dense retrieval (embeddings)
- Keyword retrieval (BM25-like)
- Hybrid retrieval (dense + keyword)
- Metadata filtering (time, source type, product)

## 5.5 Reranking
Use rerankers to reduce irrelevant context and prioritize high-confidence passages.

## 5.6 Grounding Prompt Pattern
```text
Use only the provided sources.
For every key claim, include source_id and quote_span.
If evidence is missing, answer: "insufficient evidence".
Do not use prior assumptions.
```

## 5.7 Citation-First Output Schema
```json
{
  "answer": "string",
  "claims": [
    {
      "claim": "string",
      "source_id": "string",
      "evidence": "string"
    }
  ],
  "confidence": "low|medium|high"
}
```

## 5.8 Context Risks and Controls
- Risk: irrelevant context dilution
  - Control: reranking + top-k tuning
- Risk: stale documents
  - Control: freshness filters
- Risk: malicious retrieved content
  - Control: sanitize and classify untrusted sources

## 5.9 Real-Time Retrieval Example
User asks: "What changed in refund policy this quarter?"

System behavior:
1. Retrieve latest policy docs from trusted repo
2. Inject only top relevant sections
3. Require source citations for each change
4. Return unknown if quarter-specific evidence missing

