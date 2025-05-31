height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
bmi = round(float((float(weight) /(float(height) ** 2))),2)
print("your BMI is " + str(bmi))
if bmi < 18.5:
    print("You are underweight")
elif bmi > 18.5 and bmi < 25:
    print("Your weight is normal")
elif bmi > 25 and bmi < 30:
    print("Your are overweight")
elif bmi > 30 and bmi < 35:
    print("You are obese")
if bmi > 35:
    print("You aare clinically obese")