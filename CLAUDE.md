# AI Training Exercises

This repository contains exercises for learning AI Engineering.

## Project Structure

- **Exercises**: Each exercise is in its own numbered directory (e.g., `01-llm-eval-harness`).
- **Task**: Each exercise has a `TASK.md` file defining the requirements.
- **Skills**: Agent Skills are located in `.cursor/skills` and provide specialized capabilities.

## Available Skills

The following skills are available to assist with the exercises. When asked to perform these actions, please read the corresponding `SKILL.md` file and follow its instructions.

### 1. Scaffold Exercise
- **Goal**: Generate boilerplate code, dependencies, and infrastructure for a new exercise.
- **Trigger**: "Scaffold the exercise", "Setup the project", "Start the task".
- **Source**: `.cursor/skills/scaffold-exercise/SKILL.md`
- **Action**: Read `TASK.md`, create directory structure, add `requirements.txt`/`package.json`, and generate starter code with `NotImplementedError`.

### 2. Create Task
- **Goal**: Generate a comprehensive `TASK.md` assignment for a folder.
- **Trigger**: "Create a task", "Write the assignment".
- **Source**: `.cursor/skills/task/SKILL.md`
- **Action**: Generate a detailed `TASK.md` based on the folder name and learning objectives.

### 3. Exercise Guide
- **Goal**: Create a detailed implementation plan and tradeoff analysis.
- **Trigger**: "Create a plan", "How should I approach this?", "Tradeoff analysis".
- **Source**: `.cursor/skills/exercise-guide/SKILL.md`
- **Action**: Analyze `TASK.md` and provide a step-by-step guide and architectural tradeoffs.

### 4. Data
- **Goal**: Find and download datasets.
- **Trigger**: "Find a dataset", "Get data for this".
- **Source**: `.cursor/skills/data/SKILL.md`
- **Action**: Search for and validate real-world datasets suitable for the exercise.

## Common Commands

- `ls -R`: List files to understand structure.
- `cat [folder]/TASK.md`: Read the task requirements.
