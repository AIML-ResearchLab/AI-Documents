# Why multi-head attention?

Single-head attention learns **one type of relationship**.

But language has many relationships at once:

- subject ↔ verb
- determiner ↔ noun
- tense
- long-range dependency
- semantic similarity

So instead of one attention calculation, transformer uses **multiple heads in parallel**.

Each head has its own:

![alt text](image-37.png)

So each head can learn a different pattern.

![alt text](image-38.png)

![alt text](image-39.png)

![alt text](image-40.png)
![alt text](image-41.png)

![alt text](image-42.png)

![alt text](image-43.png)
![alt text](image-44.png)

![alt text](image-45.png)

![alt text](image-46.png)


![alt text](image-47.png)

![alt text](image-48.png)

![alt text](image-49.png)

![alt text](image-50.png)

![alt text](image-51.png)

![alt text](image-52.png)

![alt text](image-53.png)

![alt text](image-54.png)

![alt text](image-55.png)

![alt text](image-56.png)

![alt text](image-57.png)

![alt text](image-58.png)

![alt text](image-59.png)

![alt text](image-60.png)

![alt text](image-61.png)

## Tiny PyTorch example

```
import torch
import math

X = torch.tensor([
    [1., 0., 1., 0.],
    [0., 2., 0., 2.],
    [1., 1., 1., 1.]
])

# Head 1
WQ1 = torch.tensor([
    [1., 0.],
    [0., 1.],
    [1., 0.],
    [0., 1.]
])

WK1 = torch.tensor([
    [1., 1.],
    [0., 1.],
    [1., 0.],
    [0., 1.]
])

WV1 = torch.tensor([
    [1., 0.],
    [0., 1.],
    [0., 1.],
    [1., 0.]
])

# Head 2
WQ2 = torch.tensor([
    [1., 1.],
    [1., 0.],
    [0., 1.],
    [1., 0.]
])

WK2 = torch.tensor([
    [0., 1.],
    [1., 0.],
    [1., 1.],
    [0., 1.]
])

WV2 = torch.tensor([
    [0., 1.],
    [1., 0.],
    [1., 0.],
    [0., 1.]
])

def attention(X, WQ, WK, WV):
    Q = X @ WQ
    K = X @ WK
    V = X @ WV
    scores = Q @ K.T / math.sqrt(Q.shape[1])
    weights = torch.softmax(scores, dim=-1)
    out = weights @ V
    return out, weights

head1, attn1 = attention(X, WQ1, WK1, WV1)
head2, attn2 = attention(X, WQ2, WK2, WV2)

concat = torch.cat([head1, head2], dim=1)

WO = torch.eye(4)
final_out = concat @ WO

print("Head1:\n", head1)
print("Attention1:\n", attn1)
print("Head2:\n", head2)
print("Attention2:\n", attn2)
print("Concatenated:\n", concat)
print("Final output:\n", final_out)
```

![alt text](image-62.png)

![alt text](image-63.png)


