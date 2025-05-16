# object = A "bundle" of related attributes (variables) and methods (functions) 
# Ex. phone, cup, book
# You need a "class" to create many objects

# class = (blueprint) used to design the structure and layout of an object

#####################

from car import Car

car1 = Car("Mercedes", 2025, "black", False)
print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)
car1.drive()
car1.stop()
car1.describe()

# car2 = Car("BMW", 2026, "blue", True)
# print(car2.model)
# print(car2.year)
# print(car2.color)
# print(car2.for_sale)
