# solution 1 (without list)
n = int(input("n: "))
scores = 0

for _ in range(n):
    number = int(input("number: "))
    scores += number

avg_numbers = scores / n

print("avg :", avg_numbers)

# solution 2 (using list)
n = int(input("n: "))
scores = []

for _ in range(n):
    number = int(input("number: "))
    scores.append(number)

sum_numbers = sum(scores)
avg_numbers = sum_numbers / n

print("avg :", avg_numbers)
