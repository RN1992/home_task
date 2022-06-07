from abc import ABC


class Car(ABC):
    max_speed = 100

    def __init__(self, age: int = 3, color: str = 'blue'):
        self.color = color
        self.age = age

        self._current_speed = 0

    @property
    def current_speed(self):
        return self._current_speed

    @property
    def is_useful(self):
        return 'That car is useful'

    def info(self):
        print(
            f'Цвет машины: {self.color}\n'
            f'Возраст машины: {self.age} лет'
        )

    def drive(self, acceleration: int):
        self._current_speed = min((self._current_speed + acceleration, self.max_speed))
        print(f'Скорость машины: {self._current_speed} км/ч')

    def stop(self):
        self._current_speed = 0
        print('Машина остановилась')

    @classmethod
    def method(cls):
        print('Вызываю classmethod у Car\n')

    @staticmethod
    def headlight(self, on_off):
        print('Фары горят') if on_off.lower() == 'on' else print('Фары не горят')


class Volvo(Car):
    max_speed = 150

    def __init__(self, price: int = 50000, age: int = 2, color: str = 'white', safety_system_gen: str = 'Mark 12'):
        super().__init__(age, color)
        self.price = price
        self.safety_system_gen = safety_system_gen

    def info(self):
        print('Volvo profile')
        super().info()
        print(f'Цена машины: {self.price} $' )

    def safety_system(self):
        print(f'Установлена система безопасности автомобиля на дороге {self.safety_system_gen}')

    @staticmethod
    def _open_trunk(__open_close):
        print('Открыть багажник') if __open_close.lower() == 'open' else print('Закрыть багажник')

    @staticmethod
    def beeping(signal):
        print("Beep-beep. It's Volvo") if signal.lower() == 'signal' else print('')


class Lada(Car):
    max_speed = 70

    def __init__(self, age: int = 8, color: str = 'баклажан', car_body: str = 'Cедан' ):
        super().__init__(age, color)
        self.car_body = car_body

    def info(self):
        print('Lada profile')
        super().info()
        print('Модель кузова:', self.car_body)

    def optional_feat(self, install):
        print('В салон установлен Диско-шар и Иконки') if install.lower() == 'yes' else print('')

    def _open_windows(self, __open_close):
        print('Окна открыты') if __open_close.lower() == 'open' else print('Окна закрыты')

    def beeping(self, signal):
        print("Beep-beep. It's Lada") if signal.lower() == 'signal' else print('')


class Plane(ABC):
    max_speed = 900

    def __init__(self, age: int = 10, color: str = 'white'):
        self.color = color
        self.age = age

        self._current_speed = 0

    def info(self):
        print(
            f'Цвет самолёта: {self.color}\n'
            f'Возраст самолёта: {self.age} лет'
        )

    def drive(self, acceleration: int):
        self._current_speed = min((self.current_speed + acceleration, self.max_speed))
        print(f'Скорость самолёта: {self.current_speed} км/ч')

    def stop(self):
        self._current_speed = 0
        print('Самолёт остановился.')

    @property
    def is_useful(self):
        return 'That plane is useful'

    @property
    def current_speed(self):
        return self._current_speed

    @classmethod
    def method(cls):
        print('Вызываю classmethod у Plane\n')

    @staticmethod
    def is_first_class(__exist):
        print('В самолёте есть места 1-го класса') if __exist.lower() == 'yes' else print('В самолёте нет мест 1-го класса')


class Boeing(Plane):
    max_speed = 1000

    def __init__(self, age: int = 8, color: str = 'white-blue', engines_amount: int = 4):
        super().__init__(age, color)
        self.engines_amount = engines_amount

    def info(self):
        print('Boeing profile')
        super().info()
        print(f'Количество двигателей: {self.engines_amount} единицы')

    def shower(self, install):
        print('На борту имеется душ для пассажиров') if install.lower() == 'yes' else print('В этом самолёте душа нет')

    def beeping(self, signal):
        print("Beep-beep. It's Boeing") if signal.lower() == 'signal' else print('')


class Airbus(Plane):
    max_speed = 1100

    def __init__(self, age: int = 5, color: str = 'white-red', wingspan: int = 80 ):
        super().__init__(age, color)
        self.wingspan = wingspan

    def info(self):
        print('Airbus profile')
        super().info()
        print(f'Размах крыльев: {self.wingspan} метров')

    def bar(self, install):
        print('На борту имеется бар для пассажиров') if install.lower() == 'yes' else print('В этом самолёте бара нет')

    def beeping(self, signal):
        print("Beep-beep. It's Airbus") if signal.lower() == 'signal' else print('')


volvo1 = Volvo()
lada1 = Lada()
boeing1 = Boeing()
airbus1 = Airbus()


for machines in (volvo1,lada1,boeing1,airbus1):
    machines.info()
    machines.drive(300)
    machines.stop()
    print(machines.is_useful)
    machines.method()
