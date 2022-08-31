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
        test_cases = title_result.get('test_cases')
        test_case = test_cases[0]

        assert test_case.get('title') == 'title1'

    def test_test_case_description_passed(self, description_result_passed):
        test_cases = description_result_passed.get('test_cases')
        test_case = test_cases[0]

        assert test_case.get('description') == 'check if description been added to test case when test case passed'

    def test_test_case_description_failed(self, description_result_failed):
        test_cases = description_result_failed.get('test_cases')
        test_case = test_cases[0]

        assert test_case.get('description') == 'check if description been added to test case when test case failed'

    def test_test_case_title_and_description(self, title_and_description_result):
        test_cases = title_and_description_result.get('test_cases')
        test_case = test_cases[0]

        assert test_case.get('title') == 'test case title and description'
        assert test_case.get('description') == 'check if title and description been added to test case'

    def test_test_case_description_and_title(self, description_and_title_result):
        test_cases = description_and_title_result.get('test_cases')
        test_case = test_cases[0]

        assert test_case.get('title') == 'test case description and title not depend on execution order'
        assert test_case.get('description') == 'check title and description when description goes first'

    def test_assertion_message_passed(self, test_result):
        ClassTestCaseAndTestSuiteAssertionEmptyPassed.run_test_cases()
        result = test_result.create_test_result()
        test_suite = result.get(ClassTestCaseAndTestSuiteAssertionEmptyPassed.__name__)
        test_cases = test_suite.get('test_cases')
        test_case = test_cases[0]

        assert test_case.get('assertion_message') == ''

    def test_assertion_message_failed(self, test_result):
        ClassTestCaseAndTestSuiteAssertionEmptyFailed.run_test_cases()
        result = test_result.create_test_result()
        test_suite = result.get(ClassTestCaseAndTestSuiteAssertionEmptyFailed.__name__)
        test_cases = test_suite.get('test_cases')
        test_case = test_cases[0]

        assert test_case.get('assertion_message') == ''

    def test_assertion_message(self, test_result):
        ClassTestCaseAndTestSuiteAssertion.run_test_cases()
        result = test_result.create_test_result()
        test_suite = result.get(ClassTestCaseAndTestSuiteAssertion.__name__)
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
        test_suite = result.get(TestClass.__name__)
        test_cases = test_suite.get('test_cases')
        test_case = test_cases[0]

        start_time = test_case.get('start_time')
        end_time = test_case.get('end_time')
        execution_time = test_case.get('execution_time')

        assert start_time != 0.0, 'start time cannot be 0.0, cause its default value'
        assert end_time != 0.0, 'end time cannot be 0.0, cause its default value'
        assert start_time != end_time, 'start and end time cannot be equal'
        assert execution_time != 0.0, 'execution_time cannot be 0.0, cause its default value'
        assert (end_time - start_time) * 1000 == execution_time, 'execution time not in milliseconds'
        assert end_time > start_time

    def test_severity_level_blocker(self, severity_level_blocker):
        test_cases = severity_level_blocker.get('test_cases')
        test_case = test_cases[0]

        assert test_case.get('severity_level') == 'blocker'

    def test_severity_level_critical(self, severity_level_critical):
        test_cases = severity_level_critical.get('test_cases')
        test_case = test_cases[0]

        assert test_case.get('severity_level') == 'critical'

    def test_severity_level_normal(self, severity_level_normal):
        test_cases = severity_level_normal.get('test_cases')
        test_case = test_cases[0]

        assert test_case.get('severity_level') == 'normal'

    def test_severity_level_minor(self, severity_level_minor):
        test_cases = severity_level_minor.get('test_cases')
        test_case = test_cases[0]

        assert test_case.get('severity_level') == 'minor'

    def test_severity_level_trivial(self, severity_level_trivial):
        test_cases = severity_level_trivial.get('test_cases')
        test_case = test_cases[0]

        assert test_case.get('severity_level') == 'trivial'

    def test_severity_level_not_enum(self, severity_level_not_enum):
        assert severity_level_not_enum == 'severity is not a type of SeverityLevel'

    def test_logs_logging(self, logs):
        assert logs.get('logs') == 'start of assertion\nend of assertion\n'
