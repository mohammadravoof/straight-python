# Input and Output
# Printing output

# formatted string literals
year = 2016
event = 'Referendum'
print(f'Results of the {year} {event}')
print()

# str.format()
yes_votes = 42_572_654
total_votes = 85_705_149
percentage = yes_votes / total_votes
print('{:>-9} YES votes {:2.2%}'.format(yes_votes, percentage))
print()

# difference of str vs repr
s = 'Hello, world.'
print(str(s))
print()

print(repr(s))
print()

print(str(1/7))
print()

x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + repr(x) + ', and y is ' + repr(y) + '...'
print(s)
print()

# The repr() of a string adds string quotes and backslashes:
hello = 'hello\nworld'
print(repr(hello))
print()
print(str(hello))
print()

# The argument to repr() may be any Python object:
print(repr((x, y, ('spam', 'eggs'))))

# using expressions inside formatted string literals
import math
print(f'The value of pi is approximately {math.pi:.3f}.')