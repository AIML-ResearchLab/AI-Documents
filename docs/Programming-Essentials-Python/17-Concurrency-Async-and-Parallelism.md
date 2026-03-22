# 17 - Concurrency, Async, and Parallelism

## 17.1 Concurrency Models in Python
- Threading: I/O-bound tasks
- Multiprocessing: CPU-bound tasks
- Asyncio: high-concurrency network I/O

## 17.2 GIL Practical Impact
The GIL limits true parallel CPU execution in threads; prefer multiprocessing for compute-heavy workloads.

## 17.3 Asyncio Fundamentals
- `async def`, `await`
- event loop design
- task cancellation and timeouts

## 17.4 Queue-Based Worker Patterns
Use producer-consumer queues for robust async pipelines.

## 17.5 Parallel Data Processing
Use process pools for feature extraction and batch inference.

## 17.6 Fault Tolerance
- bounded retries
- backoff and jitter
- dead-letter queue for irrecoverable events

## 17.7 Real-Time Example
Concurrent inference service:
1. async request intake
2. rate-limited model calls
3. timeout + fallback response
4. structured error logging

