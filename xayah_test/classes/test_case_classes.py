class ClassTestCasePassed:
    @staticmethod
    def test_test_case_passed():
        assert 1 == 1


class ClassTestCaseFailed:
    @staticmethod
    def test_test_case_failed():
        assert 1 == 2
