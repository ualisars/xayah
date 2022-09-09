from src.xayah import TestSuite
from src.xayah.step import Step


@TestSuite.init
class ClassStepPassed:
    def test_with_steps(self):
        with Step('step one'):
            assert 1 == 1
        with Step('step two'):
            assert 2 == 2


@TestSuite.init
class ClassStepFailed:
    def test_previous(self):
        with Step('passed step 1'):
            assert 1 == 1
        with Step('failed step'):
            assert 3 == 2
        with Step('passed step 1'):
            assert 2 == 2
