# solution 1
import random
import string

welcome_message = """
-------------------------
Random Password Generator
-------------------------
Password patterns:
1.Numbers
2.a-Z
3.A-Z
4.!@#$&
------------------------"""


def main():
    print(welcome_message)

    user_selected_patterns = input("> enter passsword patterns: ")
    password_length = int(input("> enter passsword length: "))

    patterns = ""

    if "1" in user_selected_patterns:
        patterns += string.digits # [0-9]

    if "2" in user_selected_patterns:
        patterns += string.ascii_lowercase # [a-z]

    if "3" in user_selected_patterns:
        patterns += string.ascii_uppercase # [A-Z]

    if "4" in user_selected_patterns:
        patterns += string.punctuation # [!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~]

    password = random.choices(patterns, k=password_length)
    password = "".join(password)

    print("your password is:", password)


main()
