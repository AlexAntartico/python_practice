'''
Here is the first simple example of a nested array for leap year
'''

year = int(input("Which year do you want to check? "))

def nested_leap():
    if year % 4 == 0:
        if year % 100 != 0:
            CHECK
        else:
            print("Not a leap year.")
    else:
        print("Not a leap year.")

if __name__ == '__main__':
    nested_leap()
