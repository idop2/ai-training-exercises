---
name: task
description: Generate a comprehensive TASK.md home assignment for a specific repository folder. Use when the user asks to create a task, assignment, or learning exercise for a folder.
---

# Task Creation Skill

## Goal
Transform a repository folder into a structured, engaging home assignment by creating a `TASK.md` file. The assignment should be educational, fun, and provide a clear path for learning the specific topic associated with the folder.

## Process

1.  **Analyze the Folder**:
    - Look at the folder name (e.g., `01-llm-eval-harness`, `15-logit-processor`) to determine the core subject.
    - If files exist, briefly skim them to understand the intended direction, but primarily focus on the folder's topic.

2.  **Determine the Learning Objective**:
    - What is the key concept? (e.g., "How LLM evaluation works", "Manipulating logits for sampling").
    - What is the "aha!" moment for this exercise?

3.  **Draft the `TASK.md` Content**:
    - **Title**: engaging and descriptive.
    - **Theory**: Explain the "why" and "how" simply. Use analogies if helpful.
    - **The Assignment**: Clear, step-by-step instructions on what to build.
    - **Deliverables**: Specific items the user must complete (code, output, analysis).
    - **Tech Stack**: Recommended libraries/tools (e.g., `numpy`, `torch`, `openai`, `pydantic`).

4.  **Review and Refine**:
    - Is it fun?
    - Is the difficulty appropriate (not too easy, not impossible)?
    - Is the tone encouraging?

5.  **Write and Clean Up**:
    - **IMPORTANT**: On case-insensitive file systems (like macOS/Windows), `TASK.md` and `task.md` are the same file.
    - First, check if a lowercase `task.md` exists. If so, **delete it** or rename it to `TASK.md`.
    - Then, write the new content to `[folder-path]/TASK.md`.
    - Confirm the file creation to the user.

## Output Format (TASK.md)

Use the following structure for the `TASK.md` file:

```markdown
# [Task Title]: [Subtitle with a fun twist]

## 🧠 Theory: [Concept Name]
[Brief, engaging explanation of the concept. Keep it under 200 words. Explain *why* this matters in the real world.]

## 🚀 The Assignment
[High-level description of what the user will build.]

### Steps
1.  **[Step 1 Name]**: [Description of what to do]
2.  **[Step 2 Name]**: [Description of what to do]
3.  **[Step 3 Name]**: [Description of what to do]

## 🛠️ Tech Stack
- [Language/Tool 1]
- [Library 1] (e.g., for [purpose])
- [Library 2]

## 📦 Deliverables
1.  [Deliverable 1] (e.g., A Python script `eval.py`)
2.  [Deliverable 2] (e.g., A report `results.md` containing...)
3.  [Deliverable 3]

## 🌟 Bonus Challenges (Optional)
- [Challenge 1]
- [Challenge 2]
```

## Tone Guidelines
- **Enthusiastic**: "Let's build a...", "Time to dive into..."
- **Clear**: Use simple language for complex topics.
- **Educational**: Focus on *learning by doing*.

## Example

**Folder**: `15-logit-processor`

**Generated `TASK.md` Title**: `# Logit Processor: Hack the Probability Distribution!`

**Theory Snippet**:
"LLMs don't just pick words randomly; they calculate probabilities (logits) for every possible next token. A Logit Processor allows you to intercept these scores before the model makes a choice. Imagine being able to ban specific words, force rhymes, or boost positive sentiment just by tweaking some numbers!"
