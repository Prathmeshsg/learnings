# Typecasting = the process of converting a variable from one data type to another
# int() str() float() bool()

name = "Bro Code"
age = 25
gpa = 3.2
is_student = True

print(type(name)) # str
print(type(age)) # int
print(type(gpa)) # float
print(type(is_student)) # bool

gpa = int(gpa) # float to int // prints 3

age = float(age) # float to int // prints 25.0

age = str(age) # int to str // prints "25"

age += 1 # Type error because age is now a string
age += "1" # concatinates like '251'

name = bool(name) # str to bool // prints True
# can give true even if single caracter exists empty string is false like ""
