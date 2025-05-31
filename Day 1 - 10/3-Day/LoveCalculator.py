import re

print("Welcome to the Love Calculator")
myName = input("What is your name: ")
herName = input("What is your their name: ")

myNameLower = myName.lower()
herNameLower = herName.lower()

CountMyScore = len(re.findall('[truelove]',myNameLower))
CountHerScore = len(re.findall('[truelove]',herNameLower))

finallScore = str(CountMyScore) + str(CountHerScore)
if finallScore < "10" or finallScore > "90":
    print(f"Your score is {finallScore}, you go together like coke and mentos.")
elif finallScore <= "50" and finallScore >= "40":
    print(f"Your score is {finallScore}, you are alright together.")
else:
    print(f"Your score is {finallScore}")