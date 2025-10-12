import secrets
import string
import math
from tkinter import *
from tkinter import messagebox

CANVAS_WIDTH = 200
CANVAS_HEIGHT = 200
PADDING_X = 50
PADDING_Y = 50
FONT_NAME = "Courier"
USER_EMAIL = "itshosyn@gmail.com"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def simple_password(length=24):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    passw = ''.join(secrets.choice(alphabet) for _ in range(length))
    password_entry.delete(0, END)
    password_entry.insert(0, passw)

def complex_password(
    length=16,
    include_upper=True,
    include_lower=True,
    include_digits=True,
    include_symbols=True,
    exclude_ambiguous=True,
    no_repeats=False,
    begin_with_letter=False
):

        # Character sets
        lowers = string.ascii_lowercase
        uppers = string.ascii_uppercase
        digits = string.digits
        symbols = "!@#$%^&*()-_=+[]{};:,.<>?/"  # safer symbols

        # Optionally remove ambiguous chars
        if exclude_ambiguous:
            ambiguous = set('lI1O0o')
            lowers = ''.join(c for c in lowers if c not in ambiguous)
            uppers = ''.join(c for c in uppers if c not in ambiguous)
            digits = ''.join(c for c in digits if c not in ambiguous)

        # Build full alphabet
        alphabet = ''
        if include_lower: alphabet += lowers
        if include_upper: alphabet += uppers
        if include_digits: alphabet += digits
        if include_symbols: alphabet += symbols

        if len(alphabet) == 0:
            raise ValueError("No character sets selected!")

        # Ensure constraints
        required_chars = []
        if include_lower: required_chars.append(secrets.choice(lowers))
        if include_upper: required_chars.append(secrets.choice(uppers))
        if include_digits: required_chars.append(secrets.choice(digits))
        if include_symbols: required_chars.append(secrets.choice(symbols))

        # Remaining length
        remaining_length = length - len(required_chars)

        # Begin with a letter if requested
        password_chars = []
        if begin_with_letter:
            letter_pool = (lowers + uppers)
            password_chars.append(secrets.choice(letter_pool))
            remaining_length -= 1

        # Fill remaining chars
        while remaining_length > 0:
            c = secrets.choice(alphabet)
            if no_repeats and c in password_chars:
                continue
            password_chars.append(c)
            remaining_length -= 1

        # Combine with required chars
        password_chars.extend(required_chars)

        # Shuffle securely
        secrets.SystemRandom().shuffle(password_chars)

        # Return password string
        return ''.join(password_chars)

def generate_complex_password(
    length=7,
    include_upper=True,
    include_lower=True,
    include_digits=True,
    include_symbols=True,
    exclude_ambiguous=True,
    no_repeats=False,
    no_sequences=True,
    begin_with_letter=False,
    quantity=1,
    verbose=False
):
    """
    Generate cryptographically secure complex passwords.
    """
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*()-_=+[]{};:,.<>?/"

    # Remove ambiguous chars
    if exclude_ambiguous:
        ambiguous = set('lI1O0o')
        lowers = ''.join(c for c in lowers if c not in ambiguous)
        uppers = ''.join(c for c in uppers if c not in ambiguous)
        digits = ''.join(c for c in digits if c not in ambiguous)

    # Build allowed alphabet
    alphabet = ''
    if include_lower: alphabet += lowers
    if include_upper: alphabet += uppers
    if include_digits: alphabet += digits
    if include_symbols: alphabet += symbols

    if len(alphabet) == 0:
        raise ValueError("No character sets selected!")

    # Helper function: check if password has sequential chars
    def has_sequence(pwd):
        for i in range(len(pwd) - 2):
            triplet = pwd[i:i+3]
            if all(ord(triplet[j+1]) - ord(triplet[j]) == 1 for j in range(2 - 1)):
                return True
        return False

    # Helper: entropy estimation
    def estimate_entropy(pwd_len, alphabet_size):
        return pwd_len * math.log2(alphabet_size)

    # Main generation loop
    def generate_one():
        required = []
        if include_lower: required.append(secrets.choice(lowers))
        if include_upper: required.append(secrets.choice(uppers))
        if include_digits: required.append(secrets.choice(digits))
        if include_symbols: required.append(secrets.choice(symbols))

        remaining_len = length - len(required)
        chars = []

        if begin_with_letter:
            letter_pool = lowers + uppers
            first = secrets.choice(letter_pool)
            chars.append(first)
            remaining_len -= 1

        # Fill remaining chars
        while remaining_len > 0:
            c = secrets.choice(alphabet)
            if no_repeats and c in chars:
                continue
            chars.append(c)
            remaining_len -= 1

        # Add required chars
        chars.extend(required)

        # Shuffle securely
        secrets.SystemRandom().shuffle(chars)
        pwd = ''.join(chars)
        # Re-roll if sequential not allowed
        if no_sequences and has_sequence(pwd):
            return generate_one()

        newpassword = pwd
        password_entry.delete(0, END)
        password_entry.insert(0, newpassword)
        return None


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    username = email_entry.get()
    password = password_entry.get()

    if website == "" or username == "" or password == "":
        messagebox.showwarning(title="Oops", message="Please fill out all fields!")
    else:
        # Confirm with user
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n\n"
                                                              f"Website: {website}\n"
                                                              f"Email: {username}\n"
                                                              f"Password: {password}\n\nSave it?")
        if is_ok:
            with open("data_user_pass.txt", "a") as file:
                file.write(f"{website} | {username} | {password}\n")

            # Clear entries
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
#Tk start
window = Tk()
window.title("Password Manager")

#config display
window.config(padx=PADDING_X, pady=PADDING_Y)

#image creation
lock_image = PhotoImage(file="./logo.png")
canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, highlightthickness=0)
canvas.create_image(CANVAS_WIDTH/2, CANVAS_HEIGHT/2, image=lock_image)
canvas.grid(column=1, row=0)

#label website
web_label = Label(text="Website: ")
web_label.grid(column=0, row=1)

#label website
username_label = Label(text="E-mail / Username: ")
username_label.grid(column=0, row=2)

#label website
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

#entries
website_entry = Entry(width=38)
website_entry.grid(column=1, row=1, columnspan=2)
email_entry = Entry(width=38)
email_entry.insert(END, USER_EMAIL)
email_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)


#calls action() when pressed
button = Button(text="Generate Password", command=simple_password)
button.grid(column=2, row=3)

#calls action() when pressed
button = Button(text="Add", width=36, command=save_password)
button.grid(column=1, row=4, columnspan=2)



window.mainloop()