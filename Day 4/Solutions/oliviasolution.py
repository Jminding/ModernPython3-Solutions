import random
number = random.randint(int(input("Lower bound (inclusive): ")), int(input("Upper bound (inclusive):  ")))

guess = int(input("Guess the number: "))


while guess != number:
    if guess > number:
        print("Your guess is higher")
    if guess < number:
        print("Your guess is lower")
    
    guess = int(input("Guess the number: "))


print("You win!")
print("The answer is "+str(number))