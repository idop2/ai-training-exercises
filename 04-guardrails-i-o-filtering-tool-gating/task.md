# Guardrails: The Gatekeeper of Your AI

## 🧠 Theory: Safety First
An AI model is powerful, but like any powerful engine, it needs safety mechanisms. **Guardrails** are the layers of filtering that wrap around your model's inputs and outputs. They prevent users from asking harmful questions (Input Filtering), ensure the model doesn't hallucinate or say something inappropriate (Output Filtering), and control which tools the model can actually access (Tool Gating). Think of it as the bouncer at the club: checking IDs and keeping the riffraff out. Without guardrails, your application is vulnerable to prompt injection, toxicity, and unauthorized actions.

## 🚀 The Assignment
You will build a `Guardrail` system that intercepts user interactions with a mock LLM. Your system will filter inputs for banned topics, sanitise outputs to remove PII (Personally Identifiable Information), and gate access to sensitive tools based on user roles.

### Steps
1.  **The Input Filter**: Create a function `check_input(prompt)` that scans for a list of banned keywords (e.g., "hack", "exploit"). If found, raise a `SecurityException`.
2.  **The Output Sanitizer**: Create a function `sanitize_output(response)` that detects patterns looking like email addresses or phone numbers and replaces them with `[REDACTED]`.
3.  **Tool Gating**: Implement a `ToolRegistry` where tools have required permissions (e.g., `delete_database` requires `admin`).
4.  **The Guarded Runner**: Combine these into a `GuardedRunner` class. It takes a user (with a role) and a prompt. It runs the input filter, "calls" the model (mock this), sanitizes the output, and if a tool call is generated, checks the user's permissions before allowing it.

## 🛠️ Tech Stack
- Python 3.10+
- `re` (Regular Expressions for pattern matching)
- `logging` (to track security events)
- Optional: `pydantic` for defining user roles and tool schemas.

## 📦 Deliverables
1.  A Python module `guardrails.py` containing your classes and functions.
2.  A test script `test_safety.py` that attempts to break your guardrails (e.g., trying to inject banned words, requesting sensitive data).
3.  A short `README.md` explaining your policy rules.

## 🌟 Bonus Challenges (Optional)
- **Fuzzy Matching**: Instead of exact keyword matching, use a small embedding model or Levenshtein distance to catch variations of banned words.
- **Hallucination Check**: Implement a basic fact-checking step that cross-references the model's output with a trusted "knowledge base" (a simple dictionary).
