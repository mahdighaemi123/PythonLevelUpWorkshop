# solution 1
n = 5
for i in range(1, n+1):
    print(i*"* ")

# solution 2
n = 5
for i in range(n):
    for j in range(n):
        if (n+j) - i <= n:
            print("* ", end="")
        else:
            print("  ", end="")
    print()
