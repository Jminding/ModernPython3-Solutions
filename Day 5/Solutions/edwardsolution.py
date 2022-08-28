print("Welcome to my restaurant!")
print("Please view the menu below:")

# restuarant menu
menu = {"Cheese Garlic Bread": 2.95, 
"Stuffed Mushrooms": 5.05, 
"Lobster Platter with Smooked Salmon and Scampi Shrimp": 50.51,
"Sirloin Steak with Mashed Potatoes and Shrimp Skewers": 80.35, 
"Seafood and Vegetable Bowl": 30.15, 
"Brownie Bite with Scoops of Chocolate Ice Cream": 12.17, 
"Vanilla Ice Cream Fruit Bowl": 10.49 }

print(menu)

print("Type 'done' to finish your order")

customer_progress = "Still ordering"
cost = 0
total_price = 0

#loop that continues when the customer is stil order
while customer_progress == "Still ordering":
    
    customer_purchased = input("What would you like to order(1 item at a time)? ")
    
    if customer_purchased in menu:
        
        cost = menu[customer_purchased]
        print(f"Great! That will be ${cost}")    
        total_price += cost
        continue    
    
    elif customer_purchased == "done":
        break
    
    else:  
       
        print("Item not in menu. Try again...")
        continue

print(f"Your total bill is ${total_price}.")
print("Thank you for stopping by!")