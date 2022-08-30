menu = {"rice": 10.00 , "Steak" : 2.00 , "Box of 6 Cookies": 10.00, "water": 1.00  }
print(menu)

price = 0

person = input( "What would you like?" " rice, Steak, Box of 6 Cookies , water:")
if person not in menu:
        print("Invalid.") 

while True:

    if person == ("rice"):
     print("What else can we get you?") 
     print ("your price is now {price}")
    price += 10.00
    if person == ("Steak"):
        print ("What else can we get you?")
        ("your price is now {price}")
        price += 2.00
    if person == ("Box of 6 Cookies"):
        print ("What else can we get you?")
        print ("your price is now {price}")
        price += 10.00
        if person == ("water"):
         print ("What else can we get you?")
        price += 1.00
        print ("your price is now {price}")
print(f"{price}")