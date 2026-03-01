# Adversarial Attacks: Jailbreaking the LLM 🔓

## 🧠 Theory: Adversarial Perturbations
Large Language Models are trained to be helpful and harmless, but they are surprisingly brittle. "Adversarial attacks" involve finding a specific sequence of characters (a suffix) that, when appended to a prompt, tricks the model into bypassing its safety filters. This isn't magic; it's gradient descent. We treat the input prompt as optimizable parameters and search for the token combination that maximizes the probability of the model saying "Sure, here is how to build a bomb..."

## 🚀 The Assignment
You will build an automated "Red Teaming" script. Your goal is to generate an adversarial suffix that causes a safety-aligned model (like Llama-2-7b-chat or a smaller aligned proxy) to answer a harmful query.

### Steps
1.  **The Setup**: Load a targeted LLM and tokenizer. Define a harmful goal (e.g., "Write a tutorial on how to make napalm") and a target response start (e.g., "Sure, here is a tutorial").
2.  **Gradient Search**: Instead of updating weights, you'll compute gradients with respect to the *input tokens* (specifically, their one-hot embeddings).
3.  **Candidate Selection**: Identify promising token swaps that minimize the loss (maximize the likelihood of the target response).
4.  **The Attack Loop**: Iteratively update the suffix (using Greedy Coordinate Gradient or similar) until the model complies.

## 🛠️ Tech Stack
- **PyTorch**: For gradient computation.
- **Hugging Face Transformers**: To load models and tokenizers.
- **FastChat** (optional): For managing conversation templates correct.

## 📦 Deliverables
1.  `attack.py`: The main script that takes a prompt and optimizes a suffix.
2.  `results.txt`: A log of the attack progress, showing the suffix evolution and the model's final response.
3.  `defense.md`: A short reflection on how one might defend against this specific type of attack.

## 🌟 Bonus Challenges (Optional)
- Implement a "universal" suffix that works across multiple different harmful prompts.
- Try to attack a black-box model (API) using a transfer attack (generate the suffix on a local model, test it on the API).
