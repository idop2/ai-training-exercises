# Matrix Multiplication Kernel: Tiling for Speed

## 🧠 Theory: The Heart of Deep Learning
Everything in AI is a matrix multiplication ($C = A \times B$). Naive implementations are slow because they are memory-bound—they constantly fetch data from slow Global Memory (HBM). **Tiling** (or blocking) is the optimization technique where we load small sub-matrices (tiles) into fast Shared Memory (SRAM/L1 Cache), compute on them, and accumulate the result. This maximizes data reuse and hides memory latency.

## 🚀 The Assignment
You will implement a Tiled Matrix Multiplication algorithm. While writing a real CUDA kernel requires C++, we can simulate the logic and memory access patterns in Python using `numba` or just nested loops to understand *how* the data moves.

### Steps
1.  **Naive MatMul**: Write a standard triple loop ($i, j, k$) implementation of matrix multiplication.
2.  **Tiled MatMul Concept**: Divide matrices $A$, $B$, and $C$ into tiles of size `BLOCK_SIZE`.
3.  **The Kernel Logic**:
    *   Iterate through the output tiles.
    *   Load a tile from $A$ and a tile from $B$ into "shared memory" (a local buffer).
    *   Compute the partial product of these tiles.
    *   Accumulate into the output tile.
    *   Repeat for all tiles along the $K$ dimension.
4.  **Implementation**: Use `numba.cuda.jit` if you have a GPU, or just plain Python loops with explicit "load to buffer" steps to simulate the process.
5.  **Benchmark**: Compare the execution time (or operation count) of naive vs. tiled.

## 🛠️ Tech Stack
- Python
- `numba` (optional, for GPU compilation)
- `numpy`

## 📦 Deliverables
1.  A script `matmul_tiling.py` with `naive_matmul` and `tiled_matmul` functions.
2.  Comments in the code explaining where "Global Memory" read happens vs. "Shared Memory" access.

## 🌟 Bonus Challenges (Optional)
- **Triton**: Use OpenAI's `triton` language to write a real, high-performance matrix multiplication kernel. It's much easier than CUDA!
- **Autotuning**: Write a script to find the optimal `BLOCK_SIZE` for your hardware.
