# tuples are datatypes in python like lists but immutable
t = 12345, 54321, 'hello!'
print("Tuple t[0] = ")
print(t[0])
print()
 
print("Entire Tuple: ")
print(t)
print()
 
# print("Tuples are immutable: ")
# t[0] = 88888
# print(t)
# print()
 
# but they can contain mutable objects
v = [1, 2, 3], [3, 2, 1]
print("Mutable objects in tuple: ")
print(v[0])
print()
 
# Tuples are usually binded with parenthesis and separated by commas
v = ([1, 2, 3], [3, 2, 1])
print("Tuple with parenthesis: ")
print(v)
print()
 
# creating an empty tuple
empty = ()
singleton = 'hello',
 
print("Length of empty tuple: ")
print(len(empty))
print()
 
print("Length of singleton tuple: ")
print(len(singleton))
print()
 
print("Printing singleton: ")
print(singleton)
print()
 
# Unpacking (Destructuring the tuple)
x, y, z = t
print("Unpacked values: ")
print("x = ")
print(x)
print()
print("y = ")
print(y)
print()
print("z = ")
print(z)
print()
 
# Sets - Unordered collection with no duplicate elements
s = { 2, 4, 6, 8, 10, 2, 4, 6, 8, 10 }
print("Set s (duplicates removed): ")
print(s)
print()
 
# in operator which will give True or False as output
print("whether 2 is there in s: ")
print(2 in s)
print()
 
print("whether 100 is there in s: ")
print(100 in s)
print()
 
# Demonstrate set operations on unique letters from two words
 
a = set('abracadabra')
b = set('alacazam')
 
print("Printing set a: ")
print(a)                                  # unique letters in a
print()
 
print("Printing set b: ")
print(b)
print()
 
print("Printing a - b: ")
print(a - b)                             # letters in a but not in b
print()
 
print("Printing a | b: ")
print(a | b)                              # letters in a or b or both
print()
 
print("Printing a & b: ")
print(a & b)                              # letters in both a and b
print()
 
print("Printing a ^ b: ")
print(a ^ b)                              # letters in a or b but not both
print()