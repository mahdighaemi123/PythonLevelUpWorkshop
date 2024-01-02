# solution 1

def full_xmass_tree(n):
    a = "*"
    b = " "
    body_width = n//4 * 2 + 1
    tree_leaves_starts = [0, n // 2, n // 2]

    def tree(n, start=0):
        for i in range(start, n):
            print(b * (n - i - 1) + a * (1 + (i * 2)))

    def body(n, width):
        for _ in range(n // 2):
            print(b * (n - width // 2 - 1) + a * width)

    def happy(n):
        text = "XMASS"
        print((n - len(text)//2 - 1) * b + text)

    for start_point in tree_leaves_starts:
        tree(n, start_point)

    body(n, body_width)
    happy(n)


for n in [3, 5, 7, 9, 11]:
    full_xmass_tree(n)
    print((n*2-1)*"-")
    print()
