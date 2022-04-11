#Libraires
import random 

#Variables
word_to_play = ['birthday', 'beekepper', 'banana', 'apple', 'orange', 'flavor']
pc_choice = random.choice(word_to_play)
len_word = len(pc_choice)

for i in range(len_word):
    print("_ ",end = " ")
        
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

print("\n")   
first_letter = input("\nPlease enter a letter: ").lower()
