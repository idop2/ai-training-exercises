# Flash Attention: Memory-Aware Attention

## 🧠 Theory: The IO Bottleneck
Standard Attention scales quadratically ($O(N^2)$) in memory. For long sequences, creating the $N \times N$ attention matrix typically causes OOM (Out of Memory) errors. **Flash Attention** solves this by *never materializing the full matrix*. It uses tiling to compute the attention output block-by-block, keeping everything in fast SRAM. It recomputes the attention scores during the backward pass (gradient checkpointing) which is actually faster than reading them from HBM!

## 🚀 The Assignment
You will implement the forward pass of the Flash Attention algorithm in Python. The goal is to understand the **tiled loop structure** and the **online softmax** trick.

### Steps
1.  **Standard Attention**: Implement `softmax(Q @ K.T) @ V` as a baseline.
2.  **Tiling Setup**: Define block sizes $B_c$ (column block) and $B_r$ (row block). Divide $Q, K, V$ into blocks.
3.  **The Outer Loops**: Iterate over blocks of $Q$ (rows of the output matrix).
4.  **The Inner Loops**: Iterate over blocks of $K$ and $V$.
5.  **Online Softmax**: Inside the inner loop, compute attention scores for the current block. Update the running max and running sum for the softmax *without* needing the full row. Rescale the previous partial output based on the new max.
6.  **Verify**: Compare your tiled output with the standard PyTorch attention output. They should be identical (within float precision).

## 🛠️ Tech Stack
- Python
- `torch`
- `numpy`

## 📦 Deliverables
1.  A script `flash_attention_sim.py` implementing the tiled logic.
2.  A test case comparing `flash_attention(q, k, v)` vs `torch.nn.functional.scaled_dot_product_attention` (or manual implementation).

## 🌟 Bonus Challenges (Optional)
- **Triton Implementation**: Write the actual Flash Attention kernel in Triton. This is a rite of passage for GPU programming!
- **Backward Pass**: Deriving the backward pass for Flash Attention is complex. Try to derive the gradients for the query block.
