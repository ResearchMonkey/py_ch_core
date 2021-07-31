# class Dog():
#     """A simple attempt to model a dog via class"""
#
#     def __init__(self, name, age):
#         """Initialize name and age attributes"""
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """Simulate a dog sitting in response to a command."""
#         print(self.name.title() + ' is now sitting')
#
#     def roll_over(self):
#         """Simulate rolling over in response to a command."""
#         print(self.name.title() + ' rolled over!')
#
#
# my_dog = Dog('willie', 6)
#
# print("My dog's name is " + my_dog.name.title() + ".")
# print(my_dog.name.title() + ' is ' + str(my_dog.age) + " years old.")
#
#
# my_dog.sit()
# my_dog.roll_over()

# class Restaurant():
#     """9-1"""
#
#     def __init__(self, restaurant_name, cuisine_type):
#         """INt"""
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         """method"""
#         print('{} serves {}!'.format(self.restaurant_name, self.cuisine_type))
#
#
# my_res = Restaurant('Sushi', 'Raw Fish')
#
# my_res.describe_restaurant()
#
#
# class  Users():
#     """user of the restraunt """
#
#     def __init__(self, first_name, last_name):
#         """int"""
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def define_user(self):
#         print('The guests name is {} {}'.format(self.first_name, self.last_name))
#
#
# user001 = Users("jason", 'goony')
#
# user001.define_user()

class Car():
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery_size = 70
        # self.autopilot = autopilot

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

my_new_car.odometer_reading = 99898
my_new_car.read_odometer()

my_new_car.update_odometer(54)
my_new_car.read_odometer()

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

my_tesla.describe_battery()
