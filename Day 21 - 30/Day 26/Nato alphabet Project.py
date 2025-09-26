import pandas as pd

#convert name to list
user_name = list(input("Enter your name: ").upper())

#read the NATO csv file
nato_data = pd.read_csv('nato_phonetic_alphabet.csv')

#new format dict build
new_nato_dict = {row.letter:row.code for (index, row) in nato_data.iterrows()}


new_nato_list = [new_nato_dict[name] for name in user_name if name in new_nato_dict]
print(new_nato_list)