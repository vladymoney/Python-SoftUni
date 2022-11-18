from project.client import Client
from project.meals.dessert import Dessert
from project.meals.main_dish import MainDish
from project.meals.starter import Starter


class FoodOrdersApp:
    def __init__(self):
        self.menu = []
        self.clients_list = []
        self.receipt = 0
# ---------------------------------------------------------------

    def register_client(self, client_phone_number):
        if self.check_if_client_exists(client_phone_number):
            raise Exception("The client has already been registered!")
        client = Client(phone_number=client_phone_number)
        self.clients_list.append(client)
        return f"Client {client_phone_number} registered successfully."
# --------------------------------------------------------

    def add_meals_to_menu(self, *meals):
        for meal in meals:
            accepted_types = ['Starter', 'Dessert', 'MainDish']
            if meal.__class__.__name__ in accepted_types:
                self.menu.append(meal)
# --------------------------------------------------------

    def show_menu(self):
        if len(self.menu) < 5:
            raise "The menu is not ready!"
        result = ''
        for meal in self.menu:
            result += f'{meal.details()}\n'
        return result.strip()
# --------------------------------------------------------

    def add_meals_to_shopping_cart(self, client_phone_number, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")
        if not self.check_if_client_exists(phone_number=client_phone_number):
            self.clients_list.append(Client(phone_number=client_phone_number))

        client = self.check_if_client_exists(phone_number=client_phone_number)
        meal_names_list = [meal.name for meal in client.shopping_cart]

        for meal_name, quant in meal_names_and_quantities.items():
            meal = self.check_if_meal_is_on_the_menu(meal_name)
            meal_names_list.append(meal_name)
            if not self.check_if_meal_is_on_the_menu(meal_name):
                raise Exception(f"{meal_name} is not on the menu!")
            if meal.quantity < quant:
                raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal_name}!")
            elif meal.quantity >= quant:
                meal.quantity -= quant
                client.bill += meal.price * quant
                client.shopping_cart.append(meal)
        return f"Client {client_phone_number} successfully ordered {', '.join(meal_names_list)} for {(client.bill):.2f}lv."
# ---------------------------------------------------------------------------------

    def cancel_order(self, client_phone_number):
        client = self.check_if_client_exists(client_phone_number)
        if len(client.shopping_cart) <= 0:
            raise Exception("There are no ordered meals!")
        for meal in client.shopping_cart:
            for meals in self.menu:
                if meals.name == meal.name:
                    meals.quantity += meal.quantity
            client.shopping_cart.remove(meal)
        return f"Client {client_phone_number} successfully canceled his order."
# -------------------------------------------------------------------------------------

    def finish_order(self, client_phone_number):
        client = self.check_if_client_exists(client_phone_number)
        if len(client.shopping_cart) <= 0:
            raise Exception("There are no ordered meals!")
        for meal in client.shopping_cart:
            client.shopping_cart.remove(meal)
        paid = client.bill
        client.bill = 0
        self.receipt += 1
        return f"Receipt #{self.receipt} with total amount of {paid:.2f} was successfully paid for {client_phone_number}."
# -------------------------------------------------------------------------------------

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."
# -------------------------------------------------------------------------------------

    def check_if_client_exists(self, phone_number):
        for client in self.clients_list:
            if client.phone_number == phone_number:
                return client

    def check_if_meal_is_on_the_menu(self, meal_name):
        for meal in self.menu:
            if meal.name == meal_name:
                return meal
        return False
# -------------------------------------------------------------------------------------




food_orders_app = FoodOrdersApp()
print(food_orders_app.register_client("0899999999"))
print(food_orders_app.register_client("0899999988"))
french_toast = Starter("French toast", 6.50, 5)
hummus_and_avocado_sandwich = Starter("Hummus and Avocado Sandwich", 7.90, 10)
tortilla_with_beef_and_pork = MainDish("Tortilla with Beef and Pork", 12.50, 12)
risotto_with_wild_mushrooms = MainDish("Risotto with Wild Mushrooms", 15)
chocolate_cake_with_mascarpone = Dessert("Chocolate Cake with Mascarpone", 4.60, 17)
chocolate_and_violets = Dessert("Chocolate and Violets", 5.20)
print(food_orders_app.add_meals_to_menu(
    french_toast, hummus_and_avocado_sandwich,
    tortilla_with_beef_and_pork,
    risotto_with_wild_mushrooms,
    chocolate_cake_with_mascarpone,
    chocolate_and_violets))
print(food_orders_app.show_menu())
food = {"Hummus and Avocado Sandwich": 5,
        "Risotto with Wild Mushrooms": 1,
        "Chocolate and Violets": 4}
print(food_orders_app.add_meals_to_shopping_cart('0899999999', **food))
print(food_orders_app.add_meals_to_shopping_cart('0899999988', **food))
additional_food = {"Risotto with Wild Mushrooms": 2,
                   "Tortilla with Beef and Pork": 2}
print(food_orders_app.add_meals_to_shopping_cart('0899999999', **additional_food))
print(food_orders_app.add_meals_to_shopping_cart('0899999988', **additional_food))
print(food_orders_app.finish_order("0899999999"))
print(food_orders_app.finish_order("0899999988"))
print(food_orders_app)



