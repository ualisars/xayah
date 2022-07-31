from xayah_test.classes.test_case_and_scenario_classes import (
    ClassTestCaseAndScenarioAssertionEmptyPassed,
    ClassTestCaseAndScenarioAssertionEmptyFailed,
    ClassTestCaseAndScenarioAssertion
)


class TestTestCaseAndTestScenario:
    def test_test_case_title(self, title_result):
        test_scenario = title_result[0]
        test_cases = test_scenario.get('test_cases')
        test_case = test_cases[0]

        assert test_case.get('title') == 'title1'

    def test_test_case_description_passed(self, description_result_passed):
        test_scenario = description_result_passed[0]
        test_cases = test_scenario.get('test_cases')
        test_case = test_cases[0]

        assert test_case.get('description') == 'check if description been added to test case when test case passed'

    def test_test_case_description_failed(self, description_result_failed):
        test_scenario = description_result_failed[0]
        test_cases = test_scenario.get('test_cases')
        test_case = test_cases[0]

        assert test_case.get('description') == 'check if description been added to test case when test case failed'

    def test_test_case_title_and_description(self, title_and_description_result):
        test_scenario = title_and_description_result[0]
        test_cases = test_scenario.get('test_cases')
        test_case = test_cases[0]

        assert test_case.get('title') == 'test case title and description'
        assert test_case.get('description') == 'check if title and description been added to test case'

    def test_test_case_description_and_title(self, description_and_title_result):
        test_scenario = description_and_title_result[0]
        test_cases = test_scenario.get('test_cases')
        test_case = test_cases[0]

        assert test_case.get('title') == 'test case description and title not depend on execution order'
        assert test_case.get('description') == 'check title and description when description goes first'

    def test_assertion_message_passed(self, test_result):
        ClassTestCaseAndScenarioAssertionEmptyPassed.run_test_cases()
        result = test_result.create_test_result()
        test_scenario = result[0]
        test_cases = test_scenario.get('test_cases')
        test_case = test_cases[0]

        assert test_case.get('assertion_message') == ''

    def test_assertion_message_failed(self, test_result):
        ClassTestCaseAndScenarioAssertionEmptyFailed.run_test_cases()
        result = test_result.create_test_result()
        test_scenario = result[0]
        test_cases = test_scenario.get('test_cases')
        test_case = test_cases[0]

        assert test_case.get('assertion_message') == ''

    def test_assertion_message(self, test_result):
        ClassTestCaseAndScenarioAssertion.run_test_cases()
        result = test_result.create_test_result()
        test_scenario = result[0]
        test_cases = test_scenario.get('test_cases')
        test_case = test_cases[0]

        assert test_case.get('assertion_message') == 'this is assertion message'
