# RLHF Pipeline: Mastering PPO

## 🧠 Theory: Proximal Policy Optimization (PPO)
Reinforcement Learning from Human Feedback (RLHF) is how we turn raw LLMs into helpful assistants. The standard algorithm is **PPO**. It works by taking small, safe steps to update the model policy. We want to maximize the reward (for helpfulness) while penalizing the model if it drifts too far from the original language model (using KL Divergence). The "Clipped Surrogate Objective" ensures updates aren't too drastic, preventing catastrophic forgetting.

## 🚀 The Assignment
You will implement the critical components of the PPO loss function. We won't build the full RL loop (which requires environment interaction), but we'll build the mathematical engine that drives the learning.

### Steps
1.  **KL Divergence Penalty**: Write a function to compute the KL divergence between the current policy logits and the reference model logits. This is the "drift tax".
2.  **Advantages**: Assume you are given "advantages" (how much better an action was than expected).
3.  **Ratio**: Calculate the probability ratio $r_t(\theta) = \frac{\pi_\theta(a_t|s_t)}{\pi_{old}(a_t|s_t)}$.
4.  **Clipped Objective**: Implement the PPO loss: $L = \min(r_t A_t, \text{clip}(r_t, 1-\epsilon, 1+\epsilon) A_t)$.
5.  **Total Loss**: Combine the policy loss (negative of objective), the value function loss (MSE), and the entropy bonus (exploration).

## 🛠️ Tech Stack
- Python
- `torch`

## 📦 Deliverables
1.  A Python script `ppo_components.py` with functions for `compute_kl_penalty` and `ppo_loss`.
2.  A unit test with dummy tensors to verify the clipping logic works (e.g., set ratio > 1+epsilon and check if gradient is clipped).

## 🌟 Bonus Challenges (Optional)
- **GAE (Generalized Advantage Estimation)**: Implement the function to calculate advantages from rewards and values.
- **Reference Model**: Simulate a "step" where you compute the KL penalty for a sequence of tokens.
