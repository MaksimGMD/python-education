"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""


class LowFuelError(Exception):
    def __str__(self):
        return "Мало топлива"


class NotEnoughFuel(Exception):
    def __str__(self):
        return "Недостаточно топлива"


class CargoOverload(Exception):
    def __str__(self):
        return "Техника перегружена"
