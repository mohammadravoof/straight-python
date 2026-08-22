# Scopes and Namespace
# Built-in
# Global
# Local
# enclosed
 
# food = "biriyani" # Global
 
# def dish():
#     food = "chapati" # enclosed
#     def plate():
#         global food
#         food = "vada" # local
#         print("Local food: ", food)
#     plate()
#     print("Enclosed food: ", food)
# dish()
# print("Global food: ", food)
 
# # Built in variable 
# # True = True
# print("Built in value: ", True)
 
# spam = "global spam"
 
def scope_test():
 
    def do_local():
        spam = "local spam"
 
    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"
 
    def do_global():
        global spam
        spam = "global spam"
 
    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)
 
scope_test()
print("In global scope:", spam)