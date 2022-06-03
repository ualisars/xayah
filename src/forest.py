from .test_result import TestCaseModel, TestScenarioModel


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Forest(metaclass=MetaSingleton):
    def __init__(self):
        self.test_result = []
        self.test_scenarios = []
        self.test_cases = {}
        self.test_classes = []

    def get_test_case(self, name):
        return self.test_cases.get(name)

    def add_test_case(self, **kwargs):
        classname = kwargs.get('classname', "")
        method = kwargs.get('method', "")
        test_name = f'{classname}::{method}'
        data = {
            "name": test_name,
            "classname": classname,
            "method": method,
            "status": kwargs.get('status', ""),
            "assertion_message": kwargs.get('assertion_message', ""),
            "description": kwargs.get('description', ""),
        }
        test_case = TestCaseModel(**data)
        print(test_case)
        self.test_cases[test_name] = test_case

    def add_test_scenario(self, **kwargs):
        data = {
            "title": kwargs.get('title', ""),
            "classname": kwargs.get('classname', "")
        }
        self.test_scenarios.append(data)

    def add_test_result(self, classname, methods):
        test_result = {
            "classname": classname,
            "test_cases": methods
        }
        self.test_result.append(test_result)
        print(self.test_result)

    def add_test_class(self, test_class):
        self.test_classes.append(test_class)
        print(self.test_classes)


