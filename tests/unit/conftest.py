from pytest import fixture
from src.test_result import TestResult


@fixture(scope='session')
def test_result():
    return TestResult()
