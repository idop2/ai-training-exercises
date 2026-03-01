import pytest
from src.ingest import chunk_text, get_embedding
from src.retrieve import cosine_similarity
from src.generate import generate_answer

def test_chunk_text_raises_not_implemented():
    with pytest.raises(NotImplementedError):
        chunk_text("This is a test text.")

def test_get_embedding_raises_not_implemented():
    with pytest.raises(NotImplementedError):
        get_embedding("test")

def test_cosine_similarity_raises_not_implemented():
    with pytest.raises(NotImplementedError):
        cosine_similarity([1.0, 0.0], [0.0, 1.0])

def test_generate_answer_raises_not_implemented():
    with pytest.raises(NotImplementedError):
        generate_answer("query", [])
