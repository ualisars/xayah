import inspect
from .test_case import TestCase
from .forest import Forest


class TestScenario:
    before_all_method = 'xayah_before_all'
    after_all_method = 'xayah_after_all'

    @staticmethod
    def init(test_class):
        def add_method():
            classname = test_class.__name__

            def run_test_cases():
                if not inspect.isclass(test_class):
                    print('Not a class')
                f = test_class()
                attrs = (getattr(f, name) for name in dir(f))
                methods = [fn for fn in attrs if inspect.isfunction(fn) or inspect.ismethod(fn)]

                method_names = []
                teardown_methods = TestScenario.get_teardown_methods(methods)

                before_all = teardown_methods.get(TestScenario.before_all_method)
                if before_all:
                    before_all()
                for method in methods:
                    method_name = method.__name__
                    if not method_name.lower().startswith('test'):
                        continue
                    try:
                        method_names.append(method.__name__)
                        test_case = TestCase.init(method, classname)
                        test_case()
                    except TypeError:
                        # Can't handle methods with required arguments.
                        pass

                after_all = teardown_methods.get(TestScenario.after_all_method)
                if after_all:
                    after_all()

                Forest().add_test_classes(classname, method_names)

            setattr(test_class, 'run_test_cases', run_test_cases)
            return test_class

        return add_method()

    @staticmethod
    def before_all(fn):
        def decorator():
            fn.__name__ = TestScenario.before_all_method
            return fn
        return decorator()

    @staticmethod
    def after_all(fn):
        def decorator():
            fn.__name__ = TestScenario.after_all_method
            return fn
        return decorator()

    @staticmethod
    def get_teardown_methods(methods):
        teardown_methods = {}
        for method in methods:
            method_name = method.__name__
            if method_name == TestScenario.before_all_method or method_name == TestScenario.after_all_method:
                teardown_methods[method_name] = method
        return teardown_methods

