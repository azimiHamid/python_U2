import pandas
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

data = pandas.read_csv("./utils_26/nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format: --> {"A": "Alfa", "B": "Bravo", ...}
data_dict = {row.letter:row.code for (index, row) in data.iterrows()}
print(data_dict["A"])


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()
output_list = [data_dict[letter] for letter in word]
print(output_list)
