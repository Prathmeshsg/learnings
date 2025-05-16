# name = input("Enter your full name: ")
# phone_num = input("Enter your phone number: ")

# result = len(name)
# result = name.find(" ")
# result = name.rfind("o")
# name = name.capitalize()
# name = name.upper()
# name = name.lower()
# result = name.isdigit()
# result = name.isalpha() # must not contain any space or it will return false
# result = name.isalnum()
# result = phone_num.count("9")


# result = phone_num.replace("9", "0")
# print(result)

#########################################

# validate user input exercise

# 1. username is no more than 12 characters
# 2. username must not contain any space
# 3. username must not contain any numbers or digits

username = input("Enter your username: ")

if len(username) > 12:
    print("Username is too long!")
elif username.find(" ") != -1:
    print("Username cannot contain any space!")
elif username.isdigit():
    print("Username cannot contain any numbers!")
else:
    print(f"Welcome {username}!")

