print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
number_of_people = int(input("What was the number of people to split bill with? "))
tip_percentage = int(input("What percentage of tip you like to give(10, 12 or 15)? "))

percent_bill = total_bill + ((tip_percentage/100)*total_bill)
how_much_each = percent_bill/number_of_people

print("each person should pay:" + str(round(how_much_each,3)))

