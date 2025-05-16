# Polymorphism = Greek word that means to "have many forms of faces"
# Poly = Many, Morph = Form

# Two ways to Achieve Polymorphism
# 1. Inheritance = An object could be treated of the same type as a parent class
# 2. "Duck Typing" = Object must have necessary attributes or methods

from abc import ABC, abstractmethod

class Shape:
    
    @abstractmethod
    def area(self):
        pass
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius ** 2
class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
        
    def area(self):
        return 0.5 * self.base * self.height
    
class Pizza(Circle):
    def __init__(self,topping, radius):
        super().__init__(radius)
        self.topping = topping
    
shapes = [Circle(4), Square(5), Triangle(6, 7), Pizza("pepperoni", 8)]

# for shape in shapes:
#     print(f"{shape.area()} cm²")
    
#########################################
#########################################

# "Duck Typing" = Another way to achieve polymorphism besides Inheritance , Object must have the minimum necessary attributes/methods 
# "If it looks like a duck and quacks like a duck, it must be a duck."

class Animal:
    alive = True
    
class Dog(Animal):
    def speak(self):
        print("Bark")
        
class Cat(Animal):
    def speak(self):
        print("Meow")
    
class Car:
    alive = False
    def speak(self):
        print("Honk")
        
animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)
