from .test_result import TestCaseModel, TestResultsModel, StepModel, TestClassesModel
from typing import List


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Forest(metaclass=MetaSingleton):
    """
    storing test documentation: test cases, its steps and so on
    and generating test result based on it
    attributes:
    - test classes: list of all classes that been decorated with TestScenario
    - test cases: all test methods of particular class
    - test result: object of classname and its methods (test cases)
    - steps: steps of a test case
    """
    def __init__(self):
        self.test_classes = []
        self.test_cases = {}
        self.test_result = []
        self.steps = {}

    def get_test_case(self, name: str) -> TestCaseModel:
        return self.test_cases.get(name)

    def add_test_case(self, **kwargs: str) -> None:
        classname = kwargs.get('classname', "")
        method = kwargs.get('method', "")
        test_name = f'{classname}::{method}'
        steps = self.get_step(method)
        data = {
            "name": test_name,
            "classname": classname,
            "method": method,
            "status": kwargs.get('status', ""),
            "steps": steps,
            "assertion_message": kwargs.get('assertion_message', ""),
            "description": kwargs.get('description', "")
        }
        test_case = TestCaseModel(**data)
        self.test_cases[test_name] = test_case.dict()

    def add_test_classes(self, classname: str, methods: List[str]) -> None:
        data = {
            "classname": classname,
            "method_names": methods
        }
        test_class = TestClassesModel(**data)
        self.test_classes.append(test_class.dict())

    def create_test_result(self) -> None:
        for test_class in self.test_classes:
            classname = test_class.get('classname', '')
            methods = []
            for method in test_class['method_names']:
                name = f'{classname}::{method}'
                test_case = self.test_cases.get(name)
                methods.append(test_case)

            data = {
                "classname": classname,
                "test_cases": methods
            }
            test_result = TestResultsModel(**data)
            self.test_result.append(test_result.dict())
            print(self.test_result)

    def add_step(self, name: str, method: str, message: str, status: str) -> None:
        data = {
            'name': name,
            'status': status,
            'message': message
        }
        step = StepModel(**data).dict()
        if not self.steps.get(method):
            steps = [step]
            self.steps[method] = steps
        else:
            self.steps[method].append(step)

    def get_step(self, method: str) -> StepModel:
        return self.steps.get(method)
