from functools import wraps
from .test_result import TestResult
from .forest import Forest


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
    def init(fn, classname=""):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            try:
                fn(*args, **kwargs)
                Forest().add_test_case(
                    classname=classname,
                    method=fn.__name__,
                    status='passed'
                )
                print(f"{fn.__name__} success")
            except AssertionError as AssError:
                Forest.add_test_case(
                    classname=classname,
                    method=fn.__name__,
                    status='failed',
                    assertion_message=str(AssError)
                )
                print(f"{fn.__name__} failed with message: {AssError}")

        return wrapper

    @staticmethod
    def write_to_json(**kwargs):
        name = kwargs.get('classname', "") + kwargs.get('method', ""),
        data = {
            "name": name,
            "classname": kwargs.get('classname', ""),
            "method": kwargs.get('method', ""),
            "status":  kwargs.get('status', ""),
            "assertion_message":  kwargs.get('assertion_message', ""),
            "description":  kwargs.get('description', ""),
        }
        test_result = TestResult(**data)
        print(test_result)
