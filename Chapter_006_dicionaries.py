# # alien_0 = {"color":"Green","points":5}
# alien_0 = {}
# alien_0["color"] = "yellow"
# alien_0["points"] = 5
# alien_0["x_position"] = 0
# alien_0["y_position"] = 25
# alien_0["speed"] = "medium"
# print(alien_0)
# # print(alien_0["color"])
# # print(alien_0["points"])
# #
# # new_points = alien_0["points"]
# # print("You just earned "+ str(new_points)+" points!")
# #
# print("Original x-position: "+ str(alien_0["x_position"]))
#
# # move alien to right
# if alien_0["speed"] == "slow":
#     x_increment = 1
# elif alien_0["speed"] == "medium":
#     x_increment = 2
# if alien_0["speed"] == "fast":
#     x_increment = 3
#
# alien_0["x_position"] = alien_0["x_position"] + x_increment
# print("New x-position: " + str(alien_0["x_position"]))
#
# del alien_0["points"]
#
# print(alien_0)

fav_lang = {
    "jen": "python",
    'sarah':"c",
    'edward':'ruby',
    'phil':'python',
}
# print("Sarah's favorite language is "+fav_lang['sarah'].title()+'.')

# user_0={
#     'username':'efermi',
#     'first':'enrico',
#     'last':'fermi',
# }
#
# for key, value in user_0.items():
#     print('\nkey: '+key)
#     print("value: "+value)
#
# for k,v in user_0.items():
#     print("\nKey: "+k)
#     print("Value: "+v)

# for name,language in fav_lang.items():
#     print(name.title()+ "'s favorite language is "+language.title()+'. \n')
#
# for name in fav_lang.keys():
#     print(name.title())
# for name in fav_lang:
#     print(name.title())

# friends = ['sarah','phil']
# for name in fav_lang.keys():
#     # print(name.title())
#
#     if name in friends:
#         print("Hi "+name.title()+ ", I see your favorite language is "+fav_lang[name].title()+"!")
#
# if "erin" not in fav_lang:
#     print("Erin, Please take our poll.")
#
# for name in sorted(fav_lang.keys()):
#     print(name.title()+" Thank you for taking our poll!")
#
# # looping through dictionaries
# print("The following langauge have been mentiond:")
# for lang in fav_lang.values():
#     print(lang.title())

# for lang in set(fav_lang.values()):
#     print(lang.title())
#
# alien_0 = {"color": "Green", "Point":5}
# alien_1 = {"color": "yellow", "Point":10}
# alien_2 = {"color": "red", "Point":15}
#
# aliens = []
#
# for alien in aliens:
#     print(alien)
#
# # makes 30 green aliens
# for alien_number in range(30):
#     new_alien = {'color':'green', 'points':5, 'speed':'slow'}
#     aliens.append(new_alien)
#
# # show the first 5 aliens
# for alien in aliens[:2]:
#     print(alien)
# print(...)
#
# # show how many aliens have been created
# print("Total number of aliens:" + str(len(aliens)))
#
# for alien in aliens[:3]:
#     if alien['color'] == "green":
#         alien['color'] = "yellow"
#         alien['speed'] = 'medium'
#         alien['points'] = 10
#
# for aliens in aliens:
#     if alien['color'] == 'yellow':
#         print('yes')

#  -------------------------------
# stopped at page 110 in PDF

# A List in a Dictionary
# pizza = {'crust':"thick", "toppings":['mushrooms', 'extra cheese']}
# print("Your ordered a "+ pizza['crust']+"-crust pizza with the following toppings")
# for toppings in pizza["toppings"]:
#     print("\t"+toppings)

fav_lang = {"Sarah":['python','ruby','c'],"jen":["c"],'ed':['python','c''ruby'],'phil':['haskell','go']}

for name, lang in fav_lang.items():
    print("\n"+name.title()+"'s fav lang are")
    for langs in lang:
        print('\t'+langs.title())
