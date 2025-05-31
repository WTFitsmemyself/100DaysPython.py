from os import system, name

banner = '''                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\ \n'''

bidders = []

print(banner)                   
print("Welcome to the secret auction program.")

def clear():
    
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
  
def append_dict():
    bidders.append(
        {
            "name": name,
            "bidValue": bidValue,
        }
    )
    return isContinue

def calcWhoIsWinner():
    listValues = []
    lenlist = len(bidders)
    
    for i in range(lenlist):
         intbidder = bidders[i]
         BidValueMikham = intbidder["bidValue"]
         listValues.append(BidValueMikham)
    listValues.sort(reverse=True)
    winnerBid = listValues[0]
    
    for i in range(lenlist):
        intbidder = bidders[i]
        BidValueMikham = intbidder["bidValue"]
        if BidValueMikham == listValues[0]:
            nameOfWinner = intbidder["name"]
    
    print(f"The winner is {nameOfWinner} with a bid of ${winnerBid}.")
    
         

edame = True
while edame == True:
    name = input("What is your name?: ")
    bidValue = float(input("What's your bid?: $"))
    isContinue = input("Are there any other bidders? Type 'yes' or 'no':  ").lower()
    
    if isContinue == "yes": 
        clear()
        append_dict()
    elif isContinue == "no":
        append_dict()
        calcWhoIsWinner()
        edame = False