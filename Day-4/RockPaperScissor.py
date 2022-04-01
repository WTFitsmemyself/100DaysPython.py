#Libraries
import random

#Variables 
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

#CODE
Selection = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
pc_choice = random.randint(0,2)

#in case of draw
if pc_choice == Selection:
    if Selection == 0:
        print(f"You choose: \n{rock}")
        print(f"Pc choose: \n{rock}")
    elif Selection == 1:
        print(f"You choose: \n{paper}")
        print(f"Pc choose: \n{paper}")
    elif Selection == 2:
        print(f"You choose: \n{scissors}")
        print(f"Pc choose: \n{scissors}")
    print("Result is Draw")
