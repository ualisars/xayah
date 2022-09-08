from pytest import fixture
from src.xayah.test_result import TestResult


@fixture(scope='function')
def test_result():
    yield TestResult()
    TestResult().clear_test_result()
