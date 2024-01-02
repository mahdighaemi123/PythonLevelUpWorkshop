# List:
# An ordered collection of items that can contain elements of different data types,
# such as numbers, strings, or even other lists.

# create empty list
nums = []
nums = list()

# create list of values
nums = [10, 20, 30]

# access item by index
# index start from 0
num1 = nums[0]  # 10
num2 = nums[1]  # 20
num3 = nums[2]  # 30

# add item to lis
nums = [10, 20, 30]
nums.append(40)  # nums=> [10,20,30,40]

# delete last item
nums = [10, 20, 30]
nums.pop()  # return 30 and nums=> [10,20]

# delete all items
nums = [10, 20, 30]
nums.clear()  # nums=> []

# add new item in 3 index
nums = [10, 20, 30]
nums.insert(3, "new_item")  # nums=> [10,20,30,"new_item"]

# sort list
nums = [30, 10, 20]
nums.sort()  # nums=> [10,20,30]

# reverse a list items places
nums = [10, 20, 30]
nums.reverse()  # nums=> [30,20,10]

# calculate sum of numbers in a list
nums = [10, 20, 30]
result = sum(nums)  # 60

# calculate length of list
nums = [10, 20, 30]
result = len(nums)  # 3

# create a new soted list from a list
nums = [30, 10, 20]
result = sorted(nums)  # return => [10,20,30] , nums=> [30,10,20]

# list of strings
chrs = ["a", "b", "c"]

# get one item with s[item_index]
result = chrs[0]     # "a"
result = chrs[-1]    # "c" (-1 mean from last start counting)

# get range of items with chrs[start_index,end_index]
result = chrs[0:2]   # ["a","b"]

# get range of items and steps with chrs[start_index,end_index,step]
result = chrs[::2]   # ["a","c"]
result = chrs[::-1]  # ["c","b","a"] (-1 for step mean from end to start)
result = chrs[::]    # ["a","b","c"] (simple copy)
