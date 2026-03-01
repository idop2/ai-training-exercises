# Model Merging: SLERP It Up!

## 🧠 Theory: Merging Without Retraining
What if you fine-tuned Llama-2 on math, and another version on code? Can you combine them? Yes! **Model Merging** lets you fuse weights. Simple averaging works sometimes, but **SLERP (Spherical Linear Interpolation)** is better. Since high-dimensional weight spaces are often hyperspherical, linear interpolation cuts *through* the sphere (losing magnitude), while SLERP follows the surface (preserving geometry).

## 🚀 The Assignment
You will implement the SLERP algorithm from scratch and apply it to merge two 1D tensors representing model weights.

### Steps
1.  **Understand SLERP**: $\text{Slerp}(p_0, p_1, t) = \frac{\sin((1-t)\Omega)}{\sin(\Omega)} p_0 + \frac{\sin(t\Omega)}{\sin(\Omega)} p_1$, where $\Omega$ is the angle between vectors.
2.  **Normalize**: Normalize the input vectors to unit length to compute the angle $\Omega$ (using dot product).
3.  **Handle Edge Cases**: If vectors are parallel (dot product ~ 1), fallback to linear interpolation to avoid division by zero.
4.  **The Function**: Write `slerp(v1, v2, t)` where `t` is the interpolation factor (0.0 to 1.0).
5.  **Visual Proof**: Create two 2D vectors, merge them with $t=0.5$, and plot the result. Compare it to linear averaging (`(v1+v2)/2`).

## 🛠️ Tech Stack
- Python
- `numpy` or `torch`
- `matplotlib` (for visualization)

## 📦 Deliverables
1.  A Python script `slerp_merge.py` with your implementation.
2.  A plot `slerp_vs_linear.png` showing the difference between linear interpolation and SLERP for two 2D vectors.

## 🌟 Bonus Challenges (Optional)
- **Full Model Merge**: Load two small Hugging Face models (same architecture), extract their `state_dict`, and merge them using your SLERP function layer-by-layer.
- **TIES Merging**: Research and implement the TIES merging method (Trim, Elect Sign, Merge).
