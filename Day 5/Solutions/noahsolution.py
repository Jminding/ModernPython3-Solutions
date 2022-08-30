menu = {"Steak": 20.00 , "Water": 1.00}
choices = list(menu.keys())
print(" The food list is ")
for i in range(len(choices)):
    print(f"{i + 1}. {choices[i]}: ${menu[choices[i]]:.2f}")
price = 0.00
while True:
    order = input("Buy stuff (say done if your order is well, done): ").title()
    if order.lower() == "done":
        break
    if order not in choices:
        print("We do not have that")
        continue
    print(f"The price of that item is ${menu[order]:.2f}.")
    price += menu[order]
print(f"Your total is ${price:.2f}.")