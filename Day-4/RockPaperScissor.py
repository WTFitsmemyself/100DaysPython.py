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

#Functions
def RockPaperScissor(choice):
    if choice == "0":
        print(rock)
        print("\n Computer Choose: \n\n")
        pc_choice = random.randint(0,2)
        print(pc_choice)
    elif choice == "1":
        print(paper)
    elif choice == "2":
        print(paper)
    else:
        print("invalid option")

#CODE
Selection = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors")       
RockPaperScissor(Selection)