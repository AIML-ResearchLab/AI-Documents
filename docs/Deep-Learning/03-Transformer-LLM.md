# What is a Transformer?

A **Transformer** is a neural network architecture introduced in the Attention Is All You Need paper (by Vaswani et al., 2017).

👉 Core idea:

Instead of reading text sequentially (like RNN/LSTM), it:

- Looks at **all words at once**
- Uses **attention mechanism** to understand relationships

## Key Components of Transformer

**1. Embedding Layer**
- Converts words → vectors

**2. Positional Encoding**
- Adds word order information

**3. Attention Mechanism (Core)**
- Finds relationships between words

**4. Feed Forward Network**
- Processes information

**5. Layer Normalization + Residuals**
- Stabilizes training

## Types of Transformer Models

**🟢 1. Encoder-Only Transformer**
**🔵 2. Decoder-Only Transformer (LLMs)**
**🟣 3. Encoder–Decoder Transformer**

