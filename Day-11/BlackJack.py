import random
from os import name, system

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
def clear():
    
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def RandomNumbersSelection():
    FirstRandomNumberUser = random.randint(0,12)
    SecondRandomNumberUser = random.randint(0,12)
    ThirdRandomNumberUser = random.randint(0,12)
    ForthRandomNumberUser = random.randint(0,12)
    FifthRandomNumberUser = random.randint(0,12)
    FirstRandomNumberPC = random.randint(0,12)
    SecondRandomNumberPC = random.randint(0,12)
    ThirdRandomNumberPC = random.randint(0,12)
    ForthRandomNumberPC = random.randint(0,12)
    FifthRandomNumberPC = random.randint(0,12)
    if FirstRandomNumberUser == SecondRandomNumberUser or FirstRandomNumberPC == SecondRandomNumberPC:
        RandomNumbersSelection()
    return FirstRandomNumberUser, SecondRandomNumberUser, FirstRandomNumberPC, SecondRandomNumberPC,ThirdRandomNumberUser,ThirdRandomNumberPC,ForthRandomNumberUser,ForthRandomNumberPC,FifthRandomNumberUser,FifthRandomNumberPC

def is_lose(list):
    sum = 0
    for i in range(0,len(list)-1):
        sum += list[i]
        if sum > 21:
            print("Computer Wins")
    return sum

def hitOrGO(AnsUser):
    if AnsUser == 'y':
        return True
    elif AnsUser == 'n':
        return False

def who_win(listUser, listPC):
    SumUser = 0
    SumPC = 0
    for i in range(0,len(listUser)-1):
        SumUser += listUser[i]
    for i in range(0,len(listPC)-1):
        SumPC += listPC[i]
    print(f"Your final hand is {listUser}")
    print(f"Computer final hand is {listPC}")
    if SumPC > SumUser:
        print("You Lose")
    else:
        print("You Win")

is_continue = True
while is_continue:
    WannaPlay = input("Do you want to play a game of BlackJack: Type 'y' or 'n': ").lower()
    if WannaPlay == 'n':
        is_continue = False
        print("GoodBye")
        exit(0)
    elif WannaPlay == 'y':
        yourCards = [0,0,0,0,0]
        computerCards = [0,0,0,0,0]
        firstRanduser, SecondRanduser, firstRandPC, SecondRandPC, thirdRanduser, thirdRandPC, forthRandUser, forthRandPC, fifthRanduser, fifthRanduser= RandomNumbersSelection()
        yourCards[0] = cards[firstRanduser]
        yourCards[1] = cards[SecondRanduser]
        computerCards[0] = cards[firstRandPC]
        computerCards[1] = cards[SecondRandPC]
        sumScore = is_lose(yourCards)
        clear()
        print(logo)
        print(f"Your cards: [{yourCards[0]}, {yourCards[1]}], Current Score: {sumScore}")
        print(f"Computer's first card: {computerCards[0]}")
        HitOrPass = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if hitOrGO(HitOrPass):
            yourCards[2] = cards[thirdRanduser]
            computerCards[2] = cards[thirdRandPC]
            is_lose(yourCards)
        else:
            who_win(yourCards,computerCards)
        
