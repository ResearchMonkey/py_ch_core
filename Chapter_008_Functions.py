def greet_user(user_name):
    """Display simple gazetting"""
    print("Hello, " + user_name.title() + '!')


# greet_user('Jess')
# greet_user('Gray')

def fav_book(book_name):
    """Enters the argument into the function and submits the title """
    print('My favorite book is {}'.format(book_name.title()))


# fav_book("alice in wonderland")

def describe_pet(animal_type, pet_name):
    """Enter the and type and pet name to print info"""
    print('\nI have a {}!'.format(animal_type))
    print("My {}'s name is {}".format(animal_type.title(), pet_name.title()))


# describe_pet("rat", 'splinter')
# describe_pet(pet_name='Leo', animal_type='Turtle')

def describe_pet_two(pet_name, animal_type='dog'):
    """Enter the ani type and pet name to print info"""
    print('\nI have a {}!'.format(animal_type))
    print("My {}'s name is {}".format(animal_type.title(), pet_name.title()))


# describe_pet_two('Higgins')

# try is yourself 8-3


def makeshirt(size="large", desc="people who love python", color='', logo=''):
    """Return a dictionary of information about a shrit size."""
    # print("You selected a {}, it fits {}".format(size, desc))
    shirt_dict = {"Size_value": size, 'Decs_size': desc}
    shirt_you_get = size + ' ' + desc
    if color:
        shirt_dict['Color'] = color
    if logo:
        shirt_dict['logo'] = logo

    print(shirt_you_get.title())
    print(shirt_dict)


# makeshirt('Small', 'Fits tiny child', logo='skull')
# makeshirt(desc='Tiny2', size='small2')
# makeshirt()

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name that is well formatted"""
    full_name = first_name + ' ' + middle_name + ' ' + last_name
    return full_name.title()


# musician = get_formatted_name('jimi', 'Hindrix')
# print(musician)
# musician = get_formatted_name('john', 'hooker')
# print(musician)
# musician = get_formatted_name('john', 'hooker', 'lee')
# print(musician)

def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person


musician = build_person('jimi', 'Hindrix', age = 22)


# print(musician)
# Using a Function with a while Loop page 145

# while True:
#     print("\nPlease tell me your name?")
#     f_name = input('First Name: ')
#     if f_name == "q":
#         break
#     l_name = input('Last Name: ')
#     if l_name == "q":
#         break
#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nHello, " + formatted_name + '!')

# Passing a List page 147

def greet_users(names):
    """Prints a list of users"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        msg1 = 'Hello, {}! Welcome to the event.'.format(name.title())
        print(msg1)
        print(msg)

user_names = ['Hanna', 'Greg', 'kent']
# greet_users(user_names)

def print_model(unprinted_model, printed_model):
    print('We still have to print {}'.format(unprinted_model))

    while unprinted_model:
        gonna_print = input("Which model did you print? : ")
        if gonna_print in unprinted_model:
            unprinted_model.remove(gonna_print)

        printed_model.append(gonna_print)
        print('We have printed {}'.format(printed_model))

        if len(unprinted_model) == 0:
            print("We are done, Good Job!")
            break
        else:
            print('We still have to print {}'.format(unprinted_model))


unprinted_model = ['blue', 'black']
printed_model = []

# print_model(unprinted_model[:], printed_model)
# Passing an Arbitrary Number of Arguments page 151

def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')
