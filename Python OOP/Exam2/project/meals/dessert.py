from meals.meal import Meal


class Dessert(Meal):
    def __init__(self):
        super(Dessert, self).__init__(self.name, self.price, self.quantity)

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if not value:
            value = 30
        self.__quantity = value

    def details(self):
        return f"Dessert {self.name}: {self.price:.2f}lv/piece"
