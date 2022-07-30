import inspect
from .test_result import TestResult


class Check:
    def __init__(self, name):
        self.name = name
        self.method = inspect.stack()[1][3]
        self.assertion_instance = AssertionError('test')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        message = ''
        if exc_val:
            message = str(exc_val)
        if type(self.assertion_instance) == exc_type:
            TestResult().add_step(name=self.name, method=self.method, message=message, category='check', status='failed')
        else:
            TestResult().add_step(name=self.name, method=self.method, message=message, category='check', status='passed')
        return True
