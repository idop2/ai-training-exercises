# LoRA Trainer: Fine-Tuning on a Budget

## 🧠 Theory: Low-Rank Adaptation (LoRA)
Fine-tuning a massive model (7B+ params) is expensive because you have to update all the weights. **LoRA** solves this by freezing the original weights $W$ and injecting a small, trainable update $\Delta W$. The trick? $\Delta W$ is decomposed into two low-rank matrices $A$ and $B$ (where $W + \Delta W = W + BA$). This reduces the number of trainable parameters by up to 10,000x! It's like adding a post-it note to a textbook instead of rewriting the whole book.

## 🚀 The Assignment
You will implement the core mathematical concept of LoRA from scratch in PyTorch. You'll create a custom layer that wraps an existing linear layer and adds the low-rank path.

### Steps
1.  **The Base Layer**: Create a standard `nn.Linear(in_features, out_features)` layer. Freeze its weights (`requires_grad=False`).
2.  **The LoRA Adapters**: Initialize two small matrices, $A$ (`in` x `rank`) and $B$ (`rank` x `out`). $A$ is usually initialized with random Gaussian, $B$ with zeros (so training starts as identity).
3.  **The Forward Pass**: Implement the logic: `output = base_layer(x) + (x @ A @ B) * scaling`.
4.  **Parameter Count**: Write a function to calculate total parameters vs. trainable parameters.
5.  **Test It**: Instantiate your LoRA layer, pass random input, and perform a backward pass to show that only $A$ and $B$ get gradients.

## 🛠️ Tech Stack
- Python
- `torch`
- `torch.nn`

## 📦 Deliverables
1.  A Python file `lora_scratch.py` with your `LoRALayer` class.
2.  A demonstration script that initializes a layer, prints the parameter reduction (e.g., "Trainable params reduced by 98%"), and verifies gradients.

## 🌟 Bonus Challenges (Optional)
- **Merge Weights**: Implement a method to merge $BA$ back into the original $W$ for inference, removing the inference latency overhead.
- **LoRA for Conv2d**: Can you adapt this idea for a Convolutional layer?
