"""
Generates a simple password
"""
import secrets
import string

def generate_simple_password():
    """
    Generates a simple password:
    - 8 characters long
    - Random upper and lower letters and digit characters
    """
    return ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(8))
