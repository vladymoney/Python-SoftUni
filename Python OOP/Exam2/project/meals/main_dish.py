from meals.meal import Meal


class MainDish(Meal):
    def __init__(self):
        super(MainDish, self).__init__(self.name, self.price, self.quantity)

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if not value:
            value = 50
        self.__quantity = value

    def details(self):
        return f"Main Dish {self.name}: {self.price:.2f}lv/piece"

