from dataclasses import dataclass

from base import Vehicle
from exceptions import CargoOverload

"""
создайте класс `Plane`, наследник `Vehicle`
"""


@dataclass
class Plane(Vehicle):
    cargo: int = 0
    max_cargo: int = 0

    def __init__(
        self, weight=0, started=False, fuel=0, fuel_consumption=0, max_cargo=0
    ):
        super().__init__(weight, started, fuel, fuel_consumption)
        self.max_cargo = max_cargo

    def load_cargo(self, load: int):
        new_cargo = self.cargo + load
        if new_cargo <= self.max_cargo:
            self.cargo = new_cargo
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        self.cargo = 0
