# Quantization Library: Shrink the Giant!

## 🧠 Theory: Doing More with Less
LLMs are huge. A 70B parameter model requires ~140GB of RAM in 16-bit precision (FP16). To run these on consumer hardware, we need **Quantization**: reducing the precision of the weights from 16-bit floats to 8-bit integers (Int8) or even 4-bit (FP4/Int4). This cuts memory usage by 2x or 4x with often negligible loss in quality.

## 🚀 The Assignment
You will write a library to perform naive quantization on tensors and measure the quantization error.

### Steps
1.  **AbsMax Quantization (Int8)**:
    *   Find the absolute maximum value in a tensor (`abs_max`).
    *   Calculate a scaling factor: `scale = 127 / abs_max`.
    *   Quantize: `int8_val = round(float_val * scale)`.
    *   Implement the `quantize` and `dequantize` functions.
2.  **Error Analysis**: Create a random float tensor. Quantize it to Int8, then dequantize it back to Float. Compute the Mean Squared Error (MSE) between the original and the reconstructed tensor.
3.  **Matrix Multiplication**: Implement a function that performs matrix multiplication directly on quantized integers (accumulating in int32) and then rescales, simulating how real quantized inference works.
4.  **FP4 (Simulated)**: Try to implement a simple 4-bit quantization (values -8 to 7). See how the error increases.

## 🛠️ Tech Stack
- **Python**
- **PyTorch** (for creating tensors and ground-truth comparisons)
- **Numpy**

## 📦 Deliverables
1.  `quantizer.py`: Your library with `quantize_int8`, `dequantize_int8`, and `matmul_int8`.
2.  `analysis.py`: A script generating a report on how much error is introduced by Int8 vs FP4 quantization on random matrices.
3.  **Comparison**: A text explanation of why `dequantize(quantize(x)) != x`.

## 🌟 Bonus Challenges
- **Block-wise Quantization**: Instead of one scale factor for the whole tensor, implement block-wise quantization (e.g., one scale factor for every 64 elements) to improve accuracy.
- **Zero-Point**: Implement asymmetric quantization (Scale + Zero-Point) to handle ReLU outputs (which are all non-negative) better.
