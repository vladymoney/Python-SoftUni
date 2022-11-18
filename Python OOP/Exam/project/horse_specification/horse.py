from horse_specification.appaloosa import Appaloosa
from horse_specification.thoroughbred import Thoroughbred
from abc import ABC, abstractmethod


class Horse(ABC):
    is_taken = False

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 4:
            raise ValueError(f"Horse name {value} is less than 4 symbols!")
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if value > Appaloosa.speed or value > Thoroughbred.speed:
            raise ValueError("Horse speed is too high!")
        self.__speed = value

    @abstractmethod
    def increase_speed(self):
        pass

    def train(self):
        if self.speed + self.increase_speed >= Appaloosa.max_speed:
            self.speed = 120
        elif self.speed + self.increase_speed >= Thoroughbred.max_speed:
            self.speed = 140