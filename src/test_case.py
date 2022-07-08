from functools import wraps
from .forest import Forest
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
            try:
                fn(*args, **kwargs)
                Forest().add_test_case(
                    classname=classname,
                    method=fn.__name__,
                    status='passed'
                )
                print(f"{fn.__name__} passed")
            except AssertionError as AssError:
                Forest().add_test_case(
                    classname=classname,
                    method=fn.__name__,
                    status='failed',
                    assertion_message=str(AssError)
                )
                print(f"{fn.__name__} failed with message: {AssError}")

        return wrapper
