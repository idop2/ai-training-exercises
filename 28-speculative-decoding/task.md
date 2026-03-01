# Speculative Decoding: Speed Up Inference with Guesswork!

## 🧠 Theory: Speculative Decoding
Speculative Decoding is a clever optimization technique to speed up Large Language Model inference without sacrificing quality. The core idea is simple: running a giant model (the "Target") is expensive, but running a tiny model (the "Draft") is cheap. Instead of generating one token at a time with the big model, use the small model to quickly "draft" a sequence of tokens. Then, run the big model *in parallel* on all drafted tokens to verify them. If the draft is correct, you accept multiple tokens at the cost of one big model forward pass! It's like having an intern draft emails for you to quickly approve or edit.

## 🚀 The Assignment
You will implement a simplified speculative decoding loop. Instead of full LLMs, you'll simulate the behavior with "mock" models to focus on the logic of drafting, verifying, and accepting/rejecting tokens.

### Steps
1.  **Mock the Models**: Create a `MockModel` class that outputs next-token probabilities. Create a "small" instance (faster, less accurate) and a "large" instance (slower, ground truth).
2.  **Implement Drafting**: Write a function that uses the small model to generate `K` draft tokens autoregressively.
3.  **Implement Verification**: Write a function that runs the large model on the drafted sequence to check if the drafted tokens match the large model's top choice (greedy decoding for simplicity).
4.  **The Loop**: Combine them into a `speculate()` function. It should draft, verify, and yield the accepted tokens. If a token is rejected, stop and yield the correct token from the large model.
5.  **Measure Speedup**: Compare the number of large model forward passes needed with and without speculation.

## 🛠️ Tech Stack
- Python
- `torch` (for basic tensor operations/mocking)
- `numpy`

## 📦 Deliverables
1.  A Python script `speculative_decoding.py` containing your `MockModel` and `speculate` function.
2.  A short report `results.md` explaining your acceptance rate and the theoretical speedup achieved in your simulation.

## 🌟 Bonus Challenges (Optional)
- **Probabilistic Verification**: Instead of greedy matching, implement rejection sampling to support temperature-based sampling while maintaining the target distribution.
- **Real Models**: Use `transformers` to load a tiny model (e.g., `distilgpt2`) and a larger one (e.g., `gpt2`) and run real speculative decoding.
