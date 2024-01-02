# create car class
class Car:
    # defide attributes and default value
    name = "-"
    color = "-"

    # definde magic function init it call when we try to create object from this class (and pass parameters)
    def __init__(self, new_name, new_color):
        self.name = new_name
        self.color = new_color

    # defide methods
    def print_my_name(self):
        print(self.name)


# create car_1 object from car class
car_1 = Car("BMW", "Red")

# call print_my_name for car_1
car_1.print_my_name()  # print("BMW")

# create car_2 object  from car class
car_2 = Car("BUGATI", "Blue")

# call print_my_name for car_2
car_2.print_my_name()  # print("BUGATI")
