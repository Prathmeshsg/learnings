# Python reading files (.txt, .json, .csv)

file_path = r"D:\Data Engineer\python\brocode\files\output(csv).txt"
# change the name accordingly

# try:
#     with open(file_path, "r") as file:
#         content = file.read()
#         print(content)
# except FileNotFoundError:
#     print(f"txt file '{file_path}' does not exist")
# except PermissionError:
#     print(f"txt file '{file_path}' does not have permission to read")
    
#########################
# json
# import json


# try:
#     with open(file_path, "r") as file:
#         content = json.load(file)
#         print(content["job"])
# except FileNotFoundError:
#     print(f"txt file '{file_path}' does not exist")
# except PermissionError:
#     print(f"txt file '{file_path}' does not have permission to read")

##############################

#csv
import csv


try:
    with open(file_path, "r") as file:
        content = csv.reader(file)
        for line in content:
            print(line[0])
except FileNotFoundError:
    print(f"txt file '{file_path}' does not exist")
except PermissionError:
    print(f"txt file '{file_path}' does not have permission to read")