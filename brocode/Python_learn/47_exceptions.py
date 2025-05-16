# Exception =  An event that interrupts the flow of a program 
# (ZeroDivisionError, TypeError, ValueError)
# 1.try, 2.except, 3.finally

# try:
#     # try some code
# except Exception:
#     # Handle the exception
# else:
#     # code to run if there is no exception
# finally:
#     # code to run no matter what

############################

try:
    number = int(input("Enter a number: "))
    print(1/ number)
except ZeroDivisionError:
    print("You can't divide by zero IDIOT!")
except ValueError:
    print("Enter only numbers plz!")
else:
    print("No exception was raised")
finally:
    print("This will always run")