from abc import ABC, abstractmethod


class Car(ABC):

    def __init__(self, brand, model, year, color):
        self.brand = brand.upper()
        self.model = model.upper()
        self.year = year
        self.color = color
        self.current_speed = 0
        self.max_speed = 100
        self.__seats = 4

    def type_vehical(self):
        return 'Я - машина.'

    def amount_seats(self):
        return f'Мое количество пассажирских мест - {self.__seats}.'

    def info(self):
        if self.color.endswith('ий'):
            self.color = self.color.replace('ий', 'его')
        if self.color.endswith('ый'):
            self.color = self.color.replace('ый', 'ого')
        long_name = f'{self.brand} {self.model} {self.year}'
        return f'Поздравляем с приобретением автомобиля {long_name.upper()} {self.color} цвета!'

    def start_car(self):
        return 'Машина завелась.'

    def begin_move(self):
        if self.current_speed == 0:
            return f'Моя скорость равна {self.current_speed} км/ч. Для начала движения нажмите на газ.'

    def stop(self):
        self.current_speed = 0
        return 'Я остановился. Моя скорость равна 0 км/ч.'

    def emergency_signal(self):
        return 'Аварийная световая сигнализация включена.'

    @abstractmethod
    def add_gas(self, add_speed: int):
        pass

    @abstractmethod
    def brand_model(self):
        pass


class Audi(Car):

    def __init__(self, brand, model, year, color):
        super().__init__(brand, model, year, color)
        self.current_speed = 0
        self.max_speed = 210

    def brand_model(self):
        return self.brand, self.model

    def add_gas(self, add_speed: int):
        self.current_speed = min(self.current_speed + add_speed, self.max_speed) + 20
        return f'Теперь я еду со скоростью {self.current_speed} км/ч, максимальная скорость - {self.max_speed} км/ч.'

    def econ(self):
        return 'Включен режим ECON.'


class Mercedes(Car):
    def __init__(self, brand, model, year, color):
        super().__init__(brand, model, year, color)
        self.current_speed = 0
        self.max_speed = 200

    def brand_model(self):
        return self.brand, self.model

    def add_gas(self, add_speed: int):
        self.current_speed = min(self.current_speed + add_speed, self.max_speed) + 10
        return f'Теперь я еду со скоростью {self.current_speed} км/ч, максимальная скорость - {self.max_speed} км/ч.'

    def auto_parking(self):
        return 'Машина припаркуется автоматически.'


class Volkswagen(Car):
    def __init__(self, brand, model, year, color):
        super().__init__(brand, model, year, color)
        self.current_speed = 0
        self.max_speed = 170

    def brand_model(self):
        return self.brand, self.model

    def add_gas(self, add_speed: int):
        self.current_speed = min(self.current_speed + add_speed, self.max_speed) - 10
        return f'Теперь я еду со скоростью {self.current_speed} км/ч, максимальная скорость - {self.max_speed} км/ч.'

    def open_close_window(self):
        return 'Открытые окна автоматически закроются при закрытии машины.'


class Airplane(ABC):
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color
        self.__engines = 2

        self.current_height = 0
        self.max_height = 15000

        self.current_speed = 0
        self.max_speed = 850

    def amount_engines(self):
        return f'У меня {self.__engines} двигателя.'

    def type_vehical(self):
        return 'Я - самолет.'

    def info(self):
        if self.color.endswith('ий'):
            self.color = self.color.replace('ий', 'его')
        if self.color.endswith('ый'):
            self.color = self.color.replace('ый', 'ого')
        return f'Поздравляем с приобретением самолета {self.brand.upper()} {self.model.upper()} {self.color} цвета!'

    def start_airplane(self):
        return 'Самолет завелся.'

    def begin_move(self):
        if self.current_speed == 0:
            return f'Моя скорость равна {self.current_speed} км/ч. Для начала движения переведите рычаг скорости вверх.'

    def raise_lever(self, value_speed: int):
        self.current_speed = min(self.current_speed + value_speed, self.max_speed)
        return f'Моя скорость - {self.current_speed} км/ч, максимальная скорость - {self.max_speed} км/ч.'

    def stop(self):
        self.current_speed = 0
        return f'Я остановился. Моя скорость равна {self.current_speed} км/ч.'

    def autopilot(self):
        return 'Автопилот включен.'

    @abstractmethod
    def brand_model(self):
        pass

    @abstractmethod
    def close_chassis(self):
        pass


