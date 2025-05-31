print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
number_of_people = int(input("What was the number of people to split bill with? "))
tip_percentage = int(input("What percentage of tip you like to give(10, 12 or 15)? "))
hundered = 100
each_person_pay = round(((total_bill * (hundered + tip_percentage)) / hundered) / number_of_people,2)
print("Each person should pay: $"+ str(each_person_pay))