# PROJECT: Menu Total

# A menu consists of a name of an item and its price.
# For example:
# menu = {"Steak": 90.00, "Cookies": 4.00, "Pumpkin Pie": 8.00, "Lamb Chop": 100.00}

# For this project, you'll:
# 1. Create a menu with any food items of your choice using dictionaries!
# 2. Take input from the user as to what their order is
#       a. For this, keep taking the user's input until they say "Done".
#       b. (Hint: use a while loop!)
# 3. Tell the user what their total is

# If you have any questions, don't hesistate to let me know!
# This assignment is due on Sunday, 8/26/22, at 5 pm.

menu = {"burger":5.00, "fries":3.50, "drink":1.00}
order = {"burger":0, "fries":0, "drink":0}

bcount = 0
fcount = 0

dcount = 0

while True:
    print("Please make a selection:")
    print("1. Burger = $5.00")
    print("2. Fries  = $3.50")
    print("3. Drink  = $1.00")
    print("4. Quit")

    choice = int(input('Please order: '))

    if choice == 1:
        amount = int(input("Enter number of Burgers: "))
        bcount += amount
    elif choice == 2:
        amount = int(input("Enter number of Fries: "))
        fcount += amount
    elif choice == 3:
        amount = int(input("Enter number of Drinks: "))
        dcount += amount
    elif choice == 4:
        sub = (bcount * 5.00) + (fcount * 3.50) + (dcount * 1.00)
        tax = sub * 0.075
        total = sub + tax

        print('Number of Burgers: {0}'.format(bcount))
        print('Number of Fries: {0}'.format(fcount))
        print('Number of Drinks: {0}'.format(dcount))
        print('Subtotal: {:0.2f}'.format(sub))
        print('Tax: {:0.2f}'.format(tax))
        print('Total: {:0.2f}'.format(total))
        break