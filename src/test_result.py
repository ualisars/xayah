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


class StepModel(BaseModel):
    name: str
    status: Literal['passed', 'failed']
    message: Optional[str]


class TestClassesModel(BaseModel):
    classname: str
    method_names: List[str]


class TestCaseModel(BaseModel):
    name: str
    classname: Optional[str]
    method: str
    status: Literal['passed', 'failed']
    steps: List[StepModel]
    assertion_message: str
    description: str


class TestResultsModel(BaseModel):
    classname: str
    test_cases: List[TestCaseModel]
