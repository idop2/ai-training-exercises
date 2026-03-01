# Code Interpreter: Build a Safe Sandbox!

## 🧠 Theory: The Code Interpreter Pattern
Large Language Models are great at writing code, but running that code is risky. A "Code Interpreter" (like in ChatGPT) isn't just a Python shell; it's a secure, isolated environment where the AI can execute code, see the results, and iterate. This allows LLMs to solve math problems, analyze data, and create charts—things they can't do with text alone. The magic lies in the *feedback loop*: Code -> Error -> Correction -> Success.

## 🚀 The Assignment
You will build a secure Python execution sandbox that an "Agent" (simulated or real) can call to run code.

### Steps
1.  **The Executor**: Write a Python script that accepts a string of Python code and executes it.
    *   *Constraint*: You must capture `stdout` (print statements) and `stderr` (errors).
    *   *Constraint*: The execution must have a timeout (e.g., 5 seconds) to prevent infinite loops.
2.  **The Sandbox**: Isolate the execution.
    *   *Simple Level*: Use Python's `subprocess` module to run the code in a separate process with limited permissions.
    *   *Advanced Level*: Use Docker to run the code in a disposable container.
3.  **The API**: Wrap this in a function `execute_code(code: str) -> dict` that returns `{ "output": "...", "error": "...", "success": bool }`.
4.  **The Data Analysis Test**: Create a test case where the input code generates a simple plot (e.g., using `matplotlib`) and saves it to a specific directory. Verify the file exists.

## 🛠️ Tech Stack
- **Python** (subprocess, sys)
- **Docker** (optional, for advanced isolation)
- **Matplotlib** (for testing data generation)

## 📦 Deliverables
1.  `sandbox.py`: The core logic for executing code safely.
2.  `test_safety.py`: A script that tries to run "bad" code (like infinite loops or accessing system files) to prove your sandbox works.
3.  `example_usage.py`: A demonstration where you simulate an LLM generating code to calculate the 100th Fibonacci number, running it, and printing the result.

## 🌟 Bonus Challenges
- **Stateful Execution**: Allow variables to persist between calls (like a Jupyter notebook).
- **Network Block**: Configure your sandbox to block internet access so the executed code can't leak data.
