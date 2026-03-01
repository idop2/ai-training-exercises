# RAG Pipeline: Give Your LLM a Second Brain

## 🧠 Theory: Open Book vs. Closed Book
Imagine taking a difficult exam.
- **Closed Book (Standard LLM)**: You rely purely on your memory (training data). If you don't know the answer, you might guess (hallucinate).
- **Open Book (RAG)**: You can look up relevant information in a textbook before answering.

**Retrieval-Augmented Generation (RAG)** is the architecture that gives LLMs an "open book" capability. It allows them to access private, up-to-date, or specific data that wasn't in their training set.

The pipeline is simple:
1.  **Ingest**: Chop documents into small pieces (chunks).
2.  **Embed**: Turn those chunks into lists of numbers (vectors) that represent their meaning.
3.  **Retrieve**: When a user asks a question, find the most similar chunks.
4.  **Generate**: Feed the user's question + the retrieved chunks to the LLM.

## 🚀 The Assignment
You will build a **RAG Pipeline from Scratch**. You'll start by manually implementing vector similarity (to understand the magic) and then use a real vector database. By the end, you'll have a CLI tool that can answer questions about any text file you feed it.

### Steps
1.  **The Indexer (Ingestion)**:
    - Create a script that reads a text file (e.g., a Paul Graham essay or your own notes).
    - **Chunking**: Split the text into manageable chunks (e.g., 3 sentences or 500 characters). *Challenge*: Don't split words in half!
    - **Embedding**: Use an API (OpenAI `text-embedding-3-small`) or a local model (SentenceTransformers) to turn each chunk into a vector.
    - **Storage**: Store these `(text, vector)` pairs in a simple list or local file (JSON/Pickle).

2.  **The Retriever (Search)**:
    - Implement a `search(query, top_k=3)` function.
    - Turn the user's query into a vector.
    - Calculate **Cosine Similarity** between the query vector and all your stored chunk vectors.
    - Return the top `k` most similar chunks.
    - *Math Check*: Use `numpy` to calculate the dot product manually!

3.  **The Generator (Chat)**:
    - Construct a prompt that looks like:
      ```
      Context: {retrieved_chunks}
      Question: {user_query}
      Answer the question using only the context above.
      ```
    - Send this to the LLM and print the response.

4.  **Citations**:
    - Modify your system to return the *source ID* or *chunk ID* of the information used.

## 🛠️ Tech Stack
- **Python** (3.10+)
- **Numpy**: For vector math (cosine similarity).
- **OpenAI SDK / SentenceTransformers**: For generating embeddings.
- **ChromaDB / LanceDB** (Optional/Advanced): If you want to swap your manual list for a real vector DB.
- **Typer**: For the CLI.

## 📦 Deliverables
1.  `rag.py`: A CLI tool with commands like `ingest <file>` and `query "<question>"`.
2.  `knowledge_base/`: A folder containing your test documents and the saved index.
3.  `manual_vs_db.md`: A short reflection on implementing vector search manually vs using a library.

## 🌟 Bonus Challenges
- **"I Don't Know"**: If the highest similarity score is below a certain threshold (e.g., 0.4), make the bot say "I don't have enough information" instead of hallucinating.
- **Hybrid Search**: Combine your vector search with a simple keyword search (BM25 style) to find exact matches.
- **Web UI**: Wrap your pipeline in a simple Streamlit app.
