

class Restaurant:
    """Practice to model a restaurant?"""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.customers = 0

    def describe_restaurant(self):
        print(f"Specialty is {self.cuisine_type} at {self.restaurant_name} "\
        "restaurant")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is currently open!!!")

    def set_number_served(self, served_customers):
        if served_customers <= 0:
            print("you have to serve customers to modify this parameter!")
        else:
            self.customers = served_customers

    def increment_number_served(self, increment_customers):
        if increment_customers >= 0:
            self.customers += increment_customers
        else:
            print("you have to serve customers to modify this parameter!")
        
        


restaurant = Restaurant("Los Alteños", "Mexican Tacos")
print(f"{restaurant.restaurant_name}")
print(f"{restaurant.cuisine_type}\n")

restaurant.describe_restaurant()
restaurant.open_restaurant()


# print # of customers, then modify value and print again:
print(f"Number of clients served is {restaurant.customers}")
restaurant.customers = 25
print(f"Number of clients served is {restaurant.customers}\n")


# added set_number_served. evaluating with 0, negative and pos
restaurant.set_number_served(0)
restaurant.set_number_served(-10)
restaurant.set_number_served(10)

print(restaurant.customers)
print()

# total of 51 extra customers served (+10 we have from above call)
restaurant.increment_number_served(51)
print(restaurant.customers)