# 04 - Data Structures, Algorithms, and Complexity

## 4.1 Lists and Tuples
- Lists: dynamic, mutable
- Tuples: fixed, immutable

## 4.2 Dictionaries and Sets
- Dict for key-value indexing
- Set for uniqueness and fast membership checks

## 4.3 Practical Structures in AI
- `dict` for feature maps
- `list` for mini-batch samples
- `set` for vocabulary deduplication

## 4.4 Algorithmic Patterns
- Searching and filtering
- Sorting
- Aggregation
- Sliding windows

## 4.5 Complexity Basics
- O(1): hash lookup
- O(n): linear scan
- O(n log n): sorting
- O(n^2): nested comparisons

AI data preprocessing quality depends on efficient operations over large datasets.

## 4.6 Example: Frequency Counter
```python
from collections import Counter

labels = ["cat", "dog", "cat", "bird"]
counts = Counter(labels)
print(counts)
```

## 4.7 When to Optimize
Optimize after profiling. Prioritize correctness and clarity first.

