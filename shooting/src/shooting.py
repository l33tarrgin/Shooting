import abc

# TODO: добавить тесты для всех методов и классов, мб разнести классы в разные файлы, поработать над структурой


class General:

    name: str
    mag_size: int
    silencer: bool
    bullet_speed: int
    props_template: str = '''
            Название: {name}
            Размер магазина: {mag_size}
            Наличие глушителя: {silencer}
            Начальная скорость полета пули: {bullet_speed}
            '''
    shot_sound: str = 'BANG!'
    current_bullet_count: int
    burst_rounds: int

    def __init__(self, name: str, mag_size: int, silencer: bool,
                 bullet_speed: int):
        self.name = name
        self.mag_size = mag_size
        self.silencer = silencer
        self.bullet_speed = bullet_speed
        self.pistol_id = id(self)
        self.current_bullet_count = self.mag_size

    def show_props(self):
        props_string = self.props_template.format(
            name=self.name,
            mag_size=self.mag_size,
            silencer='присутствует' if self.silencer else 'отсутствует',
            bullet_speed=self.bullet_speed
        )
        return props_string

    def upgrade_mag_size(self, mag_size):
        self.mag_size = mag_size
        return f"Размер магазина увеличен: текущий размер {mag_size}"

    def install_silencer(self, silencer: bool):
        self.silencer = silencer
        self.shot_sound = 'Pssss'
        return "Глушитель установлен"

    def upgrade_bullet_speed(self, bullet_speed):
        self.bullet_speed = bullet_speed
        return f"Скорость полета пули увеличена: текущая скорость {bullet_speed}"


class CycleModeShooting(General):

    def shoot_single(self):
        for i in range(self.mag_size, -1, -1):
            if i > 0:
                print(f'{self.shot_sound}\nКоличество оставшихся патронов - {i}\n'
                      f'Чтобы произвести еще один выстрел нажмите "Y"\n'
                      f'Для выхода из режима стрельбы нажмите любую кнопку')
                if input() == 'Y':
                    continue
                else:
                    return 'Стрельба закончена'
            elif i == 0:
                return self.reload_gun_shoot_single()

    def shoot_with_burst_mode(self):
        num_bull_shot = self.burst_rounds
        for i in range(self.current_bullet_count - 2, -1, -num_bull_shot):
            if i > 0:
                print(f'{self.shot_sound}\nКоличество оставшихся патронов - {i}\n'
                      f'Чтобы произвести еще один выстрел нажмите "Y"\n'
                      f'Для выхода из режима стрельбы нажмите любую кнопку')
                if input() == 'Y':
                    continue
                else:
                    return 'Стрельба закончена'
            elif i == 0:
                return self.reload_gun_shoot_with_burst_mode()

    def shoot_automatic(self):
        shoot_automatic = 0
        for i in range(self.mag_size, -1, -1):
            if i > 0:
                print(f'{self.shot_sound}\nКоличество оставшихся патронов - {i}\n'
                      f'Для выхода из режима стрельбы нажмите любую кнопку\n')
            elif i == 0:
                #return self.reload_gun_shoot_automatic()
                return self.exp_reload(shoot_automatic)

    def exp_reload(self, num): # лучше же разбить каждую перезарядку по методам, нежели так?
        if num == 0:
            print('Перезарядить магазин и продолжить стрельбу?')
            if input() == 'Y':
                self.shoot_automatic()
                return
            else:
                return 'Стрельба закончена'
        elif num == self.shoot_automatic():
            print('single')
        else:
            print('burst')

    def reload_gun_shoot_single(self):
        print('Перезарядить магазин и продолжить стрельбу?')
        if input() == 'Y':
            self.shoot_single()
            return
        else:
            return 'Стрельба закончена'

    def reload_gun_shoot_with_burst_mode(self):
        print('Перезарядить магазин и продолжить стрельбу?')
        if input() == 'Y':
            self.shoot_with_burst_mode()
            return
        else:
            return 'Стрельба закончена'

    # def reload_gun_shoot_automatic(self):
    #     print('Перезарядить магазин и продолжить стрельбу?')
    #     if input() == 'Y':
    #         self.shoot_automatic()
    #         return
    #     else:
    #         return 'Стрельба закончена'


class AutomaticRifle(CycleModeShooting, General):
    #shooting_mode = None

    def __init__(self, name: str, mag_size: int, silencer: bool, #вот тут не понятно как правильно нужно сделать
                 bullet_speed: int):
        self.name = name
        self.mag_size = mag_size
        self.silencer = silencer
        self.bullet_speed = bullet_speed
        self.current_bullet_count = self.mag_size
        self.burst_rounds = 2

    def switch_shooting_mode(self):
        available_shooting_modes = {
            '1': self.shoot_single,
            '2': self.shoot_with_burst_mode,
            '3': self.shoot_automatic
        }
        chosen_mode = input('Нажмите 1 для одиночного огня, 2 для стрельбы с отсечкой, 3 для автоматического огня: ')
        self.shooting_mode = available_shooting_modes.get(chosen_mode)

    def shoot_gun(self):
        return self.shooting_mode()


ak47 = AutomaticRifle(name='AK-47', mag_size=4, silencer=False, bullet_speed=700)
ak47.switch_shooting_mode()
ak47.shoot_gun()