print("Welcome to the rollercoaster!")

height = int(input("What is your height in cm? "))
bill = 0

if height > 120:
    print("you shall go")
    age = int(input("What is your age? "))
    if age > 18 and age >= 45 and age <= 55:
        bill = 0
    elif age > 18:
        bill = 12
    elif age <= 18 and age >= 12:
        bill = 7
    else:
        bill = 5
    TicketAnswer = input("Do you want a photo taken? Y or N : ")
    if TicketAnswer == "Y":
        bill += 3
        print(f"You should pay ${bill}")
    else:
       print(f"You should pay ${bill}") 
else:
    print("you cant go")