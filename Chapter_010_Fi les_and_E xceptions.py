import os
""" page 189 Files and Exceptions"""
my_dir = os.getcwd()


# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
#     print(contents.rstrip())

# filename = 'pi_digits.txt'
# filename = '{}/python_crash_course_files/chapter_10/pi_digits.txt'.format(my_dir)
filename = '{}/python_crash_course_files/chapter_10/pi_million_digits.txt'.format(my_dir)

# with open(filename) as file_object:
#     for line in file_object:
#         print(line.rstrip())

with open(filename) as file_object:
    lines = file_object.readlines()

# for line in lines:
#     print(line.rstrip())

pi_string = ''
for line in lines:
    pi_string += line.strip()

birthday = input("Enter your birthday, in the form of mmddyy")
if birthday in pi_string:
    print("Your birthday is in the first million digits of pi")
else:
    print("your not in pi")


print(pi_string)
print(len(pi_string))
