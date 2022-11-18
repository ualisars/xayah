from pytest import fixture
from src.xayah.test_suite import TestSuite
from src.xayah.test_case import TestCase


@fixture(scope='function')
def test_suite_title_result(test_result):
    @TestSuite.init
    @TestSuite.title('Проверка заголовка тест кейса')
    class ClassTestSuiteTitle:
        def test_title(self):
            assert 1 == 1

    ClassTestSuiteTitle.run_test_cases()
    result = test_result.create_test_result()
    return result.get(ClassTestSuiteTitle.__name__)


@fixture(scope='function')
def several_before_all(test_result):

    @TestSuite.init
    class FirstBeforeAll:
        @TestSuite.before_all
        def set_up(self):
            TestCase.add_additional_params(FirstBeforeAll, self.test_before_all, {'name': 'first before all'})

        def test_before_all(self):
            pass

    @TestSuite.init
    class SecondBeforeAll:
        @TestSuite.before_all
        def set_up(self):
            TestCase.add_additional_params(SecondBeforeAll, self.test_before_all, {'name': 'second before all'})

        def test_before_all(self):
            pass

    FirstBeforeAll.run_test_cases()
    SecondBeforeAll.run_test_cases()

    return test_result.create_test_result()
