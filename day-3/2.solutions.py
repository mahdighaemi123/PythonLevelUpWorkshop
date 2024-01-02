# solution 1
def is_triangle(a, b, c):
    return a+b > c and a+c > b and c+a > b

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            if is_triangle(a, b, c):
                print(a, b, c)