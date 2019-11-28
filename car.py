class Car:
    """A simple attempt to to rep a car"""

    def __init__(self, make, model, year, odometer=0):
        """int attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = odometer
        self.tank_size = TankSize()

    def get_descriptive_name_one(self):
        """"returns a formatted script of the car"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        # long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        long_name = '{} {} {} with {} miles'.format(
            self.year, self.make, self.model, self.odometer_reading)
        return long_name

    def read_odometer(self):
        """Print the millage"""
        print("This car has {} miles on it.".format(self.odometer_reading))
        # print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """update the mileage"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You may not roll back the mileage of this car you fool")

    def increment_odometer(self, miles):
        """adds a given amount to the mileage"""
        self.odometer_reading += miles


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=90):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")


class TankSize:
    """A simple attempt to model a tank size for an car."""

    def __init__(self, tank_size=20):
        """Initialize the battery's attributes."""
        self.tank_size = tank_size

    def describe_tank(self):
        """Print a statement describing the battery size."""
        print("This car has a {} gallon gas tank!".format(self.tank_size))


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year, odometer=''):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year, odometer)
        self.battery = Battery()

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank.")
