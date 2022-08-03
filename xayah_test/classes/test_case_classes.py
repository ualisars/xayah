class ClassTestCasePassed:
    @staticmethod
    def test_test_case_passed():
        assert 1 == 1


class ClassTestCaseFailed:
    @staticmethod
    def test_test_case_failed():
        assert 1 == 2


class ClassTestCaseAssertionMessageEmpty:
    @staticmethod
    def test_test_case_assertion_message_empty():
        assert 10 == 2


class ClassTestCaseAssertionMessage:
    @staticmethod
    def test_test_case_assertion_message():
        assert 30 == 1, '30 is not 1'
