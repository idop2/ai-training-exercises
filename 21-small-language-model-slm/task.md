# Small Language Model: Train Your Own BabyLLM!

## 🧠 Theory: Scaling Down
You don't need 7,000 GPUs to learn how language models work. "Small Language Models" (SLMs) trained on specialized datasets (like TinyStories) can learn grammar, reasoning, and coherence with just a few million parameters. This exercise connects the architecture (what you built in the previous task) with data and training dynamics.

## 🚀 The Assignment
You will train a functional Language Model (approx. 10M-50M parameters) on a small dataset.

### Steps
1.  **Data Prep**: Download the **TinyStories** dataset (or a subset).
    *   Train a tokenizer (e.g., BPE using `tokenizers` library) or use a standard one (like GPT-2's).
    *   Create a generic `DataLoader` that yields batches of inputs and targets (shifted right).
2.  **Model Config**: Instantiate a Transformer model (you can use your own from the previous task or a clean implementation like minGPT/nanoGPT). Keep it small: e.g., 6 layers, 8 heads, embedding dim 512.
3.  **The Loop**: Write a robust training loop.
    *   Loss function: Cross Entropy.
    *   Optimizer: AdamW.
    *   Scheduler: Cosine decay with warmup (crucial for Transformers!).
4.  **Evaluation**: Monitor the training loss. Periodically generate text to see how the model improves from "babbling" to coherent English.

## 🛠️ Tech Stack
- **Python**
- **PyTorch**
- **HuggingFace Datasets** (to get TinyStories)
- **WandB** (optional, for tracking loss curves)

## 📦 Deliverables
1.  `train.py`: The training script.
2.  `generate.py`: A script to load your checkpoint and generate stories starting from a prompt like "Once upon a time".
3.  `training_log.md`: A summary of your final loss and a few samples of generated text.

## 🌟 Bonus Challenges
- **Top-K Sampling**: Implement sampling strategies (Temperature, Top-K, Top-P) in your generation script to make the output more creative.
- **Save/Load**: Implement checkpointing so you can resume training if it crashes.
