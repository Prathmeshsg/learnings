# Temperature converter program

unit = input("Is this temperature in Celsius or Fahrenheit?(C or F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = temp * 1.8 + 32 # or (9 * temp) / 5 + 32
    print(f"The temperature in Fahrenheit is {round(temp, 1)}°F") # for ° use alt + 0176
elif unit == "F":
    temp = (temp - 32) / 1.8 # or (temp - 32) * 5 / 9
    print(f"The temperature is {round(temp, 1)}°C")
else:
    print(f"{unit} is Invalid unit")