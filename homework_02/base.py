from abc import ABC

from exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight=0, fuel=0, fuel_consumption=0, started=False):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = started

    def start(self):
        if not self.started:
            if self.fuel > 0:
                self.started = True
            else:
                raise LowFuelError("Мало топлива")

    def move(self, distance: int):
        new_distance = distance * self.fuel_consumption
        if self.fuel >= new_distance:
            self.fuel = self.fuel - new_distance
        else:
            raise NotEnoughFuel("Недостаточно топлива")
