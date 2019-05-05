
# This is required when the dependency is on another folder which is required here

import sys
sys.path.append('/home/amardeep/PycharmProjects/tutorial2_revamp/module_folder')


import my_module
import os
import random
import datetime
import antigravity

today = datetime.date.today() # The current date and time

print(today)

courses_info = ['History','Maths','Arts','Humanities','Science']


index = my_module.find_index(courses_info,'Arts') # from custom-made module

print(random.choice(courses_info)) # gives a random choice from the list

print(os.getcwd()) # gets the current working directory
print(index)
# print(sys.path)
print(os.__file__) # gets the dir path for that module os.py