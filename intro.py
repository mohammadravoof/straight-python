the_world_is_flat = True
if the_world_is_flat:
    print("Be careful not to fall off!")
print()

# This is the first comment
spam = 1 # and this is the second comment
text = "# This is not a comment because it's inside quotes."
print(text)
print()

print(2 + 2)
print()

print(50 - 5 * 6)
print()

print((50 - 5 * 6) / 4)
print()

print(8 / 5)
print()

print(17 % 3)
print()

print(5 ** 2)
print()

print(2 ** 8)
print()

width = 20
height = 5 * 9
print(width * height)
print()

width = 20.0
height = 5.0 * 9.0
print(width * height)
print()

print('spam eggs')
print()

print('doesn\'t')
print()

print('"Yes," they said.')
print()

print("\"Yes,\" they said.")
print()

print('"Isn\'t," they said.')
print()

s = 'First line.\nSecond line.'
print(s)
print()

print('C:\this\name')  # here \n means newline!
print()

print(r'C:\this\name')  # note the r before the quote
print()

print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")
print()

print(3 * 'un' + 'ium')
print()

print('Py' 'thon')
print()

text = ('Put several strings within parentheses '
        'to have them joined together.')
print(text)
print()

word = 'Python'
print(word[0])  # character in position 0
print(word[5])  # character in position 5
print()     

print(word[-1])  # last character
print(word[-2])  # second-last character
print(word[-6])  # first character  
print()     

print(word[0:2])  # characters from position 0 (included) to 2 (excluded)
print(word[2:5])  # characters from position 2 (included) to 5 (excluded)
print()

print(word[:2]) # character from the beginning to position 2 (excluded)
print(word[4:]) # characters from position 4 (included) to the end
print(word[-2:]) # characters from the second-last (included) to the end
print()

s = 'supercalifragilisticexpialidocious'
print(len(s))
print()