import re

def validate_phone_number(value: str) -> str:
    phone_regex = r"^[+]*[(]{0,1}[0-9]{1,4}[)]{0,1}[-\s\./0-9]*$"
    if not re.match(phone_regex, value):
        raise ValueError("Invalid phone number format")
    return value

def validate_email(value: str) -> str:
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if not re.match(email_regex, value):
        raise ValueError("Invalid email format")
    return value

def validate_password(value: str) -> str:
    if len(value) < 8:
        raise ValueError("Password must be at least 8 characters long")
    return value