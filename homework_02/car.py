"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02.engine import Engine

class Car(Vehicle):

    engine = None

    def __init__(self, weight, fuel, fuel_consumption):
        super(Car, self).__init__(weight, fuel, fuel_consumption)

    def set_engine(self, engine):
        self.engine = engine
