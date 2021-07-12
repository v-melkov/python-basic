"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine

class Car(Vehicle):

    volume = 0
    pistons = 0


    def __init__(self, weight=Vehicle.weight, fuel=Vehicle.fuel, fuel_consumption=Vehicle.fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def set_engine(volume, pistons):
        volume = 42
        pistons = 12
        return Engine(volume, pistons)

    def main(self):
        self.engine = Car.set_engine(10, 20)