
# Online Python - IDE, Editor, Compiler, Interpreter

# List operations - multiple ways

squares = []
for x in range (0,10):
    squares.append(x*x)
    
print(squares)

# Uisng List comprehensions
squares_comp = [ x*x for x in range(0,10)]
print("squares_comp : {}".format(squares_comp))

# using map function
list_1 = list(range(0,10))
def square(y):
    return y*y
ret_values = map(square,list_1)
ret_values_list = list(ret_values)
print(ret_values_list)


# list comprehensions replacing map

list_1 = list(range(0,10))
def square(y):
    return y*y
ret_values_list1 = [square(j) for j in list_1]

print("ret_values_list1 value is {}".format(ret_values_list1))
