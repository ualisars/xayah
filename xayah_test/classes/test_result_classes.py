from src import TestScenario


@TestScenario.init
class ClassResultTestPositive:
    def test_math_positive(self):
        assert 5 == 3 + 2


@TestScenario.init
class ClassTestResultFailed:
    def test_math_failed(self):
        assert 5 == 4, "4 is not 5"
