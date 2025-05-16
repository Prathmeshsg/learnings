# @property = Decorator used to define a method as a property (It can be accessed like an attribute)
# Benefit : Add additional logic when read, write, or delete attributes
# Gives you getter, setter, and deleter method

class Rectangle:
    def __init__(self, width, height):
        self._width = width # _width is a private attribute
        self._height = height # _height is a private attribute
        # private attributes only accessible in this class
        
    @property
    def width(self):
        return f"{self._width}cm"
    @property
    def height(self):
        return f"{self._height}cm"
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than 0")
            
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than 0")
            
    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")
    
    @height.deleter
    def height(self):
        del self._height
        print("Height has been deleted")
    
rectangle = Rectangle(10, 20)
rectangle.width = 5
rectangle.height = 15

# del rectangle.width
# del rectangle.height

print(rectangle.width)
print(rectangle.height)