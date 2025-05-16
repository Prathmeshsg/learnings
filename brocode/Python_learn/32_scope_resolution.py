# variable scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in

# Local Scope
# def func1():
#     a = 1
#     print(a)
    
# def func2():
#     b = 2
#     print(b)
    
# func1()
# func2()

###################
# Enclosed scope

# def func1():
#     a = 1
#     def func2():
#         print(a)
#     func2()
    
# func1()

#########################
# Global Scope

# def func1():
#     print(x)
    
# def func2():
#     print(x)

# x = 3
# func1()
# func2()

#######################
# Built-in
from math import e

def func1():
    print(e)
    
# e = 3
func1()