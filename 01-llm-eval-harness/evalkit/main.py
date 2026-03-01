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
    Calls an LLM (OpenAI) with the provided prompt.
    """
    client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = await client.chat.completions.create(
        model="gpt-5-mini",
        messages=[{"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content.strip()

async def score_result(case: TestCase, actual_output: str) -> TestResult:
    """
    Scores the actual output against the expected output using the specified metric.
    """
    passed = False
    score = 0.0
    reason = "No expected output provided"

    if not case.expected_output:
        return TestResult(case=case, actual_output=actual_output, passed=passed, score=score, reason=reason)

    expected = case.expected_output.strip().lower()
    actual = actual_output.strip().lower()

    if case.metric == "exact_match":
        if actual == expected:
            passed = True
            score = 1.0
            reason = "Exact match"
        else:
            reason = f"Expected '{case.expected_output}', got '{actual_output}'"
    
    elif case.metric == "contains":
        if expected in actual:
            passed = True
            score = 1.0
            reason = f"Output contains '{case.expected_output}'"
        else:
            reason = f"Output does not contain '{case.expected_output}'"
            
    elif case.metric == "llm_judge":
        client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        prompt = f"""
        You are an impartial judge. Grade the accuracy of the following AI response based on the expected output.
        
        Input: {case.input}
        Expected Output: {case.expected_output}
        Actual AI Response: {actual_output}
        
        Is the AI response correct and accurate according to the expected output? 
        Answer with only 'YES' or 'NO', followed by a brief reason.
        """
        response = await client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0
        )
        judge_output = response.choices[0].message.content.strip()
        if judge_output.upper().startswith("YES"):
            passed = True
            score = 1.0
        reason = f"LLM Judge: {judge_output}"

    return TestResult(
        case=case,
        actual_output=actual_output,
        passed=passed,
        score=score,
        reason=reason
    )

async def run_evals(test_cases: List[TestCase]):
    """
    Runs the evaluation loop in parallel.
    """
    console.print(f"[bold blue]Running {len(test_cases)} tests in parallel...[/bold blue]")

    async def _run_and_score(case: TestCase) -> TestResult:
        actual_output = await run_llm(case.input)
        result = await score_result(case, actual_output)
        
        status_color = "green" if result.passed else "red"
        console.print(f"[{status_color}]{'PASS' if result.passed else 'FAIL'}[/{status_color}]: {case.input[:50]}...")
        return result

    # Run tests in parallel
    results = await asyncio.gather(*[_run_and_score(case) for case in test_cases])
    return list(results)

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
