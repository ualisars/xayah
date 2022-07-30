from pytest import fixture
from src.test_scenario import TestScenario
from src.test_case import TestCase


@fixture(scope='function')
def title_result(test_result):
    @TestScenario.init
    class ClassTestCaseAndTestScenarioTitle:
        @TestCase.title('title1')
        def test_title(self):
            assert 1 == 1

    ClassTestCaseAndTestScenarioTitle.run_test_cases()
    return test_result.create_test_result()


@fixture(scope='function')
def description_result_passed(test_result):
    @TestScenario.init
    class ClassTestCaseAndTestScenarioDescriptionPassed:
        @TestCase.description('check if description been added to test case when test case passed')
        def test_description_passed(self):
            assert 1 == 1

    ClassTestCaseAndTestScenarioDescriptionPassed.run_test_cases()
    return test_result.create_test_result()


@fixture(scope='function')
def description_result_failed(test_result):
    @TestScenario.init
    class ClassTestCaseAndTestScenarioDescriptionFailed:
        @TestCase.description('check if description been added to test case when test case failed')
        def test_description_failed(self):
            assert 1 == 2

    ClassTestCaseAndTestScenarioDescriptionFailed.run_test_cases()
    return test_result.create_test_result()


@fixture(scope='function')
def title_and_description_result(test_result):
    @TestScenario.init
    class ClassTestCaseAndTestScenarioTitleDescription:
        @TestCase.title('test case title and description')
        @TestCase.description('check if title and description been added to test case')
        def test_title_and_description(self):
            assert 1 == 2

    ClassTestCaseAndTestScenarioTitleDescription.run_test_cases()
    return test_result.create_test_result()


@fixture(scope='function')
def description_and_title_result(test_result):
    @TestScenario.init
    class ClassTestCaseAndTestScenarioDescriptionTitle:
        @TestCase.description('check title and description when description goes first')
        @TestCase.title('test case description and title not depend on execution order')
        def test_title_and_description(self):
            assert 1 == 2

    ClassTestCaseAndTestScenarioDescriptionTitle.run_test_cases()
    return test_result.create_test_result()
