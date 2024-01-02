# Functions:
# A reusable block of code that can be called from anywhere in the program.

# This function calculates the sum of two numbers
# a,b are input of function and we call them parameters
def calculate_sum(a, b):
    return a + b


result = calculate_sum(1, 2)  # 3


# This function greets the user with a personalized message
# name is input of function and we call it parameter
def greet_user(name):
    print("Hello, " + name + "!")


greet_user("Mahdi")  # print("Hellom Mahdi !")
greet_user("Ali")   # print("Hellom Ali !")
