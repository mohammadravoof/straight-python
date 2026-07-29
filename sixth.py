# There is no possible call that will make it return True as the keyword 'name' will always bind to the first parameter.
def foo(name, **kwds):
    return True if 'name' in kwds else False

# But using / (positional only arguments), it is possible since it allows name as a positional argument and 'name'
#  as a key in the keyword arguments:

# def foo(name, /, **kwds):
#     return True if 'name' in kwds else False

# foo(1, **{'name': 2})

# def concat(*args, sep="/"):
#     print(sep.join(args))

# concat("earth", "mars", "venus") # using default argument
# print()
# concat("earth", "mars", "venus", sep=".") # passing a new value for the keyword argument

# Unpacking arguments from a list or tuple
# print(list(range(3, 6)))  
# args = [3, 6] # creating a list
# print(list(range(args)))  # unpacking a list into positional arguments


# Unpacking arguments from a dictionary
# def parrot(voltage, state='a stiff', action='voom'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.", end=' ')
#     print("E's", state, "!")

# d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
# parrot(d)


# lamda expression
# def make_incrementor(n):
#     return lambda x: x + n

# f = make_incrementor(42)
# print(f(0))
# print(f(1))
# print(f(10))
# print(f(5))

pairs = [
    (1, 'one'),
    (2, 'two'),
    (3, 'three'),
    (5, "five"),
    (4, 'four')
    ]
pairs.sort()
# def second(pair):
#     return pair[1]
# pairs.sort(key=second)
# pairs.sort(key=lambda pair: pair[1])
# print(pairs) # [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')] pairs

# Docstring 
# def my_function():
#     """Do nothing, but document it.

#     No, really, it doesn't do anything:

#         >>> my_function()
#         >>>
#     """
#     pass

# print(my_function.__doc__)

# Annotation in python (like Typescript) But it does not raise an error when we pass a wrong type

# def f(ham: str, eggs: str = 'eggs') -> str:
#     print("Annotations:", f.__annotations__)
#     print("Arguments:", ham, eggs)
#     return ham + ' and ' + eggs

# print(f('spam'))
# print()

# def wrong_annotation(name: str) -> str:
#     print("Annotations:", wrong_annotation.__annotations__)
#     return 123

# print(wrong_annotation('name'))
# print(type(wrong_annotation('name'))) # <class 'int'>, even though the annotation says it should return a str



