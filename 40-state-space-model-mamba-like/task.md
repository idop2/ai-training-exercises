# State Space Model: The Mamba Mentality 🐍

## 🧠 Theory: SSMs vs. Transformers
Transformers are powerful but struggle with long sequences because their attention mechanism scales quadratically ($O(N^2)$). State Space Models (SSMs), like Mamba, offer a linear-time alternative ($O(N)$) by compressing context into a fixed-size state. Think of it like a Recurrent Neural Network (RNN) that can be parallelized during training like a Transformer. The key innovation is the "selection mechanism"—letting the model choose what to remember and what to forget based on the input.

## 🚀 The Assignment
You will implement a simplified State Space Model layer from scratch, inspired by Mamba. You'll focus on the core discretization step that turns continuous parameters into recurrent weights, and then stack these layers to build a sequence model.

### Steps
1.  **The Discrete Step**: Implement the discretization function (ZOH or Bilinear) that converts continuous parameters ($\mathbf{A}, \mathbf{B}$) and a step size ($\Delta$) into discrete recurrence parameters ($\overline{\mathbf{A}}, \overline{\mathbf{B}}$).
2.  **The SSM Scan**: Implement the parallel scan (or a simple recurrent loop for understanding) to process a sequence using the discretized parameters. This is the heart of the "linear attention" idea.
3.  **Selective SSM**: Make the parameters input-dependent (i.e., $\mathbf{B}, \mathbf{C}, \Delta$ are functions of the input $x_t$). This is what makes Mamba "selective".
4.  **Training Loop**: Train your SSM on a simple "associative recall" or "copy" task to prove it can remember information over time.

## 🛠️ Tech Stack
- **PyTorch**: For building the model layers.
- **Einops**: Highly recommended for clean tensor manipulations.
- **NumPy**: for data generation.

## 📦 Deliverables
1.  `ssm.py`: A module containing your `SSMLayer` and `MambaBlock` implementation.
2.  `train.py`: A script to train the model on a toy dataset.
3.  `analysis.md`: A short report comparing the training speed/memory of your SSM vs. a simple Transformer (optional but encouraged).

## 🌟 Bonus Challenges (Optional)
- Implement the "parallel scan" algorithm efficiently using `torch.cumsum` or a custom CUDA kernel if you're brave!
- Compare the performance against a standard LSTM on the same task.
