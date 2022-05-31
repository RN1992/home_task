from abc import ABC
import json
from dataclasses import dataclass


@dataclass
class CarBase(ABC):
    age: int = 3
    color: str = 'черный'
    _current_speed: int = 0
    max_speed: int = 100

    @property
    def current_speed(self):
        return self._current_speed

    def info(self):
        return f'Цвет машины: {self.color}\n' + f'Возраст машины: {self.age} лет'

    def drive(self, acceleration: int):
        self._current_speed = min((self._current_speed + acceleration, self.max_speed))
        return f'Скорость машины: {self._current_speed} км/ч'

    def stop(self):
        self._current_speed = 0
        return f'Машина остановилась'

    def emergency_signal(self):
        return f'Аварийная сигнализация включена.'

    def auto_parking(self):
        pass

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age

    def __le__(self, other):
        return self.age <= other.age

    def __ge__(self, other):
        return self.age >= other.age

    def __eq__(self, other):
        return self.age == other.age


@dataclass
class Mazda(CarBase):
    max_speed: int = 180
    age: int = 10
    color: str = 'зеленый'
    _current_speed: int = 0
    price: int = 20000
    safety_system_gen: str = 'ESC'

    def info(self):
        ret_str = 'Mazda profile\n' + super().info() + '\n' + f'Цена машины: {self.price} €'
        return ret_str

    def safety_system(self):
        return f'Установлена система стабилизации автомобиля {self.safety_system_gen}'

    def auto_parking(self):
        return f'Машина припаркуется сама.'


@dataclass
class Mercedes(CarBase):
    name = 'Дорогая тачка'
    max_speed: int = 250
    age: int = 5
    color: str = 'золотой'
    car_design: str = 'Mercedes-Benz original'

    def info(self):
        ret_st = 'Mercedes profile\n' + super().info() + '\n' + 'Дизайн машины: ' + self.car_design
        return ret_st

    def auto_parking(self):
        return f'Машина припаркуется сама.'

    @staticmethod
    def find_petrol_station():
        print('Мне нужен бензин и я его найду!')

    @classmethod
    def say_expensive(cls):
        print('Привет! Я очень', cls.name)


class Airplane(ABC):
    max_speed = 1100

    def __init__(self, age: int = 12, color: str = 'белый'):
        self.color = color
        self.age = age

        self.current_speed = 0

    def _current_speed(self):
        return self._current_speed

    def info(self):
        return f'Цвет самолёта: {self.color}\n' + f'Возраст самолёта: {self.age} лет'

    def drive(self, acceleration: int):
        self.current_speed = min((self.current_speed + acceleration, self.max_speed))
        return f'Скорость самолёта: {self.current_speed} км/ч'

    def stop(self):
        self.current_speed = 0
        return 'Самолёт остановился.'

    def is_business_class(self, __exist):
        if __exist.lower() == 'yes':
            return 'В самолёте есть места бизнес класса'
        else:
            return 'В самолёте нет мест бизнес класса'

    def autopilot(self):
        return f'Автопилот включен.'

    def close_chassis(self):
        pass


class Boeing(Airplane):
    max_speed = 988

    def __init__(self, age: int = 8, color: str = 'красный', engines_amount: int = 4):
        super().__init__(age, color)
        self.engines_amount = engines_amount

    def info(self):
        ret_st = 'Boeing profile\n' + super().info() + '\n' + f'Количество двигателей: {self.engines_amount}'
        return ret_st

    def close_chassis(self):
        return f'Шасси закроются автоматически.'


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


def automatic_file_json():
    mazda = Mazda()
    mercedes = Mercedes()
    with open('data.json', 'w') as file:
        m_data = {'info': mazda.info(), 'speed': mercedes.current_speed}
        json.dump(m_data, file)


auto1 = Mazda()
auto2 = Mercedes()
plane1 = Boeing()
plane2 = Airbus()

for transport in (auto1, auto2, plane1, plane2):
    print(transport.info())
    print(transport.drive(500))
    print(transport.stop())
    print('.........................')

print('Идет запись в json...')
print('.........................')
with open('data.json', 'w') as f:
    auto_data = {'info': auto1.info(), 'speed': auto1.current_speed}
    json.dump(auto_data, f)

print('json file готов!')
print('.........................')
print('Идет чтение json...')
print('.........................')
with open('data.json') as f:
    try:
        data = json.load(f)
        for i in data:
            print(i, data[i], sep=':')
    except:
        print('Что-то не так с файлом. Попробую создать свой =)\n.........................')
        automatic_file_json()
        print('Готово! Файл успешно создан!')
