import random
import string

def generate_password(length, use_lower, use_upper, use_digits, use_symbols):
    characters = ""
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Please select at least one character set!"
    
    # Make sure password has at least one from each selected set
    password = []
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))
    password += [random.choice(characters) for _ in range(length - len(password))]
    random.shuffle(password)
    return ''.join(password)