# The Smart Switchboard: Building a Semantic Router

## 🧠 Theory: Meaning Over Keywords
Traditional routing uses keywords ("if 'refund' in text, call support"). But what about "I want my money back"? A **Semantic Router** uses vector embeddings to understand the *meaning* (semantics) of a query and routes it to the most relevant handler. It's like having a receptionist who understands context, sarcasm, and intent, not just a keyword search engine. This allows you to build systems that handle natural variations in user language gracefully.

## 🚀 The Assignment
You will build a `SemanticRouter` that classifies user queries into intents (e.g., `politics`, `chitchat`, `technical_support`) based on semantic similarity.

### Steps
1.  **Define Routes**: Create a list of `Route` objects. Each route has a name and a list of example utterances (e.g., `technical_support`: ["My computer is broken", "I get a 404 error", "The screen is black"]).
2.  **Embed Examples**: Use a local embedding model (like `sentence-transformers` or `all-MiniLM-L6-v2`) to pre-compute the vector embeddings for all example utterances.
3.  **The Router Logic**: Implement a `route(query)` method.
    - Compute the embedding for the user's query.
    - Calculate the cosine similarity between the query vector and all example vectors.
    - If the highest similarity score is above a threshold (e.g., 0.8), return the corresponding route name.
    - If below the threshold, return a default "I don't understand" route.
4.  **Dynamic Routing**: Use this router to direct traffic to different "agent" functions (e.g., `handle_politics()`, `handle_chitchat()`).

## 🛠️ Tech Stack
- Python 3.10+
- `numpy` (for vector math)
- `sentence-transformers` (for generating embeddings)
- `scikit-learn` (optional, for cosine_similarity utility)

## 📦 Deliverables
1.  `router.py`: The `SemanticRouter` class and logic.
2.  `test_routes.py`: A script with 10 test queries (some tricky ones!) to verify your router picks the right category.
3.  `routes.json`: A file defining your routes and examples.

## 🌟 Bonus Challenges (Optional)
- **Fast Routing**: Instead of linear scanning, use a lightweight index (like Faiss) if you have thousands of routes.
- **Hybrid Routing**: Combine keyword matching (for exact commands) with semantic routing (for fuzzy intent) to get the best of both worlds.
