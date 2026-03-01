# DPO Loss: Aligning LLMs Without the Drama

## 🧠 Theory: Direct Preference Optimization (DPO)
Before DPO, aligning LLMs required a complex pipeline: train a reward model, then use PPO reinforcement learning to optimize a policy against it. This was unstable and computationally expensive. **DPO** changed the game by deriving the optimal policy in closed form! It directly optimizes the model to increase the likelihood of preferred answers ($y_w$) over rejected ones ($y_l$), relative to a reference model. No reward model needed, just a clever loss function.

## 🚀 The Assignment
You will implement the core DPO loss function in PyTorch. This is the mathematical heart of modern LLM alignment.

### Steps
1.  **Understand the Formula**: $L_{DPO} = - \log \sigma ( \beta (\log \frac{\pi_\theta(y_w|x)}{\pi_{ref}(y_w|x)} - \log \frac{\pi_\theta(y_l|x)}{\pi_{ref}(y_l|x)}) )$.
    *   $\pi_\theta$: Your model (policy).
    *   $\pi_{ref}$: The frozen reference model.
    *   $y_w, y_l$: Winning and Losing responses.
    *   $\beta$: Temperature parameter (usually 0.1 to 0.5).
2.  **Mock Inputs**: Create dummy logits for `policy_chosen`, `policy_rejected`, `reference_chosen`, and `reference_rejected`.
3.  **Compute Log Probs**: Write a helper to compute log probabilities from logits (using `log_softmax` and `gather` if needed, or just assume inputs are log probs for simplicity).
4.  **Implement the Loss**: Translate the formula into PyTorch code. Use `F.logsigmoid` for numerical stability.
5.  **Test Gradients**: Run a backward pass to ensure gradients flow only to the policy model (not the reference).

## 🛠️ Tech Stack
- Python
- `torch`
- `torch.nn.functional`

## 📦 Deliverables
1.  A Python script `dpo_loss.py` containing the `dpo_loss` function.
2.  A test case demonstrating the loss decreases when the policy assigns higher probability to the chosen response.

## 🌟 Bonus Challenges (Optional)
- **Visualize**: Plot the loss surface as you vary the probability difference between chosen and rejected responses.
- **Batched Implementation**: Ensure your function handles batches of data correctly, using appropriate masking/padding if dealing with sequences.
