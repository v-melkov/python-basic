"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""
class LowFuelError(Exception):
    print('It\'s too low fuel to start!')

class NotEnoughFuel(Exception):
    print('Not Enough Fuel to get to destination!')

class CargoOverload(Exception):
    print('Cargo Overload!')