# SCP Foundation Dataset

## Description
This dataset contains a subset of entries from the SCP Foundation Wiki, a collaborative writing project about a fictional secret organization that documents and contains anomalous entities and phenomena.

The data is intended for use in the RAG Pipeline exercise (`02-rag-pipeline`).

## Source
- **Dataset**: [quguanni/scp-foundation-structured](https://huggingface.co/datasets/quguanni/scp-foundation-structured) on HuggingFace.
- **Original Source**: [SCP Foundation Wiki](https://scp-wiki.wikidot.com/)
- **License**: Creative Commons Attribution-ShareAlike 3.0 (CC BY-SA 3.0).

## Format
The data is stored in `scp_entries.jsonl`. Each line is a JSON object with the following structure:

```json
{
  "id": "SCP-XXX",
  "text": "Full text content of the SCP entry...",
  "metadata": {
    "source": "SCP Foundation",
    "title": "SCP-XXX",
    "object_class": "Euclid",
    "length": 1234
  }
}
```

## Generation
The dataset was generated using the `download_data.py` script in this directory, which downloads a stream of entries from HuggingFace and formats them.

## Date Accessed
March 1, 2026
