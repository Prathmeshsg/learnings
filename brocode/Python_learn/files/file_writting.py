# Python writing files (.txt, .json, .csv)
txt_data = "I like pizza!"

file_path = r"D:\Data Engineer\python\brocode\files\output(txt).txt"
# r takes the string as a raw

# write method can over right all the text
# with open(file_path, "w") as file:
#     file.write(txt_data)
#     print(f"txt file '{file_path}' was created")

#####################
# exponential
# try:
#     with open(file_path, "x") as file:
#         file.write(txt_data)
#         print(f"txt file '{file_path}' was created")

# except FileExistsError:
#     print(f"txt file '{file_path}' already exists")
    
#######################
# append

# try:
#     with open(file_path, "a") as file:
#         file.write("\n" + txt_data)
#         print(f"txt file '{file_path}' was created")

# except FileExistsError:
#     print(f"txt file '{file_path}' already exists")

############################

# employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]
# try:
#     with open(file_path, "w") as file:
#         for employee in employees:
#             file.write(employee + "\n")
#         print(f"txt file '{file_path}' was created")

# except FileExistsError:
#     print(f"txt file '{file_path}' already exists")

################################
# import json

# employee = {
#     "name": "Spongebob",
#     "age": 30,
#     "job": "cook"
# }

# try:
#     with open(file_path, "w") as file:
#         json.dump(employee, file, indent=4)
#         # or
#         # for key, value in employee.items():
#         #     file.write(f"{key}: {value}\n")
#         print(f"json file '{file_path}' was created")
# except FileExistsError:
#     print("That file already exists!")

#################################

# csv (comma seperated value) file
import csv

employees = [["Name", "Age", "Job"],
             ["Spongebob", 30, "cook"],
             ["Patrick", 35, "designer"],
             ["Sandy", 32, "developer"]]

try:
    with open(file_path, "w", newline="") as file:
        writer = csv.writer(file)
        for row in employees:
            writer.writerow(row)
        print(f"csv file '{file_path}' was created")

except FileExistsError:
    print(f"txt file '{file_path}' already exists")


