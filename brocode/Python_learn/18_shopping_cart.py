# shopping cart program

foods = []
prices = []
total = 0

while True:
    food = input("Enter food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        foods.append(food)
        price = float(input(f"Enter the price of {food}: "))
        prices.append(price)
        
print("----- YOUR CART -----")

# for food in foods:
#     print(food, end=" ")
    
# for price in prices:
#     total += price
#     print(f"${price:,.2f}", end=" ")

###########

# for x in range(len(foods)):
#     print(foods[x], f": ${prices[x]:,.2f}")
#     total += prices[x]

##############

for x in zip(foods, prices):
    print(x[0], f": ${x[1]:,.2f}")
    total += x[1]   
    

    
print(f"\nTotal: ${total:,.2f}")