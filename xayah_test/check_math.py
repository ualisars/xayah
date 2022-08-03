from src.test_suite import TestSuite


@TestSuite.init
class CheckMath:
    def test_addition(self):
        assert 5 == 2, "good"

    def test_substraction(self):
        assert 3 - 2 == 1

    def test_multiplication(self):
        assert 3 * 2 == 6
