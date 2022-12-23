from shooting import AutomaticRifle, CycleModeShooting, General
import mock

default_params = dict(name='AK-47', mag_size=4, silencer=False, bullet_speed=700)


class TestAutomaticRifle:

    gun = AutomaticRifle(**default_params)

    def test_switch_shooting_mode(self, monkeypatch):

        # arrange, описание неизменямых параметров
        old_shooting_mode = self.gun.shooting_mode
        mocked_input = mock.patch('builtins.input', return_value="2")

        # act, вызов тестируемой функции
        self.gun.switch_shooting_mode()
        # assert, сравнивание фактических результатов с ожидаемым
        assert old_shooting_mode != self.gun.shooting_mode
