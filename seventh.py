# Data Structurs
# List methods

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']

print("Count of the apple is :", fruits.count('apple'))
print()
print("Count of the banana is :", fruits.count('banana'))
print()
print("Index of the banana is :", fruits.index('banana'))
print()
print("Index of the banana starting at position 4 is :", fruits.index('banana', 4)) # Find next banana starting at position 4
print()
reversed_fruits = fruits.reverse()

print("Reversed fruits :", fruits)
print()
appended_fruits = fruits.append('grape')

print("Fruits after appending grape :", fruits)
print()
sorted_fruits = fruits.sort()

print("Sorted fruits :", fruits)
print()

poped_fruits = fruits.pop()
print("Fruits after popping :", fruits)
print()

reverse_sorted_fruits = fruits.sort(key=None, reverse=True)
print("Reverse sorted fruits :", fruits)
print()

print("Return value of Reversed fruits ", reversed_fruits)
print("Return value of Appended fruits ", appended_fruits)
print("Return value of Sorted fruits ", sorted_fruits)
print("Return value of Poped fruits ", poped_fruits)
print()

# a = ["1", 2, "3", 4]
# b = [None, 'hello', 10, True]
# # print(a)
# print(b)
# # a.sort()
# b.sort()

first = [1, 2, 3]
second = [4, 5, 6, 7]

first.extend(second)
print("First list after extending with second list :", first)
print()

first.insert(1, 7)

print("Value of first list after inserting 7 at position 1 :", first)
print()

first.remove(7)
print("Value of first list after removing 7 :", first)
print()

index_value = first.index(4, 2, 4)
print("Index of 4 starting at position 2 and ending at position 4 is :", index_value)
print()

first_copy = first.copy() # similar to first[:]
print("Copied list :", first_copy)
print()

first.reverse()
print("Reversed first list :", first)
print()

print("First copy list :", first_copy)
print()