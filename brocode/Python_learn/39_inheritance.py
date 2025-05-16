# Inheritance = Allows a class to inherit attributes and methods from another class, Helps with code reusability and extensibility

#################################

# class Animal:
#     def __init__(self, name):
#         self.name = name
#         self.is_alive = True
    
#     def eat(self):
#         print(f"{self.name} is eating")
        
#     def sleep(self):
#         print(f"{self.name} is sleeping")
        
# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} is barking like Woof-Woof")
# class Cat(Animal):
#     def speak(self):
#         print(f"{self.name} is meowing like Meow-Meow")
# class Mouse(Animal):
#     def speak(self):
#         print(f"{self.name} is squeaking like Squeak-Squeak")

# dog = Dog("Scooby")
# cat = Cat("Simba")
# mouse = Mouse("Mickey")

# print(dog.name)
# print(dog.is_alive)
# dog.eat()
# dog.sleep()
# dog.speak()

######################################
######################################

# multiple inheritance = inherit from more than one paret class like C(A, B)

# multilevel inheritance = inherit from a parent which inherits from another parent like C(B) <- B(A) <- A

class Animal:
    def __init__(self, name):
        self.name = name
    def eat(self):
        print(f"{self.name} can eat")
    def sleep(self):
        print(f"{self.name} can sleep")
class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")
class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass
class Hawk(Predator):
    pass
class Fish(Prey, Predator):
    pass

rabbit = Rabbit("Bugs")
hawk = Hawk("Tony")
fish = Fish("Nemo")

fish.eat()
fish.sleep()
fish.flee()
fish.hunt()
