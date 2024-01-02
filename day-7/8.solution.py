import time

# solution 1


def rand_1():
    return int(time.time()) % 1000


# solution 2
counter = 1


def rand_2():
    global counter
    counter += 1
    return hash(str(counter)) % 1000


for i in range(10):
    print("r1:", rand_1(), ", r2:", rand_2())
    time.sleep(1)
