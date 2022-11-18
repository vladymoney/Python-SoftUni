from project.car import Car
from project.vehicle import Vehicle


class SportCar(Car):
    Vehicle.DEFAULT_FUEL_CONSUMPTION = 10

    def drive(self, kilometers):
        if self.fuel >= self.fuel_consumption * kilometers:
            self.fuel_consumption *= kilometers
