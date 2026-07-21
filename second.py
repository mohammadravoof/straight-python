# compound data types
# 1. Lists (mutable, )
squares = [1, 4, 9, 16, 25]
print(squares)
print()

print(squares[0])
print()

print(squares[-1])
print()

print(squares[-3:])
print()

# concatenation
print(squares + [36, 49, 64, 81, 100])
print()

cube = [1, 8, 27, 65, 125] # something's wrong here
cube[3] = 64 # replace the value 
print(cube)
print()

# adding new elements to the end of a list
cube.append(216)
cube.append(7 ** 3)
print(cube)
print()

# Simple assignment in Python never copies data. It creates references to the original object.
rgb = ["red", "green", "blue"]
rgba = rgb

rgba.append("alph")
print(rgb)
print(rgba)
print()

# shallow copy
correct_rgba = rgb[:]
correct_rgba[-1] = "alpha"
print(rgb)
print(correct_rgba)
print()

letters = ["a", "b", "c", "d", "e", "f", "g"]
# replace some values
letters[2:5] = ["C", "D", "E"]
print(letters)
print()

# remove some values
letters[2:5] = []
print(letters)
print()

letters[:] = []
print(letters)
print()

letters = ["a", "b", "c", "d"]
print(len(letters))
print() 

# nested lists
a = ["a", "b", "c"]
n = [1, 2, 3]
x = [a, n]
print(x)
print()

print(x[0])
print()

print(x[0][1])
print()

print(x[1][1])
print()

# while loop
# fibonacci series: 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
a, b = 0, 1
while b < 10:
    print(b)
    a, b = b, a + b

print()

a, b = 0, 1
while b < 10:
    print(b, end=', ')
    a, b = b, a + b

print()
print()

# Since ** has higher precedence than -,
#  -3**2 will be interpreted as -(3**2)  and thus result in -9. 
# To avoid this and get 9, you can use (-3)**2

print(-3**2)
print()

print((-3)**2)
print()





