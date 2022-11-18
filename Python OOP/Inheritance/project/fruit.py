from project.food import Food


class Fruit(Food):
    def __init__(self, fruit, expiration_date):
        self.expiration_date = expiration_date
        self.fruit = fruit
