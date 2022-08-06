from src.test_suite import TestSuite
from src.test_case import TestCase
from src.step import Step


@TestSuite.init
class CheckTestCase:
    @TestCase.title('test case description')
    @TestCase.description('check whether title and description been added to test case')
    def test_test_case(self):
        assert 4 == 3, 'hello'
