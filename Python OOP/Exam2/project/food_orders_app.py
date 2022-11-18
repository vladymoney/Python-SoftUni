class FoodOrdersApp:

    menu = list()
    clients_list = list()

    def __init__(self):
        pass

    def register_client(self, client_phone_number: str):
        pass

    def add_meals_to_menu(self, *meals):
        pass

    def show_menu(self):
        pass

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        pass

    def cancel_order(self, client_phone_number: str):
        pass

    def finish_order(self, client_phone_number: str):
        pass

    def __str__(self):
        pass
