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
