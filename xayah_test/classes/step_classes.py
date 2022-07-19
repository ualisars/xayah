from src import TestScenario
from src.step import Step


@TestScenario.init
class ClassStepPassed:
    def test_with_steps(self):
        with Step('step one'):
            assert 1 == 1
        with Step('step two'):
            assert 2 == 2


@TestScenario.init
class ClassStepFailed:
    def test_previous(self):
        with Step('passed step 1'):
            assert 1 == 1
        with Step('failed step'):
            assert 3 == 2
        with Step('passed step 1'):
            assert 2 == 2
