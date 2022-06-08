from src.test_scenario import TestScenario
from src import Step


@TestScenario.init()
class TestString:
    @TestScenario.before_all
    def set_up(self):
        print('Set Up')

    @TestScenario.after_all
    def clear(self):
        print('close connection')

    def test_conct(self):
        with Step("Авторизация"):
            a = "v"
            assert 'a' == 'a'
        with Step('Запрос'):
            assert "v" == a
        with Step('Проверка схемы'):
            assert "b" == a

    def test_name(self):
        with Step("Авторизация"):
            a = "v"
            assert 'a' == 'a'
        with Step('Запрос'):
            assert "v" == a
        with Step('Проверка схемы'):
            assert "b" == a
        # assert 'blya' == 'k'
