from src.xayah import TestSuite


@TestSuite.init
class ClassResultTestPositive:
    def test_math_positive(self):
        assert 5 == 3 + 2


@TestSuite.init
class ClassTestResultFailed:
    def test_math_failed(self):
        assert 5 == 4, "4 is not 5"
