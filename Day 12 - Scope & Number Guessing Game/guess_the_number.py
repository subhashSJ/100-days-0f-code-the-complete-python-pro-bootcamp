import random
import os
from logo import logo

while True:
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100")

    chosen_number = random.randint(1, 100)

    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

    # Check for the invalid input
    while difficulty_level != "easy" and difficulty_level != "hard":
        print("Invalid Input.")
        difficulty_level = input(
            "Choose a difficulty. Type 'easy' or 'hard': ")

    if difficulty_level == "easy":
        attempts = 10
    else:
        attempts = 5

    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number")

        guessed_number = int(input("Make a guess: "))

        if guessed_number < chosen_number:
            print("Too low!")
        elif guessed_number > chosen_number:
            print("Too high!")
        else:
            print("You got it!")
            print(f"The answer was: {chosen_number}")
            break

        attempts -= 1
        if attempts == 0:
            print("You ran out of attempts. You lose. The number was: ", chosen_number)
            break

        print("Guess again.")
        
    flag = input("Do you want to play again? Type 'yes' to continue: ")
    if flag == "yes":
        os.system("cls || clear")
    else:
        break
