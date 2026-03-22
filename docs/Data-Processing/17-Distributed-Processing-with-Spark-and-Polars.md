# 17 - Distributed Processing with Spark and Polars

## 17.1 When to Use Distributed Systems
Use distributed processing when data volume or latency constraints exceed single-node capability.

## 17.2 Spark Concepts
- partitions
- shuffles
- lazy execution
- wide vs narrow transformations

## 17.3 Polars and Arrow
Columnar execution and efficient memory usage for high-performance analytics workloads.

## 17.4 Optimization Basics
- minimize shuffles
- prune columns early
- broadcast small joins

## 17.5 Real-Time Example
Process 2 TB clickstream daily with partition-aware aggregations.

