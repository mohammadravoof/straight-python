# Odds and Ends
# Instead of writing a lot of boiler plate code we can use dataclass
# from dataclasses import dataclass
 
# # @dataclass
# # class Employee:
# #     name: str
# #     dept: str
# #     salary: int
 
# class Employee:
#     def _init_(self, name, dept, salary):
#         self.name = name
#         self.dept = dept
#         self.salary = salary
 
# john = Employee('john', 'computer lab', 1000)
# print(john.dept)
# print()
# print(john.salary)
# print()
 
# Method objects
# class Employee:
#     def work(self):
#         print("Employee is working")
 
# john = Employee()
 
# m = john.work
 
 
# print("Method:")
# print(m)
 
# print("\nObject stored inside method:")
# print(m._self_)
 
# print("\nIs it john?")
# print(m._self_ is john)
 
# print("\nFunction stored inside method:")
# print(m._func_)
 
# print("\nIs it Employee.work?")
# print(m._func_ is Employee.work)
 
 
# print("\n--- Calling different ways ---")
 
# john.work()
 
# m()
 
# Employee.work(john)
 
# m._func_(m._self_)
 
# john.work._func_(john.work._self_)
 
# # iterators
# for element in [1, 2, 3]:
#     print(element)
# print()
# for element in (1, 2, 3):
#     print(element)
# print()
# dicti = {'one':1, 'two':2}
# for key, value in dicti.items():
#     print(key, value)
# print()
# for char in "123":
#     print(char)
# print()
# for line in open("myfile.txt"):
#     print(line, end='')
 
# # How does it work under the hood
# # lets take the example of for char in "123"
# char = "123"
# it = iter(char)
# print(it)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print()
 
# class Reverse:
#     """Iterator for looping over a sequence backwards."""
#     def _init_(self, data):
#         self.data = data
#         self.index = len(data)
 
#     def _iter_(self):
#         return self
 
#     def _next_(self):
#         if self.index == 0:
#             raise StopIteration
#         self.index = self.index - 1
#         return self.data[self.index]
 
# rev = Reverse('spam')
 
# for char in rev:
#     print(char)
 
 
# Generator Function
# def reverse(data):
#     for index in range(len(data)-1, -1, -1):
#         yield data[index]
 
# for char in reverse("spam"):
#     print(char)
 
# # 2. Generator expression
# data = "spam"
# g = (data[index] for index in range(len(data) - 1, -1, -1))
 
# for char in g:
#     print(char)
 
# # 3. Python's built-in iterator
# r = reversed("spam")
 
# for char in r:
#     print(char)
 
# # List comprehension vs Generator expression
# # list comprehension
# numbers = [x * 2 for x in range(5)]
 
# for x in numbers:
#     print(x)
 
# print("---")
 
# for x in numbers:
#     print(x)
 
# # generator expression
# numbers = (x * 2 for x in range(5))
 
# for x in numbers:
#     print(x)
 
# print("---")
 
# for x in numbers:
#     print(x)