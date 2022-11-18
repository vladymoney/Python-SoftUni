class Profile:
    def __init__(self, username, password):
        self.password = password
        self.username = username

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not 5 <= len(self.username) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        is_length = len(value) >= 8
        is_upper_case_presented = [char for char in value if char.isupper()]
        is_digit_presented = [char for char in value if char.isdigit()]

        if not is_upper_case_presented or is_digit_presented or is_length:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'


profile_with_invalid_password = Profile('My_username', 'My-password')