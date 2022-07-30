from .test_result_models import TestCaseModel, TestScenarioModel, StepModel, TestClassesModel
from typing import List


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class TestResult(metaclass=MetaSingleton):
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
        self.test_scenarios = []
        self.steps = {}

    def __repr__(self):
        return f'''
            test_classes: {self.test_classes}\n 
            test_cases: {self.test_cases}\n 
            test_scenarios: {self.test_scenarios}\n 
            steps: {self.steps}
        '''

    def get_test_case(self, name: str) -> TestCaseModel:
        """
        get test case by its name (classname:method)
        :param name: test case name ({classname}::{method})
        :return: TestCaseModel
        """
        return self.test_cases.get(name)

    def add_test_case(self, **kwargs: str or StepModel) -> None:
        classname = kwargs.get('classname', "")
        method = kwargs.get('method', "")
        test_case_name = f'{classname}::{method}'

        test_case = self.test_cases.get(test_case_name)

        kwargs.update({'name': test_case_name})

        if test_case:
            test_case.update(**kwargs)
        else:
            test_case = TestCaseModel(**kwargs)
            self.test_cases[test_case_name] = test_case.dict()

    def add_test_case_old(self, **kwargs: str or StepModel) -> None:
        classname = kwargs.get('classname', "")
        method = kwargs.get('method', "")
        test_name = f'{classname}::{method}'
        steps = kwargs.get('steps')
        if steps is None:
            steps = []
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

    def create_test_result(self) -> List[TestScenarioModel]:
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
            test_scenario = TestScenarioModel(**data)
            self.test_scenarios.append(test_scenario.dict())
            return self.test_scenarios

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

    def get_steps(self, method: str) -> List[StepModel]:
        return self.steps.get(method, [])

    def clear_test_result(self) -> None:
        self.test_classes = []
        self.test_cases = {}
        self.test_scenarios = []
        self.steps = {}
