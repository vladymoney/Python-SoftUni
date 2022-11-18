class Client:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.shopping_cart = []
        self.bill = 0.0

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        for char in value:
            if not char.isnumeric():
                raise ValueError("Invalid phone number!")
            if len(value) < 10:
                raise ValueError("Invalid phone number!")
            if int(value[0]) != 0:
                raise ValueError("Invalid phone number!")
        self.__phone_number = value

