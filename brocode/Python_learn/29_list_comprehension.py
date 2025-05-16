# List comprehension = A concise way to create lists in Python Compact and easier to read than traditional loops 
#  [expression for value in iterable if condition]

# doubles = []
# for x in range(1, 11):
#     doubles.append(x * 2)
    
# print(doubles)

# doubles = [x * 2 for x in range(1, 11)]
# triples = [y * 3 for y in range(1, 11)]
# squares = [z * z for z in range(1, 11)]
# print(doubles)
# print(triples)
# print(squares)

########################################

# fruits = ["apple", "orange", "banana", "coconut"]
# fruitss = [fruit.upper() for fruit in fruits]
# print(fruitss)

###########################################33
# conditions
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# odd = [x for x in numbers if x % 2 != 0]
# even = [x for x in numbers if x % 2 == 0]
# print(odd)
# print(even)

# numbers = [1, -2, 3, -4, 5, -6]

# positive_num = [num for num in numbers if num >= 0]
# negative_num = [num for num in numbers if num <= 0]
# print(positive_num)
# print(negative_num)

###################

# grades = [85, 42, 79, 90, 56, 61, 30]

# passing_grades = [grade for grade in grades if grade >= 60]
# print(passing_grades)
