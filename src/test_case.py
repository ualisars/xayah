from functools import wraps
from .test_result import TestResult
from typing import Callable, List, Dict
from .test_result import StepModel
import inspect


class TestCase:
    """
    stores class method information
    such as classname, method' name, status
    and also stores meta information: title, description and so on
    """
    @staticmethod
    def title(title: str) -> Callable:
        """
        Add title to test case
        :param title: test case title
        """
        def add_title_to_test_case(fn: Callable):
            method_name = fn.__name__
            class_name = inspect.stack()[1][3]

            TestResult().add_test_case(title=title, method=method_name, classname=class_name)
            return fn
        return add_title_to_test_case

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
    def init(fn: Callable, classname: str = ""):
        """
        intercepts asserts in method and write
        information to test result
        :param fn: method to be decorated
        :param classname: name of the parent class
        """
        @wraps(fn)
        def wrapper(*args, **kwargs):
            method = fn.__name__
            try:
                fn(*args, **kwargs)
                steps = TestResult().get_steps(method)
                status = TestCase.check_status(steps)
                TestResult().add_test_case(
                    classname=classname,
                    method=method,
                    status=status,
                    steps=steps
                )
                print(f"test_case: {fn.__name__} passed")
            except AssertionError as AssError:
                assertion = str(AssError).split('\n')
                assertion_message = assertion[0]
                steps = TestResult().get_steps(method)
                TestResult().add_test_case(
                    classname=classname,
                    method=method,
                    status='failed',
                    assertion_message=assertion_message,
                    steps=steps
                )
                print(f"{fn.__name__} failed with message: {AssError}")

        return wrapper
