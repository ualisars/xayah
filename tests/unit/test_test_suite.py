from src import TestSuite


class TestTestSuite:
    @TestSuite.init
    class RunTestCases:
        def __init__(self):
            self.values = []

        def test_append_1(self):
            self.values.append(1)

        def test_append_2(self):
            self.values.append(2)

    @TestSuite.init
    class TestClass:
        default_string = ""

        @TestSuite.before_all
        def set_default_string(self):
            self.default_string = "xayah"

        def test_something(self):
            assert 1 == 1

    def test_init(self):
        run_test_cases = getattr(self.TestClass, 'run_test_cases', 'None')
        assert run_test_cases is not 'None', "attribute run_test_cases not found at class TestClass"

    def test_run_test_cases(self):
        self.RunTestCases.run_test_cases()
        assert 1 == 1
