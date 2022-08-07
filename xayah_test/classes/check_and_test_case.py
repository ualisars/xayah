from src.test_suite import TestSuite
from src.check import Check


@TestSuite.init
class ClassChecksAndTestCasePassed:
    def test_all_checks_passed(self):
        with Check('passed check 1'):
            assert 1 == 1
        with Check('passed check 2'):
            assert 2 == 2


@TestSuite.init
class ClassCheckAndTestCaseFailed:
    def test_one_check_failed(self):
        with Check('failed check 1'):
            assert 10 == 11


@TestSuite.init
class ClassAtLeastOneCheckAndTestCaseFailed:
    def test_at_least_one_check_failed(self):
        with Check('passed check 1'):
            assert 1 == 1
        with Check('failed check'):
            assert 2 == 4
        with Check('passed check'):
            assert 3 == 3


@TestSuite.init
class ClassCheckAndTestCaseExecutionTime:
    def test_execution_time(self):
        with Check('passed check 1'):
            assert 1 == 1


@TestSuite.init
class ClassCheckAndTestCaseExecutionTime2Checks:
    def test_execution_time(self):
        with Check('failed check 1'):
            assert 1 == 4
        with Check('failed check 2'):
            assert 10 == 2
