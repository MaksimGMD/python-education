from base import Vehicle
from exceptions import CargoOverload

"""
создайте класс `Plane`, наследник `Vehicle`
"""


class Plane(Vehicle):
    def __init__(
        self, weight=0, fuel=100, fuel_consumption=15, max_cargo=1000, cargo=0
    ):
        super().__init__(weight, fuel, fuel_consumption)
        self.max_cargo = max_cargo
        self.cargo = cargo

    def load_cargo(self, amount):
        total_cargo = self.cargo + amount
        if total_cargo <= self.max_cargo:
            self.cargo = total_cargo
        else:
            raise CargoOverload("Cargo overload")

    def remove_all_cargo(self):
        previous_cargo = self.cargo
        self.cargo = 0
        return previous_cargo
