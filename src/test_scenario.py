import inspect
from .test_case import TestCase
from .forest import Forest
from typing import Callable, Dict, List


class TestScenario:
    before_all_method = 'xayah_before_all'
    after_all_method = 'xayah_after_all'

    @staticmethod
    def init(test_class: type) -> Callable:
        """
        attach run_test_cases method to decorated class
        :param test_class: class to be decorated
        """
        def add_method() -> type:
            def run_test_cases(*args: Dict[str, str]) -> None:
                """
                run all test methods inside test class
                :param args: variables that will be accessed in test class
                e.g {'driver': Driver()}
                """
                if not inspect.isclass(test_class):
                    print('Not a class')
                f = test_class()
                attrs = (getattr(f, name) for name in dir(f))
                methods = [fn for fn in attrs if inspect.isfunction(fn) or inspect.ismethod(fn)]
                teardown_methods = TestScenario.get_teardown_methods(methods)
                if not args:
                    args = ({},)
                for param in args:
                    classname = test_class.__name__ + param.get('name', '')
                    setattr(test_class, 'test_param', param)
                    before_all = teardown_methods.get(TestScenario.before_all_method)
                    if before_all:
                        before_all()
                    method_names = TestScenario.run_methods(classname, methods)

                    after_all = teardown_methods.get(TestScenario.after_all_method)
                    if after_all:
                        after_all()

                    # store test class and all its methods to create test result
                    Forest().add_test_classes(classname, method_names)

            setattr(test_class, 'run_test_cases', run_test_cases)
            return test_class

        return add_method()

    @staticmethod
    def before_all(fn: Callable) -> Callable:
        """
        change the name of decorated method,
        so it can be called before test methods
        :param fn: method to be decorated
        """
        def decorator():
            fn.__name__ = TestScenario.before_all_method
            return fn
        return decorator()

    @staticmethod
    def after_all(fn: Callable) -> Callable:
        """
        change the name of decorated method,
        so it can be called after test methods
        :param fn: method to be decorated
        """
        def decorator():
            fn.__name__ = TestScenario.after_all_method
            return fn
        return decorator()

    @staticmethod
    def get_teardown_methods(methods: List[Callable]) -> Dict[str, Callable]:
        """
        generated the dict consisted of before_all and after_all methods
        from all methods
        :param methods: list of all methods in the class
        :return: dict consisted of before_all and after_all methods
        """
        teardown_methods = {}
        for method in methods:
            method_name = method.__name__
            if method_name == TestScenario.before_all_method or method_name == TestScenario.after_all_method:
                teardown_methods[method_name] = method
        return teardown_methods

    @staticmethod
    def run_methods(classname: str, methods: List[Callable]) -> List[str]:
        """
        run all methods in the class that have test prefix, e.g. test_login
        :param classname: name of the class
        :param methods: all methods in the class
        """
        method_names = []
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
        return method_names
