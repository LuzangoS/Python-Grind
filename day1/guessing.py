import random

secret = random.randint(1, 20)
attempts = 0

while attempts < 5:
    guess = int(input("Guess a number between 1 and 20: "))
    attempts += 1

    if guess < secret:
        print("Too low! Try again.")
    elif guess > secret:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {secret} in {attempts} attempts.")
        break

else:
    print(f"Sorry, you've used all your attempts. The secret number was {secret}.")