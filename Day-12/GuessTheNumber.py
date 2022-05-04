import random
RandNum = random.randint(1,100)

def difficulty(Difficulty):
    if Difficulty == "easy":
        attemps = 10
        return attemps
    elif Difficulty == "hard":
        attemps = 5
        return attemps
    else:
        print("I don't know what to say")
        exit(1)
        
def guess(attempts):
    attempUser = 1
    while attempUser < attempts:
        NumGuess = int(input("Guess a Number: "))
        if NumGuess > RandNum:
            print("Too High")
            leftAttemp = attempts - attempUser
            print(f"There are {leftAttemp} left")
            attempUser += 1
        elif NumGuess < RandNum:
            print("Too Low")
            leftAttemp = attempts - attempUser
            print(f"There are {leftAttemp} left")
            attempUser += 1
        elif NumGuess == RandNum:
            print("You guess correct.")
            print(f"Number is {RandNum}")
            exit(0)

print("Welcome to the guessing number.")
print("I'm thinking of a number between 0 and 100.")
Difficulty = input("Choose a dictionary, Type 'easy' or 'hard': ").lower()
attempsDecided = difficulty(Difficulty)
guess(attempsDecided)