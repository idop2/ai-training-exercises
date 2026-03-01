import json
from typing import List
from .models import Chunk
import numpy as np

def cosine_similarity(vec1: List[float], vec2: List[float]) -> float:
    """
    Calculate the cosine similarity between two vectors.
    """
    # TODO: Implement cosine similarity using numpy
    # np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
    raise NotImplementedError("Implement cosine_similarity in retrieve.py")

def load_index(index_path: str) -> List[Chunk]:
    """Load chunks from a JSON file."""
    if not index_path.exists():
        raise FileNotFoundError(f"Index {index_path} not found.")
    
    with open(index_path, "r") as f:
        data = json.load(f)
    return [Chunk(**chunk) for chunk in data]

def search(query: str, chunks: List[Chunk], top_k: int = 3) -> List[Chunk]:
    """
    Find the most similar chunks to the query.
    1. Embed the query.
    2. Compare query vector with all chunk vectors.
    3. Return top_k most similar chunks.
    """
    # TODO: Embed the query
    # query_vector = get_embedding(query) (you may want to import get_embedding)
    
    # TODO: Calculate similarities
    # scores = [(chunk, cosine_similarity(query_vector, chunk.vector)) for chunk in chunks]
    
    # TODO: Sort by score descending and return top k
    raise NotImplementedError("Implement search in retrieve.py")
