from src import TestScenario
from src.check import Check


@TestScenario.init
class ClassCheckPassed:
    def test_with_checks(self):
        with Check('check 1'):
            assert 1 == 1
        with Check('check 2'):
            assert 2 == 2


@TestScenario.init
class ClassCheckFailed:
    def test_previous_failed(self):
        with Check('check 1 passed'):
            assert 1 == 1
        with Check('check 2 failed'):
            assert 2 == 5
        with Check('check 3 passed'):
            assert 3 == 3
