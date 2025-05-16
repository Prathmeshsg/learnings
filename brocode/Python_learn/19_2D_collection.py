# groceries = [["apple", "banana", "coconut"], 
#              ["tomato", "potato", "celery", "carrot"],
#               ["chicken", "fish", "turkey"]]

# print(groceries[1][3])
###############
# fruits = ["apple", "banana", "banana", "coconut"]
# vegetables = ["tomato", "potato", "celery", "carrot"]
# meats = ["chicken", "fish", "turkey"]

# groceries = [fruits, vegetables, meats]

# for collection in groceries:
#     for food in collection:
#         print(food, end=" ")
#     print()

######################################################

# 2D phone keypad

num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*",0,"#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()

