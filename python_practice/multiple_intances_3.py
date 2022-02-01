# https://www.python.org/dev/peps/pep-0008/#blank-lines
# Surround top-level function and class definitions with two blank lines
# Method definitions inside a class are surrounded by a single blank line


class Dog:
    '''A simple attempt to model a Dog'''

    def __init__(self, name, age):
        '''Initialize age and name attributes'''
        self.name = name
        self.age = age
    
    def sit(self):
        '''Simulate a dog sitting in response to a command'''
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        '''Simulate rolling over in response to a command'''
        print(f"{self.name} rolled over!!!")


my_dog = Dog("Willie", 6)
your_dog = Dog("Lucy", 3)

print(f"My dog's name is: {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is: {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
