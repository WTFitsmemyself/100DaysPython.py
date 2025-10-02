import secrets
import string

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

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
