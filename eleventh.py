# Dictionaries
tel = {'jack' : 4098, 'sape' : 4139}
print('Printing tel: ')
print(tel)
print()

tel['guido'] = 4127
print('printing tel after adding guido: ')
print(tel)
print()

print('Printing jack\'s number: ')
print(tel['jack'])
print()

# print('Priting non existent key: ')
# print(tel['irv'])
# print()

print('Printing non existent key using get() keyword: ')
print(tel.get('irv'))
print()

print("Deleting 'sape' from tell:")
del tel['sape']
print(tel)
print()

print("Printing tel after adding 'irv': ")
tel['irv'] = 4127
print(tel)
print()

print("printing the keys of tel as list: ")
print(list(tel))
print()

print("printing the keys of tel as list after sorting: ")
print(sorted(tel))
print()

print("Whether 'guido' present in tel ?")
print('guido' in tel)
print()

print("Whether 'jack' no present in tel ?")
print('jack' not in tel)
print()

print("The dict() constructor builds dictionaries directly from sequences of key-value pairs:")
print(dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]))
print()

print(dict(sape=4139, guido=4127, jack=4098))
print()

print("Dict comprehensions can be used to create dictionaries from arbitrary key and value expressions:")
print({x: x**2 for x in (2, 4, 6)})
print()

# Looping techniques -
# items() - When looping through dictionaries, the key and corresponding value can be retrieved at the same time using the items() method.
print("Used items():")
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
 print(k, v)
print()

# enumerate() - When looping through a sequence, the position index and corresponding value can be retrieved at the same time using the enumerate() function.
print("Used enumerate():")
for i, v in enumerate(['tic', 'tac', 'toe']):
 print(i, v)
print()

# zip() - To loop over two or more sequences at the same time, the entries can be paired with the zip() function.
print("Used zip():")
questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
 print('What is your {0}? It is {1}.'.format(q, a))
print()

# reversed() - To loop over a sequence in reverse, first specify the sequence in a forward direction and then call the reversed() function.
print("Used reversed():")
for i in reversed(range(1, 10, 2)):
 print(i)
print()

# sorted() - To loop over a sequence in sorted order, use the sorted() function which returns a new sorted list while leaving the source unaltered.
print("Used sorted():")
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for i in sorted(basket):
 print(i)
print()

# set() & sorted() - Using set() on a sequence eliminates duplicate elements. The use of sorted() in combination with set() over a sequence is an
# idiomatic way to loop over unique elements of the sequence in sorted order.
print("Used set() along with sorted():") # used set inside because it will remove duplicated but it will be unordered.
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
 print(f)
print()

# isnan() - It is sometimes tempting to change a list while you are looping over it; however, it is often simpler and safer to create a new list instead.
print("Used isnan() to filter:")
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
 if not math.isnan(value):
    filtered_data.append(value)

print(filtered_data)