# Python file detection

import os
# "D:\Users\Prathmesh\Desktop\on desktop\test.txt" this won't run cause of t(it takes as tab)
file_path = "D:\\Users\\Prathmesh\\Desktop\\on desktop\\test.txt"
# "D:/Users/Prathmesh/Desktop/on desktop/test.txt"
# or "D:\\Users\\Prathmesh\\Desktop\\on desktop\\test.txt"


if os.path.exists(file_path):
    print(f"The location '{file_path}' do exists")
    
    if os.path.isfile(file_path):
        print("That is a file")
    elif os.path.isdir(file_path):
        print("That is a directory")
else:
    print(f"The location '{file_path}' does not exist")
    