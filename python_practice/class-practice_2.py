# Dog class will sotore a name and an age
# we will give dog the ability to sit() and roll_over()

class Dog:
    '''A simple attempt to model a dog'''

    def __init__(self, name, age):
        '''Initialize name and age attributes'''
        self.name = name
        self.age = age

    def sit(self):
        '''Simulate a dog sitting in response to a command'''
        print(f"{self.name} is now sitting")

    def roll_over(self):
        '''Simulate rolling over to a command'''
        print(f"{self.name} rolled over!")


my_dog = Dog("Willie", 6)

print(f"My dog's name is:{my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

my_dog.sit()
my_dog.roll_over()

