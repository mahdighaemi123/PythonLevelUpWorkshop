# solution 1
import copy

a = ["a", "b", [1, 2, 3]]
b = copy.deepcopy(a)
a[2].append(4)

print(a)
print(b)

# solution 2 (dont use)
a = ["a", "b", [1, 2, 3]]
b = []
b.append(a[0])
b.append(a[1])
b.append(a[2].copy())

print(a)
print(b)
