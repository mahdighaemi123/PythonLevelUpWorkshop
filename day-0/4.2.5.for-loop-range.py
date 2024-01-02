# Range:
# A built-in function in Python that generates a sequence of numbers
# which is often used with for loops for iterating a specific number of times.

# range(end) ->  (by default start = 0 , step = 1)
for i in range(3):
    print(i)  # 0 , 1 , 2

# range(start,end) -> (by default step = 1)
for i in range(0, 3):
    print(i)  # 0 , 1 , 2

# range(start,end,step)
for i in range(0, 3, 2):
    print(i)  # 0 , 2
