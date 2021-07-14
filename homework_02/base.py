from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle:
    '''
    Создаём класс Vehicle со значениями по умолчанию
    '''
    weight = 20400
    started = False
    fuel = 560
    fuel_consumption = 0.43  # 1km


    def __init__(self, weight=weight, fuel=fuel, fuel_consumption=fuel_consumption):
        '''
        Инициализируем экземпляр класса
        Если значения веса, топлива и расхода не переданы,
        возьмём их из атрибутов класса
        :param weight: вес
        :param fuel: запас топлива
        :param fuel_consumption: расход топлива
        '''
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption


    def start(self):
        '''
        Проверяем наличие топлива и при значении выше 0 стартуем двигатель
        иначе вызываем ошибку LowFuelError
        :return: двигатель запущен
        '''
        if self.started is not True:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError
        return self.started


    def move(self, distance):
        '''
        Проверяем, достаточно ли топлива для перемещения на определённую дистанцию
        Если хватает, вычитаем потраченное топливо
        иначе вызываем ошибку NotEnoughFuel
        :param distance: дистанция для проверки
        :return: возвращаем оставшееся количество топлива
        '''
        if self.fuel / self.fuel_consumption < distance:
            raise NotEnoughFuel
        else:
            self.fuel = self.fuel - distance * self.fuel_consumption
        return self.fuel
