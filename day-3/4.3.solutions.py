# solution 1
n = 5
a = "* "
b = "  "
for i in range(n):
    print(b*(n-i-1) + a*(1+(i*2)))

# solution 2
n = 9
for i in range(n//2+1):
    for j in range(n):

        if j <= n//2:
            if n//2 > i+j:
                print("  ", end="")
            else:
                print("* ", end="")

        else:
            if j-i <= n//2:
                print("* ", end="")
            else:
                print("  ", end="")

    print()
