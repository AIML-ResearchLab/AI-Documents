# 08 - NumPy, Linear Algebra, and Vectorization

## 8.1 Why NumPy
NumPy provides high-performance numerical arrays and vectorized operations, foundational for AI and scientific computing.

## 8.2 ndarray Basics
```python
import numpy as np

x = np.array([1, 2, 3], dtype=np.float32)
print(x.shape, x.dtype)
```

## 8.3 Vectorization
Prefer vectorized operations over Python loops for speed.

```python
scores = np.array([10, 20, 30])
normalized = scores / scores.max()
```

## 8.4 Broadcasting
NumPy can align different shapes automatically under broadcasting rules.

```python
m = np.array([[1, 2], [3, 4]])
b = np.array([10, 20])
print(m + b)
```

## 8.5 Essential Operations
- Reshape: `x.reshape(...)`
- Aggregate: `sum`, `mean`, `std`
- Boolean masks for filtering
- Matrix multiplication with `@`

## 8.6 Linear Algebra Essentials
- Dot product
- Matrix multiplication
- Transpose
- Norms
- Eigen concepts (intro)

## 8.7 Performance Tips
- Use contiguous arrays when possible
- Avoid unnecessary copies
- Profile bottlenecks before optimizing

