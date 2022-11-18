class Pizza:
    def __init__(self, name, dough, toppings_capacity, calculate_total_weight, toppings):
        self.__toppings = toppings
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.calculate_total_weight = calculate_total_weight

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("The name cannot be an empty string")
        self.__name = value

    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value

    @property
    def toppings_capacity(self):
        return self.__topping_capacity

    @toppings_capacity.setter
    def toppings_capacity(self, value):
        if self.toppings_capacity <= 0:
            raise ValueError("The topping's capacity cannot be less or equal to zero")
        self.__topping_capacity = value

    def add_topping(self, topping, weight):
            if self.toppings_capacity >= self.toppings_capacity:
                raise ValueError("Not enough space for another topping")
            elif topping in self.__toppings:
                weight += topping
            else:
                self.__toppings += topping

    def calculate_total_weight(self):
        return self.__dough.weight + sum(self.__toppings.values())

