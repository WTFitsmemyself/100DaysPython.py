#Libraires
import random 

#Variables
word_to_play = ['birthday', 'beekepper', 'banana', 'apple', 'orange', 'flavor']
pc_choice = random.choice(word_to_play)
len_word = len(pc_choice)
max_choice = 6
NumberOfChoices = 0

#functions
def ShowBlanks(): 
    for i in range(len_word):
        blanks = print("_",end = " ")
    return blanks

def clear():
    print('\x1bc')


banner = ''' _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       '''
                   
first_try_banner = '''      _______
     |/      |
     |      (_)
     |      
     |       
     |       
     |
    _|___'''

second_try_banner = '''      _______
     |/      |
     |      (_)
     |       |
     |       |
     |      
     |
    _|___'''

third_try_banner = '''      _______
     |/      |
     |      (_)
     |      \|
     |       |
     |       
     |
    _|___'''

fourth_try_banner = '''      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |       
     |
    _|___'''

fifth_try_banner = '''      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      /  
     |
    _|___'''
                   
full_dead_banner = '''      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \ 
     |
    _|___'''

print(banner)

while NumberOfChoices < max_choice:
    first_letter = input("\nGuess a letter: ").lower()
    blank = ShowBlanks()
    print(f"\n{blank}")
    