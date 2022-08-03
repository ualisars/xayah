from pytest import fixture
from src.test_suite import TestSuite
from src.test_case import TestCase


@fixture(scope='function')
def title_result(test_result):
    @TestSuite.init
    class ClassTestCaseAndTestSuiteTitle:
        @TestCase.title('title1')
        def test_title(self):
            assert 1 == 1

    ClassTestCaseAndTestSuiteTitle.run_test_cases()
    return test_result.create_test_result()


@fixture(scope='function')
def description_result_passed(test_result):
    @TestSuite.init
    class ClassTestCaseAndTestSuiteDescriptionPassed:
        @TestCase.description('check if description been added to test case when test case passed')
        def test_description_passed(self):
            assert 1 == 1

    ClassTestCaseAndTestSuiteDescriptionPassed.run_test_cases()
    return test_result.create_test_result()


@fixture(scope='function')
def description_result_failed(test_result):
    @TestSuite.init
    class ClassTestCaseAndTestSuiteDescriptionFailed:
        @TestCase.description('check if description been added to test case when test case failed')
        def test_description_failed(self):
            assert 1 == 2

    ClassTestCaseAndTestSuiteDescriptionFailed.run_test_cases()
    return test_result.create_test_result()


@fixture(scope='function')
def title_and_description_result(test_result):
    @TestSuite.init
    class ClassTestCaseAndTestSuiteTitleDescription:
        @TestCase.title('test case title and description')
        @TestCase.description('check if title and description been added to test case')
        def test_title_and_description(self):
            assert 1 == 2

    ClassTestCaseAndTestSuiteTitleDescription.run_test_cases()
    return test_result.create_test_result()


@fixture(scope='function')
def description_and_title_result(test_result):
    @TestSuite.init
    class ClassTestCaseAndTestSuiteDescriptionTitle:
        @TestCase.description('check title and description when description goes first')
        @TestCase.title('test case description and title not depend on execution order')
        def test_title_and_description(self):
            assert 1 == 2

    ClassTestCaseAndTestSuiteDescriptionTitle.run_test_cases()
    return test_result.create_test_result()
