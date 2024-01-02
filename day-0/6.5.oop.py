# create car class and object for -> bmw, x3, black , drive() buy() sell()
class Car:
    # define attr for class
    name = ""
    color = ""
    model = ""

    # define magic function for run when creating object
    def __init__(self, name, color, model):
        self.name = name
        self.color = color
        self.model = model
        self.build_date = "2024"

    # define methods for class
    # always first input is self refer to object called on
    def drive(self):
        pass

    # methods can gave input we call them parameter
    # define buy method with price parameter
    def buy(self, price):
        pass

    # define sell method with time parameter
    def sell(self, time):
        pass


# create two object from Car
car_1 = Car("BMW", "BLACK", "X3")
car_2 = Car("PAGANI", "RED", "I3")

# change atrrs for car_1 object
car_1.name = "BMW"
car_1.color = "BLACK"
car_1.model = "X3"

# call methods for car_1 object
car_1.buy(2000)
car_1.drive()
car_1.sell("2024")

# print where car_1 address in ram by default
print(car_1)  # <__main__.Car object at 0x00000000>

# print name from car_1 object
print(car_1.name)  # BMW
