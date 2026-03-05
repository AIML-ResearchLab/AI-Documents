# 28 - Cost, Latency, and Storage Optimization

## 28.1 Cost Drivers
- compute-intensive transforms
- repeated full refresh jobs
- inefficient file formats
- excessive intermediate materialization

## 28.2 Optimization Tactics
- incremental processing
- partition pruning
- compaction and clustering
- storage lifecycle policies

## 28.3 Latency Optimization
- parallel execution
- precomputed aggregates
- low-latency serving paths

## 28.4 Tradeoff Management
Optimize cost without violating freshness and quality SLAs.

## 28.5 Real-Time Example
Switch hourly full-refresh job to incremental merge and reduce compute cost significantly.

