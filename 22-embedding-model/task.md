# Embedding Model: The Search Engine Core!

## 🧠 Theory: Text to Vectors
How do computers understand that "King" - "Man" + "Woman" ≈ "Queen"? Or that "bicycle" is related to "pedal"? They use **Embeddings**—dense vector representations of text. While LLMs predict the *next* token, Embedding Models are trained to pull similar texts close together in vector space and push dissimilar ones apart. This is the backbone of semantic search and RAG.

## 🚀 The Assignment
You will build and train a model to generate semantic embeddings using a Contrastive Loss approach.

### Steps
1.  **The Architecture**: Use a small BERT-like model (or a truncated Transformer encoder). You want the pooling output (e.g., the average of all token vectors) to represent the sentence.
2.  **The Data**: Create (or download) a dataset of pairs.
    *   *Positive pairs*: (Sentence, Paraphrase) or (Question, Answer).
    *   *Negative pairs*: (Sentence, Random Sentence).
3.  **Contrastive Loss**: Implement **InfoNCE** or **Triplet Loss**.
    *   Goal: Maximize the cosine similarity between positive pairs and minimize it for negative pairs (or other samples in the batch).
4.  **Training**: Train the model on your pairs.
5.  **Visualization**: Use PCA or t-SNE to visualize a few test sentences. "Cat" and "Dog" should be closer than "Cat" and "Car".

## 🛠️ Tech Stack
- **Python**
- **PyTorch**
- **Scikit-Learn** (for PCA/t-SNE)
- **Sentence-Transformers** (optional, for reference/data)

## 📦 Deliverables
1.  `model.py`: Your embedding model architecture.
2.  `train.py`: The training loop with your contrastive loss implementation.
3.  `visualize.py`: A script that takes a list of words/sentences, computes embeddings, and saves a 2D scatter plot.

## 🌟 Bonus Challenges
- **Hard Negatives**: Improve training by mining "hard negatives"—sentences that look similar (e.g., share words) but have different meanings.
- **MTEB**: Run a simplified evaluation using the MTEB (Massive Text Embedding Benchmark) framework logic on a tiny subset.
