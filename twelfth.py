# more on conditions
# For example, if A and C are true but B is false, A and B and C does not evaluate the expression C.
# When used as a general value and not as a Boolean, the return value of a short-circuit operator is the last evaluated argument.
string1, string2, string3 = '', 'Trondheim', 'Hammer Dance'
non_null = string1 or string2 or string3 # return as soon as true value is got or else it will consider last element
print("or operator:")
print(non_null)
print()

string1, string2, string3 = 'Hello', '', 'Hammer Dance'
result = string1 and string2 and string3 # returns as soon as false value is got or else it will consider last element
print("and operator:")
print(result)
print()

print("Printing comparison sequence")
print("(1, 2, 3) < (1, 2, 2)")
print((1, 2, 3) < (1, 2, 4))
print()

print("[1, 2, 3] < [1, 2, 4]")
print([1, 2, 3] < [1, 2, 4])
print()

print("'ABC' < 'C' < 'Pascal' < 'Python'")
print('ABC' < 'C' < 'Pascal' < 'Python')
print()

print("(1, 2, 3, 4) < (1, 2, 4)")
print((1, 2, 3, 4) < (1, 2, 4))
print()

print("(1, 2) < (1, 2, -1)")
print((1, 2) < (1, 2, -1))
print()

print("(1, 2, 3) == (1.0, 2.0, 3.0)")
print((1, 2, 3) == (1.0, 2.0, 3.0))
print()

print("(1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4)")
print((1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4))
print()

# module (its like a custom library which is created by us)
import fibo

print("Printing fibonacci numbers from the module: ")
fibo.fib(1000)
print()

print("Returning the value of fibonacci numbers from the module: ")
result = fibo.fib2(100)
print(result)
print()

print("Printing the name of the module using _name_:")
print(fibo._name_)
print()

# You can also assign the function to local variable
fibo = fibo.fib
print("Printing fibonacci numbers using local variable function: ")
fibo(1000)