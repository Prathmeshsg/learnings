# super() = Function used in a child class to call methods from a parent class (superclass). 
# Allows you to extend the functionality of the inherited methods

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled
    
    def describe(self):
        print(f"It is {self.color} and {'filled' if self.is_filled else 'not filled'}")

class Circle(Shape):
    def __init__(self,color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius
        
    def describe(self):
        print(f"It is a circle with an area of {3.14 * self.radius ** 2}cm^2")
        super().describe()

class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width
        
    def describe(self):
        print(f"It is a square with an area of {self.width ** 2}cm^2")
        super().describe()
        
class Triangle(Shape):
    def __init__(self, color, is_filled, width, height):
        super().__init__(color, is_filled)
        self.width = width
        self.height = height
        
    def describe(self):
        print(f"It is a triangle with an area of {self.width * self.height / 2}cm^2")
        super().describe()
        
circle = Circle("Red", True, 5)
# # Or can write like Circle(color= "red", is_filled= True, radius= 5)
# print(circle.color)
# print(circle.is_filled)
# print(circle.radius)

# circle.describe()

square = Square("Green", False, 6)

# print(square.color)
# print(square.is_filled)
# print(square.width)
# square.describe()

triangle = Triangle("Blue", True, 7, 8)

# print(triangle.color)
# print(triangle.is_filled)
# print(triangle.width)
# print(triangle.height)

# triangle.describe()