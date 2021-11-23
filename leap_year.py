'''
Here is the first simple example of a nested array for leap year
'''

year = int(input("Which year do you want to check? "))

def nested_leap():
    if year % 4 != 0:
        print("not leap year")
    elif year % 100 == 100:
        print("not leap year")
    elif year % 400 != 0:
        print("not leap year")
    else:
        print("leap year")


if __name__ == '__main__':
    nested_leap()
