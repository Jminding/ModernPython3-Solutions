import random
secret_number = random.randint(1, 20)
while True:
    guess = int(input("Guess the secret number: "))
    if secret_number > guess:
        print("The secret number is higher then your current guess!")
    elif secret_number < guess:
        print("The secret number is lower then your current guess!")
    else:
        print("That the secret number! You win! " + str(secret_number) + " was the secret number!")
        print(str(secret_number) + " was the secret number!")
        break
print("Thankyou for playing!")

