from pydantic import BaseModel
from typing import List, Optional

class Chunk(BaseModel):
    id: str
    text: str
    vector: Optional[List[float]] = None
    source: str

class Document(BaseModel):
    id: str
    text: str
    chunks: List[Chunk] = []
