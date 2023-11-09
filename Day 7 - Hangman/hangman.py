import random
from hangman_art import stages, logo
from hangman_words import word_list


chosen_word = random.choice(word_list)

actual_char_list = list(chosen_word)

# Creating a list of Nones of length equal to length of the chosen_word
char_list = [None]*len(actual_char_list)

lives = 6

# Printing Hangman logo
print(logo)

while lives > 0 and char_list != actual_char_list:
    char = input("Guess a letter: ").lower()

    if char in char_list:
        print(f"You have already guessed {char}.")
    
    if char not in actual_char_list:
        print(f"You guessed {char}, that is not in the word. You lose a life")
        for i in range(len(char_list)):
            if char_list[i] == None:
                print("_", end =" ")
            else:
                print(char_list[i], end =" ")
        lives-=1
        print("\n")
        print(stages[lives])
    else:
        for i in range(len(actual_char_list)):
            if actual_char_list[i] == char:
                char_list[i] = char
        
        for i in range(len(char_list)):
            if char_list[i] == None:
                print("_", end =" ")        
            else:
                print(char_list[i], end =" ")
        print("\n")
        print(stages[lives])

if(lives > 0):
    print("You Win!!")
else:
    print(f"You Lose. The word was: {chosen_word}")