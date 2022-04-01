print("Welcome to Python Pizza Deliveries!")
bill = 0
size = input("What size pizza do you want? (S, M or L): ")
AnswerPeperoni = input("Do you want Peperoni on your pizza? Y or N: ")
AnswerChesse = input("Do you want extra cheese? Y or N: ")

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
if size == "S" and AnswerPeperoni == "Y":
    bill += 2
elif AnswerPeperoni == "Y":
    bill += 3
if AnswerChesse == "Y":
    bill += 1

print(f"Your Finall bill is ${bill}")