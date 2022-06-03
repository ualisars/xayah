from src.test_scenario import TestScenario


@TestScenario.init()
class TestString:
    def test_conct(self):
        assert "a" + "b" == "ab"
