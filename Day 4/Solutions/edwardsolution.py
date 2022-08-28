import random

print("I am thinking of a number between 0 and 30")
guesses_left = 5

number = random.randint(1,29)

while guesses_left > 0:
    guess = int(input("Guess the number within 5 tries... "))
    if guess < number:
        print("Too low. Try again...")
        guesses_left -= 1
    elif guess > number:
        print("Too high. Try again...")
        guesses_left -= 1
    else:
        print(f"Correct! The number was {number}")
        break 

if guess != number:
    print(f"You ran out of tries, the number was {number}")
