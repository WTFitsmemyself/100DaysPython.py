#Libraires
import random 

#Variables
word_to_play = ['birthday', 'beekepper', 'banana', 'apple', 'orange', 'flavor']
pc_choice = random.choice(word_to_play)
len_word = len(pc_choice)
max_choice = 6
NumberOfChoices = 0
blanks_list = ['_'] * len_word
#functions
        
def clear():
    print('\x1bc')

def CheckLetter(letter):
    for i in range(len(pc_choice)):
        if letter == pc_choice[i]:
            print("Rights")
        else:
            print("Wrong")
    
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

# while NumberOfChoices < max_choice:
print(f"Chosen word is {pc_choice}")
while NumberOfChoices < max_choice:
    guess = input("\nGuess a letter: ").lower()
    for i in range(len(pc_choice)):
        if guess == pc_choice[i]:
            blanks_list[i] = pc_choice[i]
    NumberOfChoices += 1
    print(blanks_list)

