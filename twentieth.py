# Attribute look up - Inheritance, Multiple Inheritance
class Building:
    purpose = 'Commercial'
 
class House:
    region = 'middle'
 
class Warehouse(House, Building):
   purpose = 'storage'
   region = 'west'
 
w1 = Warehouse()
print(w1.purpose, w1.region)
print()
 
w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)
print()
 
# calling the other method inside the class
 
def add(self, x):
        self.data.append(x)
 
class Bag:
    def _init_(self):
        self.data = []
 
    add = add # Assign the outside function to a class attribute
 
    def addtwice(self, x):
        self.add(x)
        self.add(x)
 
b1 = Bag()
b1.add(1)
print(b1.data)
print()
 
b2 = Bag()
b2.addtwice(1)
print(b2.data)
print()
 
class Mapping:
    def _init_(self, iterable):
        self.items_list = []
        self.__update(iterable)
 
    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)
 
    __update = update   # private reference to original update()
 
 
class MappingSubclass(Mapping):
 
    def update(self, keys, values):
        for item in zip(keys, values):
            self.items_list.append(item)
 
 
# -------------------------
# Create objects
# -------------------------
 
m1 = Mapping([1, 2, 3])
m2 = MappingSubclass([1, 2, 3])
 
print("m1:", m1.items_list)
print("m2:", m2.items_list)
 
 
# Call subclass's update()
m2.update(["a", "b"], [10, 20])
 
print("m2 after update():", m2.items_list)