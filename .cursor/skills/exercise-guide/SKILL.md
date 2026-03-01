---
name: exercise-guide
description: Create a detailed instruction plan and one-pager tradeoff analysis for an AI learning exercise in the current repo. Use when the user asks for help with an exercise, or wants a plan/tradeoffs for a specific folder (e.g., 01-llm-eval-harness).
---

# Exercise Guide

## Goal
Help the user build the exercise with a focus on deep learning, understanding limitations, and exploring tradeoffs. Do not just provide the final code. Guide the user through the implementation journey, emphasizing hands-on learning.

## Instructions

1.  **Identify the Exercise**:
    - Determine the relevant exercise folder (e.g., `01-llm-eval-harness/`) from the user's request or context.
    - Read the `task.md` file in that folder to understand the requirements.

2.  **Analyze the Task**:
    - Identify the core learning objectives (e.g., "Build an eval harness" -> learn about prompt management, scoring metrics, and evaluation workflows).
    - Determine the key technical challenges and decisions the user will face.

3.  **Generate a One-Pager Tradeoff Analysis**:
    - **Architecture**: Discuss high-level design choices (e.g., monolithic script vs modular package).
    - **Tools/Libraries**: Compare using raw libraries (for learning internals) vs high-level frameworks (for speed/production).
    - **Complexity**: Analyze simple vs robust implementations.
    - **Performance vs Learnability**: Highlight where optimization might obscure understanding vs where it's critical.
    - **Production Readiness**: clearly distinguish educational simplifications from production best practices.

4.  **Create a Detailed Instruction Plan**:
    - Break the task into logical, sequential steps.
    - For each step:
        - Explain the **Goal** (what to achieve).
        - Explain the **Concept** (why it matters).
        - Suggest **Actions** (what to code/design).
        - Include **Learning Checkpoints** (questions or tests to verify understanding).
    - Suggest libraries that maximize learning (e.g., implementing from scratch vs using a "black box" library).
    - Add **Thought Experiments** or **Bonus Challenges** to deepen understanding.

## Output Format

### Part 1: One-Pager Tradeoffs (Conceptual Architecture)
Structure this section clearly, using tables or lists to compare options. Focus on the "why" behind each choice.

**Example Table Structure:**
| Decision Point | Option A (Educational/Simple) | Option B (Production/Robust) | Tradeoff Analysis |
| :--- | :--- | :--- | :--- |
| **Storage** | JSON Files | SQL Database | JSON is easier to inspect and debug manually, good for learning file I/O. SQL is better for scale but adds setup overhead. |
| **Model** | Local Mock / API | Real LLM Integration | Mock allows fast iterating on logic. Real LLM tests actual behavior but costs money/time. |

### Part 2: Implementation Plan (Step-by-Step Guide)
Use a numbered list with sub-bullets for details. Encourage iterative development.

**Example Plan Step:**
**Step 1: Define the Evaluation Schema**
*   **Goal**: Create a data structure to hold test cases.
*   **Concept**: What constitutes a test case? (Input prompt, Expected output, assertion type).
*   **Action**: Create a `TestCase` class or type definition.
*   **Learning Point**: Why structure matters for extensibility.
*   **Checkpoint**: Can you represent a simple Q&A test case in this structure?

## Guidelines
- **Prioritize Learning**: Encourage the user to understand *how* things work, even if it means writing more code initially.
- **Explain "Why"**: Don't just give commands; explain the reasoning behind architectural decisions.
- **Highlight Limitations**: Be explicit about what the exercise solution *doesn't* cover compared to a real-world system.
