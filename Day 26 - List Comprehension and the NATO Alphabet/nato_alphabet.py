import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

nato_phonetic_dict = {
    row.letter: row.code for (index, row) in df.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
while True:
    word = input("Enter a word: ")
    try:
        nato_phonetic_alphabet_list = [
            nato_phonetic_dict[key] for key in word.upper()]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
    else:
        break

print(nato_phonetic_alphabet_list)
