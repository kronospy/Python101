import random

def guessing_game():
    secret_number = random.randint(1, 40)
    attempts = 0

    while attempts < 3:
        guess = int(input("Guess the number between 1 to 40: "))
        attempts += 1
        if guess == secret_number:
            print("congrats you win")
            print(f"the secret number is {secret_number}")
            break
        elif guess > secret_number:
            print("too, high Try Again")
        elif guess < secret_number:
            print("too low, Try agian")

guessing_game()