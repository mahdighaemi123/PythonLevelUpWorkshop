# While Loop:
# A control flow statement that allows a particular block of code to be executed repeatedly
# as long as a specified condition is true

# normal while
count = 10
while count > 0:
    print(count)  # 10 9 8 7 6 5 4 3 2 1
    count -= 1


# while with continue
count = 10
while count > 0:

    count -= 1

    if count % 2 == 1:
        continue

    print(count) # 8 6 4 2 0


# while with break
count = 10
while True:
    count -= 1

    if count == 5:
        break

    print(count)  # 9 8 7 6
