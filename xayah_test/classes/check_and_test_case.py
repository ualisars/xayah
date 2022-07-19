from src.test_scenario import TestScenario
from src.check import Check


@TestScenario.init
class ClassChecksAndTestCasePassed:
    def test_all_checks_passed(self):
        with Check('passed check 1'):
            assert 1 == 1
        with Check('passed check 2'):
            assert 2 == 2


@TestScenario.init
class ClassCheckAndTestCaseFailed:
    def test_one_check_failed(self):
        with Check('failed check 1'):
            assert 10 == 11


@TestScenario.init
class ClassAtLeastOneCheckAndTestCaseFailed:
    def test_at_least_one_check_failed(self):
        with Check('passed check 1'):
            assert 1 == 1
        with Check('failed check'):
            assert 2 == 4
        with Check('passed check'):
            assert 3 == 3
