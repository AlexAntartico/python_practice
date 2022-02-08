from datetime import date
import random


class User:
    """
    Class to define a standar user with some attributes such as
    first name, last name, location, last access, a random acc number and
    a counter for login attempts
    """
    def __init__(self, first_name, last_name, location) -> str:
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.location = location.title()
        self.last_access = date.today()
        self.account_number = random.randint(2000, 10000)
        self.login_attempts = 0  # initializing login atempts

    def describe_user(self):
        print(
            f"first name is: {self.first_name}\n"\
            f"last name is: {self.last_name}\n"\
            f"{self.first_name}'s last access is: {self.last_access}\n"\
            f"{self.first_name}'s account number is {self.account_number}\n"\
            f"{self.first_name} is from {self.location}\n"
        )

    def greet_user(self):
        print(f"Hello {self.first_name}, glad you are here with us today!!!")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    """
    Class inherited from User to create special kind of user: Admin
    and describes attributes and/or methods
    """
    def __init__(self, first_name, last_name, location) -> str:
        super().__init__(first_name, last_name, location)

class Privilege(Admin):
    """
    Class define privileges
    """
    def __init__(self, first_name, last_name, location) -> str:
        super().__init__(self, first_name, last_name, location)
        self.privileges = ["can add post", "can delete post", "can ban user",  
        "can block ip"]

    def show_privileges(self):
        print("Admin priveleges:\n")
        for self.action in self.privileges:
            print(self.action)


alex = User("alex", "garcia", "Guadalajara, Mexico")
alex.describe_user()
alex.greet_user()

# increment several times, print and then reset, print again

for i in range (0, 10):
    alex.increment_login_attempts()
    print(f"login attempts: {alex.login_attempts}")

alex.reset_login_attempts()
print(f"\nlogin attempts: {alex.login_attempts}")


eduardo = Privilege("kone", "garcia", "Zapopan")
print("\n")


