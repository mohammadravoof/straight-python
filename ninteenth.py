# Class and Objects
class MyClass:
    """A simple example class"""
    i = 12345
 
    def f(self):
        return 'hello world'
 
x = MyClass()
print("Printing i: ", x.i)
print()
 
print("Printing x.f(): ", x.f()) #this is a method
print()
 
print("Printing MyClass.f(): ", MyClass.f(x)) #this is a function
 
# Difference between method and function
class Person:
    def _init_(self, name):
        self.name = name
 
    def speak(self):
        return f"Hi, I am {self.name}"
 
# Create two individual people (instances)
alice = Person("Alice")
bob = Person("Bob")
 
print(Person.speak(alice))  # <function Person.speak at 0x...>
print(bob.speak())   # <bound method Person.speak of <Person object for Alice>>
 
# x.counter = 1
# while x.counter < 10:
#     x.counter = x.counter * 2
# print("Printing x.counter: ", x.counter)
# print()
 
y = {
    'r':3.0,
    'i':-4.5
}
 
z = {
     'r':10,
     'i':20
}
 
class Complex:
    def _init_(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart
 
y = Complex(3.0, -4.5)
z = Complex(10, 20)
print("Printing y.r and y.i: ", y.r, y.i)
print("Printing z.r and z.i: ", z.r, z.i)
print()
 
# Class and instance variable
class Dog:
    kind = 'canine'         # class variable shared by all instances
    def _init_(self, name):
        self.name = name    # instance variable unique to each instance
 
d = Dog('Fido')
e = Dog('Buddy')
print("Printing d.kind: ", d.kind)                  # shared by all dogs
print()
print("Printing e.kind: ", e.kind)                  # shared by all dogs
print()
print("Printing d.name: ", d.name)                  # unique to d
print()
print("Printing e.name: ", e.name)                  # unique to e
print()
 
# Mistaken use of class variable
class Dog:
    tricks = []             # mistaken use of a class variable
    def _init_(self, name):
        self.name = name
    def add_trick(self, trick):
        self.tricks.append(trick)
 
d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print("Printing d.tricks: ", d.tricks)                # unexpectedly shared by all dogs
print()
print("Printing e.tricks: ", e.tricks)                # unexpectedly shared by all dogs
print()
 
# Correct use of class variable
class Dog:
    def _init_(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog
    def add_trick(self, trick):
        self.tricks.append(trick)
 
d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print("Printing d.tricks: ", d.tricks)
print()
print("Printing e.tricks: ", e.tricks)
print()
 
d = {
    "name": "Fido",
    "tricks": ["roll over"]
}
 
e = {
    "name": "Buddy",
    "tricks": ["play dead"]
}