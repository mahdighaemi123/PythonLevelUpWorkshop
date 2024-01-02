# solution 1
names = input().split()
uniqe_names = list(set(names))
print(",".join(uniqe_names))

# solution 2
text = input()
names = text.split(" ")
uniqe_names = []

for name in names:
    if name not in uniqe_names:
        uniqe_names.append(name)

result = ""

for name in uniqe_names:
    result = result + name+","

print(result)