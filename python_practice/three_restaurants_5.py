

class Restaurant:
    """Practice to model a restaurant?"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\n Specialty is {self.cuisine_type} at {self.restaurant_name}"\
        " restaurant")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is currently open!!!")


altenos = Restaurant("Los Altenos", "Mexican Tacos")
muralla = Restaurant("La gran muralla", "Chinese food")
suehiro = Restaurant("Suehiro", "Sushi & Sake")


altenos.describe_restaurant()
muralla.describe_restaurant()
suehiro.describe_restaurant()
