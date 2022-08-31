import pytest
from pytest import fixture
from src.test_suite import TestSuite
from src.test_case import TestCase
from src.severity_level import SeverityLevel
import logging


@fixture(scope='function')
def title_result(test_result):
    @TestSuite.init
    class ClassTestCaseAndTestSuiteTitle:
        @TestCase.title('title1')
        def test_title(self):
            assert 1 == 1

    ClassTestCaseAndTestSuiteTitle.run_test_cases()
    result = test_result.create_test_result()
    return result.get(ClassTestCaseAndTestSuiteTitle.__name__)


@fixture(scope='function')
def description_result_passed(test_result):
    @TestSuite.init
    class ClassTestCaseAndTestSuiteDescriptionPassed:
        @TestCase.description('check if description been added to test case when test case passed')
        def test_description_passed(self):
            assert 1 == 1

    ClassTestCaseAndTestSuiteDescriptionPassed.run_test_cases()
    result = test_result.create_test_result()
    return result.get(ClassTestCaseAndTestSuiteDescriptionPassed.__name__)


@fixture(scope='function')
def description_result_failed(test_result):
    @TestSuite.init
    class ClassTestCaseAndTestSuiteDescriptionFailed:
        @TestCase.description('check if description been added to test case when test case failed')
        def test_description_failed(self):
            assert 1 == 2

    ClassTestCaseAndTestSuiteDescriptionFailed.run_test_cases()
    result = test_result.create_test_result()
    return result.get(ClassTestCaseAndTestSuiteDescriptionFailed.__name__)


@fixture(scope='function')
def title_and_description_result(test_result):
    @TestSuite.init
    class ClassTestCaseAndTestSuiteTitleDescription:
        @TestCase.title('test case title and description')
        @TestCase.description('check if title and description been added to test case')
        def test_title_and_description(self):
            assert 1 == 2

    ClassTestCaseAndTestSuiteTitleDescription.run_test_cases()
    result = test_result.create_test_result()
    return result.get(ClassTestCaseAndTestSuiteTitleDescription.__name__)


@fixture(scope='function')
def description_and_title_result(test_result):
    @TestSuite.init
    class ClassTestCaseAndTestSuiteDescriptionTitle:
        @TestCase.description('check title and description when description goes first')
        @TestCase.title('test case description and title not depend on execution order')
        def test_title_and_description(self):
            assert 1 == 2

    ClassTestCaseAndTestSuiteDescriptionTitle.run_test_cases()
    result = test_result.create_test_result()
    return result.get(ClassTestCaseAndTestSuiteDescriptionTitle.__name__)


@fixture(scope='function')
def severity_level_blocker(test_result):
    @TestSuite.init
    class ClassTestCaseAndTestSuiteSeverity:
        @TestCase.severity(SeverityLevel.BLOCKER)
        def test_severity(self):
            assert 2 == 2

    ClassTestCaseAndTestSuiteSeverity.run_test_cases()
    result = test_result.create_test_result()
    return result.get(ClassTestCaseAndTestSuiteSeverity.__name__)


@fixture(scope='function')
def severity_level_critical(test_result):
    @TestSuite.init
    class ClassTestCaseAndTestSuiteSeverityCritical:
        @TestCase.severity(SeverityLevel.CRITICAL)
        def test_severity(self):
            assert 2 == 2

    ClassTestCaseAndTestSuiteSeverityCritical.run_test_cases()
    result = test_result.create_test_result()
    return result.get(ClassTestCaseAndTestSuiteSeverityCritical.__name__)


@fixture(scope='function')
def severity_level_normal(test_result):
    @TestSuite.init
    class ClassTestCaseAndTestSuiteSeverityNormal:
        @TestCase.severity(SeverityLevel.NORMAL)
        def test_severity(self):
            assert 2 == 2

    ClassTestCaseAndTestSuiteSeverityNormal.run_test_cases()
    result = test_result.create_test_result()
    return result.get(ClassTestCaseAndTestSuiteSeverityNormal.__name__)


@fixture(scope='function')
def severity_level_minor(test_result):
    @TestSuite.init
    class ClassTestCaseAndTestSuiteSeverityMinor:
        @TestCase.severity(SeverityLevel.MINOR)
        def test_severity(self):
            assert 2 == 2

    ClassTestCaseAndTestSuiteSeverityMinor.run_test_cases()
    result = test_result.create_test_result()
    return result.get(ClassTestCaseAndTestSuiteSeverityMinor.__name__)


@fixture(scope='function')
def severity_level_trivial(test_result):
    @TestSuite.init
    class ClassTestCaseAndTestSuiteSeverityTrivial:
        @TestCase.severity(SeverityLevel.TRIVIAL)
        def test_severity(self):
            assert 2 == 2

    ClassTestCaseAndTestSuiteSeverityTrivial.run_test_cases()
    result = test_result.create_test_result()
    return result.get(ClassTestCaseAndTestSuiteSeverityTrivial.__name__)


@fixture(scope='function')
def severity_level_not_enum(test_result):
    with pytest.raises(ValueError) as VE:
        @TestSuite.init
        class ClassTestCaseAndTestSuiteSeverityNotEnum:
            @TestCase.severity('important')
            def test_severity(self):
                assert 2 == 2

        ClassTestCaseAndTestSuiteSeverityNotEnum.run_test_cases()

    return str(VE.value)


@fixture(scope='function')
def logs(test_result):
    @TestSuite.init
    class ClassTestCaseAndTestSuiteLogging:
        @staticmethod
        def test_logging():
            root = logging.getLogger()
            root.setLevel(logging.DEBUG)

            handler = logging.StreamHandler()
            handler.setLevel(logging.DEBUG)
            root.addHandler(handler)

            logging.basicConfig(level=logging.NOTSET)
            logger = logging.getLogger('test_logs')
            logger.setLevel(logging.DEBUG)
            logger.info('start of assertion')
            assert 1 == 1
            logger.debug('end of assertion')

    ClassTestCaseAndTestSuiteLogging.run_test_cases()
    result = test_result.create_test_result()
    test_suite = result.get(ClassTestCaseAndTestSuiteLogging.__name__)
    test_cases = test_suite.get('test_cases')
    return test_cases[0]
