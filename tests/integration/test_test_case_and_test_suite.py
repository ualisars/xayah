from pytest import mark
from xayah_test.classes.test_case_and_test_suite_classes import (
    ClassTestCaseAndTestSuiteAssertionEmptyPassed,
    ClassTestCaseAndTestSuiteAssertionEmptyFailed,
    ClassTestCaseAndTestSuiteAssertion,
    ClassTestCaseAndTestSuiteExecutionTimePassed,
    ClassTestCaseAndTestSuiteExecutionTimeFailed
)


class TestTestCaseAndTestTestSuite:
    def test_test_case_title(self, title_result):
        test_suite = title_result[0]
        test_cases = test_suite.get('test_cases')
        test_case = test_cases[0]

        assert test_case.get('title') == 'title1'

    def test_test_case_description_passed(self, description_result_passed):
        test_suite = description_result_passed[0]
        test_cases = test_suite.get('test_cases')
        test_case = test_cases[0]

        assert test_case.get('description') == 'check if description been added to test case when test case passed'

    def test_test_case_description_failed(self, description_result_failed):
        test_suite = description_result_failed[0]
        test_cases = test_suite.get('test_cases')
        test_case = test_cases[0]

        assert test_case.get('description') == 'check if description been added to test case when test case failed'

    def test_test_case_title_and_description(self, title_and_description_result):
        test_suite = title_and_description_result[0]
        test_cases = test_suite.get('test_cases')
        test_case = test_cases[0]

        assert test_case.get('title') == 'test case title and description'
        assert test_case.get('description') == 'check if title and description been added to test case'

    def test_test_case_description_and_title(self, description_and_title_result):
        test_suite = description_and_title_result[0]
        test_cases = test_suite.get('test_cases')
        test_case = test_cases[0]

        assert test_case.get('title') == 'test case description and title not depend on execution order'
        assert test_case.get('description') == 'check title and description when description goes first'

    def test_assertion_message_passed(self, test_result):
        ClassTestCaseAndTestSuiteAssertionEmptyPassed.run_test_cases()
        result = test_result.create_test_result()
        test_suite = result[0]
        test_cases = test_suite.get('test_cases')
        test_case = test_cases[0]

        assert test_case.get('assertion_message') == ''

    def test_assertion_message_failed(self, test_result):
        ClassTestCaseAndTestSuiteAssertionEmptyFailed.run_test_cases()
        result = test_result.create_test_result()
        test_suite = result[0]
        test_cases = test_suite.get('test_cases')
        test_case = test_cases[0]

        assert test_case.get('assertion_message') == ''

    def test_assertion_message(self, test_result):
        ClassTestCaseAndTestSuiteAssertion.run_test_cases()
        result = test_result.create_test_result()
        test_suite = result[0]
        test_cases = test_suite.get('test_cases')
        test_case = test_cases[0]

        assert test_case.get('assertion_message') == 'this is assertion message'

    @mark.parametrize('TestClass', (
        ClassTestCaseAndTestSuiteExecutionTimePassed,
        ClassTestCaseAndTestSuiteExecutionTimeFailed
    ))
    def test_execution_time(self, TestClass, test_result):
        TestClass.run_test_cases()
        result = test_result.create_test_result()
        test_suite = result[0]
        test_cases = test_suite.get('test_cases')
        test_case = test_cases[0]

        start_time = test_case.get('start_time')
        end_time = test_case.get('end_time')
        execution_time = test_case.get('execution_time')

        assert start_time != 0.0, 'start time cannot be 0.0, cause its default value'
        assert end_time != 0.0, 'end time cannot be 0.0, cause its default value'
        assert start_time != end_time, 'start and end time cannot be equal'
        assert execution_time != 0.0, 'execution_time cannot be 0.0, cause its default value'
        assert end_time > start_time
