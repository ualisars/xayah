class TestTestCaseAndTestScenario:
    def test_test_case_title(self, title_result):
        test_scenario = title_result[0]
        test_cases = test_scenario.get('test_cases')
        test_case = test_cases[0]

        assert test_case.get('title') == 'title1'
