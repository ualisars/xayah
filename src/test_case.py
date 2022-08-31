from functools import wraps
from .test_result import TestResult
from .severity_level import SeverityLevel
from typing import Callable, List, Dict
from .test_result import StepModel
import time
import inspect
from io import StringIO
import sys


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
    def severity(severity: SeverityLevel or str) -> Callable:
        """
        add severity level to the test case
        :param severity: Enum of SeverityLevel
        """
        if not isinstance(severity, SeverityLevel):
            raise ValueError('severity is not a type of SeverityLevel')
        return TestCase.__add_test_case_field('severity_level', severity.value)

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
        """
        generate object with assertion_message and assertion itself
        :param assertions: list of string consists of assertion error substrings
        :return: object {'assertion_message: string, assertion: string}
        """
        assertion_obj = {
            'assertion': '',
            'assertion_message': ''
        }
        assertions_length = len(assertions)
        if assertions_length == 1 and 'assert' in assertions[0]:
            assertion_obj.update({'assertion': assertions[0]})
        elif assertions_length == 1:
            assertion_obj.update({'assertion_message': assertions[0]})
        elif assertions_length == 2:
            assertion_obj.update({
                'assertion_message': assertions[0],
                'assertion': assertions[1]
            })
        elif assertions_length == 3:
            assertion_obj.update({'assertion': assertions[0]})
        elif assertions_length == 4:
            assertion_obj.update({
                'assertion_message': assertions[0],
                'assertion': assertions[1]
            })
        return assertion_obj

    @staticmethod
    def get_stderr_as_string(
        tmp_stdout: sys.stdout,
        tmp_stderr: sys.stderr,
        stdout_result: StringIO,
        stderr_result: StringIO
    ) -> str:
        """
        :param tmp_stdout: link to stdout
        :param tmp_stderr: link to stderr
        :param stdout_result: io.StringIO object that replaced stdout
        :param stderr_result: io.StringIO object that replaced stderr
        :return: logs in string
        """
        # redirect output to sys.stdout
        sys.stdout = tmp_stdout
        # get standard output as a string
        stdout_str = stdout_result.getvalue()

        # redirect output to sys.stdout
        sys.stderr = tmp_stderr
        # get standard output as a string
        stderr_str = stderr_result.getvalue()
        return stdout_str + stderr_str

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
            start_time = 0.0
            # save the link to display it in console later
            tmp_stdout = sys.stdout

            # save the link to stderr
            tmp_stderr = sys.stderr

            # in result will be stored everything
            # that written to standard output
            stdout_result = StringIO()
            sys.stdout = stdout_result

            # in stderr_result will be stored everything
            # that written to sys.stderr
            stderr_result = StringIO()
            sys.stderr = stderr_result
            try:
                # execute function and measure execution time
                start_time = time.time()
                fn(*args, **kwargs)
                logs = TestCase.get_stderr_as_string(tmp_stdout, tmp_stderr, stdout_result, stderr_result)
                end_time = time.time()
                execution_time = (end_time - start_time) * 1000

                steps = TestResult().get_steps(method_name)
                status = TestCase.check_status(steps)
                TestResult().add_test_case(
                    class_name=class_name,
                    method_name=method_name,
                    status=status,
                    steps=steps,
                    start_time=start_time,
                    end_time=end_time,
                    execution_time=execution_time,
                    logs=logs
                )
                print(f"test_case: {fn.__name__} passed")
            except AssertionError as AssError:
                logs = TestCase.get_stderr_as_string(tmp_stdout, tmp_stderr, stdout_result, stderr_result)
                end_time = time.time()
                execution_time = (end_time - start_time) * 1000
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
                    assertion=assertion,
                    steps=steps,
                    start_time=start_time,
                    end_time=end_time,
                    execution_time=execution_time,
                    logs=logs
                )
                print(f"{fn.__name__} failed with message: {AssError}")

        return wrapper
