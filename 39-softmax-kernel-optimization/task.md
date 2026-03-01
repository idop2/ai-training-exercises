# Softmax Optimization: Online & Safe

## 🧠 Theory: Numerical Stability & One-Pass Algorithms
The Softmax function $\frac{e^{x_i}}{\sum e^{x_j}}$ is tricky.
1.  **Overflow**: If $x_i$ is large (e.g., 100), $e^{100}$ overflows float capacity. Solution: "Safe Softmax" (subtract max $x$ before exp).
2.  **Memory Bandwidth**: Standard Safe Softmax needs 3 passes: (1) Find max, (2) Sum exponentials, (3) Divide. This reads inputs from memory 3 times!
3.  **Online Softmax**: Computes max and sum in a *single pass* by updating them incrementally. This is critical for fusing softmax into other kernels (like Flash Attention).

## 🚀 The Assignment
You will implement "Online Softmax" and compare it with the standard 3-pass implementation.

### Steps
1.  **Standard Safe Softmax**: Implement the 3-pass version.
    *   `m = max(x)`
    *   `e = exp(x - m)`
    *   `out = e / sum(e)`
2.  **Online Softmax Logic**:
    *   Initialize `m_prev = -inf`, `d_prev = 0`.
    *   Iterate through $x_i$:
        *   Update max: `m_curr = max(m_prev, x_i)`
        *   Update sum (denominator): `d_curr = d_prev * exp(m_prev - m_curr) + exp(x_i - m_curr)`
    *   Compute final output using the final max and sum.
3.  **Vectorize vs. Loop**: Implement the online version using a loop to simulate the stream of data.
4.  **Verification**: Prove mathematically or empirically that Online Softmax yields the same result as Standard Safe Softmax.

## 🛠️ Tech Stack
- Python
- `numpy`
- `torch`

## 📦 Deliverables
1.  A script `online_softmax.py` containing both implementations.
2.  A unit test checking equality on random input vectors (including some large values to test stability).

## 🌟 Bonus Challenges (Optional)
- **Welford's Algorithm**: Look up Welford's algorithm for online variance. It's the same principle! Implement it.
- **Triton Kernel**: Implement a fused Softmax kernel in Triton that reads data once and writes the output.
