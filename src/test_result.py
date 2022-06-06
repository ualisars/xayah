from pydantic import BaseModel
from pydantic.types import Optional
from pydantic.typing import Literal, List


class TestResult(BaseModel):
    name: str
    class_name: Optional[str]
    method: str
    status: Literal['passed', 'failed']
    assertion_message: str
    description: str


class TestScenarioModel(BaseModel):
    title: str
    classname: str


class Step(BaseModel):
    name: str
    status: Literal['passed', 'failed']
    method: str


class TestCaseModel(BaseModel):
    name: str
    classname: Optional[str]
    method: str
    status: Literal['passed', 'failed']
    steps: List[Step]
    assertion_message: str
    description: str


class TestResultsModel(BaseModel):
    test_scenario: TestScenarioModel
    test_cases: List[TestCaseModel]
