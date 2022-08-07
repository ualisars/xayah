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
    - start_time: start of the step in seconds since the Epoch
    - end_time: end of the step in seconds since the Epoch
    - execution_time: time required to execute step in milliseconds
    """
    name: str
    status: Literal['passed', 'failed']
    category: Literal['step', 'check']
    message: Optional[str]
    start_time: float = 0.0
    end_time: float = 0.0
    execution_time: float = 0.0


class TestClassesModel(BaseModel):
    """
    represents class with all test methods
    stored all classed been run in test
    used to created test result
    attributes:
    - class_name: name of the class
    - method_names: names of the class' methods
    """
    class_name: str
    method_names: List[str]


class TestCaseModel(BaseModel):
    """
    Represents test case
    attributes:
    - name: name of the test case
    - class_name: name of the parent class
    - method_name: name of the test method
    - steps: testcase steps
    - assertion_message: message shows a reason why test case failed
    - assertion: assertion itself e.g. assert name == 'Jon Snow'
    - title: test case title
    - description: additional information about test case
    - start_time: start of the test case in seconds since the Epoch
    - end_time: end of the test case in seconds since the Epoch
    - execution_time: time required to execute test case in milliseconds
    """
    name: str
    class_name: Optional[str]
    method_name: str
    status: Literal['passed', 'failed'] = 'failed'
    steps: List[StepModel] = []
    assertion_message: str = ''
    assertion: str = ''
    title: str = ''
    description: str = ''
    start_time: float = 0.0
    end_time: float = 0.0
    execution_time: float = 0.0


class TestSuiteModel(BaseModel):
    """
    represents all test cases been run
    attributes:
    - class_name: name of the run class
    - test_cases: methods of the class with test prefix
    """
    class_name: str
    test_cases: List[TestCaseModel]
