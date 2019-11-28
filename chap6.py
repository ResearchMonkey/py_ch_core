alien_0 = {"color": "Green", "Point":5}
alien_1 = {"color": "yellow", "Point":10}
alien_2 = {"color": "red", "Point":15}

new_points = alien_0["Point"]
print("You just earned "+ str(new_points)+ " points!")

print(alien_0)
alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

print(alien_0["color"])

alien_0["color"]= "yellow"
print(alien_0["color"])
print("The alien is now "+alien_0["color"]+".")
alien_0["speed"] = "medium"
print(alien_0["speed"])
print("Original x-position: "+ str(alien_0["x_position"]))

if alien_0["speed"] == "slow":
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    # THis is is fast alien
    x_increment = 3

alien_0["x_position"] = alien_0["x_position"] + x_increment
print("New x_position: " + str(alien_0['x_position']))

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for key, value in favorite_languages.items():
    print("\nKey: " + key)
    print("Value: " + value)

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is "+ language.title()+".")
firends = ["phil","sarah"]
for name in favorite_languages.keys():
    print(name.title())
    if name in firends:
        print("Hi "+ name.title()+ ", I see your favorite language is "+ favorite_languages[name].title())

if "erin" not in favorite_languages.keys():
    print("Erin, please take out poll!")

for name in sorted(favorite_languages.keys()):
    print(name.title()+", Thank you for taking out poll.")

print("The following langauge have been listed")
for language in favorite_languages.values():
    print(language.title())

aliens = [alien_0,alien_1,alien_2]

for alien in aliens:
    print(alien)
