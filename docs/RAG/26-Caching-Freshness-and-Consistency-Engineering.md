# 26 - Caching, Freshness, and Consistency Engineering

## 26.1 Cache Layers
query cache, embedding cache, retrieval cache, and response cache.

## 26.2 Freshness Policy
cache TTL tied to source update frequency and risk class.

## 26.3 Consistency Risks
stale cache can conflict with newly indexed source updates.

## 26.4 Real-Time Example
Critical policy domain bypasses long-lived cache for freshness safety.

