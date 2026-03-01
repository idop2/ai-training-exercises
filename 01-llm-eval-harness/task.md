# LLM Evaluation Harness: From Vibes to Verification

## 🧠 Theory: Why Evaluate?
Building LLM apps is easy; knowing if they work is hard. Most developers rely on "vibe checks"—manually looking at a few outputs and saying, "Yeah, looks good." But vibes don't scale, and they definitely don't catch regressions when you change your prompt or swap models.

An **Evaluation Harness** is your testing framework for AI. It automates the process of:
1.  **Dataset Loading**: Reading a set of inputs and expected outputs.
2.  **Inference**: Running those inputs through your LLM.
3.  **Scoring**: mathematically or semantically grading the output.
4.  **Reporting**: Telling you if your new prompt is actually better or if you just broke everything.

This exercise is about moving from "I think it works" to "I *know* it works."

## 🚀 The Assignment
You will build `evalkit`, a lightweight CLI tool that runs prompt-based tests against an LLM. You'll start with simple string matching and work your way up to implementing an "LLM-as-a-judge" scorer.

### Steps
1.  **Define the Test Schema**:
    - Design a `TestCase` class/model using Pydantic. It should store the `input_prompt`, `expected_output` (optional), and a `metric` type (e.g., "exact_match", "contains", "llm_judge").
    - Create a small dataset of 10-20 test cases in a JSON or YAML file.

2.  **Build the Runner**:
    - Create a Python script that loads your test cases.
    - Implement a function to call an LLM API (OpenAI, Anthropic, or a local model via Ollama) with the `input_prompt`.
    - **Tip**: Use `asyncio` to run these in parallel, or your eval will take forever!

3.  **Implement Scorers**:
    - **Deterministic**: Implement `exact_match` (output == expected) and `contains` (output includes expected substring).
    - **Probabilistic (The "Judge")**: Implement an `llm_judge` scorer. This uses a *second* LLM call to grade the output of the first one based on a rubric (e.g., "Is this response polite?").

4.  **Generate a Report**:
    - After running all tests, output a summary.
    - Calculate the **Pass Rate** (percentage of passing tests).
    - Use a library like `rich` to print a pretty table to the terminal, showing which specific tests failed and why.

## 🛠️ Tech Stack
- **Python** (3.10+)
- **Pydantic**: For robust data validation of your test schemas.
- **OpenAI SDK / LiteLLM**: To interact with language models.
- **Rich**: For beautiful terminal output and tables.
- **Typer / Click**: For building the CLI interface.

## 📦 Deliverables
1.  `evalkit/` folder containing your source code.
2.  `tests.json`: A sample suite of at least 10 diverse test cases (e.g., translation, summarization, fact-checking).
3.  A `README.md` explaining how to run your harness (e.g., `python main.py run --file tests.json`).
4.  **The Report**: A screenshot or text file showing the final output of your harness running on your test suite.

## 🌟 Bonus Challenges
- **CI/CD Gate**: Make your script return a non-zero exit code if the pass rate is below a threshold (e.g., 90%). This is how you block bad PRs!
- **HTML Report**: Generate a standalone HTML file with a nice view of the results (passed/failed tests, collapsible details).
- **Cost Tracking**: Estimate and display the cost of the eval run based on token usage.
