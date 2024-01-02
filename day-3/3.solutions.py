# solution 1
x = 4
y = 3
a = " -"
b = "| "

for i in range(y*2+1):
    if i % 2 == 0:
        print(x * a)
    else:
        print((x+1)*b)


# solution 2
x = 4
y = 3
a = " -"
b = "| "

for i in range(y*2+1):

    if i % 2 == 0:
        for j in range(x):
            print(a, end="")
    else:
        for j in range(x+1):
            print(b, end="")

    print()