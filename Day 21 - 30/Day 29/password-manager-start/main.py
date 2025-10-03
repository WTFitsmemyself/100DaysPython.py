import secrets
import string
import math
from tkinter import *


CANVAS_WIDTH = 200
CANVAS_HEIGHT = 200
PADDING_X = 20
PADDING_Y = 20
FONT_NAME = "Courier"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def simple_password(length=16):
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

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
    length=16,
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

        return pwd

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
#Tk start
window = Tk()
window.title("Password Manager")
#config display
window.config(padx=PADDING_X, pady=PADDING_Y)
#image creation
lock_image = PhotoImage(file="./logo.png")
canvas = Canvas(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(column=1, row=0)







window.mainloop()