class Boeing(Airplane):
    def __init__(self, brand, model, color):
        super().__init__(brand, model, color)
        self.max_speed = 900
        self.max_height = 12500

    def brand_model(self):
        return self.brand, self.model

    def passengers_capacity(self):
        return 'Я пассажирский самолет. Моя пассажировместимость 189 человек. '

    def close_chassis(self):
        return 'Шасси закроются автоматически.'


class Airbus(Airplane):
    def __init__(self, brand, model, color):
        super().__init__(brand, model, color)
        self.max_speed = 850
        self.max_height = 11900

    def brand_model(self):
        return self.brand, self.model

    def load_capacity(self):
        return 'Я транспортный самолет. Моя грузоподъемность 37 тонн.'

    def close_chassis(self):
        return 'Шасси закрыты.'


class Eagle(Airplane):
    def __init__(self, brand, model, color):
        super().__init__(brand, model, color)
        self.max_speed = 2650
        self.max_height = 20000

    def brand_model(self):
        return self.brand, self.model

    def feature(self: int):
        return 'Мое достоинство - скорость.'

    def close_chassis(self):
        return 'Шасси закроются автоматически на высоте 2000 метров.'


def main():
    audi1 = Audi('Audi', 'a4', '2016', 'белый')
    print(audi1.info())
    print(audi1.amount_seats())
    print(audi1.begin_move())
    print(audi1.emergency_signal())
    print()

    audi2 = Audi('Audi', 'rs8', '2020', 'черный')
    audi2.max_speed = 300
    print(audi2.brand_model())
    print(f'Моя скорость равна {audi2.current_speed} км/ч.')
    print(audi2.add_gas(250))
    print(audi2.econ())
    print(audi2.stop())
    print()

    mercedes1 = Mercedes('Mercedes', 'gl63', '2020', 'синий')
    mercedes1.max_speed = 280
    print(mercedes1.info())
    print(f'Максимальная скорость - {mercedes1.max_speed} км/ч.')
    print(mercedes1.type_vehical(), mercedes1.brand_model())
    print()

    mercedes2 = Mercedes('Mercedes', 'cla', '2020', 'желтый')
    print(mercedes2.start_car())
    print(mercedes2.add_gas(250))
    print(mercedes2.auto_parking())
    print()

    volkswagen1 = Volkswagen('Volkswagen', 'tiguan', '2016', 'белый')
    print(volkswagen1.info())
    print(volkswagen1.open_close_window())
    print()

    volkswagen2 = Volkswagen('Cla2502', 'polo', '2020', 'синий')
    print(volkswagen2.start_car())
    print(volkswagen2.begin_move())
    print(volkswagen2.add_gas(150))
    print(volkswagen2.stop())
    print()

    boeing1 = Boeing('Boeing', '737', 'белый')
    boeing1.max_speed = 1100
    print(boeing1.info())
    print(boeing1.type_vehical())
    print(boeing1.autopilot())
    print(boeing1.passengers_capacity())
    print()

    boeing2 = Boeing('Boeing', '777', 'белый')
    print(f'Мой цвет - {boeing2.color}.')
    print(boeing2.close_chassis())
    print(boeing2.raise_lever(1000))
    print(boeing2.brand_model())
    print()

    airbus1 = Airbus('Airbus', 'A300', 'серый')
    print(f'Моя максимальная скорость - {airbus1.max_speed} км/ч.')
    print(airbus1.raise_lever(250))
    print(airbus1.close_chassis())
    print()

    airbus2 = Airbus('Airbus', 'A380', 'черный')
    airbus2.max_speed = 780
    print(airbus2.load_capacity())
    print(airbus2.brand_model())
    print()

    eagle1 = Eagle('Eagle', 'F-15', 'серый')
    print(eagle1.info())
    print(eagle1.type_vehical())
    print(eagle1.feature())
    print(eagle1.close_chassis())
    print()

    vehicle = [audi1, audi2, mercedes1, mercedes2, volkswagen1, volkswagen2,
               boeing1, boeing2, airbus1, airbus2, eagle1]
    for i in vehicle:
        print(i.type_vehical(),
              i.brand_model(),
              f'[MAX_SPEED] - {i.max_speed} км/ч')
        print()


if __name__ == '__main__':
    main()
