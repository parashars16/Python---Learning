item = input("What item do you like to buy?:")
price = float(input("What is the price?:"))
quantity = int(input("How many would you like?"))

total = price*quantity

print(f"you have bought {quantity} * {item}")
print(f"your total is ${round(total , 2)}")

