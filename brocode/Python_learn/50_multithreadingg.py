# Multithreading = Used to perform multiple tasks concurrently (multitasking)
# Good for I/O bound tasks like reading files or fetching data from APIs
# threading.Thread(target = my_function)

import threading
import time

def walk_dog(first, last):
    time.sleep(6)
    print(f"You finish walking the {first} {last} dog")
    
def take_out_trash():
    time.sleep(2)
    print("You finish taking out the trash")
    
def get_mail():
    time.sleep(4)
    print("You finish getting mail")
    
# walk_dog()
# take_out_trash()
# get_mail()

task1 = threading.Thread(target=walk_dog, args=("Scooby", "Doo")) # remember to pass , after args
task1.start()

task2 = threading.Thread(target=take_out_trash)
task2.start()

task3 = threading.Thread(target=get_mail)
task3.start()

task1.join()
task2.join()
task3.join()
print("All tasks have been completed")