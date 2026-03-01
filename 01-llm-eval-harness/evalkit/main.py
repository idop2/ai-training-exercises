import typer
import asyncio
import os
from typing import List
from rich.console import Console
from rich.table import Table
from dotenv import load_dotenv
from openai import AsyncOpenAI

from .models import TestCase, TestResult
from .loader import load_test_cases

# Load environment variables (e.g., OPENAI_API_KEY)
load_dotenv()

app = typer.Typer()
console = Console()

async def run_llm(prompt: str) -> str:
    """
    TODO: Implement this function to call an LLM (e.g., OpenAI).
    
    1. Initialize AsyncOpenAI client (use os.getenv("OPENAI_API_KEY"))
    2. Call chat.completions.create with the prompt
    3. Return the content string
    """
    # client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    raise NotImplementedError("Step 1: Implement the LLM API call in run_llm()")

def score_result(case: TestCase, actual_output: str) -> TestResult:
    """
    TODO: Implement scoring logic.
    
    1. Check for exact match (case-insensitive)
    2. (Bonus) Implement an 'LLM Judge' that asks the LLM if the answer is correct
    """
    raise NotImplementedError("Step 2: Implement scoring logic in score_result()")

async def run_evals(test_cases: List[TestCase]):
    """
    Runs the evaluation loop.
    """
    results: List[TestResult] = []
    
    console.print(f"[bold blue]Running {len(test_cases)} tests...[/bold blue]")

    # TODO: Run these in parallel using asyncio.gather for better performance
    for case in test_cases:
        actual_output = await run_llm(case.input)
        result = score_result(case, actual_output)
        results.append(result)
        
        # Print immediate feedback
        status_color = "green" if result.passed else "red"
        console.print(f"[{status_color}]{'PASS' if result.passed else 'FAIL'}[/{status_color}]: {case.input[:50]}...")

    return results

def print_report(results: List[TestResult]):
    """
    Prints a nice table of results using Rich.
    """
    table = Table(title="Evaluation Results")
    table.add_column("Category", style="cyan")
    table.add_column("Input", style="magenta")
    table.add_column("Actual Output", style="green")
    table.add_column("Passed", style="bold")
    table.add_column("Score")
    
    for result in results:
        status = "[green]YES[/green]" if result.passed else "[red]NO[/red]"
        table.add_row(
            result.case.category or "N/A",
            result.case.input[:30] + "..." if len(result.case.input) > 30 else result.case.input,
            result.actual_output[:30] + "..." if len(result.actual_output) > 30 else result.actual_output,
            status,
            str(result.score)
        )
        
    console.print(table)
    
    # Calculate stats
    total = len(results)
    passed = sum(1 for r in results if r.passed)
    pass_rate = (passed / total) * 100 if total > 0 else 0
    
    console.print(f"\n[bold]Pass Rate: {pass_rate:.1f}% ({passed}/{total})[/bold]")

@app.command()
def run(file: str = typer.Argument(..., help="Path to the test cases file (JSON/JSONL)")):
    """
    Run the evaluation harness on a test file.
    """
    try:
        test_cases = load_test_cases(file)
        # Run async function from sync CLI
        results = asyncio.run(run_evals(test_cases))
        print_report(results)
    except Exception as e:
        console.print(f"[bold red]Error:[/bold red] {e}")
        # raise typer.Exit(code=1) # Don't exit here so we can see the stack trace for learning

if __name__ == "__main__":
    app()
