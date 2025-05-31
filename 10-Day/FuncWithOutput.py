first_name = input("Enter your first name: ").lower()
last_name = input("Enter your last name: ").lower()

def format_name(f_name, l_name):
    first = f_name.capitalize()
    last = l_name.capitalize()
    result = first + " " + last
    return result
    
print(format_name(first_name, last_name))