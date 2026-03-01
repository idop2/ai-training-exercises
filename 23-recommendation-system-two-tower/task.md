# Recommendation System: The Two-Tower Architecture!

## 🧠 Theory: Matching Users to Items
Netflix, YouTube, and Amazon all use recommendation systems to find the needle in the haystack. When you have millions of users and millions of items, you can't run a heavy model on every pair. The solution? **Two-Tower Networks**. One neural network encodes the User, another encodes the Item. You train them so that the dot product of their outputs is high if the user likes the item. This allows for lightning-fast retrieval using Approximate Nearest Neighbors.

## 🚀 The Assignment
You will build a Two-Tower retrieval model for a movie recommendation scenario.

### Steps
1.  **Data**: Use the **MovieLens** small dataset.
2.  **User Tower**: Build a Neural Network that takes user features (ID embedding, age, genre history) and outputs a vector (e.g., dim=64).
3.  **Item Tower**: Build a Neural Network that takes movie features (ID embedding, title embedding, genre) and outputs a vector of the same size.
4.  **Training**:
    *   Input: Pairs of (User, Movie) with a label (1 for watched/liked, 0 for negative/random sample).
    *   Loss: Binary Cross Entropy or Contrastive Loss on the dot product of the two vectors.
5.  **Retrieval**:
    *   Pre-compute vectors for ALL movies.
    *   For a specific user, compute their vector.
    *   Find the top 5 movies with the highest dot product.

## 🛠️ Tech Stack
- **Python**
- **PyTorch** or **TensorFlow/Keras**
- **Pandas** (for data processing)
- **Faiss** (optional, for efficient vector search)

## 📦 Deliverables
1.  `model.py`: Definition of the UserTower and ItemTower.
2.  `train.py`: Script to train the towers.
3.  `recommend.py`: A script where you input a User ID and it prints out the top 5 recommended movie titles.

## 🌟 Bonus Challenges
- **Cold Start**: How does your model handle a new user with no history? Implement a fallback strategy.
- **ANN**: Use a library like `Faiss` to index the movie vectors and demonstrate how much faster it is than a brute-force sort.
