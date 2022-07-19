from xayah_test.classes.test_case_classes import ClassTestCasePassed, ClassTestCaseFailed
from src.test_case import TestCase


class TestTestCase:
    def test_test_case_smoke(self, test_result):
        classname = ClassTestCasePassed.__name__
        test_case = TestCase.init(ClassTestCasePassed.test_test_case_passed, classname)
        test_case()
        method_name = 'test_test_case_passed'
        test_case_name = f'{classname}::{method_name}'
        test_case = test_result.get_test_case(test_case_name)

        assert test_case is not None, 'test case is not added to test result'

        assert test_case.get('name') == test_case_name

        assert test_case.get('classname') == classname

        assert test_case.get('method') == method_name

        assert test_case.get('status') == 'passed'

    def test_test_case_failed(self, test_result):
        classname = ClassTestCaseFailed.__name__
        test_case = TestCase.init(ClassTestCaseFailed.test_test_case_failed, classname)
        test_case()
        method_name = 'test_test_case_failed'
        test_case_name = f'{classname}::{method_name}'
        test_case = test_result.get_test_case(test_case_name)

        assert test_case is not None, 'test case is not added to test result'

        assert test_case.get('name') == test_case_name

        assert test_case.get('classname') == classname

        assert test_case.get('method') == method_name

        assert test_case.get('status') == 'failed'
