# 21 - FAISS: Architecture, Features, and Operations

## 21.1 Positioning
FAISS is a high-performance similarity search library, not a full networked database service.

## 21.2 Indexing Capabilities
Includes exact and ANN indexes such as Flat, IVF, HNSW, and product quantization variants.

## 21.3 Retrieval Features
Provides CPU and GPU acceleration for large-scale nearest-neighbor workloads.

## 21.4 Operational Considerations
You must build surrounding service layers for persistence, multi-tenancy, auth, and APIs.

## 21.5 Best Fit
Custom infrastructure teams needing maximum control and performance.

## 21.6 Real-Time Example
Research team runs GPU-accelerated similarity experiments before productionizing in managed stack.
