# Python compound interest calculator

principle = 0
rate = 0
time = 0

# while principle <= 0:
#     principle = float(input("Enter the principal amount: "))
#     if principle <= 0:
#         print("Principal amount must be greater than 0")

# while rate <= 0:
#     rate = float(input("Enter the rate of interest: "))
#     if rate <= 0:
#         print("Rate of interest must be greater than 0")

# while time <= 0:
#     time = float(input("Enter the number of years: "))
#     if time <= 0:
#         print("Number of years must be greater than 0")

# compound_interest = principle * pow(1 + rate / 100, time)

# print(f"Your compound interest is {compound_interest:,.2f}")

#######################################

# for entering 0 as well

while True:
    principle = float(input("Enter the principal amount: "))
    if principle < 0:
        print("Principal amount must be greater than 0")
    else:
        break

while True:
    rate = float(input("Enter the rate of interest: "))
    if rate < 0:
        print("Rate of interest must be greater than 0")
    else:
        break

while True:
    time = float(input("Enter the number of years: "))
    if time < 0:
        print("Number of years must be greater than 0")
    else:
        break

compound_interest = principle * pow(1 + rate / 100, time)

print(f"Your compound interest is {compound_interest:,.2f}")
