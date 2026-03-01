# Data Curation: The MinHash Deduplicator!

## 🧠 Theory: Fuzzy Deduplication
In the era of massive datasets (CommonCrawl, etc.), duplicates are everywhere. Exact duplicates are easy to find (hashing), but what about "near-duplicates"? Maybe a sentence was changed, or a paragraph moved. Training on duplicates hurts model performance and memorization. **MinHash** and **Locality Sensitive Hashing (LSH)** are magical algorithms that let us find similar documents in massive datasets without comparing every pair (which would take forever!).

## 🚀 The Assignment
You will build a MinHash + LSH pipeline to detect and remove near-duplicate documents from a dataset.

### Steps
1.  **Shingling**: Implement a function to convert text into a set of "shingles" (n-grams). For example, "The cat sat" -> {"The cat", "cat sat"}.
2.  **MinHash Signatures**: Create a `MinHash` class.
    *   Generate `K` random hash functions.
    *   For each document, compute its signature: the minimum hash value for each of the `K` functions across all its shingles.
    *   *Why?* The probability that two sets have the same min-hash is equal to their Jaccard similarity!
3.  **LSH Index**: Implement Locality Sensitive Hashing.
    *   Divide the MinHash signatures into "bands".
    *   Hash the bands into buckets. If two documents land in the same bucket for any band, they are "candidates".
4.  **The Deduplicator**: Run your pipeline on a list of sentences, finding and removing the near-duplicates.

## 🛠️ Tech Stack
- **Python**
- **Numpy** (for efficient array operations)
- **Regex** (for basic text cleaning)

## 📦 Deliverables
1.  `minhash.py`: Your implementation of Shingling, MinHash, and LSH.
2.  `dedup.py`: A script that takes a list of strings (some very similar) and returns a clean list.
3.  `report.md`: A short explanation of how changing the number of hashes (`K`) and bands affects your false positives/negatives.

## 🌟 Bonus Challenges
- **Real Data**: Download a small slice of a dataset (like TinyStories or a Wikipedia dump) and dedup it.
- **Optimization**: Use `mmh3` (MurmurHash3) for faster hashing.
