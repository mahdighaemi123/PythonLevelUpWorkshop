# Math library:
# A library that provides additional mathematical functions and operations

# import math lib
import math

# neper number
result = math.pi  # 3.141592653589793

# log 8 with base 2
result = math.log(8, 2)  # 3

# 2 power of 3 -> 2^3
result = math.pow(2, 3)  # 8

# round to down
result = math.floor(2.1)  # 2
result = math.floor(2.5)  # 2
result = math.floor(2.9)  # 2

# round flooer to middle to down
# and round middle to high to up
result = round(2.1)      # 2
result = round(2.5)      # 3
result = round(2.9)      # 3

# round to up
result = math.ceil(2.1)  # 3
result = math.ceil(2.5)  # 3
result = math.ceil(2.9)  # 3
