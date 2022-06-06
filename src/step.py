import inspect
from .forest import Forest


class Step:
    def __init__(self, name):
        self.name = name
        self.method = inspect.stack()[1][3]
        self.assertion_instance = AssertionError('test')

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if type(self.assertion_instance) == exc_type:
            Forest().add_step(name=self.name, method=self.method, status='failed')
        else:
            Forest().add_step(name=self.name, method=self.method, status='passed')
