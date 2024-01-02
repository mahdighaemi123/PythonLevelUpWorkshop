# solution 1
import re


def is_valid_email(email):
    pattern = r"^[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$"
    return re.match(pattern, email) is not None


# solution 2 (not good way)
def is_valid_email(email):
    if "@" not in email:
        return False

    if not "".endswith(".com") and not email.endswith(".ir"):
        return False

    return email
