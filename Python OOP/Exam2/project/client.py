class Client:

    shopping_cart = list()
    bill = 0.0

    def __init__(self, phone_number):
        self.phone_number = phone_number


    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        self.__phone_number = value
        if value[0] != 0 and len(value) != 10:
            raise ValueError("Invalid phone number!")

