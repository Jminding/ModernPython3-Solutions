import random

number = random.randint(int(input("Lower bound (inclusive): ")), int(input("Upper bound (inclusive):  ")))
guessingsussybakas = 5 
while guessingsussybakas > 0: 
  guess = int(input("Guess: ")) 
  if guess > number:
    print("Guess too high!")
  elif guess < number:
    print("Guess too low")
  else:
    print("Congrats! You got the number right! Now I'm gonna commit arson!")
    break
  guessingsussybakas -= 1  # decrement the number of tries remaining by one