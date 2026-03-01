import json
from typing import List
from pathlib import Path
from .models import Chunk
import uuid
import os
import openai
from dotenv import load_dotenv

load_dotenv()

def load_file(file_path: Path) -> str:
    """Read a text file."""
    if not file_path.exists():
        raise FileNotFoundError(f"File {file_path} not found.")
    return file_path.read_text(encoding="utf-8")

def chunk_text(text: str, chunk_size: int = 500) -> List[str]:
    """
    Split the text into chunks of roughly chunk_size characters.
    Challenge: Try to split by sentences or paragraphs, not mid-word.
    """
    # TODO: Implement chunking logic here
    raise NotImplementedError("Implement chunk_text in ingest.py")

def get_embedding(text: str) -> List[float]:
    """
    Get embedding for a single string using OpenAI or SentenceTransformers.
    """
    # TODO: Implement embedding logic here
    # Example using OpenAI:
    # client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    # response = client.embeddings.create(input=text, model="text-embedding-3-small")
    # return response.data[0].embedding
    raise NotImplementedError("Implement get_embedding in ingest.py")

def embed_chunks(chunks: List[str], source: str) -> List[Chunk]:
    """
    Turn a list of text chunks into Chunk objects with embeddings.
    """
    embedded_chunks = []
    for text in chunks:
        vector = get_embedding(text)
        chunk = Chunk(
            id=str(uuid.uuid4()),
            text=text,
            vector=vector,
            source=source
        )
        embedded_chunks.append(chunk)
    return embedded_chunks

def save_index(chunks: List[Chunk], index_path: Path):
    """Save the list of chunks to a JSON file."""
    data = [chunk.model_dump() for chunk in chunks]
    index_path.parent.mkdir(parents=True, exist_ok=True)
    with open(index_path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"Saved {len(chunks)} chunks to {index_path}")
