# import datetime

# date = datetime.date(2025, 1, 2)
# # print(date)

# today = datetime.date.today()
# # print(today)


# time = datetime.time(12, 30, 0)
# # print(time)

# # datetime
# now = datetime.datetime.now()

# now = now.strftime("%d-%m-%Y--%H:%M:%S-%p")
# # print(now)


# target_datetime = datetime.datetime(2026, 1, 2, 12, 30, 0)
# current_datetime = datetime.datetime.now()

# if target_datetime < current_datetime:
#     print("Target datetime has passed")
# else:
#     print("Target datetime has not passed")
    

######################################
#####################################

# Python Alarm Clock

import time
import datetime
import pygame

def set_alaram(alarm_time):
    print(f"Alarm set for {alarm_time}")
    sound_file = "my_music.mp3"
    is_running = True
    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        
        time.sleep(1)
        if current_time == alarm_time:
            print("WAKE UP!")
            # pygame.mixer.init()
            # pygame.mixer.music.load(sound_file)
            # pygame.mixer.music.play()
            # while pygame.mixer.music.get_busy():
            #     time.sleep(1)
            is_running = False
    
    
if __name__ == "__main__":
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alaram(alarm_time)


