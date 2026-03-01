from typing import List
from .models import Chunk
import openai
import os
from dotenv import load_dotenv

load_dotenv()

def generate_answer(query: str, chunks: List[Chunk]) -> str:
    """
    Construct a prompt with the retrieved chunks and ask the LLM.
    """
    # TODO: Build the context string from chunks
    # context = "\n\n".join([chunk.text for chunk in chunks])
    
    # TODO: Create a prompt
    # messages = [
    #     {"role": "system", "content": "You are a helpful assistant. Use the provided context to answer the user's question."},
    #     {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {query}"}
    # ]
    
    # TODO: Call OpenAI API (or other LLM)
    # client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    # response = client.chat.completions.create(model="gpt-4o", messages=messages)
    # return response.choices[0].message.content
    
    raise NotImplementedError("Implement generate_answer in generate.py")
