from src.test_scenario import TestScenario
from src.test_case import TestCase


@TestScenario.init
class CheckTestCase:
    @TestCase.title('test case description')
    @TestCase.description('check whether title and description been added to test case')
    def test_test_case(self):
        assert 1 == 1
