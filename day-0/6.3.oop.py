# Person class
class Person:
    # define attributes and default value
    name = "-"
    age = 0

    # define methods
    # always first parameter is self meaning object it self
    def sayHi(self):
        print("hi "+self.name)


# create person_1 object from person class
person_1 = Person()

# change name and age of person_1
person_1.name = "ali"
person_1.age = 20

# call sayHi for person_1
person_1.sayHi()  # print("hi ali")

# print where person_1 stores in ram
print(person_1)  # <__main__.Person object at 0x000000000>

# read atrrbiute from person_1
print(person_1.name)  # ali
print(person_1.age)  # "20"

# create person_2 object from person class
person_2 = Person()

# change name and age of person_2
person_2.name = "mahdi"
person_2.age = 30

# call sayHi for person_2
person_2.sayHi()

# print where person_2 stores in ram
print(person_2)  # <__main__.Person object at 0x000000001>

# read atrrbiute from person_1
print(person_2.name)  # "mahdi"
print(person_2.age)  # "30"
