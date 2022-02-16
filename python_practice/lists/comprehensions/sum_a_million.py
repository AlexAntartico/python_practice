# Make a list of the numbers form one to one million, then use min()
# and max() to make sure your list actually starts at one and ends at
# one million. Also, use the sum() function to see how quickly Python
# can add a million numbers

million_list = [i for i in range(1, 1_000_001)]

min_val = min(million_list)
max_val = max(million_list)
sum_val = sum(million_list)

# lets assume you will make some charts or operations with values,
# thats why we are saving them.
# remember you can do something like
# print(f"min() value is: {min(million_list)}")
print(f"min() value is: {min_val}")
print(f"max() value is: {max_val}")
print(f"sum() value is: {sum_val}")
