# The Architect: Building a Knowledge Graph from Scratch

## 🧠 Theory: Connecting the Dots
Text is linear, but knowledge is interconnected. A **Knowledge Graph (KG)** represents information as entities (nodes) and relationships (edges), capturing the "who, what, and how" in a structured way. This allows AI systems to reason about complex connections ("Alice works for Acme, Acme is located in NY, so Alice works in NY") that simple vector search often misses. It's the difference between reading a book and having a map of the characters' relationships.

## 🚀 The Assignment
You will build a `KGBuilder` pipeline that transforms raw unstructured text into a structured graph.

### Steps
1.  **The Extractor**: Create a prompt for an LLM that takes a piece of text (e.g., a news article about a tech merger) and outputs a list of Entities (Name, Type) and Relationships (Source, Target, Label).
    - Example: `{"entities": [{"name": "Apple", "type": "ORG"}, {"name": "Tim Cook", "type": "PERSON"}], "relations": [{"source": "Tim Cook", "target": "Apple", "label": "CEO_OF"}]}`
2.  **The Graph Builder**: Use the `networkx` library to programmatically build a graph from the extracted JSON. Add nodes for entities and edges for relationships.
3.  **Visualization**: Use `pyvis` or `matplotlib` to generate a visual representation of your graph. See the connections come to life!
4.  **Querying**: Write a simple function `find_neighbors(entity_name)` that returns all directly connected entities.

## 🛠️ Tech Stack
- Python 3.10+
- `networkx` (standard graph library)
- `pyvis` (for interactive HTML visualizations)
- `openai` or `anthropic` (for extraction)

## 📦 Deliverables
1.  `extractor.py`: The LLM logic to parse text into graph elements.
2.  `graph_builder.py`: The code to construct and query the NetworkX graph.
3.  `graph.html`: An interactive visualization of your knowledge graph.

## 🌟 Bonus Challenges (Optional)
- **Graph Database**: Instead of NetworkX (in-memory), store your graph in a real graph database like **Neo4j** (using the python driver).
- **Coreference Resolution**: Handle cases where "He" or "The company" refers to a previously mentioned entity.
