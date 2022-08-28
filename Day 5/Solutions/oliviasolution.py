menu = {"Steak": 50.00, "Grape Juice": 4.00, "Tomato Soup": 8.00, "Lobster": 100.00}

print("Welcome! Take a look at our menu.")
print(menu)

order = input("May I take your order? ") 
total = float(0)
while order != "done":
    price = menu[order]
    total += price  
    print("The total price of your order is " + str(total))
    order = input("Anything else? ")

print("The total price of your order is " + str(total))
print("Enjoy your meal!")
