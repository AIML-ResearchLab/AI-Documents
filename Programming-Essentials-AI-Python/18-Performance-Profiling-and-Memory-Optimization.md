# 18 - Performance Profiling and Memory Optimization

## 18.1 Performance Mindset
Measure first. Optimize only validated bottlenecks.

## 18.2 Profiling Tools
- `cProfile` for function-level profiling
- `line_profiler` for hot lines
- `memory_profiler` and `tracemalloc` for memory usage

## 18.3 Common Bottlenecks
- Python loops over large arrays
- excessive object allocations
- repeated serialization/deserialization

## 18.4 Optimization Strategies
- vectorization with NumPy
- algorithmic improvements
- caching repeated computations
- minimizing copies

## 18.5 Memory Optimization
- generators for streaming
- chunked processing
- compact dtypes (`float32`, categorical)

## 18.6 Native Acceleration Options
- Numba for JIT compilation
- Cython for hotspot sections
- Rust/C++ extensions for extreme paths

## 18.7 Real-Time Example
Batch scoring latency reduction:
- profile endpoint
- eliminate dataframe copies
- vectorize transforms
- reduce p95 latency by measurable target

