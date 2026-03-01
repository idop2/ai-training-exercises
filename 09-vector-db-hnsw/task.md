# Vectors in Space: Building a Mini Vector Database

## 🧠 Theory: The Brain's Filing Cabinet
**Vector Databases** are the memory of modern AI applications. They store high-dimensional vectors (embeddings) representing text, images, or audio. To find similar items quickly among millions, they use Approximate Nearest Neighbor (ANN) algorithms like **HNSW** (Hierarchical Navigable Small World). This lets you find "conceptual neighbors" in milliseconds rather than scanning every single item (brute force), which is prohibitively slow for large datasets.

## 🚀 The Assignment
You will build a simple `VectorStore` from scratch. You will start with a basic brute-force search and then implement a simple optimization to understand how vector indexing works.

### Steps
1.  **The Store**: Create a `VectorStore` class that can store vectors (numpy arrays) along with metadata (e.g., `{"id": 1, "text": "hello"}`).
2.  **Brute Force Search**: Implement a `search(query_vector, k=5)` method that calculates the cosine distance between the query and *every* stored vector, sorts them, and returns the top `k`. Benchmark this with 10,000 vectors.
3.  **Simple Indexing**: Implement a basic index to speed up search. A simple approach is **IVF (Inverted File Index)**:
    - Cluster vectors into `C` clusters (using K-Means).
    - Assign each vector to a cluster centroid.
    - At query time, find the nearest cluster centroid and *only* search vectors within that cluster (and maybe its neighbors).
4.  **HNSW Concept**: (Optional/Advanced) Read about HNSW graph structures. Implement a very simple graph where each node connects to its nearest neighbors, and search traverses the graph greedily.

## 🛠️ Tech Stack
- Python 3.10+
- `numpy` (essential for vector operations)
- `scikit-learn` (for K-Means or generating dummy data)
- `time` (for benchmarking)

## 📦 Deliverables
1.  `vector_store.py`: Your `VectorStore` implementation with `add` and `search` methods.
2.  `benchmark.py`: A script that inserts 10,000 random vectors and compares the search time of brute-force vs. your indexed method.
3.  `README.md`: Explain your indexing strategy and the speedup you achieved.

## 🌟 Bonus Challenges (Optional)
- **Persistence**: Save your index to disk and load it back.
- **Filtering**: Add metadata filtering (e.g., `search(query, filter={"category": "news"})`) to your search process.
