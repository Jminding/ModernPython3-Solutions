menu = {"chicken nuggets":3.75, "biscuit":0.75, "mashed potatoes":2.00, "chicken wings":6.00}

order = input("Hello! Welcome to McDaniels! What Would You Like To Order?")
print (menu)
total = 0.00
while order != "done":
    price = menu[order]
    total += price  
    print("The total price of your order is " + str(total))
    order = input("Anything else? ")

print("The total price of your order is " + str(total))
print("Thank You for Ordering From McDaniels! Enjoy your meal!")
