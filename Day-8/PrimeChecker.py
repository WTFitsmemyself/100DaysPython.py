NumberSelected = int(input("Please Type a Number: "))

def PrimeChecker(Number):
    if Number < 0:
        print("Negative numbers are not prime")
    elif Number == 0 or Number == 1:
        print("0 and 1 are not prime")
    elif Number == 2:
        print("Prime Number")
    elif Number == 3:
        print("Prime Number")
    elif Number == 5:
        print("Prime Number")
    elif Number != 2 and Number % 2 == 0:
        print("NOT a Prime Number")
    elif Number != 3 and Number % 3 == 0:
        print("NOT a Prime Number")
    elif Number != 5 and Number % 5 == 0:
        print("NOT a Prime Number")
    else:
        print("Prime Number")

PrimeChecker(NumberSelected)