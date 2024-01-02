# Dictionary:
# A data structure that stores elements as key-value pairs,
# allowing for efficient retrieval of values based on their corresponding keys

# create empty dictionary
d = dict()
d = {}

# create dictionary with values
d = {
    "mahdi": 20,
    "ali": 21
}

# add/update values
d["mahdi"] = 20
d["ali"] = 21

# delete
del d["mahdi"]

# read valus by key
value = d["ali"]
value = d.get("key", "default")


d = {
    "mahdi": 20,
    "ali": 21
}

# get all keys
keys = d.keys()  # ["mahdi","ali"]

# get all valus
values = d.values()  # [21,20]
