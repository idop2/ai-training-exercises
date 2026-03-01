# Vector DB Client SDK: Building the Bridge 🌉

## 🧠 Theory: Vector Search & Client SDKs
Vector Databases (like Pinecone, Milvus, Qdrant) are the backbone of modern RAG systems. They store high-dimensional vectors and allow for semantic search (finding vectors that are "close" in meaning). A "Client SDK" is the library developers use to interact with the database—it handles connection, data serialization, and API calls. Building one forces you to understand the network protocol and the underlying data structures.

## 🚀 The Assignment
You will design and implement a Python client library (SDK) for a hypothetical Vector Database called "VectorVault." You don't need the actual database; you'll simulate the server-side logic (or mock it) to focus on the client architecture: managing connections, batching requests, and handling errors gracefully.

### Steps
1.  **Define the API**: Create a `VectorVaultClient` class with methods like `connect()`, `create_collection()`, `upsert(vectors)`, `query(vector, top_k)`, and `delete(ids)`.
2.  **Mock the Server**: Implement a simple in-memory "server" (a class or a local HTTP server using FastAPI) that stores vectors in a dictionary and performs a brute-force cosine similarity search.
3.  **The Client Logic**: Implement the client methods. Ensure they handle network errors (simulated), validate inputs (e.g., vector dimensions), and serialize data to JSON/Protobuf.
4.  **Testing**: Write a test suite that uses your SDK to insert 100 vectors and query for the nearest neighbor.

## 🛠️ Tech Stack
- **Python**: The language of choice for AI SDKs.
- **Requests** (or **gRPC**): For communication (if building a real server).
- **NumPy**: For vector math in the mock server.
- **Pydantic**: For data validation.

## 📦 Deliverables
1.  `client.py`: The SDK code.
2.  `mock_server.py`: The simulated backend.
3.  `example_usage.py`: A script demonstrating how a user would install and use your library.

## 🌟 Bonus Challenges (Optional)
- Implement an async version of the client using `aiohttp`.
- Add a "batching" feature that automatically groups small `upsert` calls into larger chunks for efficiency.
