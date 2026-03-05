# 28 - Cost, Latency, and Inference Optimization

## 28.1 Cost Drivers
audio duration, model size, decoding complexity, and streaming overhead.

## 28.2 Optimization Methods
- model compression
- chunk sizing
- dynamic routing by call type
- caching reusable outputs

## 28.3 SLO Management
Track p95 latency and quality degradation jointly.

## 28.4 Real-Time Example
Latency budget met by routing short calls to compact ASR model.

