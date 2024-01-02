# solution 1 (faster)
my_dictionaty = {
    "mahdi":10,
    "ali":20
}

name = input("name: ")
score = my_dictionaty[name]

print(score)

# solution 2
names = ["mahdi", "ali"]
scores = [10, 20]

name = input("name: ")
index = names.index(name)

score = scores[index]

print(score)