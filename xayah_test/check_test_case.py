from src.xayah.test_suite import TestSuite
from src.xayah.test_case import TestCase
from src.xayah.step import Step
from src.xayah.shared_data import SharedData


@TestSuite.init
class CheckTestCase:
    @TestSuite.before_all
    def init(self):
        SharedData.share('driver', 'chrome')

    @TestCase.title('test case description')
    @TestCase.description('check whether title and description been added to test case')
    def test_test_case(self):
        with Step('hello'):
            assert 3 == 3
        with Step('goodbye'):
            driver = SharedData.get('driver')
            assert driver == 'chrome'
