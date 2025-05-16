# if __name__ == '__main__': (this script can be imported OR run standalone), Function and classes in this module can be reused without the main block of code executing
# Good practice -> 
# (code is modular,
# helps readability,
# avoid unintended execution)

# ex. library = import library for functionality when running library directly, display a help page

def favorite_food(food):
    print(f"Your favorite food is {food}")
def main():
    print("This is script1")
    favorite_food("Pizza")
    print("Thank You!")
    
if __name__ == '__main__':
    main()