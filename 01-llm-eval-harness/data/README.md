# Sci-Fi Jeopardy Dataset

This dataset contains a subset of Jeopardy questions related to Science Fiction, Fantasy, and Pop Culture.
It is intended for use in the LLM Evaluation Harness exercise.

## Source
- **Dataset**: `openaccess-ai-collective/jeopardy`
- **URL**: https://huggingface.co/datasets/openaccess-ai-collective/jeopardy
- **License**: Apache 2.0 (matches source)

## Description
The data was filtered from the full Jeopardy dataset using keywords such as:
- SCIENCE FICTION, SCI-FI
- STAR TREK, STAR WARS, DUNE, DOCTOR WHO
- SUPERHERO, MARVEL, DC COMICS

## Format
The data is in JSONL format with the following fields:
- `input`: The Jeopardy "answer" (which acts as the question/prompt for the contestant).
- `output`: The Jeopardy "question" (the correct response).
- `category`: The Jeopardy category (e.g., "CLASSIC STAR TREK").

Note: In Jeopardy, the prompt is technically the "answer" and the contestant provides the "question". 
For this dataset, `input` is the clue provided by the host, and `output` is the correct response.

## Sample
```json
{"category": "CLASSIC STAR TREK", "input": "'From the Old Germanic for \"legs\", it's Dr. McCoy's nickname'", "output": "\"Bones\""}
```

## Usage
Load this dataset to evaluate LLM performance on Sci-Fi trivia.
