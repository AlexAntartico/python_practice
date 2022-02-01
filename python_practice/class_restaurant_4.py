# from https://note.nkmk.me/en/python-long-string/
# s = 'https://ja.wikipedia.org/wiki/'\
#    '%E3%83%97%E3%83%AD%E3%82%B0%E3%83'\
#    '%A9%E3%83%9F%E3%83%B3%E3%82%B0%E8%A8%80%E8%AA%9E'

# prints long line
# https://ja.wikipedia.org/wiki/%E3%83%97%E3%83%AD%E3%82%B0%E3%83%A9%E3%83%9F%E3%83%B3%E3%82%B0%E8%A8%80%E8%AA%9E


class Restaurant:
    """Practice to model a restaurant?"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Specialty is {self.cuisine_type} at {self.restaurant_name} "\
        "restaurant")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is currently open!!!")


restaurant = Restaurant("Los Alteños", "Mexican Tacos")
print(f"{restaurant.restaurant_name}")
print(f"{restaurant.cuisine_type}\n")

restaurant.describe_restaurant()
restaurant.open_restaurant()
