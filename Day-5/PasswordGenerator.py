import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
Password = []

print("Welcome to Password Generator!")
HowManyLetters = input("How many letters would you like in your Password?: ")
HowManySymbols = input("How many symbols would you like in your Password?: ")
HowManyNumbers = input("How many numbers would you like in your Password?: ")


def ListToString(list):
    string = ""
    for i in range(len(list)):
        string += list[i]
    return string


for i in range(0, int(HowManyLetters)):
    randomics = random.choice(letters)
    Password.append(randomics)

for i in range(0, int(HowManySymbols)):
    randomics = random.choice(symbols)
    Password.append(randomics)

for i in range(0, int(HowManyNumbers)):
    randomics = random.choice(numbers)
    Password.append(randomics)

random.shuffle(Password)
Password_String = ListToString(Password)

print(f"Your Password is: {Password_String}")
