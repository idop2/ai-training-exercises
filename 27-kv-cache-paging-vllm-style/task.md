# KV Cache Paging: Managing LLM Memory!

## 🧠 Theory: The vLLM Revolution
When generating text with an LLM, we cache the Key and Value matrices (KV Cache) so we don't have to recompute them for every new token. However, these caches grow dynamically, and allocating memory for the maximum possible length is wasteful. **PagedAttention** (introduced by vLLM) solves this by chopping the KV cache into "pages" or blocks that can be stored in non-contiguous memory, just like how an OS manages RAM. This allows for massive batch sizes and high throughput.

## 🚀 The Assignment
You will implement a simplified simulation of Paged Attention and a block manager.

### Steps
1.  **The Block Table**: Implement a `BlockTable` structure that maps a logical sequence (e.g., "Request A") to physical blocks of memory (e.g., "Block 4, Block 9").
2.  **Memory Manager**: Create a `BlockAllocator`.
    *   It manages a fixed pool of memory blocks.
    *   `allocate()`: Returns a free block index.
    *   `free()`: Returns a block to the pool.
3.  **Paged Attention Kernel (Simulated)**: Write a function `paged_attention(query, block_table, physical_memory)`.
    *   Instead of reading a contiguous KV tensor, it should use the `block_table` to look up the correct pieces of `physical_memory` to compute attention scores.
4.  **Simulation**: Simulate two sequences generating tokens. As they grow, allocate new blocks for them dynamically.

## 🛠️ Tech Stack
- **Python**
- **PyTorch** (for the attention calculation)

## 📦 Deliverables
1.  `memory_manager.py`: Your BlockAllocator and BlockTable classes.
2.  `paged_attn.py`: The attention function that reads from non-contiguous blocks.
3.  `benchmark.py`: A comparison showing memory fragmentation (waste) in a standard "contiguous allocation" vs. your "paged allocation" for varied sequence lengths.

## 🌟 Bonus Challenges
- **Beam Search**: Simulate how PagedAttention handles beam search (where multiple sequences might share the exact same initial blocks). Implement a "Copy-on-Write" mechanism for the blocks.
- **GPU Kernel**: (Hard) If you know CUDA/Triton, try writing the actual kernel that reads from block tables.
