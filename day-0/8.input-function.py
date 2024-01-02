# input function:
# getting a string input from user in terminal

# we can read input text from terminal entered by user
user_entered_text = input()

# also we can show a message when we are doing this
user_entered_text = input("enter your name: ")

# remmember this input function always retuen string
# if you want number you shoud cast it with int(),float()
user_entered_text = input("enter your age: ")
numberic_age = int(user_entered_text)
