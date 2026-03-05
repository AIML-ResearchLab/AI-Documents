# 12 - Deep Learning Foundations and PyTorch

## 12.1 Core Concepts
- Tensor operations
- Neural network layers
- Forward and backward pass
- Loss functions
- Optimization

## 12.2 PyTorch Essentials
```python
import torch

x = torch.tensor([[1.0, 2.0], [3.0, 4.0]])
print(x.shape)
```

## 12.3 Dataset and DataLoader
Use `Dataset` and `DataLoader` for scalable training input pipelines.

## 12.4 Training Loop Structure
1. `model.train()`
2. Forward pass
3. Compute loss
4. `loss.backward()`
5. `optimizer.step()`
6. `optimizer.zero_grad()`

## 12.5 Validation Loop
Use `model.eval()` and no-grad mode to compute validation metrics.

## 12.6 Regularization
- Dropout
- Weight decay
- Early stopping
- Data augmentation

## 12.7 GPU Basics
- Move tensors/models to device
- Watch GPU memory
- Use mixed precision when appropriate

## 12.8 Real-Time Training Example
Binary text intent classifier:
- Embedding layer
- Sequence encoder
- Linear output + sigmoid
- Metric: F1 + latency per request

