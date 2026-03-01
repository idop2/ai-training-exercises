# MoE Routing: Sparsity is the New Scale

## 🧠 Theory: Mixture of Experts (MoE)
How do we make models 10x larger without making them 10x slower? **Mixture of Experts (MoE)**! Instead of one dense Feed-Forward Network (FFN), we have many "experts" (e.g., 8 or 64). For each token, a "Router" (gating network) decides which experts (usually Top-1 or Top-2) should process it. This way, we only activate a fraction of the parameters per inference step, enabling massive model capacity with efficient compute.

## 🚀 The Assignment
You will build a modular Mixture of Experts layer in PyTorch, complete with a trainable gating mechanism.

### Steps
1.  **Define the Expert**: Create a simple MLP block (Linear -> ReLU -> Linear).
2.  **Define the Router**: Create a Linear layer that projects the input to `num_experts` logits.
3.  **Top-K Gating**: Implement the logic to select the top `k` indices from the router's output. Use `torch.topk`.
4.  **The Forward Pass**:
    *   Route inputs: For each token, identify the top-k experts.
    *   Dispatch: Send the token to the selected experts.
    *   Combine: Weighted sum of the expert outputs (using the router's softmax probabilities).
5.  **Load Balancing Loss (Bonus)**: In real training, experts collapse (one expert does everything). Implement the "auxiliary loss" that encourages equal utilization of experts.

## 🛠️ Tech Stack
- Python
- `torch`
- `torch.nn`

## 📦 Deliverables
1.  A Python file `moe_layer.py` containing your `MoELayer`.
2.  A test script creating an MoE with 4 experts, routing top-2, and verifying the output shape and gradient flow.

## 🌟 Bonus Challenges (Optional)
- **Visualize Routing**: Create a heatmap showing which experts are selected for different inputs.
- **Switch Transformer**: Implement the specific routing logic from the Switch Transformer paper (Top-1 routing with capacity factor).
