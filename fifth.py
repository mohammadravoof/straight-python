# function
def fib(n): # write Fibonacci series less than n
    """Print a Fibonacci series less than n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b

# Assign the function to a variable, Every time we re run the function address changes because it creates a new function object in memory
print("Address of the function fib:", fib, " This is the hexadecimal base 16, thats why 0x at the start")
print("Address of the function fib:", id(fib), " This is the number")
print("Both are equal")
print(id(fib), " This is number -> hexadecimal base 16")
print(hex(id(fib)), " This is hexadecimal base 16 -> number")

f = fib
print("Address of the variable f:", id(f))

# function always returns a value, if we don't return anything it will return None
returned_value = f(10)
print("\nReturned value of the function f:", returned_value)



# Default argument values
i = 5

def f(arg=i):
    print(arg)

i = 6
# f()  # prints 5 because the default value is evaluated at the time of function definition, not at the time of function call

def f(a, L=[]):
    L.append(a)
    return L

# print(f(1)) 
# print(f(2))
# print(f(3)) # prints [1, 2, 3] because the default value for L is evaluated only once when the function is defined,
            #so the same list is used for all calls to f.

def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

# print(f(1))
# print(f(2))
# print(f(3))

# keyword arguments
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

# parrot(1000)                                          # 1 positional argument
# parrot(voltage=1000)                                  # 1 keyword argument
# parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
# parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
# parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
# parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

# parrot()                     # required argument missing
# parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
# parrot(110, voltage=220)     # duplicate value for the same argument
# parrot(actor='John Cleese')  # unknown keyword argument

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

# cheeseshop("Limburger", "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            shopkeeper="Michael Palin",
#            client="John Cleese",
#            sketch="Cheese Shop Sketch")

# Special parameters
def standard_arg(arg):
    print(arg)

def pos_only_arg(arg, /):
    print(arg)

def kwd_only_arg(*, arg):
    print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

# print("Standard argument:")
# standard_arg(2)
# standard_arg(arg=2)
# print()

# print("Positional only argument:")
# pos_only_arg(1)
# pos_only_arg(arg=1)  # This will raise a TypeError
# print()

# print("Keyword only argument:")
# kwd_only_arg(arg=3)
# kwd_only_arg(3)  # This will raise a TypeError
# print()

# print("Combined example:")
# combined_example(1, standard=2, kwd_only=3)
# combined_example(1, 2, kwd_only=3)
# combined_example(1, 2, 3)  # This will raise a TypeError
# combined_example(pos_only=1, standard=2, kwd_only=3)  # This will raise a TypeError

