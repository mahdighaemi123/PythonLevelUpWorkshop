# solution 1
intro = """
---------------------------
         Calculator
---------------------------
Supported actions:
1. add with +
2. substract with -
3. multiply with *
4. divide with /
---------------------------      
"""

operations = {
    "+": lambda a, b: a+b,
    "-": lambda a, b: a-b,
    "*": lambda a, b: a*b,
    "/": lambda a, b: a/b
}


def calculate(inputuser):
    for opration in operations.keys():
        if opration in inputuser:
            num1, num2 = map(int, inputuser.split(opration))
            return operations[opration](num1, num2)


def main():
    print(intro)
    while (1):
        try:
            print("Enter your calculation or type exit")
            myinput = input("> ")
            if myinput == "exit":
                exit()

            print(calculate(myinput))
        except:
            print("error")


main()

# solution 2
intro = """
---------------------------
         Calculator
---------------------------
Supported actions:
1. add with +
2. substract with -
3. multiply with *
4. divide with /
---------------------------      
"""


def calculate(inputuser):

    if "/" in inputuser:
        num1, num2 = map(int, inputuser.split("/"))
        result = num1/num2

    elif "*" in inputuser:
        num1, num2 = map(int, inputuser.split("*"))
        result = num1*num2

    elif "-" in inputuser:
        num1, num2 = map(int, inputuser.split("-"))
        result = num1-num2

    elif "+" in inputuser:
        num1, num2 = map(int, inputuser.split("+"))
        result = num1+num2

    return result


def main():
    print(intro)
    while (1):
        try:
            print("Enter your calculation or type exit")
            myinput = input("> ")
            if myinput == "exit":
                exit()

            print(calculate(myinput))
        except:
            print("error")


main()
