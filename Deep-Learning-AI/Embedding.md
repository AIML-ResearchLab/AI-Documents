







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
