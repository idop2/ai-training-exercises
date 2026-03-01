---
name: scaffold-exercise
description: Scaffolds a new coding exercise by analyzing TASK.md and generating boilerplate code, tests, and configuration. Use when the user asks to "setup", "start", or "prepare" a new exercise or task.
---

# Scaffold Exercise

## Goal
To prepare a coding exercise for a student by generating all the "boring" infrastructure (CLI, data loading, configuration) so they can focus entirely on the "interesting" core logic (algorithms, API calls, model implementation).

## Workflow

1.  **Analyze the Task**:
    - Read the `TASK.md` file in the target directory.
    - Identify the core learning objectives ("Interesting" parts).
    - Identify the necessary infrastructure ("Boring" parts).

2.  **Plan the Scaffold**:
    - **Directory Structure**: Create a clean, standard layout (e.g., `src/`, `data/`, `tests/`).
        - **Override**: If `TASK.md` specifies different folder names (e.g. `knowledge_base/` instead of `data/`), follow `TASK.md`.
    - **Deliverables**: Create empty placeholder files for any non-code deliverables mentioned in `TASK.md` (e.g., `reflection.md`, `architecture_diagram.png`).
    - **Dependencies**: Create a `requirements.txt` or `package.json`.
    - **Configuration**: Create `.env.example` for secrets (API keys).
    - **Data**: Create or download sample data (JSON/CSV/TXT) to test against.
        - Ensure the `ingest` command works out-of-the-box with this sample data.

3.  **Generate Code**:
    - **Infrastructure**: Fully implement data loaders, CLI arguments parsing, and main execution loops.
    - **Core Logic**: Create function signatures but raise `NotImplementedError` with helpful TODO comments explaining what to do.
    - **Type Hints**: Use strong typing (e.g., Pydantic models) to define inputs/outputs clearly.

4.  **Create Verification**:
    - Create a test file or a runner script that executes the student's code against the sample data.
    - Ensure it fails gracefully (with the `NotImplementedError` message) until the student completes the task.

5.  **Documentation**:
    - Create a `README.md` in the exercise folder explaining:
        - How to install dependencies.
        - How to set up environment variables.
        - How to run the code.
        - What specific functions need to be implemented.

## implementation Guidelines

### Python Exercises
- Use `typer` or `click` for CLIs.
- Use `pydantic` for data validation.
- Use `pytest` for testing.
- Use `rich` for pretty terminal output.
- Always include a `__main__.py` or `main.py` entry point.

### JavaScript/TypeScript Exercises
- Use `commander` for CLIs.
- Use `zod` for validation.
- Use `jest` or `vitest` for testing.
- Include a `package.json` with scripts (`start`, `test`).

## Example Prompt for Agent
"Read TASK.md in `05-agent-loop/`. Create a Python scaffold where `agent.py` has the loop logic as `NotImplementedError`, but `cli.py` and `loader.py` are fully working. Create a `run` command that tries to execute the agent."
