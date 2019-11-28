cars = ["audi", "bmw", "subaru", "toyota"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())
if "ford" not in cars:
    cars.append("ford")
    print(cars)
    print("Added Ford")
else:
    print("Its there already!")

driver_min_age = 18
driver_max_age = 90

my_age = 17

if (my_age >= driver_min_age) and (my_age <= driver_max_age):
    print("At", my_age, "your able to drive in this state.")
else:
    if my_age <= driver_min_age:
        print("At", my_age, "your to young to drive in this state!")
    if my_age >= driver_max_age:
        print("At", my_age, "your to old to drive in this state!")

min_age = 4
jr_age = range(4, 19)

your_age = 13

if your_age in jr_age:
    print("Your fee is $5.00 today, Enjoy the show!")
elif your_age <= min_age:
    print("Your getting in free today! Enjoy the show!")
else:
    print("Your admission fee if $10.00, Enjoy the show!")

if your_age <= 4:
    price = 0
elif your_age < 18:
    price = 5
else:
    price = 10

print("Your admission fee is $" + str(price) + ".00.")
in_stock = ['mushrooms', 'extra cheese', "meat", 'green peppers']
out_stock = ["olives"]

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese', "olives"]

for requested_topping in requested_toppings:
    if requested_topping in out_stock:
        print("Sorry, we are out of " + requested_topping, "right now.")
    else:
        print("Adding", requested_topping + ".")
if requested_toppings == []:
    print("Are you sure you want a plain pizza?")
else:
    print("\nYour Pizza is being made.")

numbers = range(1, 10)
for number in numbers:
    if number == 1:
        num_end = "st"
    elif number == 2:
        num_end = "nd"
    elif number == 3:
        num_end = "rd"
    else:
        num_end = "th"
    print(str(number) + num_end)

alien_colors = ["green", "yellow", "red"]
player_points = 0
for alien in alien_colors:
    if alien == "red":
        player_points += 15
        print("player earned 15 points")
    elif alien == "yellow":
        player_points += 10
        print("player earned 10 points")
    elif alien == "green":
        player_points += 5
        print("player earned 5 points")

print("The player has", player_points, "points")

your_age = 77

if your_age <= 2:
    print("A baby")
elif your_age > 2 and your_age < 4:
    print("a Toddler")
elif your_age >= 4 and your_age <= 12:
    print("A Kid")
elif your_age >= 13 and your_age <= 19:
    print("Tennager")
elif your_age >= 20 and your_age <= 65:
    print("Adult")
elif your_age > 65:
    print("Elder")
