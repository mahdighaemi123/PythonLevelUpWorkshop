# try-except:
# syntax for handling errors in try scoop

# when any error happend in try scoop
# expect scoop codes will run
try:

    print(1/0)

except:
    print("error happend")


# also we can catch information about error
try:

    print(1/0)

except Exception as error:
    print(error)


# anly catch ZeroDivitionError
# it wont catch other type of error
try:

    print(1/0)

except ZeroDivisionError as error:
    print(error)