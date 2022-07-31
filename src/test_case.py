from functools import wraps
from .test_result import TestResult
from typing import Callable, List, Dict
from .test_result import StepModel
import inspect


class TestCase:
    """
    stores class method information
    such as class_name, method_name, status
    and also stores meta information: title, description and so on
    """

    @staticmethod
    def __add_test_case_field(name: str, value: str):
        """
        add field to test case
        :param name: field that will be added to test case, e.g title
        :param value: value of the field
        """
        def add_field(fn: Callable):
            method_name = fn.__name__
            class_name = inspect.stack()[1][3]
            field = {name: value}

            TestResult().add_test_case(method_name=method_name, class_name=class_name, **field)
            return fn
        return add_field

    @staticmethod
    def title(title: str) -> Callable:
        """
        Add title to test case
        :param title: test case title
        """
        return TestCase.__add_test_case_field('title', title)

    @staticmethod
    def description(description: str) -> Callable:
        """
        add description to test case
        :param description: test case description
        """
        return TestCase.__add_test_case_field('description', description)

    @staticmethod
    def check_status(steps: List[StepModel] or List[Dict]) -> str:
        """
        loop through all steps and if t least one step is failed so
        test case if failed too. It's made because check is not marked
        test case failed automatically
        :param steps: list of steps List[StepModel]
        :return: test case status: passed or failed
        """
        for step in steps:
            if step.get('status') == 'failed':
                return 'failed'
        return 'passed'

    @staticmethod
    def _get_assertions(assertions: List[str]) -> Dict[str, str]:
        assertion_obj = {
            'assertion': '',
            'assertion_message': ''
        }
        assertions_length = len(assertions)
        if assertions_length == 2:
            assertion_obj.update({'assertion_message': assertions[0]})
        elif assertions_length == 3:
            assertion_obj.update({
                'assertion_message': assertions[0],
                'assertion': assertions[1]
            })
        return assertion_obj

    @staticmethod
    def init(fn: Callable, class_name: str = ""):
        """
        intercepts asserts in method and write
        information to test result
        :param fn: method to be decorated
        :param class_name: name of the parent class
        """
        @wraps(fn)
        def wrapper(*args, **kwargs):
            method_name = fn.__name__
            try:
                fn(*args, **kwargs)
                steps = TestResult().get_steps(method_name)
                status = TestCase.check_status(steps)
                TestResult().add_test_case(
                    class_name=class_name,
                    method_name=method_name,
                    status=status,
                    steps=steps
                )
                print(f"test_case: {fn.__name__} passed")
            except AssertionError as AssError:
                assertions = str(AssError).split('\n')
                assertion_msg = TestCase._get_assertions(assertions)
                assertion_message = assertion_msg.get('assertion_message', '')
                assertion = assertion_msg.get('assertion', '')
                steps = TestResult().get_steps(method_name)
                TestResult().add_test_case(
                    class_name=class_name,
                    method_name=method_name,
                    status='failed',
                    assertion_message=assertion_message,
                    steps=steps
                )
                print(f"{fn.__name__} failed with message: {AssError}")

        return wrapper
