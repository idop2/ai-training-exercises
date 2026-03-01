# RAG Pipeline Exercise

This exercise guides you through building a Retrieval-Augmented Generation (RAG) pipeline from scratch.

## Setup

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Environment Variables**:
    Copy `.env.example` to `.env` and add your OpenAI API key.
    ```bash
    cp .env.example .env
    # Edit .env with your key
    ```

## Usage

The main entry point is `rag.py`. It uses `typer` for CLI commands.

### Ingest Documents
This command reads a text file, chunks it, embeds the chunks, and saves them to `knowledge_base/index.json`.

```bash
python rag.py ingest knowledge_base/sample.txt
```

### Query
This command searches for relevant chunks and generates an answer using an LLM.

```bash
python rag.py query "What is RAG?"
```

## Your Task

You need to implement the core logic in the `src/` directory.

1.  **`src/ingest.py`**:
    - Implement `chunk_text`: Split text intelligently (e.g., by sentences).
    - Implement `get_embedding`: Generate embeddings using OpenAI or SentenceTransformers.

2.  **`src/retrieve.py`**:
    - Implement `cosine_similarity`: Calculate similarity between two vectors.
    - Implement `search`: Find the top-k most similar chunks to a query.

3.  **`src/generate.py`**:
    - Implement `generate_answer`: Construct a prompt with context and query the LLM.

## Testing

Run the tests to verify your implementation. Initially, they will fail with `NotImplementedError`.

```bash
pytest
```

Good luck!
