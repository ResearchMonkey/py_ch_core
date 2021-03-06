import os
""" page 189 Files and Exceptions"""
my_dir = os.getcwd()


# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())

# filename = 'pi_digits.txt'
# filename = '{}/python_crash_course_files/chapter_10/pi_digits.txt'.format(my_dir)
# filename = '{}/python_crash_course_files/chapter_10/pi_million_digits.txt'.format(my_dir)

# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())

# with open(filename) as file_object:
#     lines = file_object.readlines()
#
# # for line in lines:
# #     print(line.rstrip())
#
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
#
# birthday = input("Enter your birthday, in the form of mmddyy")
# if birthday in pi_string:
#     print("Your birthday is in the first million digits of pi")
# else:
#     print("your not in pi")
#
#
# print(pi_string)
# print(len(pi_string))

# filename = '{}/python_crash_course_files/chapter_10/programming.txt'.format(my_dir)
#
# with open(filename, 'w') as file_object:
#     file_object.write('I love Programming, well love is a strong word. \n')
#     file_object.write('I love creating new games.')
#
# with open(filename, 'a') as file_object:
#     file_object.write("\nTHis is a new line")

"""Exceptions page 200"""

# print(5/0)

# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")

# print("Give me two numbers, and I'll divide them.")
# print("Enter 'q' to quit.")
#
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("Second number: ")
#     try:
#         answer = int(first_number) / int(second_number)
#     except ZeroDivisionError:
#         print("You can't divide by zero!")
#     else:
#         print(answer)

# file_dir = f'{my_dir}/python_crash_course_files/chapter_10'
#
# filename = f'{file_dir}/alice.txt'
# filenames = [f'{file_dir}/alice.txt', f'{file_dir}/siddhartha.txt', f'{file_dir}/moby_dick.txt', f'{file_dir}/little_women.txt']
#
# def count_words(filename):
#     try:
#         with open(filename, encoding='utf-8') as f_obj:
#             contents = f_obj.read()
#     except FileNotFoundError:
#         # print(f'Sorry, the file {filename} does not exist.')
#         pass
#     else:
#         # Count the approximate number of words in the file.
#         words = contents.split()
#         num_words = len(words)
#         print(' The file {} has about {} words'.format(filename, str(num_words)))
#
# count_words(f'{my_dir}/python_crash_course_files/chapter_10/alice.txt')
#
# for files in filenames:
#     count_words(files)

""""Storing Data page 208"""

import json

numbers = [2, 3, 5, 7, 11, 13]

filename = 'numbers.json'

# with open(filename, 'w') as f_obj:
#     json.dump(numbers, f_obj)

# with open(filename) as f_obj:
#     numbers = json.load(f_obj)
#
# print(numbers)

"""Saving and Reading User-Generated Data page 210"""


filename = 'username.json'


# def greet_user():
#     """gets the new users name and checks"""
#     try:
#         username = input("What is your name?")
#         with open(filename) as f_obj:
#             username = json.load(f_obj)

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input('What is your name? ')
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f'Welcome back, {username}!')
