import sys
shiftString = []
asci_banner='''
░█▀▀░█▀█░█▀▀░█▀▀░█▀█░█▀▄░░░█▀▀░▀█▀░█▀█░█░█░█▀▀░█▀▄
░█░░░█▀█░█▀▀░▀▀█░█▀█░█▀▄░░░█░░░░█░░█▀▀░█▀█░█▀▀░█▀▄
░▀▀▀░▀░▀░▀▀▀░▀▀▀░▀░▀░▀░▀░░░▀▀▀░▀▀▀░▀░░░▀░▀░▀▀▀░▀░▀
'''

def ShiftCheck(NumberShift):
    if NumberShift < 0 or NumberShift > 26:
        print("Invalid Shift, Number must be between 0 and 26")

def user_choice_Check(UserChoice):
    if UserChoice == 'encode' or UserChoice == 'decode':
        print("")
    else:
        print("Invalid Choice.")
        exit(1)

def encode(MessageUsr,shiftnumber):
    lenMessage = len(MessageUsr)
    for i in range(0,lenMessage):
        num_letter = ord(MessageUsr[i]) 
        temp = chr(num_letter + shiftnumber)
        shiftString.append(temp)
        
def decode(MessageUsr,shiftnumber):
    lenMessage = len(MessageUsr)
    for i in range(0,lenMessage):
        num_letter = ord(MessageUsr[i]) 
        temp = chr(num_letter - shiftnumber)
        shiftString.append(temp)
        
    
#Banner Printing      
print(asci_banner)

#user choice check
user_choice = input("Type 'encode' to encrypt, type 'decode' to decrypt: ").lower()
user_choice_Check(user_choice)

#message
MessageUser = input("Type Your Massage: ")

#shift number check
ShiftNumber = int(input("\nType the shift number: "))
ShiftCheck(ShiftNumber)

if user_choice == 'encode':
    encode(MessageUser,ShiftNumber)
    print("\nYour encode Cipher is: ")
    print(''.join(shiftString))
elif user_choice == 'decode':
    decode(MessageUser,ShiftNumber)
    print("\nYour decode Cipher is: ")
    print(''.join(shiftString))