# Condition:
# We use conditions in programming to instruct the computer to execute a 
# specific part of the program under certain circumstances.


# if elif and else
temp = -50

if temp < 0:
    print("ice")

elif temp < 100:
    print("water")

else:
    print("steam")


# one line condition
age = 21
have_licence = True if age >= 18 else False


# nested if else
num1 = 20
num2 = 22

if num1 % 2 == 0:
    if num2 % 2 ==0:
        print("both even")
    else:
        print("num 1 even","num 2 odd")
else:
    if num2 % 2 ==0:
        print("num 1 odd","num 2 even")
    else:
        print("both odd")

