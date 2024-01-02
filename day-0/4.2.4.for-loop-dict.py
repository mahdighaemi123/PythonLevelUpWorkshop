# Dictionaries:
d = {
    "mahdi": 20,
    "ali": 21
}

# iterate on all keys
for key in d:
    print(key, d[key])

# iterate on all key value perires
# .items() will retuen list of key value pair [(key1,value1),...]
for (key, value) in d.items():
    print(key, value)
