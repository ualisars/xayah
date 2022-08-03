from src.test_suite import TestSuite
from src.step import Step


@TestSuite.init
class ClassStepAndTestCasePassed:
    def test_all_steps_passed(self):
        with Step('passed step 1'):
            assert 1 == 1
        with Step('passed step 2'):
            assert 2 == 2


@TestSuite.init
class ClassStepAndTestCaseFailed:
    def test_all_steps_passed(self):
        with Step('passed step 1'):
            assert 1 == 1
        with Step('failed step 2'):
            assert 2 == 200
