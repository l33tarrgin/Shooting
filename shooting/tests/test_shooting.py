from shooting import AutomaticRifle, CycleModeShooting, General

default_params = dict(name='AK-47', mag_size=4, silencer=False, bullet_speed=700)

class TestGeneral:

    general = General(**default_params)

    def test_switch_shooting_mode(self):

        # arrange, описание неизменямых параметров

        # act, вызов тестируемой функции

        # assert, сравнивание фактических результатов с ожидаемым