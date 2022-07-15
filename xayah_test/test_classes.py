from src import TestScenario
from src.step import Step
from src.check import Check


@TestScenario.init
class TestResultTestPositive:
    def test_math_positive(self):
        assert 5 == 3 + 2


@TestScenario.init
class ClassTestFailed:
    def test_math_failed(self):
        assert 5 == 4, "4 is not 5"


@TestScenario.init
class StepTestSmoke:
    def test_with_steps(self):
        with Step('step one'):
            assert 1 == 1
        with Step('step two'):
            assert 2 == 2


@TestScenario.init
class StepClassFailedStep:
    def test_previous(self):
        with Step('passed step 1'):
            assert 1 == 1
        with Step('failed step'):
            assert 3 == 2
        with Step('passed step 1'):
            assert 2 == 2


@TestScenario.init
class CheckClassSmoke:
    def test_with_checks(self):
        with Check('check 1'):
            assert 1 == 1
        with Check('check 2'):
            assert 2 == 2


@TestScenario.init
class CheckClassPreviousFailed:
    def test_previous_failed(self):
        with Check('check 1 passed'):
            assert 1 == 1
        with Check('check 2 failed'):
            assert 2 == 5
        with Check('check 3 passed'):
            assert 3 == 3
