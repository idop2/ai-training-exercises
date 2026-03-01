# LLM Evaluation Harness

This project is a scaffold for building an LLM evaluation framework.
The boring parts (CLI, data loading, basic models) are done.
Your job is to implement the interesting parts: the LLM integration, the scoring logic, and the reporting.

## Setup

1.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Set up API Keys**:
    Copy `.env.example` to `.env` and add your OpenAI API key (or other provider).
    ```bash
    cp .env.example .env
    ```

## Usage

Run the harness with the sample data:

```bash
python -m evalkit.main run data/tests.json
```

Or use the larger dataset:

```bash
python -m evalkit.main run data/sci_fi_jeopardy.jsonl
```

**Note**: The code will raise `NotImplementedError` until you complete the tasks below!

## Your Tasks

Open `evalkit/main.py` and look for the `TODO` comments.

1.  **Implement `run_llm`**:
    *   Initialize the `AsyncOpenAI` client.
    *   Call `chat.completions.create` with the prompt.
    *   Return the response content.
    *   *Why?* While standard, this connects your harness to the "brain".

2.  **Implement `score_result`**:
    *   Start with a simple exact match (compare `actual_output` vs `case.expected_output`).
    *   **Challenge**: Implement an "LLM Judge". Call the LLM *again* with a prompt asking it to grade the answer (e.g. "Is the answer 'Paris' close enough to 'The capital is Paris'?").
    *   *Why?* This is the heart of modern AI evaluation.

3.  **Optimize**:
    *   Update `run_evals` to use `asyncio.gather` for parallel execution.

## Project Structure

*   `evalkit/models.py`: Defines `TestCase` and `TestResult` data structures.
*   `evalkit/loader.py`: Handles loading test cases from files.
*   `evalkit/main.py`: The main entry point. **This is where you will write most of your code.**
