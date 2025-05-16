# friends = 10

# friends += 1 or friends = friends + 1
# friends -= 2 or friends = friends - 2
# friends *= 2 or friends = friends * 2
# friends /= 2 or friends = friends / 2
# friends **= 2 or friends = friends ** 2

# remainder = friends % 2
# print(remainder)

#########################################

# x = 3.14
# y = 4
# z = 5

# result = round(x) # 3
# result = abs(y)  # 4 - (absolute value)
# result = pow(4, 3) # 64
# result = max(x, y, z) # 5
# result = min(x, y, z) # 3.14

##########################################

# import math

# x = 9.1

# # print(math.pi)
# # print(math.e) # exponential constant
# result = math.sqrt(x) # 3.0
# result = math.ceil(x) # 10
# result = math.floor(x) # 9

#######################################

# import math

# radius = float(input("Enter the radius: "))

# circumference = 2 * math.pi * radius
# area = math.pi * radius ** 2

# print(f"The circumference is: {round(circumference, 2)}")
# print(f"The area is: {round(area, 2)}")

########################################
# hypotenous right angle triangle
import math


a = float(input("Enter side A: "))
b = float(input("Enter side B: "))
c = pow(a, 2) + pow(b, 2)

c = math.sqrt(c)

print(f"The hypotenous is(side C): {c}")



