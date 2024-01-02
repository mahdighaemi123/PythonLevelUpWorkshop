# solution 1
text = "1-2-121-73-4"
numbers = text.split("-")
numbers = [int(number) for number in numbers]
numbers = filter(lambda number: number % 2 == 0, numbers)
numbers = [str(number) for number in numbers]
print("-".join(numbers))

# solution 2
text = "1-2-121-73-4"
numbers = text.split("-")
result = []

for number in numbers:
    if int(number) % 2 == 0:
        result.append(number)

result = [str(number) for number in result]
print("-".join(result))
