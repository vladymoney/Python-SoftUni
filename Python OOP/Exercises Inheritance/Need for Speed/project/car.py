from project.vehicle import Vehicle


class Car(Vehicle):
    Vehicle.DEFAULT_FUEL_CONSUMPTION = 3

    def drive(self, kilometers):
        if self.fuel >= self.fuel_consumption * kilometers:
            self.fuel_consumption *= kilometers
