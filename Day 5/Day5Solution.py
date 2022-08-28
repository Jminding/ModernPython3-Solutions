import os, platform

if platform.system() == "Windows":
    os.system('cls')
else:
    os.system('clear')

menu = {
    "Salad": 10.00,
    "Steak": 50.00,
    "Porkchop": 35.00,
    "Grilled Chicken": 30.00,
    "Spaghetti": 20.00,
    "Ice Cream": 5.00,
    "Chocolate Mousse": 15.00,
    "Creme Brulee": 12.00
}

menu_items = list(menu.keys())

print("   Dinner Menu")

for i in range(len(menu_items)):
    print(f"{i + 1}. {menu_items[i]}: ${menu[menu_items[i]]:.2f}")

print()

total_price = 0.00

while True:
    order = input("Add an item to your order (say \"done\" if your order is complete): ").title()
    if order.lower() == "done":
        break
    if order.lower() == "chicken":
        order = "grilled chicken".title()
    if order not in menu_items:
        print("Sorry, we don't have that on our menu. Please order something else.")
        print()
        continue
    print(f"The price of that item is ${menu[order]:.2f}.")
    total_price += menu[order]
    print()

print(f"Your total is ${total_price:.2f}.")
