# Cast variables types:
# Variable type casting refers to the process of changing the type of a variable


# cast to int
age = int(21.0) # 21
age = int("21") # 21
age = int(21)   # 21
# age = int("21.0") -> error (it cant part string float)
# age = int("n") -> error


# cast to float      
age = 21 + 0.0    # 21.0
age = float(21)   # 21.0  
age = float("21") # 21.0  
# age = float("n") -> error


# cast to string
name = str(21) # "21"
name = "mahdi" + str(21) # "mahdi21"
# name = "mahdi" + 21 # Error


# cast to bool
is_up = bool(0)      # false
is_up = bool(1)      # true
is_up = bool("")     # false
is_up = bool("123")  # true