# string:
# it’s a sequence of characters

# create a empty string
s = ""

# create string with values
s = "my string "

# first chracter of every word sill capital and other will be lower
result = s.capitalize()  # My String

# all chracter will be uppercase
result = s.upper()  # "MY STRING"

# all chracter will be lowercase
result = s.lower()  # "my string"

# count how many "a" exist in my string
result = s.count("a")  # 0

# get index of "a" if exist else return -1
result = s.find("a")  # -1

# get index of "a" if exist else error
result = s.index("m")  # 0

# replace all of "my" to "hi"
result = s.replace("my", "hi")  # hi string

# remove space from left and right of string
result = s.strip()  # "hi string"

# join a list
result = "-".join(["1", "2", "3"])  # "1-2-3"


# get spetial part of string with indexs

# get one chr with s[chr_index]
s = "abc"
result = s[0]     # "a"
result = s[-1]    # "c" (-1 mean from last start counting)

# get range of string with s[start_index,end_index]
result = s[0:2]   # "ab"

# get range of string and steps with s[start_index,end_index,step]
result = s[::2]   # "ac"
result = s[::-1]  # "cba" (-1 for step mean from end to start)
result = s[::]    # "abc" (simple copy)
