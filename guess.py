import random

secret = random.randint(1, 30)
guess = 0

while guess != secret:
    guess = int(input("Guess the secret number (between 1 and 30): "))

    if guess == secret:
        print("You've guessed it - congratulations! It's number " + str(secret) + "!")
    elif guess < secret:
        print("Sorry, your guess is too small... The secret number is not " + str(guess))
    else:
        print("Sorry, your guess is too big... The secret number is not " + str(guess))
