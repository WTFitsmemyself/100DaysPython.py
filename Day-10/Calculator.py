banner = ''' _____________________
|  _________________  |
| | Hosyn           | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|'''

def calc(first_num, second_num, operation):
    if operation == "+":
        result = first_num + second_num
        print(f"{first_num} {operation} {second_num} = {result}")
        return result
    elif operation == "-":
        result = first_num - second_num
        print(f"{first_num} {operation} {second_num} = {result}")
        return result
    elif operation == "*":
        result = first_num * second_num
        print(f"{first_num} {operation} {second_num} = {result}")
        return result
    elif operation == "/":
        result = first_num / second_num
        print(f"{first_num} {operation} {second_num} = {result}")
        return result
    else:
        print("Invalid operation")

def show_operations():
    print("+")
    print("-")
    print("*")
    print("/")

def first():
    first_num = float(input("What's the first number: "))
    show_operations()
    operation = input("Pick and operation: ")
    second_num = float(input("What's the second number: "))
    result_feli = calc(first_num, second_num, operation)
    return result_feli

def second(result):
    first_num = result
    operation = input("Pick and operation: ")
    second_num = float(input("What's the second number: "))
    result_feli = calc(first_num, second_num, operation)
    return result_feli
        
print(banner)
result_feli = first()
yORn = input(f"Type 'y' to continue calculating with {result_feli}, or type 'n' to start a new calculation: ")
if yORn == "y":
    second(result_feli)
else:
    first()
        