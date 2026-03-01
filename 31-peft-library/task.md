# PEFT Library: Efficient Fine-Tuning Made Easy

## 🧠 Theory: The PEFT Ecosystem
While implementing LoRA from scratch is educational, in production we use robust libraries. Hugging Face's **PEFT** (Parameter-Efficient Fine-Tuning) library abstracts away the complexity. It supports LoRA, Prefix Tuning, P-Tuning, and prompt tuning. It seamlessly integrates with the `transformers` library, allowing you to fine-tune massive models on consumer hardware.

## 🚀 The Assignment
You will use the `peft` library to prepare a Hugging Face model for fine-tuning using LoRA configuration.

### Steps
1.  **Load a Base Model**: Use `transformers` to load a small model like `gpt2` or `opt-125m`.
2.  **Define Config**: Create a `LoraConfig`. Experiment with parameters like `r` (rank), `lora_alpha`, and `target_modules` (e.g., `["q_proj", "v_proj"]` or similar depending on model architecture).
3.  **Inject Adapters**: Use `get_peft_model(model, config)` to wrap the base model.
4.  **Inspect**: Print the trainable parameters. Use the helper function `print_trainable_parameters()` provided by PEFT or write your own.
5.  **Training Loop**: Set up a dummy training loop (feed random data, compute loss, `loss.backward()`, `optimizer.step()`) to verify the pipeline works.

## 🛠️ Tech Stack
- Python
- `transformers`
- `peft`
- `torch`

## 📦 Deliverables
1.  A script `peft_setup.py` that loads a model, applies LoRA, and prints the parameter stats.
2.  Console output showing the reduction in trainable parameters (screenshot or text file).

## 🌟 Bonus Challenges (Optional)
- **Save & Load**: Save the PEFT adapter weights using `model.save_pretrained()`, then load the base model and adapters separately to verify inference works.
- **Compare Configs**: Try different values for `r` (rank). How does it affect the number of trainable parameters?
