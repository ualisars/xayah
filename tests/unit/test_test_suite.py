from src.xayah import TestSuite


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

    def test_title(self, test_suite_title_result):
        title = test_suite_title_result.get('title', '')
        assert title == 'Проверка заголовка тест кейса'

    def test_several_before_all(self, several_before_all):
        first_before_all = several_before_all.get('FirstBeforeAll')
        first_before_all_test_case = first_before_all.get('test_cases')[0]
        first_before_all_add_param_name = first_before_all_test_case.get('additional_params').get('name')

        second_before_all = several_before_all.get('SecondBeforeAll')
        second_before_all_test_case = second_before_all.get('test_cases')[0]
        second_before_all_add_param_name = second_before_all_test_case.get('additional_params').get('name')

        assert first_before_all_add_param_name == 'first before all'
        assert second_before_all_add_param_name == 'second before all'
