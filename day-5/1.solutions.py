# solution 1
import random
intro = """
---------------------------
Math Game
---------------------------      
if you whant exit just type exit
"""

def generate_operation():
    num_1 = random.randint(1, 20)
    num_2 = random.randint(1, 20)
    operations = ["+", "*"]
    operation = random.choice(operations)
    message = f"{num_1} {operation} {num_2}"

    if operation == "*":
        result = num_1 * num_2
    elif operation == "+":
        result = num_1 + num_2

    return [message, result]


def check(user_input, result):
    if user_input == result:
        print("you win correct answer")
    else:
        print(f"you lose correct answer is {result}")


def main():
    print(intro)
    while (1):
        message, result = generate_operation()
        print(f"what is result of {message}")
        user_input = input("> ")
        if user_input == "exit":
            exit()
        user_input = int(user_input)
        check(user_input, result)


main()
