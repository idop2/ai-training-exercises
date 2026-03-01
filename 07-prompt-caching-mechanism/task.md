# Speed Demon: Implementing Prompt Caching

## 🧠 Theory: Why Repeat Yourself?
LLMs are stateless, meaning you usually send the entire conversation history and system prompt with every request. This is slow and expensive, especially for long contexts (like a whole book or a large codebase). **Prompt Caching** allows you to store the processed representation (KV cache) of the static parts of your prompt (like a long system instruction or a 50-shot example list). When a new request comes in with the same prefix, the model can skip processing those tokens and jump straight to generation.

## 🚀 The Assignment
You will simulate a **Prompt Caching** mechanism. Since we don't have direct access to model internals here, you will build a caching layer that hashes prompt prefixes and retrieves "pre-computed" responses (or mocks the latency savings).

### Steps
1.  **Prefix Identification**: Create a function `get_prefix_hash(prompt)` that identifies the common prefix (e.g., the system message) and generates a unique hash for it.
2.  **The Cache Store**: Implement a `PromptCache` class using a dictionary or a local database (like SQLite). It stores `(prefix_hash, timestamp, data)`.
3.  **The Cached Client**: Create a wrapper around a mock LLM function. When `generate(prompt)` is called:
    - Check if the prefix is in the cache.
    - If hit: Log "Cache Hit!", simulate a fast response (0.1s delay), and return the result.
    - If miss: Log "Cache Miss!", simulate a slow response (2.0s delay), store the prefix in the cache, and return the result.
4.  **TTL (Time To Live)**: Implement an eviction policy where cached items expire after 5 minutes.

## 🛠️ Tech Stack
- Python 3.10+
- `hashlib` (for hashing strings)
- `time` (for simulating latency)
- `sqlite3` or `diskcache` (optional, for persistent storage)

## 📦 Deliverables
1.  `cache_manager.py`: Your caching logic and storage class.
2.  `client.py`: The simulated LLM client that uses the cache.
3.  `benchmark.py`: A script that runs the same prompt 5 times and measures the total time, demonstrating the speedup after the first run.

## 🌟 Bonus Challenges (Optional)
- **Semantic Caching**: Instead of exact string matching, use vector embeddings to find *similar* prompts and reuse their cached responses (semantic similarity).
- **Partial Caching**: Implement logic to detect *how much* of the prompt is shared and simulate partial processing savings.
