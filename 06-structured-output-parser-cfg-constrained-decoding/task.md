# Taming the Chaos: Structured Output & Constrained Decoding

## 🧠 Theory: Structure from Noise
LLMs naturally output unstructured text. But your application needs **JSON**, **SQL**, or specific formats like valid function calls. **Constrained Decoding** forces the model to follow a strict grammar (like a Context-Free Grammar or CFG) during generation, ensuring 100% syntactically correct output every time. It's like putting the model on rails so it can't derail into invalid syntax. This is crucial for building robust pipelines that don't crash on slightly malformed JSON.

## 🚀 The Assignment
You will create a `StructuredGenerator` that forces an LLM to output valid JSON matching a specific schema. You will use a combination of prompt engineering and output validation/repair.

### Steps
1.  **Define a Schema**: Create a Pydantic model or JSON schema for a `UserProfile` (e.g., `name`, `age`, `interests: List[str]`, `is_premium`).
2.  **The Prompt Template**: Write a prompt template that strictly instructs the model to only output JSON matching this schema. Include few-shot examples.
3.  **The Validator**: Create a function `validate_output(raw_text)` that attempts to parse the JSON and validates it against your schema. If parsing fails, retry with an error message (this is a simple form of "constrained generation" via feedback).
4.  **Advanced Constraint**: Implement a simple CFG parser or use a library (like `guidance` or `instructor`) to *force* the output format.

## 🛠️ Tech Stack
- Python 3.10+
- `pydantic` (for schema validation)
- `json`
- Optional: `guidance`, `outlines`, or `lmql` (if you want to implement true constrained decoding)

## 📦 Deliverables
1.  `schema.py`: Your Pydantic model definitions.
2.  `generator.py`: The function that prompts the LLM and handles validation/retries.
3.  `test_structure.py`: A script that generates 10 different user profiles and verifies they are all valid JSON.

## 🌟 Bonus Challenges (Optional)
- **JSON Repair**: Write a function that attempts to fix common JSON errors (e.g., missing closing braces, trailing commas) before validation.
- **CFG Implementation**: Create a minimal CFG parser that rejects invalid tokens as they are generated (if you have access to token-level probabilities).
