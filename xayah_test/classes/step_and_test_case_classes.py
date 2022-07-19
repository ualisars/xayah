from src.test_scenario import TestScenario
from src.step import Step


@TestScenario.init
class ClassStepAndTestCasePassed:
    def test_all_steps_passed(self):
        with Step('passed step 1'):
            assert 1 == 1
        with Step('passed step 2'):
            assert 2 == 2


@TestScenario.init
class ClassStepAndTestCaseFailed:
    def test_all_steps_passed(self):
        with Step('passed step 1'):
            assert 1 == 1
        with Step('failed step 2'):
            assert 2 == 200
