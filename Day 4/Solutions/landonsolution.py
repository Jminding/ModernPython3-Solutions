import random
number = random.randint(int(input("Lower bound (inclusive): ")), int(input("Upper bound (inclusive):  ")))

Guess = int(input("Guess a number between and including the 2 numbers: "))

while number != Guess:
    if number < Guess:
        print("Lower")
        Guess = int(input("Guess another number: "))
    elif number > Guess:
        print("Higher")
        Guess = int(input("Guess another number: "))

while number == Guess:
    print("Cheater 'you win' ")
    break