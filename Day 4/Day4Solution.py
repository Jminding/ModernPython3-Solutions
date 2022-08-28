import random, os, platform, time

lower, upper = None, None
while True:
    try:
        lower, upper = int(input("Lower bound (inclusive): ")), int(input("Upper bound (inclusive):  "))
        if lower > upper:
            if platform.system() == "Windows":
                os.system('cls')
            else:
                os.system('clear')
            print("Invalid range, try again")
            time.sleep(0.5)
            continue
        break
    except ValueError:
        if platform.system() == "Windows":
            os.system('cls')
        else:
            os.system('clear')
        print("Invalid range, try again")
        time.sleep(0.5)

number = random.randint(lower, upper)
guess = None
num_tries = 0
while guess != number:
    num_tries += 1
    print()
    print(f"Range: {lower} ~ {upper}")
    try:
        guess = int(input("Guess: "))
    except ValueError:
        print("That's an invalid guess, try again")
        num_tries -= 1  # nullify this try because it doesn't count
        continue
    if guess > number:
        print(f"{guess} is higher than the number.")
    elif guess < number:
        print(f"{guess} is lower than the number.")
    else:
        print(f"You got it! The number was {number}! It took you {num_tries} attempt(s) to figure the number out.")
