# What is an Encoder-Only Transformer?
An **Encoder-Only Transformer** is a Transformer model used mainly for **understanding text**, not generating long text.

It reads the full sentence at once and builds a contextual understanding of every word.

An Encoder-only Transformer processes the entire input sentence at once (bidirectional context) and produces context-aware embeddings.

## Popular Encoder-Only Transformer LLMs

**1. BERT (Most Important)**
**2. RoBERTa (Improved BERT)**
**3. ALBERT (Lightweight BERT)**
**4. DistilBERT (Compressed BERT)**
**5. ELECTRA (Efficient Training)**


## Where is it used in real life?
Encoder-only models are great for:

- sentiment analysis
- text classification
- spam detection
- intent detection
- named entity recognition
- semantic search
- document matching


## Step-by-Step Architecture

**Step 1: Input Text**

Suppose input is:

`"Ganesh loves machine learning"`

The model cannot directly understand text.
First it converts text into tokens.

**Step 2: Tokenization**

Sentence is broken into tokens.

Example:

`["[CLS]", "Ganesh", "loves", "machine", "learning", "[SEP]"]`

Special tokens:

- **[CLS]** → used for sentence-level tasks
- **[SEP]** → marks end of sentence

Each token is converted into an ID using vocabulary.

Example:

`[101, 2567, 7459, 3698, 4083, 102]`

**Step 3: Token Embedding**

Each token ID is mapped to a dense vector.

Example:

- vocab size = 30,000
- embedding size = 768

So each token becomes a vector of size 768.

```
[CLS]      → [0.12, 0.45, ...]
Ganesh     → [0.91, 0.22, ...]
loves      → [0.37, 0.88, ...]
machine    → [0.55, 0.19, ...]
learning   → [0.63, 0.42, ...]
[SEP]      → [0.11, 0.09, ...]
```

Now shape becomes:

```
(sequence_length, hidden_size)
= (6, 768)
```

**Step 4: Positional Embedding**

Transformer does not know word order by itself.

So we add **position information**.

Positions:

`[0, 1, 2, 3, 4, 5]`

Each position also has an embedding vector.

Then:

`Final Input Embedding = Token Embedding + Position Embedding`

Sometimes segment embedding is also added in BERT for sentence pairs.

So in BERT:

```
Input Representation
= Token Embedding
+ Positional Embedding
+ Segment Embedding
```

**4. Encoder Block**

This is the core of the encoder-only transformer.

Each encoder block contains:

```
Input
 ↓
Multi-Head Self-Attention
 ↓
Add & Layer Normalization
 ↓
Feed Forward Neural Network
 ↓
Add & Layer Normalization
 ↓
Output
```

This block is repeated many times:

- BERT-base → 12 encoder layers
- BERT-large → 24 encoder layers

**5. Multi-Head Self-Attention**

This is the most important part.

Each token looks at all other tokens and decides:

- which words are important
- how much attention to give each word

For example in:

`"Ganesh loves machine learning"`

The token **"learning"** may pay strong attention to **"machine"**.

The token **"loves"** may pay attention to **"Ganesh"**.

This is why encoder models understand context well.

**Inside Self-Attention**

From input embeddings, model creates 3 vectors for each token:

- **Query (Q)**
- **Key (K)**
- **Value (V)**

These are created using learned weight matrices:

```
Q = XWQ
K = XWK
V = XWV
```

Where:

- `X` = input matrix
- `WQ, WK, WV` = learned parameters

**Attention Score**

For each token:

![alt text](image.png)

**What are Q, K, V?**

- **Q (Query)** → What I am looking for
- **K (Key)** → What I contain (identity of each token)
- **V (Value)** → Actual information/content

👉 Think of it like a search system:

| Component | Meaning        |
| --------- | -------------- |
| Query (Q) | Question       |
| Key (K)   | Index / labels |
| Value (V) | Actual data    |


**Step-by-Step Breakdown**

![alt text](image-1.png)

- Multiply Query with all Keys
- This gives **how much each word relates to others**

👉 Example sentence:

`"The cat sat on the mat"`

If model is processing `"sat"`, it checks:

- How related is "sat" to "cat"? ✔️ high
- How related to "mat"? ✔️ medium
- How related to "the"? ❌ low

👉 Result = **attention scores matrix**

![alt text](image-2.png)

- Prevents values from becoming too large
- Stabilizes training

👉 Why needed?

- Large dot products → softmax becomes too sharp → bad gradients

![alt text](image-3.png)

- Converts scores into **probabilities**
- All values between 0 and 1
- Sum = 1

👉 Example:

| Token | Score |
| ----- | ----- |
| cat   | 0.6   |
| mat   | 0.3   |
| the   | 0.1   |


![alt text](image-4.png)

- Now we **combine actual information**
- Each token contributes based on importance

