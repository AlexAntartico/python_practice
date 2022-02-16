# Make a list of the first 10 square numbers 

squares = []

# To be fair, this is how its usually done but if you dont really
# need to store the square value caues its a cheap script or you wont
# use it in large projects you can skip it

# for i in range(1, 11):
#     square = i ** 2
#     squares.append(square)

# you can invoque the append() method into the list object
# and add the arguments you want to append
for i in range(1, 11):
    squares.append(i ** 2)


print(squares)  # this will print output as a list

# below will iterate over the list and print values in a normal format
for j in squares:
    print(f"{j} ")