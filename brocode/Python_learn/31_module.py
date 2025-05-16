# module = A file containing code you want to include in your program use 'import' to include a module (built-in or your own) useful to break up a large program reusable separate files

# print(help("modules"))

# import math as m
# print(m.pi)

# from math import pi
# print(pi)

# from math import e # not good practice as same named variable could appear

# import math as m

# a, b, c, d, e = 1, 2, 3, 4, 5

# print(m.e ** a)
# print(m.e ** b)
# print(m.e ** c)
# print(m.e ** d)
# print(m.e ** e)

###############################

import maths

result = maths.pi
result = maths.square(3)
result = maths.cube(3)
result = maths.circumference(3)
result = maths.area(3)

print(result)
    