# 16 - Matrix Calculus and Backpropagation

## 16.1 Why Matrix Calculus
Deep learning training is gradient computation over matrix/tensor operations.

## 16.2 Core Derivatives
- gradient of dot products
- Jacobians for vector functions
- chain rule for composed layers

## 16.3 Backpropagation View
Backprop reuses intermediate derivatives from output to input efficiently.

## 16.4 Practical Rule
Keep tensor shape annotations for each derivative to avoid silent gradient bugs.

## 16.5 Real-Time Example
Derive gradients for linear layer: `y = Wx + b`.

