from xayah_test.classes.test_case_classes import (
    ClassTestCasePassed,
    ClassTestCaseFailed,
    ClassTestCaseAssertionMessageEmpty,
    ClassTestCaseAssertionMessage
)
from src.test_case import TestCase


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
