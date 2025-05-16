# Static methods = A method that belong to a class rather than any object from that class (instance), Usuall used for general utility functions

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        
    def get_info(self):
        return f"{self.name} is a {self.position}"
    
    @staticmethod # general utility function/method
    def is_valid_position(position):
        valid_position = ["manager", "developer", "designer"]
        return position in valid_position
    
employee1 = Employee("John", "manager")
employee2 = Employee("Jane", "developer")
employee3 = Employee("Patrick", "designer")

print(employee1.get_info())
print(employee2.get_info())
print(employee3.get_info())

    
# print(Employee.is_valid_position("scientist"))