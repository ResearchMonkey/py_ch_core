# class Dog():
#     """A simple attempt to code a dog"""
#     def __init__(self, name, age):
#         """Initialize name and age attributes."""
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         """Simulate a dog sitting in response to a command."""
#         print(self.name.title() + " is now sitting")
#
#     def roll_over(self):
#         """Simulate rolling over in response to a command."""
#         print(self.name.title() + " is now rolling over")


# my_dog = Dog('willie', 6)


# print("My dogs name is {}. My dog is {} years old".format(my_dog.name.title(), my_dog.age))
# print(my_dog.roll_over())

# Try It Yourself page 166

# class Restaurant:
#     """makes a res"""
#     def __init__(self, restaurant_name, cuisine_type):
#         """adding name and food type"""
#         self.name = restaurant_name
#         self.type = cuisine_type
#
#     def describe_restaurant(self):
#         """state the name and the type of food served"""
#         print("{} serves the best {} in the tri state area.".format(self.name.title(), self.type))
#
#     def open_restaurant(self):
#         """open message"""
#         print("{} is open for the day".format(self.name.title()))

# my_res = Restaurant("Lucky house", 'Chinese')

# print(my_res.describe_restaurant())
# print(my_res.open_restaurant())

# stopped at Working with Classes and Instances on page 167


# class Car:
#     """A simple attempt to to rep a car"""
#
#     def __init__(self, make, model, year, odometer=0):
#         """int attributes to describe a car"""
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = odometer
#         self.tank_size = TankSize()
#
#     def get_descriptive_name_one(self):
#         """"returns a formatted script of the car"""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         # long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         long_name = '{} {} {} with {} miles'.format(
#             self.year, self.make, self.model, self.odometer_reading)
#         return long_name
#
#     def read_odometer(self):
#         """Print the millage"""
#         print("This car has {} miles on it.".format(self.odometer_reading))
#         # print("This car has " + str(self.odometer_reading) + " miles on it.")
#
#     def update_odometer(self, mileage):
#         """update the mileage"""
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print("You may not roll back the mileage of this car you fool")
#
#     def increment_odometer(self, miles):
#         """adds a given amount to the mileage"""
#         self.odometer_reading += miles

from car import Car, ElectricCar

# class Battery:
#     """A simple attempt to model a battery for an electric car."""
#
#     def __init__(self, battery_size=90):
#         """Initialize the battery's attributes."""
#         self.battery_size = battery_size
#
#     def describe_battery(self):
#         """Print a statement describing the battery size."""
#         print("This car has a " + str(self.battery_size) + "-kWh battery.")
#
#
# class TankSize:
#     """A simple attempt to model a tank size for an car."""
#
#     def __init__(self, tank_size=20):
#         """Initialize the battery's attributes."""
#         self.tank_size = tank_size
#
#     def describe_tank(self):
#         """Print a statement describing the battery size."""
#         print("This car has a {} gallon gas tank!".format(self.tank_size))
#
#
# class ElectricCar(Car):
#     """Represent aspects of a car, specific to electric vehicles."""
#
#     def __init__(self, make, model, year, odometer=''):
#         """Initialize attributes of the parent class."""
#         super().__init__(make, model, year, odometer)
#         self.battery = Battery()
#
#     def fill_gas_tank(self):
#         """Electric cars don't have gas tanks."""
#         print("This car doesn't need a gas tank.")


my_first = Car("Pontiac", 'Grand AM', 2001, 1111)

my_tesla = ElectricCar('tesla', 'Model s', 2016, 2222)

# print(my_first.get_descriptive_name())
# my_first.read_odometer()
# """Ways to interact with a method"""
# # Directly
# my_first.odometer_reading = 23
# print("Added 23 directly to method for my_first")
# my_first.read_odometer()
# # Modifying an Attribute’s Value Through a Method
#
# my_first.update_odometer(25)
# print("Set 25 via update to method for my_first")
# my_first.read_odometer()
#
# # Incrementing an Attribute’s Value Through a Method
# print("Adding  5 via increment_odometer i am updating via method for my_first")
# my_first.increment_odometer(5)
# my_first.read_odometer()

# print(my_first.get_descriptive_name())
# my_first.tank_size.describe_tank()
#
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()

"""The Python Standard Library Page 185"""
from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

"""Styling Classes page 186"""
