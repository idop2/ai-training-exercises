# The Dispatcher: Building a Function Calling Router

## 🧠 Theory: Turning Talk into Action
LLMs are great at chatting, but they become superpowers when they can *do* things. **Function Calling** (or Tool Use) allows models to structure their output as executable commands rather than just text. A **Router** takes a user's intent ("What's the weather in Tokyo?") and decides which tool (e.g., `get_weather(city="Tokyo")`) to call. It's the bridge between natural language and your code's API, enabling agents to interact with the real world.

## 🚀 The Assignment
You will implement a `FunctionRouter` that acts as the brain for a simple agent. It will maintain a registry of available tools, interpret user queries, select the right tool, and execute it.

### Steps
1.  **Tool Registry**: Define a set of Python functions (e.g., `calculate_sum(a, b)`, `get_weather(city)`, `send_email(recipient, subject)`). Create a schema generator that turns these function signatures into a JSON format the LLM can understand.
2.  **The Router**: Build a `FunctionRouter` class. It should take a user query and your tool schemas, then prompt an LLM (use a mock or a real API like OpenAI/Anthropic) to pick a tool and generate the arguments.
3.  **Argument Parsing**: Parse the LLM's response (usually JSON) and validate it against the function's expected arguments.
4.  **Execution Loop**: Dynamically call the Python function with the parsed arguments and return the result to the user.

## 🛠️ Tech Stack
- Python 3.10+
- `inspect` module (to automatically generate schemas from python functions)
- `json`
- `openai` or `anthropic` (or any LLM client)

## 📦 Deliverables
1.  `tools.py`: A file containing your mock tools and the schema generator.
2.  `router.py`: The core routing logic that handles the LLM interaction and function execution.
3.  `main.py`: A CLI loop where you can type queries like "Email Bob about the meeting" and see the system "send" the email.

## 🌟 Bonus Challenges (Optional)
- **Parallel Calls**: Update your router to handle queries that require multiple tools at once (e.g., "What's the weather in Paris and London?").
- **Recursive Routing**: Allow a tool to call another tool, or have the router handle multi-step reasoning (Chain of Thought) before selecting a tool.
