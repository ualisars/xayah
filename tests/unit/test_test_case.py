from xayah_test.classes.test_case_classes import (
    ClassTestCasePassed,
    ClassTestCaseFailed,
    ClassTestCaseAssertionMessageEmpty,
    ClassTestCaseAssertionMessage,
    ClassTestCaseExecutionTimePassed,
    ClassTestCaseExecutionTimeFailed,
    ClassTestCaseLogsPrint,
    ClassTestCaseLogging,
    ClassTestCasePrintAndLogging,
    ClassTestCaseAllLogging,
    ClassTestCaseFailedAssertionPrint,
    ClassTestCaseFailedAssertionLogging
)
from src.test_case import TestCase
from pytest import mark


class TestTestCase:
    def test_test_case_smoke(self, test_result):
        class_name = ClassTestCasePassed.__name__
        test_case = TestCase.init(ClassTestCasePassed.test_test_case_passed, class_name)
        test_case()
        method_name = 'test_test_case_passed'
        test_case_name = f'{class_name}::{method_name}'
        test_case = test_result.get_test_case(test_case_name)

        assert test_case is not None, 'test case is not added to test result'

        assert test_case.get('name') == test_case_name

        assert test_case.get('class_name') == class_name

        assert test_case.get('method_name') == method_name

        assert test_case.get('status') == 'passed'

    def test_test_case_failed(self, test_result):
        class_name = ClassTestCaseFailed.__name__
        test_case = TestCase.init(ClassTestCaseFailed.test_test_case_failed, class_name)
        test_case()
        method_name = 'test_test_case_failed'
        test_case_name = f'{class_name}::{method_name}'
        test_case = test_result.get_test_case(test_case_name)

        assert test_case is not None, 'test case is not added to test result'

        assert test_case.get('name') == test_case_name

        assert test_case.get('class_name') == class_name

        assert test_case.get('method_name') == method_name

        assert test_case.get('status') == 'failed'

    def test_assertion_message_empty(self, test_result):
        class_name = ClassTestCaseAssertionMessageEmpty.__name__
        test_case = TestCase.init(
            ClassTestCaseAssertionMessageEmpty.test_test_case_assertion_message_empty,
            class_name
        )
        test_case()
        method_name = 'test_test_case_assertion_message_empty'
        test_case_name = f'{class_name}::{method_name}'
        test_case = test_result.get_test_case(test_case_name)

        assertion_message = test_case.get('assertion_message')

        assert assertion_message == ''

    def test_assertion_message(self, test_result):
        class_name = ClassTestCaseAssertionMessage.__name__
        test_case = TestCase.init(
            ClassTestCaseAssertionMessage.test_test_case_assertion_message,
            class_name
        )
        test_case()
        method_name = 'test_test_case_assertion_message'
        test_case_name = f'{class_name}::{method_name}'
        test_case = test_result.get_test_case(test_case_name)

        assert test_case.get('assertion_message') == '30 is not 1'

    def test_check_status_passed(self):
        steps = [
            {'name': 'step1', 'status': 'passed', 'message': ''},
            {'name': 'step2', 'status': 'passed', 'message': ''}
        ]
        status = TestCase.check_status(steps)
        assert status == 'passed'

    def test_check_status_failed(self):
        steps = [
            {'name': 'step1', 'status': 'passed', 'message': ''},
            {'name': 'step2', 'status': 'failed', 'message': ''},
            {'name': 'step3', 'status': 'passed', 'message': ''}
        ]
        status = TestCase.check_status(steps)
        assert status == 'failed'

    def test_get_assertions_one_string(self):
        assertion = 'assert 5 == 2'
        assertions = [assertion]
        assertion_obj = TestCase._get_assertions(assertions)

        assert assertion_obj.get('assertion_message') == ''
        assert assertion_obj.get('assertion') == assertion

    def test_get_assertions_two_strings(self):
        assertion = 'assert 5 == 2'
        assertion_message = '5 is not 2'
        assertions = [assertion_message, assertion]
        assertion_obj = TestCase._get_assertions(assertions)

        assert assertion_obj.get('assertion_message') == assertion_message
        assert assertion_obj.get('assertion') == assertion

    def test_get_assertions_three_strings(self):
        assertion = 'assert 5 == 2'
        assertions = [assertion, '5', '2']
        assertion_obj = TestCase._get_assertions(assertions)

        assert assertion_obj.get('assertion_message') == ''
        assert assertion_obj.get('assertion') == assertion

    def test_get_assertions_four_strings(self):
        assertion = 'assert 5 == 2'
        assertion_message = '5 is not 2'
        assertions = [assertion_message, assertion, '5', '2']
        assertion_obj = TestCase._get_assertions(assertions)

        assert assertion_obj.get('assertion_message') == assertion_message
        assert assertion_obj.get('assertion') == assertion

    @mark.parametrize('TestClass', (ClassTestCaseExecutionTimePassed, ClassTestCaseExecutionTimeFailed))
    def test_execution_time_passed(self, TestClass, test_result):
        class_name = TestClass.__name__
        test_case = TestCase.init(
            TestClass.test_execution_time,
            class_name
        )
        test_case()
        method_name = 'test_execution_time'
        test_case_name = f'{class_name}::{method_name}'
        test_case = test_result.get_test_case(test_case_name)

        start_time = test_case.get('start_time')
        end_time = test_case.get('end_time')
        execution_time = test_case.get('execution_time')

        assert start_time != 0.0, 'start time cannot be 0.0, cause its default value'
        assert end_time != 0.0, 'end time cannot be 0.0, cause its default value'
        assert execution_time != 0.0, 'execution_time cannot be 0.0, cause its default value'
        assert end_time > start_time

    def test_logs_print(self, test_result):
        class_name = ClassTestCaseLogsPrint.__name__
        test_case = TestCase.init(
            ClassTestCaseLogsPrint.test_print,
            class_name
        )
        test_case()
        method_name = ClassTestCaseLogsPrint.test_print.__name__
        test_case_name = f'{class_name}::{method_name}'
        test_case = test_result.get_test_case(test_case_name)

        assertion_message = test_case.get('logs')

        assert assertion_message == 'start of assertions\nend of assertions\n'

    def test_logs_logging(self, test_result):
        class_name = ClassTestCaseLogging.__name__
        test_case = TestCase.init(
            ClassTestCaseLogging.test_logging,
            class_name
        )
        test_case()
        method_name = ClassTestCaseLogging.test_logging.__name__
        test_case_name = f'{class_name}::{method_name}'
        test_case = test_result.get_test_case(test_case_name)

        assertion_message = test_case.get('logs')

        assert assertion_message == 'start of assertion\nend of assertion\n'

    def test_logs_print_and_logging(self, test_result):
        class_name = ClassTestCasePrintAndLogging.__name__
        test_case = TestCase.init(
            ClassTestCasePrintAndLogging.test_print_and_logging,
            class_name
        )
        test_case()
        method_name = ClassTestCasePrintAndLogging.test_print_and_logging.__name__
        test_case_name = f'{class_name}::{method_name}'
        test_case = test_result.get_test_case(test_case_name)

        assertion_message = test_case.get('logs')

        assert assertion_message == 'print\nlogging\n'

    def test_logs_all_loggings(self, test_result):
        class_name = ClassTestCaseAllLogging.__name__
        test_case = TestCase.init(
            ClassTestCaseAllLogging.test_logging,
            class_name
        )
        test_case()
        method_name = ClassTestCaseAllLogging.test_logging.__name__
        test_case_name = f'{class_name}::{method_name}'
        test_case = test_result.get_test_case(test_case_name)

        assertion_message = test_case.get('logs')

        assert assertion_message == 'INFO\nDEBUG\nWARNING\nERROR\nCRITICAL\n'

    def test_logs_failed_assertion_print(self, test_result):
        class_name = ClassTestCaseFailedAssertionPrint.__name__
        test_case = TestCase.init(
            ClassTestCaseFailedAssertionPrint.test_logging,
            class_name
        )
        test_case()
        method_name = ClassTestCaseFailedAssertionPrint.test_logging.__name__
        test_case_name = f'{class_name}::{method_name}'
        test_case = test_result.get_test_case(test_case_name)

        assertion_message = test_case.get('logs')

        assert assertion_message == 'failed\n'

    def test_logs_failed_assertion_logging(self, test_result):
        class_name = ClassTestCaseFailedAssertionLogging.__name__
        test_case = TestCase.init(
            ClassTestCaseFailedAssertionLogging.test_logging,
            class_name
        )
        test_case()
        method_name = ClassTestCaseFailedAssertionLogging.test_logging.__name__
        test_case_name = f'{class_name}::{method_name}'
        test_case = test_result.get_test_case(test_case_name)

        assertion_message = test_case.get('logs')

        assert assertion_message == 'failed\n'
