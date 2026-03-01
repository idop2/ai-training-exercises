# Beyond Keywords: Implementing Graph RAG

## 🧠 Theory: The Best of Both Worlds
Standard RAG retrieves documents based on similarity. But what if the answer requires hopping between concepts? **Graph RAG** enhances retrieval by traversing a Knowledge Graph. Instead of just finding a chunk mentioning "Apple", it can traverse the graph to find "Apple -> produces -> iPhone -> competitors -> Samsung", providing much richer context for the LLM. It helps answer multi-hop questions that keyword search fails on.

## 🚀 The Assignment
You will build a **Graph RAG** system that queries your previously built Knowledge Graph.

### Steps
1.  **Entity Linking**: Create a function `link_entities(query)` that identifies key entities in a user's question (e.g., "Who competes with the iPhone maker?"). Use string matching or fuzzy search against your graph's nodes.
2.  **Graph Traversal**: Implement a `get_context(entity, depth=2)` function using `networkx`. Starting from the linked entity ("iPhone"), traverse 2 hops out to find connected concepts ("Apple", "competitors", "Samsung").
3.  **Context Construction**: Convert this subgraph (list of triples: Subject-Predicate-Object) into natural language text.
4.  **Generation**: Feed this structured context to an LLM to answer the user's question. Compare the answer with standard RAG (retrieving the raw text chunk).

## 🛠️ Tech Stack
- Python 3.10+
- `networkx` (for graph operations)
- `openai` or `anthropic` (for answering)
- `fuzzywuzzy` or `thefuzz` (for entity linking)

## 📦 Deliverables
1.  `linker.py`: Logic to map user queries to graph nodes.
2.  `rag.py`: The core RAG pipeline (Traverse -> Contextualize -> Generate).
3.  `comparison.md`: A short report comparing an answer from Graph RAG vs. standard RAG on a complex question.

## 🌟 Bonus Challenges (Optional)
- **Hybrid RAG**: Combine vector search (find relevant text chunks) with graph traversal (find related entities) for the ultimate context window.
- **Community Detection**: Use algorithms like Leiden to find clusters of related nodes and summarize entire topics.