👉 Final output = weighted sum of values

**3. Full Intuition in One Line**

👉
`Attention = "Look at all words → decide importance → combine useful information"`

## Final Summary

![alt text](image-5.png)

![alt text](image-6.png)

Suppose sentence is:

`"The cat sat"`

We have 3 tokens:

- The
- cat
- sat

Assume each token is already converted into an embedding vector of size 4.

👉 How do words like “The”, “cat”, “sat” become embedding vectors of size 4?

Let’s break it down step by step (`practical + intuitive`).

**Step 1: Build a Vocabulary**

First, the model creates a **vocabulary** of all words (or tokens).

**Example:**

```
"The" → index 0  
"cat" → index 1  
"sat" → index 2  
```

**Step 2: One-Hot Encoding (Initial Representation)**

Each word is converted into a **one-hot vector:**

| Word | One-hot vector |
| ---- | -------------- |
| The  | [1, 0, 0]      |
| cat  | [0, 1, 0]      |
| sat  | [0, 0, 1]      |


This is **not useful for learning meaning**, just an index representation.

**Step 3: Embedding Matrix (Learned)**

Now comes the key idea 👇

The model has a **learnable embedding matrix:**

**What is E?**

👉 E is the Embedding Matrix

It is a learnable lookup table that converts tokens (words) into vectors.

**Formal Definition**

![alt text](image-7.png)

Where:

- V = vocabulary size (number of unique tokens)
- d = embedding dimension (vector size)

**Example**

- Vocabulary size V=3 → ("The", "cat", "sat")
- Embedding size d=4

So:

![alt text](image-8.png)

**What Does Each Row Mean?**

| Row   | Token | Meaning                   |
| ----- | ----- | ------------------------- |
| Row 0 | "The" | embedding vector of "The" |
| Row 1 | "cat" | embedding vector of "cat" |
| Row 2 | "sat" | embedding vector of "sat" |

**How It Works (Super Important)**

👉 When the model sees a word:

1. Convert word → index
2. Use index to lookup row in E

Example:

```
"The" → index 0 → E[0] → [1, 0, 1, 0]
"cat" → index 1 → E[1] → [0, 2, 0, 2]
"sat" → index 2 → E[2] → [1, 1, 1, 1]
```

**Key Insight**

**👉 E is NOT computed each time**

It is:

✔ Stored in the model
✔ Learned during training
✔ Updated via backpropagation

**Intuition**

Think of **E like a dictionary**:

```
"The" → [1, 0, 1, 0]
"cat" → [0, 2, 0, 2]
"sat" → [1, 1, 1, 1]
```

**In Real LLMs**

- Vocabulary size → 30K to 100K+
- Embedding size → 768, 1024, 4096+

So:

![alt text](image-9.png)

Huge matrix 🚀

**Final Answer**

**👉 E = Embedding Matrix**

It is a `trainable matrix that maps tokens → vectors`


**Let’s do full self-attention calculation step by step using example.**

We will use the sentence:

**"The cat sat"**

![alt text](image-10.png)

![alt text](image-11.png)

![alt text](image-12.png)

![alt text](image-13.png)

![alt text](image-14.png)

![alt text](image-15.png)

![alt text](image-16.png)

![alt text](image-17.png)

![alt text](image-18.png)

![alt text](image-19.png)

![alt text](image-20.png)

![alt text](image-21.png)

![alt text](image-22.png)

![alt text](image-23.png)

![alt text](image-24.png)

![alt text](image-25.png)

![alt text](image-26.png)

![alt text](image-27.png)

![alt text](image-28.png)

![alt text](image-29.png)

![alt text](image-30.png)

![alt text](image-31.png)

![alt text](image-32.png)

![alt text](image-33.png)

![alt text](image-34.png)

![alt text](image-35.png)

![alt text](image-36.png)


## 16) Tiny PyTorch example

```
import torch
import math

X = torch.tensor([
    [1., 0., 1., 0.],
    [0., 2., 0., 2.],
    [1., 1., 1., 1.]
])

W_Q = torch.tensor([
    [1., 0.],
    [0., 1.],
    [1., 0.],
    [0., 1.]
])

W_K = torch.tensor([
    [1., 1.],
    [0., 1.],
    [1., 0.],
    [0., 1.]
])

W_V = torch.tensor([
    [1., 0.],
    [0., 1.],
    [0., 1.],
    [1., 0.]
])

Q = X @ W_Q
K = X @ W_K
V = X @ W_V

scores = Q @ K.T
scaled_scores = scores / math.sqrt(2)
weights = torch.softmax(scaled_scores, dim=-1)
output = weights @ V

print("Q:\n", Q)
print("K:\n", K)
print("V:\n", V)
print("Scores:\n", scores)
print("Weights:\n", weights)
print("Output:\n", output)
```



