from art import logo, vs
from game_data import data
import random
import os


def check_answer(choice, A, B):
    """Returns True if chosen answer is correct else returns False"""
    if choice == 'a':
        if A['follower_count'] > B['follower_count']:
            return True
        else:
            return False
    elif choice == 'b':
        if A['follower_count'] < B['follower_count']:
            return True
        else:
            return False

A = random.choice(data)
B = random.choice(data)
score = 0

while True:
    while A == B:
        B = random.choice(data)

    print(logo)

    if score != 0:
        print(f"You're right! Current score: {score}")

    print(
        f"Compare A: {A['name']}, a {A['description']}, from {A['country']}.")
    print(vs)
    print(
        f"Against B: {B['name']}, a {B['description']}, from {B['country']}.")

    choice = input("who has more followers? Type 'A' or 'B': ").lower()
    while choice != "a" and choice != "b":
        print("Invalid Input.Try again.")
        choice = input("who has more followers? Type 'A' or 'B': ")

    os.system("clear || cls")

    if check_answer(choice, A, B):
        score += 1
        A = B
    else:
        break

print(logo)
print(f"Sorry, that's wrong. Final score: {score}")
