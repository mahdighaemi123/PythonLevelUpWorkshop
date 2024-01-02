# solution 1
def divide(a, b):
    count = 0
    while (a >= b):
        a = a-b
        count += 1

    remainer = a
    return count, remainer


print(divide(10, 2))
