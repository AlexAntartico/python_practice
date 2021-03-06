# you can perform simple statistics with lists such as min, max and sum 

simple_list = []

for i in range(1, 16):
    simple_list.append(i)

print(f"This is the min number of the list: {min(simple_list)}")
print(f"This is the max number of the list: {max(simple_list)}")
print(f"This is the min number of the list: {sum(simple_list)}\n")


# Usually, a for cycle will print everything in a new line, this is
# because print statement has argument end="\n" set as default, this will 
# make any print statements end in a new line. To override this, change the 
# end parameter to any specific argument you need.
print("List numbers are:\n")
for j in simple_list:
    print(f"{j} ", end=" ")

# Note this will  add a space af ter each result, this is good to visually 
# present things to human peple, bad to use a mathematical formula because your
# list will not end with a number but with a space or any other random  thigng 
# you decide to use, so be mindful when changing sep= or end= parameters and
# what will diferent arguments passed will do.  


print("\nUsing List comprehensions:\n")
squares = [value ** 2 for value in range(1, 11)]
print(squares)

