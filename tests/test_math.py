from src.test_scenario import TestScenario


@TestScenario.init()
class TestMath:
    @staticmethod
    def test_addition():
        print('Addition')

    def test_substraction(self):
        print('Substraction')

    @staticmethod
    def test_multiplication():
        print('Multiplication')
