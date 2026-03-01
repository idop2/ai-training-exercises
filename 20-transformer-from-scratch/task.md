# Transformer from Scratch: All You Need is Code!

## 🧠 Theory: The Architecture that Changed Everything
The Transformer (from "Attention is All You Need") is the foundation of modern AI. GPT, BERT, Claude, Llama—they're all Transformers. While it's easy to import `nn.Transformer`, building one from scratch forces you to understand the flow of information: how queries, keys, and values interact, what LayerNorm actually does, and why we need positional encodings.

## 🚀 The Assignment
You will implement a GPT-style (Decoder-only) Transformer in PyTorch, building up from the raw tensor operations.

### Steps
1.  **Self-Attention**: Implement the `Head` class.
    *   Create Linear layers for Key, Query, and Value.
    *   Compute attention scores: `softmax((Q @ K.T) / sqrt(d_k))`.
    *   Apply the mask (so tokens can't look into the future).
    *   Aggregate values.
2.  **Multi-Head Attention**: Create a `MultiHeadAttention` class that runs multiple `Head`s in parallel and concatenates their outputs.
3.  **Feed-Forward Network**: Implement the simple MLP part (Linear -> ReLU/GELU -> Linear).
4.  **The Block**: Combine Attention and Feed-Forward with Residual connections and Layer Normalization.
5.  **The Model**: Assemble the full GPT model: Embedding -> Positional Encoding -> Blocks -> Final LayerNorm -> Linear Head.

## 🛠️ Tech Stack
- **Python**
- **PyTorch** (Basic tensor operations and `nn.Module` only. Avoid `nn.Transformer` or `nn.MultiheadAttention`).

## 📦 Deliverables
1.  `model.py`: Your complete Transformer implementation.
2.  `test_forward.py`: A script that passes random integer tokens into your model and ensures the output shape is `(batch_size, sequence_length, vocab_size)`.
3.  **Count Params**: A small utility to print the total number of parameters in your model.

## 🌟 Bonus Challenges
- **Training Loop**: Write a simple training loop to overfit the model on a single sentence (it should memorize it perfectly).
- **KV Cache**: Modify your attention mechanism to support KV-caching for faster inference.
