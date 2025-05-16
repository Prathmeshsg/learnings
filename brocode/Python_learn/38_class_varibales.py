# class variables = Shared among all instances of a class, Defined outside the constructor, Allow you to share data among all objects created from that class

class Student:
    class_year = 2024
    num_students = 0
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1
        
student1 = Student("Spongebob", 30)
student2 = Student("Patrick",35)
student3 = Student("Sandy", 32)

# print(student1.name)
# print(student1.age)
# # always write as below code don't write like :- print(student1.class_year)
# print(Student.num_students)
# print(Student.class_year)

print(f"My graduaating class of {Student.class_year} has {Student.num_students} students")
print(student1.name)
print(student2.name)
print(student3.name)