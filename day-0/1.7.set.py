# Set:
# An unordered collection of unique elements, with no duplicate values allowed.

# create empty set
s = set()

# create a set with valus
s = {1, 2, 3}      # {1,3,2}
s = set([1, 2, 3])  # {1,3,2}

# add item to set
s.add("apple")  # {1,3,2,"apple"}
s.add("banana")  # {1,3,2,"apple"}

# check if item exist in set (very fast)
result = "apple" in s  # True

# print all items
print(s)
