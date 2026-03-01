from typing import Optional, List
from pydantic import BaseModel, Field, AliasChoices

class TestCase(BaseModel):
    """
    Represents a single test case for evaluation.
    """
    input: str
    expected_output: Optional[str] = Field(
        default=None, 
        validation_alias=AliasChoices('expected_output', 'output')
    )
    category: Optional[str] = None
    metric: str = "contains"  # Changed default to 'contains' for better initial results

class TestResult(BaseModel):
    """
    Represents the result of running a single test case.
    """
    case: TestCase
    actual_output: str
    passed: bool
    score: float = 0.0
    reason: Optional[str] = None
