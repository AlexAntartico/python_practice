

class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year) -> None:
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0  # value is initialized to 0 here

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer.")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles


my_used_car = Car("subaru", "outback", 2015)
print(my_used_car.get_descriptive_name())

# using a method to directly modify an attribute's value:
my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

# update current attribute's value using a method
my_used_car.increment_odometer(189)
my_used_car.read_odometer()


my_new_car = Car("audi", "a4", 2019)  # Creating a new class instance

my_new_car.update_odometer(23)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()


# Modifying attributes value directly:
# my_new_car.odometer_reading = 23
# my_new_car.read_odometer()