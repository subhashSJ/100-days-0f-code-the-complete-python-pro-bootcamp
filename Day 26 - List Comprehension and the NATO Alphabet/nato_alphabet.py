import pandas as pd

df = pd.read_csv("nato_phonetic_alphabet.csv")

nato_phonetic_dict = {
    row.letter: row.code for (index, row) in df.iterrows()}

# Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ")

nato_phonetic_alphabet_list = [
    nato_phonetic_dict[key] for key in word.upper()]
print(nato_phonetic_alphabet_list)
