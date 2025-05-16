# conditional expression = A one-line shortcut for the if-else statement (ternary operator) 
# Print or assign one of Two values based on a condition
# x if condition else y

num = 5
a = 6
b = 7
age = 25
temp = 20
user_role = "admin"

# print("Positive" if num > 0 else "Negative")
# result = "Even" if num % 2 == 0 else "Odd"
# max_num = a if a > b else b
# min_num = a if a < b else b
# status = "Adult" if age >= 18 else "Child"
# weather = "Hot" if temp > 20 else "Cold"
access_level = "Full access" if user_role == "admin" else "Limited access"


print(access_level)