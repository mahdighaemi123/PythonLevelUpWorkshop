# solution 1
for i in range(1, 100):
    if i % 5 == 0:
        print("hop")

    else:
        print(i)

# solution 2
i = 1
while True:
    if i == 100:
        break

    if i - (i//5*5) == 0:
        print("hop")
    else:
        print(i)

    i += 1
