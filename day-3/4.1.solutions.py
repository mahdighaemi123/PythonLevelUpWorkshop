# solution 1
n = 5
for i in range(1, n+1):
    print("  "*(n-i)+(n-(n-i))*"* ")

# solution 2
n = 5
for i in range(n):
    for j in range(n):
        if n-(i+j)-1 <= 0:
            print("* ", end="")
        else:
            print("  ", end="")
    print()
