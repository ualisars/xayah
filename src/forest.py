from .test_result import TestCaseModel, TestScenarioModel, TestResultsModel, StepModel, TestClassesModel


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Forest(metaclass=MetaSingleton):
    def __init__(self):
        self.test_classes = []
        self.test_scenarios = []
        self.test_cases = {}
        self.test_result = []
        self.steps = {}

    def get_test_case(self, name):
        return self.test_cases.get(name)

    def add_test_case(self, **kwargs):
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

    def add_test_scenario(self, **kwargs):
        data = {
            "title": kwargs.get('title', ""),
            "classname": kwargs.get('classname', "")
        }
        test_scenario = TestScenarioModel(**data)
        self.test_scenarios.append(test_scenario.dict())

    def add_test_classes(self, classname, methods):
        data = {
            "classname": classname,
            "method_names": methods
        }
        test_class = TestClassesModel(**data)
        self.test_classes.append(test_class.dict())

    def create_test_result(self):
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

    def add_step(self, name, method, status):
        data = {
            'name': name,
            'status': status
        }
        step = StepModel(**data).dict()
        if not self.steps.get(method):
            steps = [step]
            self.steps[method] = steps
        else:
            self.steps[method].append(step)

    def get_step(self, method):
        return self.steps.get(method)
