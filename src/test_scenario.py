import inspect
from .test_case import TestCase


class TestScenario:
    @classmethod
    def init(cls):
        def add_method(test_class):
            def run_test_cases():
                if not inspect.isclass(test_class):
                    print('Not a class')
                f = test_class()
                attrs = (getattr(f, name) for name in dir(f))
                methods = [fn for fn in attrs if inspect.isfunction(fn) or inspect.ismethod(fn)]

                for method in methods:
                    if not method.__name__.lower().startswith('test'):
                        continue
                    try:
                        classname = test_class.__name__
                        test_case = TestCase.init(method, classname)
                        test_case()
                    except TypeError:
                        # Can't handle methods with required arguments.
                        pass

            setattr(test_class, 'run_test_cases', run_test_cases)
            return test_class

        return add_method
