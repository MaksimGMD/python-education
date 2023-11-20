from dataclasses import dataclass

from base import Vehicle
from engine import Engine


"""
создайте класс `Car`, наследник `Vehicle`
"""


@dataclass
class Car(Vehicle):
    engine: Engine = None

    def set_engine(self, engine: Engine):
        self.engine = Engine


myCar = Car()
