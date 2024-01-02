# solution 1
list = [1, 2, 3, 4, 5]
result = []

n = 3

for i in range(len(list)):
    if i >= n-1:
        result.append(sum(list[i-n+1:i+1])/n)
    else:
        result.append(None)

print(result)


# solution 2
list = [1, 2, 3, 4, 5]
n = 3
result = [None] * (n-1)

for i in range(n-1, len(list)):
    result.append(sum(list[i-n+1:i+1])/n)

print(result)
