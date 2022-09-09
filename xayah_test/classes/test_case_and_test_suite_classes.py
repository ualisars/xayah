from src.xayah.test_suite import TestSuite


@TestSuite.init
class ClassTestCaseAndTestSuiteAssertionEmptyPassed:
    @staticmethod
    def test_empty_assertion_message_passed():
        assert 2 == 2


@TestSuite.init
class ClassTestCaseAndTestSuiteAssertionEmptyFailed:
    @staticmethod
    def test_empty_assertion_message_failed():
        assert 10 == 2


@TestSuite.init
class ClassTestCaseAndTestSuiteAssertion:
    @staticmethod
    def test_assertion_message():
        assert 1 == 20, "this is assertion message"


@TestSuite.init
class ClassTestCaseAndTestSuiteExecutionTimePassed:
    @staticmethod
    def test_assertion_message():
        assert 20 == 20


@TestSuite.init
class ClassTestCaseAndTestSuiteExecutionTimeFailed:
    @staticmethod
    def test_assertion_message():
        assert 1 == 20, "this is assertion message"
