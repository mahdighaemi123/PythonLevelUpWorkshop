# solution 1

import math
n = int(input())
print(math.factorial(n))

# solution 2
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


n = int(input())
print(factorial(n))

# solution 3
n = int(input())
r = 1
for i in range(1, n+1):
    r = r * i
print(r)
