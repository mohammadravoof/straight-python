vec = [-4, -2, 0, 2, 4]
# create a new list with the values doubled
print("Doubled values:")
print([x*2 for x in vec])
print()

# filter the list to exclude negative numbers
print("Positive values:")
print([x for x in vec if x >= 0])
print()

# apply a function to all the elements
print("Absolute values:")
print([abs(x) for x in vec])
print()

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
print("Stripped fruits:")
print([weapon.strip() for weapon in freshfruit])
print()

# create a list of 2-tuples like (number, square)
print("Number and square:")
print([(x, x**2) for x in range(6)])
print()

# the tuple must be parenthesized, otherwise an error is raised
print("Number and square:")
# print([x, x**2 for x in range(6)])
print()

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
print("Flattened list:")
print([num for elem in vec for num in elem])
print()

# nested list comprehensions
from math import pi
print("Rounded values of pi:")
print([str(round(pi, i)) for i in range(1, 6)])
print()

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print("Transposed matrix:")
print([[row[i] for row in matrix] for i in range(4)])
print()

# transpose a matrix using built-in functions
print("Transposed matrix (using zip):")
print(list(zip(*matrix)))
print()


# delete a single element
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print("After deleting the first element:")
print(a)
print()

del a[2]
print("After deleting the third element:")
print(a)
print()

del a[2:4]
print("After deleting elements at indices 2 and 3:")
print(a)
print()

del a[:]
print("After deleting all elements:")
print(a)
print()