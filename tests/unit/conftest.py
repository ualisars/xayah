from pytest import fixture
from src.test_suite import TestSuite


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
