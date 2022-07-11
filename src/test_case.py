from functools import wraps
from .test_result import TestResult
from typing import Callable


class TestCase:
    @classmethod
    def title(cls, title):
        def decorator(fn):
            print('title', title)
            print('fn', fn)

            def wrapper(*args, **kwargs):
                print('args', args)
                print('kwargs', kwargs)
                fn(*args, **kwargs)
                print(f'title: {title}')
            return wrapper
        return decorator

    @staticmethod
    def init(fn: Callable, classname: str = ""):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            method = fn.__name__
            steps = TestResult.get_step(method)
            try:
                fn(*args, **kwargs)
                TestResult().add_test_case(
                    classname=classname,
                    method=method,
                    status='passed',
                    steps=steps
                )
                print(f"{fn.__name__} passed")
            except AssertionError as AssError:
                TestResult().add_test_case(
                    classname=classname,
                    method=method,
                    status='failed',
                    assertion_message=str(AssError),
                    steps=steps
                )
                print(f"{fn.__name__} failed with message: {AssError}")

        return wrapper
