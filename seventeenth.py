# syntax error
# while True print('Hello world')
 
# exceptions - ZeroDivisionError, NameError, TypeError
# 10 * (1/0)
 
# 4 + spam*3
 
# '2' + 2
 
 
# # Handling exceptions
# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")
 
 
# Exception handling Inheritance
# Here Exception <- B <- C <- D
# Like Animal <- Mammal <- Dog
class B(Exception):
    pass
 
class C(B):
    pass
 
class D(C):
    pass
 
for cls in [B, C, D]:
    try:
        raise cls()
    except B:
        print("B")
    except C:
        print("C")
    except D:
        print("D")