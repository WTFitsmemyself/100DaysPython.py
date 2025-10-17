import pandas as pd

#convert name to list
nato_data = pd.read_csv('nato_phonetic_alphabet.csv')

# new format dict build
new_nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

def generate_nato_dict():
    user_name = list(input("Enter your name: ").upper())
    try:
        new_nato_list = [new_nato_dict[name] for name in user_name]
    except KeyError:
        print("No such name")
        generate_nato_dict()
    else:
        print(new_nato_list)

generate_nato_dict()