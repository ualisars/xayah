from src.xayah.test_suite import TestSuite
from src.xayah.step import Step


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


@TestSuite.init
class ClassStepAndTestCaseExecutionTime1Step:
    def test_execution_time(self):
        with Step('passed step'):
            assert 1 == 1


@TestSuite.init
class ClassStepAndTestCaseExecutionTime2Steps:
    def test_execution_time(self):
        with Step('step 1'):
            assert 1 == 1
        with Step('step 2'):
            assert 3 == 2
