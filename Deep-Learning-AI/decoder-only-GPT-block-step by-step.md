# What is a decoder-only GPT block?

![alt text](image-90.png)

## 2) Full GPT pipeline overview

For input sentence:

```"The cat sat"```

the decoder-only GPT flow is:

![alt text](image-91.png)


![alt text](image-92.png)

![alt text](image-93.png)

![alt text](image-94.png)

![alt text](image-95.png)

![alt text](image-96.png)

![alt text](image-97.png)

![alt text](image-98.png)

![alt text](image-99.png)

![alt text](image-100.png)

![alt text](image-101.png)

![alt text](image-102.png)

![alt text](image-103.png)

![alt text](image-104.png)

![alt text](image-105.png)

![alt text](image-106.png)

![alt text](image-107.png)

![alt text](image-108.png)

![alt text](image-109.png)

![alt text](image-110.png)

![alt text](image-111.png)

![alt text](image-112.png)

![alt text](image-113.png)

![alt text](image-114.png)

![alt text](image-115.png)

![alt text](image-116.png)

## 25) Complete block structure diagram

Here is the decoder-only GPT block in compact form:

```
Input tokens
   ↓
Token Embedding
   ↓
Positional Embedding
   ↓
Add
   ↓
Masked Multi-Head Self-Attention
   ↓
Add & LayerNorm
   ↓
Feed-Forward Network
   ↓
Add & LayerNorm
   ↓
Next GPT block
   ↓
...
   ↓
Final hidden state
   ↓
Linear projection to vocabulary
   ↓
Softmax
   ↓
Next-token probabilities
```

## 26) Very important role of each part

![alt text](image-117.png)


![alt text](image-118.png)

![alt text](image-119.png)

## 28) Tiny PyTorch-style GPT block

```
import torch
import torch.nn as nn
import math

class SimpleMaskedAttention(nn.Module):
    def __init__(self, d_model):
        super().__init__()
        self.Wq = nn.Linear(d_model, d_model)
        self.Wk = nn.Linear(d_model, d_model)
        self.Wv = nn.Linear(d_model, d_model)
        self.Wo = nn.Linear(d_model, d_model)

    def forward(self, x):
        # x: [seq_len, d_model]
        Q = self.Wq(x)
        K = self.Wk(x)
        V = self.Wv(x)

        scores = Q @ K.T / math.sqrt(x.size(-1))

        seq_len = x.size(0)
        mask = torch.triu(torch.ones(seq_len, seq_len), diagonal=1).bool()
        scores = scores.masked_fill(mask, float('-inf'))

        weights = torch.softmax(scores, dim=-1)
        out = weights @ V
        return self.Wo(out)

class GPTBlock(nn.Module):
    def __init__(self, d_model, d_ff):
        super().__init__()
        self.attn = SimpleMaskedAttention(d_model)
        self.ln1 = nn.LayerNorm(d_model)
        self.ffn = nn.Sequential(
            nn.Linear(d_model, d_ff),
            nn.GELU(),
            nn.Linear(d_ff, d_model)
        )
        self.ln2 = nn.LayerNorm(d_model)

    def forward(self, x):
        x = self.ln1(x + self.attn(x))
        x = self.ln2(x + self.ffn(x))
        return x
```

## 29) Full GPT model skeleton

```
class TinyGPT(nn.Module):
    def __init__(self, vocab_size, d_model, d_ff, max_len, num_layers):
        super().__init__()
        self.token_emb = nn.Embedding(vocab_size, d_model)
        self.pos_emb = nn.Embedding(max_len, d_model)
        self.blocks = nn.ModuleList([
            GPTBlock(d_model, d_ff) for _ in range(num_layers)
        ])
        self.lm_head = nn.Linear(d_model, vocab_size)

    def forward(self, token_ids):
        seq_len = token_ids.size(0)
        positions = torch.arange(seq_len)

        x = self.token_emb(token_ids) + self.pos_emb(positions)

        for block in self.blocks:
            x = block(x)

        logits = self.lm_head(x)
        return logits
```

## 30) Final intuition

A decoder-only GPT block does this:

```
take token embeddings with positions,
let each token look only left using masked attention,
refine each token through feed-forward layers,
repeat many times,
then predict the next token.
```

## 31) One-sentence mental model

**GPT = stacked masked self-attention blocks + next-token prediction**


