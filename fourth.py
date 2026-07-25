# # match statement (switch case but without using break)
# def http_error(status):
#     match status:
#         case 400:                # you can also combine multiple cases with | ex: case 400 | 401 | 402:, case 400 or 401 or 402:
#             return "Bad request"
#         case 404:
#             return "Not found"
#         case 418:
#             return "I'm a teapot"
#         case _:
#             return "Something's wrong with the internet"

# print(http_error(323))

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# def where_is(point):
#     match point:
#         case Point(x=0, y=0):
#             print("Origin")
#         case Point(x=0, y=y):
#             print(f"Y={y}")
#         case Point(x=x, y=0):
#             print(f"X={x}")
#         case Point(x=x, y=y):
#             print(f"X={x}, Y={y}")
#         case _:
#             print("Not a point")

# where_is(Point(1, 2))
# where_is(Point(1, y=2))
# where_is(Point(x=1, y=2))
# where_is(Point(y=2, x=1))

# # function
# def fib(n):    # write Fibonacci series less than n
#     """Print a Fibonacci series less than n."""
#     a, b = 0, 1
#     while a < n:
#         print(a, end=' ')
#         a, b = b, a+b
#     print()

# # Now call the function we just defined:
# fib(2000)


#         # Iteration 1:
#         # Before: a = 0, b = 1
#         # Condition: 0 < 2000 -> True
#         # Prints: 0
#         # a = old b = 1
#         # b = old a + old b = 0 + 1 = 1
#         # After: a = 1, b = 1

#         # Iteration 2:
#         # Before: a = 1, b = 1
#         # Condition: 1 < 2000 -> True
#         # Prints: 1
#         # a = old b = 1
#         # b = old a + old b = 1 + 1 = 2
#         # After: a = 1, b = 2

#         # Iteration 3:
#         # Before: a = 1, b = 2
#         # Condition: 1 < 2000 -> True
#         # Prints: 1
#         # a = old b = 2
#         # b = old a + old b = 1 + 2 = 3
#         # After: a = 2, b = 3

#         # ... iterations continue ...

#         # Second-last iteration (Iteration 17):
#         # Before: a = 987, b = 1597
#         # Condition: 987 < 2000 -> True
#         # Prints: 987
#         # a = old b = 1597
#         # b = old a + old b = 987 + 1597 = 2584
#         # After: a = 1597, b = 2584

#         # Last iteration (Iteration 18):
#         # Before: a = 1597, b = 2584
#         # Condition: 1597 < 2000 -> True
#         # Prints: 1597
#         # a = old b = 2584
#         # b = old a + old b = 1597 + 2584 = 4181
#         # After: a = 2584, b = 4181

#         # Next while-loop check:
#         # Condition: 2584 < 2000 -> False
#         # Therefore, the while loop ends.
#         # 2584 is NOT printed because the condition is False.