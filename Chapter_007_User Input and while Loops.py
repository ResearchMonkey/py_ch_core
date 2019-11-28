# message = input("Tell me something and I will repeat it back to you: ")
# print(message)
# prompt = "if you tell me your name I can personalize the message you see"
# prompt += "\nWhat is your first name?"
# name = input(prompt)
# print('\nHello, '+ name+"!")
# age = input("How old are you?")
# age = int(age)
# print(age >= 12)
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1
# prompt = "\nTell me something and I will repeate it back you you:"
# prompt += "\nEnter to 'Quit' to end the program"
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)
# unconfirmed_users = ["alice","brian",'candace']
# confirmed_users = []
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#     print("Verifying user: "+ current_user.title())
#     confirmed_users.append(current_user)
#     print("\nThe following user has been confirmed: ")
#     for confirmed_user in confirmed_users:
#         print(confirmed_user.title())
# print(unconfirmed_users)
# print(confirmed_users)
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
# while "cat" in pets:
#     pets.remove("cat")
# print(pets)
# while not "cat" in pets:
#     pets.append("cat")
# print(pets)
#
# responses = {}
#
# polling_active = True
#
# while polling_active:
#     name = input("\nWhat is your name?")
#     response = input("What mountain do you want to climb?")
#
#     responses[name] = response
#
#     repeat = input("\nWhould you like to let someone else respond? (yes/no) ")
#     if repeat == 'no':
#         polling_active = False
#
# print('\n --- Poll Results ---')
# for name, response in responses.items():
#     print(name + " would you like to climb "+ response+".")
# Finished work
not_done = ["ham",'turkey','roast beef', 'tuna']
finished_work = []
unscheduled_work = []

working_hours = True

while working_hours:
    cook = input("\nCook Name?")
    response = input("What work did you complete?")

    if response in not_done:
        finished_work.append(response)
        not_done.remove(response)
        print("\nThanks, We still need to complete -")
        for work in not_done:
            print(work,",")
    else:
        print('\nThat is not scheduled work, we still need to complete - ')
        for work in not_done:
            print(work.title()+',')
        unscheduled_work.append(response)

    if response == "day":
        working_hours = False
        print("Have a Good Night")
        print("Done today")
        for work in finished_work:
            print(work+',')
        print("Orders remaining for tomorrow")
        for work in not_done:
            print(work+",")

# page 131