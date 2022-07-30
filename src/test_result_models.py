from pydantic import BaseModel
from pydantic.types import Optional
from pydantic.typing import Literal, List


class StepModel(BaseModel):
    """
    test case steps
    attributes:
    - name: step's title
    - status: shows whether step passed or failed
    - category: which category step belongs to (step or check)
    - message: reason why this step is failed
    """
    name: str
    status: Literal['passed', 'failed']
    category: Literal['step', 'check']
    message: Optional[str]


class TestClassesModel(BaseModel):
    """
    represents class with all test methods
    stored all classed been run in test
    used to created test result
    attributes:
    - classname: name of the class
    - method_names: names of the class' methods
    """
    classname: str
    method_names: List[str]


class TestCaseModel(BaseModel):
    """
    Represents test case
    attributes:
    - name: name of the test case
    - classname: name of the parent class
    - method: name of the test method
    - steps: testcase steps
    - assertion_message: message shows a reason why test case failed
    - description: additional information about test case
    """
    name: str
    classname: Optional[str]
    method: str
    status: Literal['passed', 'failed'] = 'failed'
    steps: List[StepModel] = []
    assertion_message: str = ''
    title: str = ''
    description: str = ''


class TestScenarioModel(BaseModel):
    """
    represents all test cases been run
    attributes:
    - classname: name of the run class
    - test_cases: methods of the class with test prefix
    """
    classname: str
    test_cases: List[TestCaseModel]
