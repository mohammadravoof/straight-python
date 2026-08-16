table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')
 
# '!a' applies ascii(), '!s' applies str(), and '!r' applies repr()
animals = 'éels'
print(f'My hovercraft is full of {animals}.')
print()
print(f'My hovercraft is full of {animals!a}.')
print()
print(f'My hovercraft is full of {animals!s}.')
print()
print(f'My hovercraft is full of {animals!r}.')
print()
 
# using = to pass a variable using name
 
bugs = 'roaches'
count = 13
area = 'living room'
print(f'Debugging {bugs=} {count=} {area=}')
print()
 
# basic string format
print('We are the {} who say "{}!"'.format('knights', 'Ni'))
print()
 
# using position 
print('{0} and {1}'.format('spam', 'eggs'))
print()
print('{1} and {0}'.format('spam', 'eggs'))
print()
 
# using keyword arguments
print('This {food} is {adjective}.'.format(food='spam', adjective='absolutely horrible'))
print()
 
# postion and keyword combined
print('The story of {0}, {1}, and {other}.'.format('Bill', 'Manfred', other='Georg'))
print()
 
# using postion and []
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 8637678}
table2 = {'Vinay': 1000, 'Udhay': 420, 'Shyam': 456}
print('Jack: {0[Jack]:d}; Sjoerd: {0[Sjoerd]:d}; Udhay: {1[Udhay]:d}'.format(table, table2))
print()
 
# using keyword argument passing **
print('Jack: {Jack:d}; Sjoerd: {Sjoerd:d}; Udhay: {Udhay:d}'.format(**table, **table2))
print()
 
 
table = {k: str(v) for k, v in vars().items()}
message = " ".join([f'{k}: ' + '{' + k +'};\n' for k in table.keys()])
print(message.format(**table))
print()
 
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
 
 
# same above but formatted manually # rjust = right justify
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).center(3), repr(x*x*x).ljust(4))
    # Note use of 'end' on previous line
    # print(repr(x*x*x).rjust(4))