# What is Embedding?

**Embedding** is a way to convert data (text, image, audio, etc.) into a **numerical vector (list of numbers)** so that machines (especially AI models) can **understand relationships, meaning, and similarity**.

👉 In simple words:

**Embedding = Meaning → Numbers**

## Why do we need Embeddings?

Computers don’t understand words like humans.
They only understand numbers.

So we convert:

| Human Input | Embedding (Vector Representation) |
| ----------- | --------------------------------- |
| "cat"       | [0.12, -0.45, 0.88, ...]          |
| "dog"       | [0.10, -0.40, 0.85, ...]          |


👉 Notice: "cat" and "dog" vectors are similar → because meaning is similar.


## Types of Embeddings

| Type               | Description              | Example         |
| ------------------ | ------------------------ | --------------- |
| Word Embedding     | Each word → vector       | "king", "queen" |
| Sentence Embedding | Full sentence → vector   | "I love AI"     |
| Document Embedding | Entire document → vector | PDF, article    |
| Image Embedding    | Image → vector           | Cat image       |
| Audio Embedding    | Sound → vector           | Speech          |


## How Embedding Works (Concept)

1. Input text → Tokenization
2. Tokens → Passed through model (Transformer encoder)
3. Output → Dense vector (embedding)


👉 Example:

```
Input: "The cat sat"
↓
Tokens: ["The", "cat", "sat"]
↓
Embedding:
[
 [0.2, 0.8, -0.1],
 [0.9, 0.1,  0.3],
 [0.4, 0.7,  0.5]
]
```

## Real Example (Step-by-Step)

**Sentence:**

👉 "I love dogs"


Embedding might look like:

`[0.21, -0.33, 0.89, 0.44]`


**Another sentence:**

👉 "I like puppies"

Embedding:

`[0.20, -0.30, 0.87, 0.40]`

👉 These vectors are very close → meaning is similar

## Key Property: Similarity

We measure similarity using:

- **Cosine Similarity**
- **Euclidean Distance**

👉 Example:

```
Similarity("dog", "puppy") ≈ 0.95  (very similar)
Similarity("dog", "car")   ≈ 0.10  (not similar)
```

## Where Embeddings are Used

**1. Semantic Search**

Search by meaning, not exact words

👉 "best phone" ≈ "top mobile"

**2. RAG (Retrieval-Augmented Generation)**

`User Query → Embedding → Vector DB → Similar docs → LLM answer`

**3. Recommendation Systems**

👉 Netflix, Amazon

"Users with similar embeddings get similar recommendations"

**4. Clustering**

Group similar data automatically

**5. Chatbots / LLM Memory**

Store past conversations as embeddings

## Embedding Model (Important)

👉 Embeddings are generated using **Encoder models**

Examples:

| Model                   | Type    |
| ----------------------- | ------- |
| BERT                    | Encoder |
| Sentence-BERT           | Encoder |
| OpenAI Embedding Models | Encoder |
| MiniLM                  | Encoder |


## Important Characteristics

| Property   | Meaning                     |
| ---------- | --------------------------- |
| Dense      | Compact vector (not sparse) |
| Semantic   | Captures meaning            |
| Fixed Size | Same size for all inputs    |
| Comparable | Can measure similarity      |


## Simple Analogy

Think of embedding like **GPS coordinates of meaning**:

| Word  | Meaning Location |
| ----- | ---------------- |
| "cat" | (x=10, y=20)     |
| "dog" | (x=11, y=19)     |
| "car" | (x=100, y=200)   |


👉 Close points = similar meaning

**Summary**

👉 Embedding is:

- Converting data → vectors
- Capturing meaning in numbers
- Used for similarity, search, and AI reasoning







## Complete Embedding Models Table

| Category     | Model Name             | Type       | Architecture         | Context Aware | Multilingual | Modality   | Dimension | Open Source | Best Use Case         |
| ------------ | ---------------------- | ---------- | -------------------- | ------------- | ------------ | ---------- | --------- | ----------- | --------------------- |
| Word         | Word2Vec               | Word       | Shallow NN           | ❌             | ❌            | Text       | 100–300   | ✅           | Basic NLP             |
| Word         | GloVe                  | Word       | Matrix Factorization | ❌             | ❌            | Text       | 100–300   | ✅           | Word similarity       |
| Word         | FastText               | Word       | Subword Model        | ❌             | ⚠️           | Text       | 100–300   | ✅           | OOV handling          |
| Sentence     | Sentence-BERT          | Sentence   | Encoder (BERT)       | ✅             | ⚠️           | Text       | 384–768   | ✅           | RAG, semantic search  |
| Sentence     | E5                     | Sentence   | Encoder              | ✅             | ✅            | Text       | 384–1024  | ✅           | Retrieval (SOTA)      |
| Sentence     | MiniLM                 | Sentence   | Encoder              | ✅             | ❌            | Text       | 384       | ✅           | Fast inference        |
| Sentence     | MPNet                  | Sentence   | Encoder              | ✅             | ❌            | Text       | 768       | ✅           | High accuracy         |
| Sentence     | DistilBERT             | Sentence   | Encoder              | ✅             | ❌            | Text       | 768       | ✅           | Lightweight NLP       |
| Sentence     | text-embedding-3-small | Sentence   | Encoder-like         | ✅             | ✅            | Text       | ~1536     | ❌           | RAG, applications     |
| Sentence     | text-embedding-3-large | Sentence   | Encoder-like         | ✅             | ✅            | Text       | ~3072     | ❌           | High-quality search   |
| Multilingual | LaBSE                  | Sentence   | Encoder              | ✅             | ✅            | Text       | 768       | ✅           | Cross-language search |
| Multilingual | mBERT                  | Token/Sent | Encoder              | ✅             | ✅            | Text       | 768       | ✅           | Multilingual NLP      |
| Multilingual | XLM-R                  | Sentence   | Encoder              | ✅             | ✅            | Text       | 768       | ✅           | Multilingual RAG      |
| Code         | CodeBERT               | Code       | Encoder              | ✅             | ❌            | Code/Text  | 768       | ✅           | Code search           |
| Code         | GraphCodeBERT          | Code       | Encoder              | ✅             | ❌            | Code       | 768       | ✅           | Code understanding    |
| Multimodal   | CLIP                   | Multi      | Dual Encoder         | ✅             | ⚠️           | Image+Text | 512–768   | ✅           | Image search          |
| Multimodal   | DINO                   | Image      | Encoder              | ✅             | ❌            | Image      | 384–768   | ✅           | Vision tasks          |
| Audio        | Wav2Vec                | Audio      | Encoder              | ✅             | ❌            | Audio      | 512–1024  | ✅           | Speech recognition    |
