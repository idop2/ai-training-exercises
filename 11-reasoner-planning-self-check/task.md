# Think Before You Speak: Adding Reasoning & Planning

## 🧠 Theory: The Agent Loop
Most LLMs are "reactive"—they answer immediately. But complex tasks require **reasoning** (breaking a problem down), **planning** (sequencing steps), and **self-correction** (checking if the answer is right). This loop transforms a simple chatbot into a powerful agent capable of solving multi-step problems, like debugging code or planning a multi-city trip.

## 🚀 The Assignment
You will build a `ReasoningAgent` that doesn't just answer but follows a structured thought process.

### Steps
1.  **The Planner**: Create a `Plan` function. Given a complex user goal (e.g., "Plan a 3-day trip to Paris under $500"), use an LLM to generate a step-by-step plan (e.g., `1. Search for flights`, `2. Find budget hotels`, `3. Create itinerary`).
2.  **The Executor**: Create an `Execute` loop. For each step in the plan, use a mock tool (e.g., `search_tool(query)`) or ask the LLM to generate the next action.
3.  **The Reflector (Self-Check)**: Create a `Reflect` function. After generating a final answer, have the model critique its own work ("Did I meet the budget constraint? Is the itinerary realistic?"). If the check fails (e.g., score < 8/10), the agent should revise its plan and try again.

## 🛠️ Tech Stack
- Python 3.10+
- `openai` or `anthropic` (for reasoning)
- `langchain` (optional, for tools/chains) or just raw API calls.

## 📦 Deliverables
1.  `agent.py`: Your `ReasoningAgent` class.
2.  `test_planning.py`: A script that runs the agent on a complex query (e.g., "Solve this riddle: X is half of Y, and Y is 10. What is X^2?").
3.  `logs/`: A folder containing the agent's thought traces (intermediate plans and reflections).

## 🌟 Bonus Challenges (Optional)
- **ReAct Pattern**: Combine Reasoning and Acting (interleaved thought -> action -> observation -> thought).
- **Tool Use**: Give the agent real tools (like a calculator or a weather API) to solve problems that require external data.
