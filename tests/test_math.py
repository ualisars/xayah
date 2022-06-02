from src.test_scenario import TestScenario
from src import TestCase


@TestScenario.init()
class TestMath:
    @TestCase.init
    def test_addition(self):
        assert 5 == 2, "good"

    @TestCase.init
    def test_substraction(self):
        assert 3 - 2 == 1

    @TestCase.init
    def test_multiplication(self):
        assert 3 * 2 == 6
