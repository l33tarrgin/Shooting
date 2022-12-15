import abc


# TODO: добавить тесты для всех методов и классов, мб разнести классы в разные файлы, поработать над структурой

class FireWeapon(abc.ABC):
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

    def show_props(self):
        props_string = self.props_template.format(
            name=self.name,
            mag_size=self.mag_size,
            silencer='присутствует' if self.silencer else 'отсутствует',
            bullet_speed=self.bullet_speed
        )
        return props_string

    @abc.abstractmethod
    def shoot_gun(self):
        pass

    def shoot_single(self):
        while True:
            while self.current_bullet_count > 0:
                self.current_bullet_count -= 1
                print(f'{self.shot_sound}\nКоличество оставшихся патронов - {self.current_bullet_count}\n'
                      f'Чтобы произвести еще один выстрел нажмите "Y"\n'
                      f'Для выхода из режима стрельбы нажмите любую кнопку')
                if input() == 'Y':
                    continue
                else:
                    return 'Стрельба закончена'
            self.reload_gun()

    def shoot_automatic(self):
        while True:
            while self.current_bullet_count > 0:
                self.current_bullet_count -= 1
                print(f'{self.shot_sound}\nКоличество оставшихся патронов - {self.current_bullet_count}\n')
            self.reload_gun()

    def shoot_with_burst_mode(self, burst_rounds: int = 0):
        while True:
            while self.current_bullet_count > 0:
                counter = burst_rounds or self.burst_rounds
                while counter > 0:
                    self.current_bullet_count -= 1
                    counter -= 1
                    print(f'{self.shot_sound}\nКоличество оставшихся патронов - {self.current_bullet_count}\n')
                state = input(f'Чтобы произвести еще один выстрел нажмите "Y"\n'
                              'Для выхода из режима стрельбы нажмите любую кнопку')
                if state == 'Y':
                    self.shoot_with_burst_mode(burst_rounds=self.burst_rounds)
                else:
                    return 'Стрельба закончена'

                self.reload_gun()

    def reload_gun(self):
        print('Перезарядить магазин и продолжить стрельбу?')
        if input() == 'Y':
            self.current_bullet_count = self.mag_size
            return
        else:
            return 'Стрельба закончена'

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


class Pistol(FireWeapon):
    def __init__(self, name: str, mag_size: int, silencer: bool,
                 bullet_speed: int):
        self.name = name
        self.mag_size = mag_size
        self.silencer = silencer
        self.bullet_speed = bullet_speed
        self.pistol_id = id(self)
        self.current_bullet_count = self.mag_size

    def kill_human(self):
        self.shoot_gun()
        print('Ай бля маслину поймал')

    def incomplete_disassembly_pm(self):  # TODO: переписать метод, для наглядной демонстрации сборки разборки
        # start = datetime.now()
        # list_filled = {1: 'Trigger Guard (close)', 2: 'Recoil Spring', 3: 'Magazine', 4: 'Trigger Guard (open)',
        #                5: 'Slide'}
        # right_list_for_user = ['4', '3', '5', '1', '2']
        # empty_list_for_user = []
        #
        # print(
        #     f'Произведите в правильном порядке неполную сборку пистолета Макарова! \n'
        #     f'Нажмите Y для начала сборки и подсчета времени. Для выхода из режима нажмите любую кнопку')
        # if input() == 'Y':
        #     print('The assembly has begun! Time limit = 12sec')
        #     self.start = datetime.now()
        #
        #     for i in self.list_filled.values():  # цикл для соотнесения частей пистолета и записи введенных значений
        #         print(i)
        #         self.empty_list_for_user.append(input())
        #     if self.empty_list_for_user == self.right_list_for_user:
        #         print(f'Good, your time: {datetime.now() - self.start}')
        #     else:
        #         print(f'Bad, your time {datetime.now() - self.start}')
        return 'Неполная сборка пистолета Макарова завершена.'

    def shoot_gun(self):
        return self.shoot_single()


class AutomaticRifle(FireWeapon):
    shooting_mode = None

    def __init__(self, name: str, mag_size: int, silencer: bool,
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


# ak47 = AutomaticRifle(name='AK-47', mag_size=30, silencer=False, bullet_speed=700)
# ak47.switch_shooting_mode()
# ak47.shoot_gun()
