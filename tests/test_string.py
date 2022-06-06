from src.test_scenario import TestScenario
from src import Step


@TestScenario.init()
class TestString:
    def test_conct(self):
        with Step("Авторизация"):
            a = "v"
            assert 'a' == 'a'
        with Step('Запрос'):
            assert "v" == a
        with Step('Проверка схемы'):
            assert "b" == a
        # assert 'blya' == 'k'
