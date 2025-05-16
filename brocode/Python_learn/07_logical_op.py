# logical operators = evaluate multiple conditions (or, and, not) 
# or = at least one condition must be True
# and = all conditions must True
# not = reverse the condition (not False, not True)

###############################

# temp = -5
# is_raining = False

# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is still active")

################################################


temp = 20
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is hot outside")
    print("It is sunny")
elif temp <= 0 and is_sunny:
    print("It is cold outside")
    print("It is sunny")
elif 28 > temp > 0 and is_sunny:    
    print("It is hot outside")
    print("It is sunny")
elif temp >= 28 and not is_sunny:
    print("It is hot outside")
    print("It is Cloudy")
elif temp <= 0 and not is_sunny:
    print("It is cold outside")
    print("It is Cloudy")
elif 28 > temp > 0 and not is_sunny:    
    print("It is hot outside")
    print("It is Cloudy")
else:
    print("It is not hot outside")