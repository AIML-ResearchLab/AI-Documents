# Masked Multi-Head Attention in Decoder

This is just **multi-head self-attention + a mask that blocks future tokens**.

That masking is the key idea.

## 1) Why do we need masking?

In a decoder language model, the model predicts the next token **left to right**.

Example sentence:

`“The cat sat”`

During training, when predicting:

- token 1 should only see token 1
- token 2 should see tokens 1 and 2
- token 3 should see tokens 1, 2, and 3

**It must not look ahead.**

So:

- “The” cannot see “cat” or “sat”
- “cat” cannot see “sat”

Otherwise the model would cheat.

![alt text](images/image-64.png)

![alt text](images/image-65.png)

![alt text](images/image-66.png)

![alt text](images/image-67.png)

![alt text](images/image-68.png)

![alt text](images/image-69.png)

![alt text](images/image-70.png)

![alt text](images/image-71.png)

![alt text](images/image-72.png)

![alt text](images/image-73.png)

![alt text](images/image-74.png)

![alt text](images/image-75.png)

![alt text](images/image-76.png)

![alt text](images/image-77.png)

![alt text](images/image-78.png)

![alt text](images/image-79.png)

![alt text](images/image-80.png)

![alt text](images/image-81.png)

![alt text](images/image-82.png)

![alt text](images/image-83.png)

![alt text](images/image-84.png)

![alt text](images/image-85.png)

## PyTorch-style code

```
import torch
import math

X = torch.tensor([
    [1., 0., 1., 0.],
    [0., 2., 0., 2.],
    [1., 1., 1., 1.]
])

WQ = torch.tensor([
    [1., 0.],
    [0., 1.],
    [1., 0.],
    [0., 1.]
])

WK = torch.tensor([
    [1., 1.],
    [0., 1.],
    [1., 0.],
    [0., 1.]
])

WV = torch.tensor([
    [1., 0.],
    [0., 1.],
    [0., 1.],
    [1., 0.]
])

Q = X @ WQ
K = X @ WK
V = X @ WV

scores = (Q @ K.T) / math.sqrt(2)

# causal mask
seq_len = X.shape[0]
mask = torch.triu(torch.ones(seq_len, seq_len), diagonal=1)
scores = scores.masked_fill(mask == 1, float('-inf'))

weights = torch.softmax(scores, dim=-1)
output = weights @ V

print("Scores after mask:\n", scores)
print("Weights:\n", weights)
print("Output:\n", output)
```

![alt text](images/image-86.png)

![alt text](images/image-87.png)

![alt text](images/image-88.png)

![alt text](images/image-89.png)

