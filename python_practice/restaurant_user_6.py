from datetime import date
import random


class User:

    def __init__(self, first_name, last_name, location) -> str:
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.location = location.title()
        self.last_access = date.today()
        self.account_number = random.randint(2000, 10000)

    def describe_user(self):
        print(
            f"first name is: {self.first_name}\n"\
            f"last name is: {self.last_name}\n"\
            f"{self.first_name}'s last access is: {self.last_access}\n"\
            f"{self.first_name}'s account number is {self.account_number}\n"\
            f"{self.first_name} is from {self.location}\n"
        )

    def greet_user(self):
        print(f"Hello {self.first_name}, glad you are here with ust today!!!")


alex = User("alex", "garcia", "Guadalajara, Mexico")
alex.describe_user()
alex.greet_user()