"""
Generates a strong password
"""
import secrets
import string
import re
import random

def generate_strong_password():
    """
    Specs:
    - 8 characters long
    - At least one letter, one digit and one special character
    """
    # Prepare strings
    alphabet = string.ascii_letters
    digits = string.digits
    special_characters = '@.+-_'
    full_characters = alphabet + digits + special_characters

    # Create random password with letters
    password = secrets.choice(alphabet) + ''.join(secrets.choice(full_characters) for i in range(7))

    # Checks if password has a digit
    try:
        digit_position = re.search(r'\d', password).start()
    except AttributeError:
        digit_position = random.randint(1,7)
    password = password[:digit_position] + secrets.choice(digits) + password[digit_position+1:]
    
    # Checks if password has a special character
    try:
        special_position = re.search(r'[\@\.\+\-\_]', password).start()
    except AttributeError:
        special_position = random.randint(1,7)
        while special_position == digit_position:
            special_position = random.randint(1,7)
    password = password[:special_position] \
                + secrets.choice(special_characters) \
                + password[special_position+1:]

    return password
