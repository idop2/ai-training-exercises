from typing import Optional, List
from pydantic import BaseModel

class TestCase(BaseModel):
    """
    Represents a single test case for evaluation.
    """
    input: str
    expected_output: Optional[str] = None
    category: Optional[str] = None
    # metric: str = "exact_match"  # Optional: allow overriding metric per test case

class TestResult(BaseModel):
    """
    Represents the result of running a single test case.
    """
    case: TestCase
    actual_output: str
    passed: bool
    score: float = 0.0
    reason: Optional[str] = None
