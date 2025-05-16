# Membership operators = used to test whether a value or variable is found in a sequence (string, list, tuple, set, or dictionary)
# 1. in     2. not in

# word = "apple"

# letter = input("Guess a letter in the secret word: ")

# while True:
#     if letter in word:
#         print(f"There is a {letter}")
#         break
#     else:
#         print(f"{letter} was not found")
#         letter = input("Guess a letter in the secret word: ")

#####

# while True:
#     if letter not in word:
#         print(f"{letter} was not found")
#         letter = input("Guess a letter in the secret word: ")
        
#     else:
#         print(f"There is {letter}")
#         break

###############################################

# students = {"Spongebob", "Patrick", "Sandy"}

# student = input("Enter the name of a student: ")
# while True:
#     if student in students:
#         print(f"{student} is a student")
#         break
#     else:
#         print(f"{student} was not found")
#         print("Try again!")
#         student = input("Enter the name of a student: ")
        
################################################

# grades = {"Sandy": "A",
#           "Squidward": "B",
#           "Spongebob": "C",
#           "Patrick": "D",}

# student = input("Enter the name of a student: ")

# if student in grades:
#     print(f"{student}'s grade is {grades[student]}")
# else:
#     print(f"{student} was not found")

########################################

# email = "Brocode@gmail.com"

# if '@' in email and '.' in email:
#     print("valid email")
# else:
#     print("Invalid email")