from src.test_scenario import TestScenario


@TestScenario.init
class ClassTestCaseAndScenarioAssertionEmptyPassed:
    @staticmethod
    def test_empty_assertion_message_passed():
        assert 2 == 2


@TestScenario.init
class ClassTestCaseAndScenarioAssertionEmptyFailed:
    @staticmethod
    def test_empty_assertion_message_failed():
        assert 10 == 2


@TestScenario.init
class ClassTestCaseAndScenarioAssertion:
    @staticmethod
    def test_assertion_message():
        assert 1 == 20, "this is assertion message"
