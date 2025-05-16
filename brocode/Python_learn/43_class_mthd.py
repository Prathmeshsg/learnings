# Class methods = Allow operations related to the class itself
# Take (cls{refers to class}) as the first parameter, which represents the class itself.

# Instance methods = Best for operations on instances of the class (objects)
# Static methods = Best for utility functions that do not need access to class data
# Class methods = Best for class-level data or require access to the class itself

class Student:
    count = 0
    total_gpa = 0
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.count += 1
        Student.total_gpa += gpa
    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name} has a {self.gpa} GPA"
    
    # CLASS METHOD
    @classmethod
    def get_count(cls):
        return f"Total number of students: {cls.count}"
    
    @classmethod
    def get_average(cls):
        return f"Average GPA: {cls.total_gpa / cls.count:.2f}"
    
student1 = Student("Spongebob", 3.2)
student2 = Student("Patrick", 2.0)
student3 = Student("Sandy", 4.0)
print(Student.get_count())
print(Student.get_average())