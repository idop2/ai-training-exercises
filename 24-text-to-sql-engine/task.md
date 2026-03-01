# Text-to-SQL: Talk to your Database!

## 🧠 Theory: The Bridge to Structured Data
Most of the world's data lives in SQL databases, not text files. Enabling LLMs to query these databases is a superpower. However, you can't just feed the whole database to the LLM. You need a **Text-to-SQL** engine: a system that takes a natural language question, understands the database schema, generates a valid SQL query, executes it, and explains the answer.

## 🚀 The Assignment
You will build a Text-to-SQL pipeline that can answer questions about a sample database.

### Steps
1.  **The Database**: Set up a simple SQLite database (e.g., a "Sales" DB with tables for `Customers`, `Orders`, and `Products`). Populate it with dummy data.
2.  **Schema Extraction**: Write a function to extract the `CREATE TABLE` statements or a summary of the schema to feed into the prompt.
3.  **The Prompt**: Design a system prompt for the LLM.
    *   "You are an SQL expert. Here is the schema: {...}. Answer the user's question by generating a single SQL query."
4.  **Execution & Safety**:
    *   Take the LLM's output.
    *   (Crucial) Validate it prevents dangerous operations like `DROP` or `DELETE`.
    *   Execute it against the SQLite DB.
5.  **The Response**: Return the raw rows or ask the LLM to summarize the findings.

## 🛠️ Tech Stack
- **Python**
- **SQLite3**
- **LangChain** (optional, or just raw API calls)
- **OpenAI API** / **Ollama**

## 📦 Deliverables
1.  `db_setup.py`: Script to create and populate the dummy database.
2.  `engine.py`: The core logic that takes a question and returns the answer.
3.  `cli.py`: A command-line interface where the user can type "How many red widgets did we sell?" and get an answer.

## 🌟 Bonus Challenges
- **Self-Correction**: If the SQL query fails (e.g., syntax error), feed the error message *back* to the LLM and ask it to fix the query.
- **RAG for Schema**: If you had 100 tables, you couldn't fit them all in the context. Implement a retrieval step to find only the relevant tables for the user's question.
