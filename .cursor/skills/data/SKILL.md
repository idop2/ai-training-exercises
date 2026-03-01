---
name: data
description: Search for, validate, and download interesting, real-world datasets for AI exercises. Use when the user needs data for an exercise, asks for a dataset, or needs to populate an assignment with real-world examples.
---

# Data Acquisition

## Process

1.  **Analyze Requirements**:
    -   Identify the exercise folder (e.g., `01-llm-eval-harness`, `02-rag-pipeline`).
    -   Determine the data type (Text, Tabular, Vision) and format (JSONL, Parquet, CSV).
    -   **Crucial**: Select "interesting" data. Avoid generic datasets (e.g., iris, titanic) unless specifically requested. Look for:
        -   Pop culture (movies, scripts, lyrics).
        -   Sci-fi / Fantasy lore.
        -   Real-world bizarre events (UFO sightings, ghost stories).
        -   Scientific data (NASA, CERN, Biology).
        -   Historical documents (letters, speeches).

    -   **Refinement**: Don't just dump a massive dataset. Filter for specific, high-quality subsets (e.g., "Sci-Fi" category from a trivia dataset, "Startup" advice from a forum dump).

2.  **Search Strategy**:
    -   Use `WebSearch` to find open datasets.
    -   Keywords: "huggingface datasets [topic]", "kaggle [topic] dataset json", "github [topic] dataset raw".
    -   Prioritize direct download links or Python-accessible libraries (`datasets`, `pandas`).

3.  **Implementation**:
    -   Create a directory `data/` in the target exercise folder if it doesn't exist.
    -   Write a Python script (`download_data.py`) to:
        -   Fetch the data using `requests` or `datasets`.
        -   Validate the schema/content (check for empty fields, nulls).
        -   **Filter/Subset**: Select only relevant or interesting records (e.g., specific category, high quality score).
        -   **Normalize**: Rename columns to `input` (prompt/question) and `output` (response/answer) for LLM tasks.
        -   Save it to `data/` with a descriptive filename (e.g., `sci_fi_jeopardy.jsonl`).
        -   Print a sample (first 5 rows) to verify "interestingness".
    -   Run the script and verify the output.
    -   **Cleanup**: Delete the download script (`download_data.py`) and any other temporary files. Ensure only the dataset and `README.md` remain.
    -   Create a `data/README.md` with:
        -   Source URL.
        -   License info.
        -   Description of the data.
        -   Date accessed.

## Guidelines

-   **Attribution**: Always cite the source and license.
-   **Size**: Check file sizes before downloading. Prefer <100MB for exercises unless specified.
-   **Privacy**: Do not download PII (Personally Identifiable Information).
-   **Format**: Prefer JSONL for text/LLM tasks (`input`/`output` keys), Parquet for tabular/large data.
-   **Cleanup**: Delete the download script and any temporary files. Keep only the final dataset and README.

## Example Sources

-   **HuggingFace**: `load_dataset("org/dataset")`
-   **NASA API**: `requests.get("api.nasa.gov/...")`
-   **Project Gutenberg**: Public domain books.
-   **Wikipedia**: Dumps or API.
