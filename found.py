import os
import logging
import time
import os
import datetime
import shutil


# new_Directory = 'C:/'
my_dir = os.getcwd()
def create_folders_spord():
    paths = ('C:\Spord_Creation',
             "C:\Spord_Creation\Spord_File_JMCA",
             "C:\Spord_Creation\Spord_File_JYCA",
             "C:\Spord_Creation\Spord_File_JYUS",
             "C:\Spord_Creation\Spord_File_JMUS",
             "C:\Spord_Creation\Spord_File_LBCA",
             'C:\spord_temp')

    for path in paths:
        try:
            os.mkdir(path)
        except OSError:
            print("Directory {} was not created".format(path))
        else:
            print("Successfully created the directory {} ".format(path))


# https://docs.python.org/3.5/library/os.html#os.scandir
# Global variables
dest_file_present = False
source_file_present = False
dest_path_long = 'C:\spord_temp'
source_path = "C:\Spord_Creation\Spord_File_JMCA"
file_name = 'spordc.txt'

path = '/Home/python'

# checks to see if there are any files in the dest_path_long
num_files = len([f for f in os.listdir(dest_path_long) if os.path.isfile(os.path.join(dest_path_long, f))])
# if num_files == 0:
#     print("No files in the {} directory".format(dest_path_long))
# else:
#     print('There are files in {}'.format(dest_path_long))

def check_dest_for_file(dest_path):
    for entry in os.scandir(dest_path):
        print(entry)
        if entry.name == file_name:
            print("File {} is present in {}".format(file_name, dest_path))
            dest_file_present = True
        else:
            dest_file_present = False
            print("File {}, is NOT present in {}".format(file_name, dest_path))
            print('Getting a new {}'.format(file_name))


check_dest_for_file(dest_path_long)


def check_source_for_file():
    for entry in os.scandir(source_path):
        print(entry)
        # Search for and move file_name_if present
        if entry.name == file_name and dest_file_present=False:
            print("File {}, is present in {}".format(file_name, source_path))
            print("We are moving {} to {}".format(file_name, dest_path_long))
            shutil.move('{}\{}'.format(source_path, file_name),'{}\{}'.format(dest_path_long, file_name))
        else:
            # change name of a file in source_path to file name
            print('No file present')
            os.rename('{}{}'.format(source_path, entry), '{}{}'.format(source_path, file_name))