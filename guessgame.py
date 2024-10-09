import random

print("Welcome to the Number Guessing Game!")
# print("I'm thinking of a number between 1 and 100")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")

easy = 10
hard = 5
attempts = 10

if level == "hard":
    attempts = hard
elif level == "easy":
    attempts = easy

print(f"I'm thinking of a number between 1 and 100.")
r_num = random.randint(1, 100)

while attempts > 0:
    print(f"You have {attempts} attempt{'s' if attempts > 1 else ''} remaining to guess the number.")
    guess_value = int(input("Make a guess: "))
    attempts -= 1

    if guess_value == r_num:
        print(f"You got it! The answer was {r_num}.")
        attempts = 0
    elif guess_value < r_num and attempts > 0:
        print("Too low.")
    elif guess_value > r_num and attempts > 0:
        print("Too high.")
    elif attempts <= 0:
        print(f"You've run out of guesses, you lose.")
        attempts = 0
    else:
        print("Something an expected happen!")


