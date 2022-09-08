from src import TestSuite
from src.xayah.check import Check


@TestSuite.init
class ClassCheckPassed:
    def test_with_checks(self):
        with Check('check 1'):
            assert 1 == 1
        with Check('check 2'):
            assert 2 == 2


@TestSuite.init
class ClassCheckFailed:
    def test_previous_failed(self):
        with Check('check 1 passed'):
            assert 1 == 1
        with Check('check 2 failed'):
            assert 2 == 5
        with Check('check 3 passed'):
            assert 3 == 3
