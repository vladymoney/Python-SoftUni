from meals.meal import Meal


class Starter(Meal):
    def __init__(self):
        super(Starter, self).__init__(self.name, self.price, self.quantity)

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if not value:
            value = 60
        self.__quantity = value

    def details(self):
        return f"Starter {self.name}: {self.price:.2f}lv/piece"