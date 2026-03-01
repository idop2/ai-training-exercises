# The Language of Machines: Implementing BPE Tokenization

## 🧠 Theory: How LLMs Read
LLMs don't read words like we do; they process sequences of integers called **tokens**. **Byte Pair Encoding (BPE)** is a fundamental algorithm that iteratively merges the most frequent pairs of characters (or bytes) into new tokens. This allows the model to handle rare words by breaking them down into subword units while keeping common words as single tokens. It's the standard for modern models like GPT-4, Llama 2, and more.

## 🚀 The Assignment
You will build a `BPETokenizer` from scratch. You will train it on a small corpus of text (e.g., a short story), learn the merge rules, and then use it to encode and decode strings.

### Steps
1.  **Training Phase**:
    - Start with a vocabulary of all unique characters in your corpus.
    - Tokenize the corpus into characters (e.g., "h e l l o").
    - Count the most frequent pair of adjacent tokens (e.g., "l l" appears 10 times).
    - Merge that pair into a new token ("ll").
    - Repeat this `N` times (e.g., 500 merges) to grow your vocabulary.
    - Store the merge rules (e.g., `('l', 'l') -> 'll'`).
2.  **Encoding Phase**:
    - Implement `encode(text)`: Split the text into characters, then iteratively apply your merge rules in order until no more merges are possible.
    - Return the list of token IDs.
3.  **Decoding Phase**:
    - Implement `decode(ids)`: Look up the tokens corresponding to the IDs and join them back into a string.

## 🛠️ Tech Stack
- Python 3.10+
- No external tokenization libraries (like `tokenizers` or `transformers`).
- `collections.Counter` (useful for counting pairs).

## 📦 Deliverables
1.  `tokenizer.py`: Your `BPETokenizer` class with `train`, `encode`, and `decode` methods.
2.  `test_tokenizer.py`: A script that trains on a sample text (e.g., *Alice in Wonderland*) and verifies that `decode(encode(text)) == text`.
3.  `vocab.json`: The saved vocabulary and merge rules.

## 🌟 Bonus Challenges (Optional)
- **GPT-2 Style**: Handle special characters and whitespace correctly (e.g., using a specific regex to split words before BPE).
- **Efficiency**: Optimize the pair counting step. Instead of re-scanning the whole text every iteration, can you update the counts locally?
