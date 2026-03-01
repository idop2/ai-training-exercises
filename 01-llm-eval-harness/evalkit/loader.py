import json
from typing import List
from pathlib import Path
from .models import TestCase

def load_test_cases(file_path: str) -> List[TestCase]:
    """
    Loads test cases from a JSON or JSONL file.
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    test_cases = []
    
    with open(path, "r", encoding="utf-8") as f:
        # Check if it's a JSON list or JSONL
        content = f.read().strip()
        
        try:
            # Try parsing as a JSON list first
            data = json.loads(content)
            if isinstance(data, list):
                for item in data:
                    test_cases.append(TestCase(**item))
            else:
                # Maybe it's a single object?
                test_cases.append(TestCase(**data))
        except json.JSONDecodeError:
            # If that fails, try parsing line by line (JSONL)
            lines = content.split('\n')
            for line in lines:
                if line.strip():
                    item = json.loads(line)
                    test_cases.append(TestCase(**item))
                    
    return test_cases
