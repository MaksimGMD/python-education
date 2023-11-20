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
                raise LowFuelError()

    def move(self, distance):
        if self.fuel > distance * self.fuel_consumption:
            self.fuel = self.fuel - distance * self.fuel_consumption
        else:
            raise NotEnoughFuel()

# car = Vehicle(100, 0, 2)
# print(car.started)
# car.start()
# print(car.started)
