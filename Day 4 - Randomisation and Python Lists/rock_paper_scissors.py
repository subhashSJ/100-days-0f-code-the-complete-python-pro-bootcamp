# Win conditions for the Rock Paper Scissors game:
    # Rock wins against scisors
	# Scisors win against paper
	# Paper wins against rock

from random import randint

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
map = [rock, paper, scissors]

while True:
    user_choice = int(
        input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if not ([0, 1, 2].count(user_choice)):
        print("Invalid input. Please enter a valid number.")
        continue
    print(map[user_choice])

    computer_choice = randint(0, 2)
    print("Computer chose:")
    print(map[computer_choice])

    win_conditions = [[0, 2], [2, 1], [1, 0]]

    if win_conditions.count([user_choice, computer_choice]):
        print("You won!!")
    elif user_choice == computer_choice:
        print("It's a draw")
    else:
        print("You lose")

    play_again = input(
        "Would you like to play again? Type 'Y' for yes, 'N' for no\n")
    if play_again.lower() == 'n':
        break
