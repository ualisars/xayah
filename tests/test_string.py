from src.test_scenario import TestScenario
from src import Step
from src import Check


@TestScenario.init
class TestString:
    @TestScenario.before_all
    def set_up(self):
        print('Set Up')

    @TestScenario.after_all
    def clear(self):
        print('close connection')

    def test_conct(self):
        print(self.test_param['name'])
        with Step("Авторизация"):
            a = "v"
            assert 'a' == 'v', 'понятно'
        with Step('Запрос'):
            assert "v" == a
        with Step('Проверка схемы'):
            assert "b" == a

    def test_name(self):
        with Check("Авторизация"):
            a = "v"
            assert 'a' == 'a'
        with Check('Запрос'):
            assert "v" == 'b', 'не работает'
        with Check('Проверка схемы'):
            assert "b" == a
        assert 'blya' == 'k'
