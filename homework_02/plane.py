"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    cargo = 0
    max_cargo = 10000


    def __init__(self, weight=Vehicle.weight, fuel=Vehicle.fuel, fuel_consumption=Vehicle.fuel_consumption, max_cargo=None):
        '''
        переопределяем значение max_cargo
        или устанавливаем равным атрибуту класса

        остальные значения определяем или берём из родительского класса
        (если не указать конструкцию типа weight=Vehicle.weight, pytest выдаёт ошибку при проверке)

        :param max_cargo: максимальный вес
        '''
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

        if max_cargo == None:
            self.max_cargo = Plane.max_cargo
        else:
            self.max_cargo = max_cargo


    def load_cargo(self, current_cargo):
        '''
        Метод, который принимает число и проверяет,
        что в сумме с текущим cargo не будет перегруза
        иначе вызывает ошибку CargoOverload
        :param current_cargo: принимаемое число
        :return: возвращаем текущий вес груза
        '''
        if self.cargo + current_cargo > self.max_cargo:
            raise CargoOverload
        else:
            self.cargo += current_cargo
        return self.cargo

    def remove_all_cargo(self):
        '''
        обнуляем вес предварительно сохранив его во временную переменную
        затем возвращаем сохраненный вес
        :return: сохраненный до обнуления вес
        '''
        temp_cargo = self.cargo
        self.cargo = 0
        return temp_cargo
