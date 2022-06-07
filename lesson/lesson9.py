from abc import ABC


class CarBase(ABC):
    max_speed = 110

    def __init__(self, age: int = 3, color: str = 'черный'):
        self.color = color
        self.age = age
        self._current_speed = 0
        self.max_speed = 100

    def current_speed(self):
        return self._current_speed

    def info(self):
        print(
            f'Цвет машины: {self.color}\n'
            f'Возраст машины: {self.age} лет')

    def drive(self, acceleration: int):
        self._current_speed = min((self._current_speed + acceleration, self.max_speed))
        print(f'Скорость машины: {self._current_speed} км/ч')

    def stop(self):
        self._current_speed = 0
        print(f'Машина остановилась')

    def emergency_signal(self):
        print(f'Аварийная сигнализация включена.')

    def auto_parking(self):
        pass


class Mazda(CarBase):
    max_speed = 180

    def __init__(self, price: int = 20000, age: int = 10, color: str = 'зеленый', safety_system_gen: str = 'ESC'):
        super().__init__(age, color)
        self.price = price
        self.safety_system_gen = safety_system_gen

    def info(self):
        print('Mazda profile')
        super().info()
        print(f'Цена машины: {self.price} €')

    def safety_system(self):
        print(f'Установлена система стабилизации автомобиля {self.safety_system_gen}')

    def auto_parking(self):
        print(f'Машина припаркуется сама.')


class Mercedes(CarBase):
    max_speed = 250

    def __init__(self, age: int = 5, color: str = 'золотой', car_design: str = 'Mercedes-Benz original'):
        super().__init__(age, color)
        self.car_design = car_design

    def info(self):
        print('Mercedes profile')
        super().info()
        print('Дизайн машины:', self.car_design)

    def auto_parking(self):
        print(f'Машина припаркуется сама.')


class Airplane(ABC):
    max_speed = 1100

    def __init__(self, age: int = 12, color: str = 'белый'):
        self.color = color
        self.age = age

        self.current_speed = 0

    def _current_speed(self):
        return self._current_speed

    def info(self):
        print(
            f'Цвет самолёта: {self.color}\n'
            f'Возраст самолёта: {self.age} лет'
        )

    def drive(self, acceleration: int):
        self.current_speed = min((self.current_speed + acceleration, self.max_speed))
        print(f'Скорость самолёта: {self.current_speed} км/ч')

    def stop(self):
        self.current_speed = 0
        print('Самолёт остановился.')

    def is_business_class(self, __exist):
        print('В самолёте есть места бизнес класса') if __exist.lower() == 'yes' else print(
            'В самолёте нет мест бизнес класса')

    def autopilot(self):
        print(f'Автопилот включен.')

    def close_chassis(self):
        pass


class Boeing(Airplane):
    max_speed = 988

    def __init__(self, age: int = 8, color: str = 'красный', engines_amount: int = 4):
        super().__init__(age, color)
        self.engines_amount = engines_amount

    def info(self):
        print('Boeing profile')
        super().info()
        print(f'Количество двигателей: {self.engines_amount}')

    def close_chassis(self):
        print(f'Шасси закроются автоматически.')


class Airbus(Airplane):
    max_speed = 1185

    def __init__(self, age: int = 5, color: str = 'голубой', seats: int = 180):
        super().__init__(age, color)
        self.seats = seats

    def info(self):
        print('Airbus profile')
        super().info()
        print(f'Количество посадочных мест: {self.seats}')

    def close_chassis(self):
        print(f'Шасси закрыты.')


auto1 = Mazda()
auto2 = Mercedes()
plane1 = Boeing()
plane2 = Airbus()


for transport in (auto1, auto2, plane1, plane2):
    transport.info()
    transport.drive(500)
    transport.stop()
    