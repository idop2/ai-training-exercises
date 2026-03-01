# Logit Processor: Hack the Probability Distribution!

## 🧠 Theory: Controlling the Uncontrollable
LLMs don't just pick words randomly; they calculate probabilities (logits) for every possible next token. A **Logit Processor** allows you to intercept these scores before the model makes a choice. Imagine being able to ban specific words, force rhymes, or boost positive sentiment just by tweaking some numbers! This gives you fine-grained control over generation that prompt engineering can't match.

## 🚀 The Assignment
You will build a `LogitProcessor` to modify the output of a local LLM (or a simulated one).

### Steps
1.  **The Interface**: Create a `LogitProcessor` abstract class with a `__call__(input_ids, scores)` method. This mimics the Hugging Face `LogitsProcessor` API.
2.  **Ban Words**: Implement a `NoBadWordsLogitProcessor` that sets the probability of specific token IDs (e.g., curse words) to `-infinity`.
3.  **Force Format**: Implement a simplified `JsonOnlyLogitProcessor` that boosts the probability of tokens valid in JSON syntax (e.g., `"{", "}", ":", ","`).
4.  **Sampling**: Write a `sample(logits, temperature=1.0)` function that applies softmax and selects a token based on the modified distribution.

## 🛠️ Tech Stack
- Python 3.10+
- `torch` or `numpy` (for tensor manipulation)
- `transformers` (optional, if you want to test on a real model like GPT-2)

## 📦 Deliverables
1.  `processor.py`: Your logit processor classes.
2.  `sampler.py`: The logic to sample from logits.
3.  `demo.py`: A script that runs a small language model (or mock logits) and shows how applying your processor changes the output (e.g., forcing a sentence to end with a specific word).

## 🌟 Bonus Challenges (Optional)
- **Rhyme Generator**: Create a processor that forces the model to rhyme by boosting tokens that end with the same phonetic sound as the previous line.
- **Watermarking**: Implement a subtle watermark by boosting specific tokens based on a random seed, allowing you to detect AI-generated text later.
