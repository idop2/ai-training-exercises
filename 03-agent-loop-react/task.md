# ReAct Agent Loop: Think, Act, Observe!

## 🧠 Theory: The ReAct Pattern
Large Language Models (LLMs) are powerful, but they can hallucinate or struggle with complex, multi-step tasks. The **ReAct** (Reason + Act) pattern solves this by prompting the model to interleave **Reasoning** traces (thoughts) with **Actions** (tool calls).

Instead of just asking "What is the capital of France multiplied by 5?", the model is taught to think:
1.  **Thought**: I need to find the capital of France first.
2.  **Action**: `search("capital of France")`
3.  **Observation**: "Paris"
4.  **Thought**: Now I need to multiply 5 by something... wait, I can't multiply text. I need to know the number of letters in "Paris" maybe? Or just multiply 5 by... (Wait, the question is ambiguous). Let's assume the user meant "What is 5 times the number of letters in the capital of France?".
5.  **Action**: `calculator(5 * 5)`
6.  **Observation**: 25
7.  **Final Answer**: 25.

By making the model "show its work", we get better reliability, debuggability, and the ability to use external tools!

## 🚀 The Assignment
Build a ReAct agent loop **from scratch**. No frameworks like LangChain or AutoGen allowed! You will implement the raw loop that interacts with an LLM, parses its output for tool calls, executes them, and feeds the result back.

### Steps

1.  **Define Your Tools**:
    - Create a `tools.py` file with simple Python functions:
        - `search(query)`: Returns a mock search result (e.g., rigid string matching or a simple dictionary).
        - `calculator(expression)`: Evaluates a mathematical expression (safely!).
        - `doc_lookup(doc_name)`: Returns the content of a mock document.

2.  **The System Prompt**:
    - Craft a system prompt that enforces the ReAct format. It should look something like this:
      ```text
      Use the following format:
      Question: the input question
      Thought: you should always think about what to do
      Action: the action to take, should be one of [search, calculator, doc_lookup]
      Action Input: the input to the action
      Observation: the result of the action
      ... (this Thought/Action/Action Input/Observation can repeat N times)
      Thought: I now know the final answer
      Final Answer: the final answer to the original input question
      ```

3.  **The Agent Loop (`agent.py`)**:
    - Implement a `run_agent(question)` function.
    - **Loop**:
        1.  Append the user's question to the history.
        2.  Call the LLM with the current history.
        3.  **Parse** the LLM's output. Look for `Action:` and `Action Input:`.
        4.  **Execute**: If an action is found, call the corresponding Python function from `tools.py`.
        5.  **Observe**: Append the tool's return value as `Observation: ...` to the history.
        6.  **Repeat**: Go back to step 2.
    - **Terminate**: If the LLM outputs `Final Answer:`, break the loop and return the answer.

## 🛠️ Tech Stack
- **Python 3.10+**
- **LLM Client**: `openai`, `anthropic`, or similar.
- **Regex (`re`)**: For robustly parsing the `Action:` and `Action Input:` lines.

## 📦 Deliverables
1.  **`tools.py`**: The file containing your tool functions.
2.  **`agent.py`**: The script containing your `run_agent` loop and main execution block.
3.  **`trace.log`**: A text file showing a full execution trace of your agent answering a complex question (e.g., "What is the population of the capital of France divided by 1000?").

## 🌟 Bonus Challenges (Optional)
-   **Step Budget**: Add a `max_steps` parameter to your loop to prevent infinite loops if the model gets stuck.
-   **Structured Trace**: Instead of just printing text, save the execution trace as a structured JSON list (`[{"thought": "...", "action": "...", "observation": "..."}, ...]`).
-   **Replay Mode**: Implement a "replay" feature where you can feed a previous trace (from the JSON above) into the agent to see if it reaches the same conclusion, or to debug specific steps.
-   **Deterministic Tools**: For `search`, ensure your mock returns consistent results so your tests are repeatable.
