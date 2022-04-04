import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to Password Generator!")
HowManyLetters = input("How many letters would you like in your Password?: ")
HowManySymbols = input("How many symbols would you like in your Password?: ")
HowManyNumbers = input("How many numbers would you like in your Password?: ")

for i in range(1,int(HowManyLetters)):
    randomics = random.choices(letters,None)
    print(f"{randomics}")
            


# print(f"Here is your Password: {Password}")



# if HowManySymbols != 0:
#     for i in range(1,int(HowManySymbols)):