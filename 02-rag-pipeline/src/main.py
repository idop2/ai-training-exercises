import typer
import os
from pathlib import Path
from rich.console import Console
from .ingest import load_file, chunk_text, embed_chunks, save_index
from .retrieve import load_index, search
from .generate import generate_answer
from .models import Chunk, Document

app = typer.Typer()
console = Console()

DATA_DIR = Path(__file__).parent.parent / "knowledge_base"
INDEX_PATH = DATA_DIR / "index.json"

@app.command()
def ingest(file_path: Path):
    """
    Ingest a text file into the vector index.
    """
    console.print(f"[bold green]Ingesting {file_path}...[/bold green]")
    try:
        text = load_file(file_path)
        chunks = chunk_text(text)
        console.print(f"Split text into {len(chunks)} chunks.")
        
        embedded_chunks = embed_chunks(chunks, source=file_path.name)
        console.print(f"Generated embeddings for {len(embedded_chunks)} chunks.")
        
        save_index(embedded_chunks, INDEX_PATH)
        console.print(f"[bold green]Index saved to {INDEX_PATH}[/bold green]")
    except NotImplementedError as e:
        console.print(f"[bold red]Error: {e}[/bold red]")
    except Exception as e:
        console.print(f"[bold red]Unexpected Error: {e}[/bold red]")

@app.command()
def query(question: str):
    """
    Ask a question about the ingested documents.
    """
    console.print(f"[bold blue]Question: {question}[/bold blue]")
    try:
        if not INDEX_PATH.exists():
            console.print("[bold red]Index not found. Run ingest first.[/bold red]")
            raise typer.Exit(code=1)
            
        chunks = load_index(INDEX_PATH)
        relevant_chunks = search(question, chunks)
        
        console.print("\n[bold yellow]Relevant Context:[/bold yellow]")
        for i, chunk in enumerate(relevant_chunks):
            console.print(f"{i+1}. {chunk.text[:100]}... (Source: {chunk.source})")
            
        answer = generate_answer(question, relevant_chunks)
        console.print("\n[bold green]Answer:[/bold green]")
        console.print(answer)
        
    except NotImplementedError as e:
        console.print(f"[bold red]Error: {e}[/bold red]")
    except Exception as e:
        console.print(f"[bold red]Unexpected Error: {e}[/bold red]")

if __name__ == "__main__":
    app()
