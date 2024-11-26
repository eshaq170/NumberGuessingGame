import random

def guess_number(target, guess):
    if guess < target:
        return "Too low!"
    elif guess > target:
        return "Too high!"
    else:
        return "Correct!"

def play_game():
    target = random.randint(1, 100)
    print("Guess a number between 1 and 100.")
    while True:
        try:
            guess = int(input("Enter your guess: "))
            result = guess_number(target, guess)
            print(result)
            if result == "Correct!":
                break
        except ValueError:
            print("Please enter a valid number.")
