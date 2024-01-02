import random

# solution 1 (include float numbers)
min = int(input("min: "))
max = int(input("max: "))

r = min + random.random()*(max-min)
print(r)

# solution 2 (only int numbers)
min = int(input("min: "))
max = int(input("max: "))

number = random.randint(min, max)
print(number)

# solution 3 (only int numbers)
min = int(input("min: "))
max = int(input("max: "))

number = random.randrange(min, max)
print(number)
