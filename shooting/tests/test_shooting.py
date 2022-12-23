from shooting import AutomaticRifle, CycleModeShooting, General
import mock

default_params = dict(name='AK-47', mag_size=4, silencer=False, bullet_speed=700)


class TestAutomaticRifle:

    gun = AutomaticRifle(**default_params)

    def test_upgrade_mag_size(self):
        # arrange, описание незменяемых параметров
        old_mag_size = self.gun.mag_size
        new_mag_size = 12

        # act, вызов тестируемой функции
        result = self.gun.upgrade_mag_size(new_mag_size)

        # assert, сравнивание фактических результатов с ожидаемым
        # assert result == new_mag_size # чому нет?
        assert result == 'Размер магазина увеличен: текущий размер 12'
        assert result != old_mag_size

    def test_install_silencer(self):
        # arrange, описание незменяемых параметров
        old_install_silencer = self.gun.install_silencer
        new_install_silencer = True

        # act, вызов тестируемой функции
        result = self.gun.install_silencer(new_install_silencer)

        # assert, сравнивание фактических результатов с ожидаемым
        assert result == "Глушитель установлен"
        assert result != old_install_silencer

    def test_upgrade_bullet_speed(self):
        # arrange, описание незменяемых параметров
        old_bullet_speed = self.gun.bullet_speed
        new_bullet_speed = 1000

        # act, вызов тестируемой функции
        result = self.gun.upgrade_bullet_speed(new_bullet_speed)

        # assert, сравнивание фактических результатов с ожидаемым
        assert result == 'Скорость полета пули увеличена: текущая скорость 1000'
        assert result != old_bullet_speed

    def test_switch_shooting_mode(self, monkeypatch):
        # arrange, описание неизменямых параметров
        old_shooting_mode = self.gun.shooting_mode

        # act, вызов тестируемой функции
        self.gun.switch_shooting_mode()

        # assert, сравнивание фактических результатов с ожидаемым
        assert old_shooting_mode != self.gun.shooting_mode
