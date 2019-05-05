import os
from datetime import datetime

# os.removedirs('ostut/comeon/well/')

# os.makedirs('ostut/comeon/well/')

# print(os.getcwd())

# print(os.listdir())

os.chdir('/home/amardeep/PycharmProjects/new_trial/')

print(os.getcwd())

# os.rename('amar.txt','amaran.txt')

print(datetime.fromtimestamp(os.stat('amaran.txt').st_mtime))

# for dirpath, dirfile, filename in os.walk(os.getcwd()):
#     print("Current directory: " + str(dirpath))
#     print("Current file: " + str(dirfile))
#     print("Filename: " + str(filename))

print(os.environ.get("HOME")) # to get the home directory

filepath = os.path.join(os.getcwd(),'amaran.txt')

print(filepath)

print(os.path.basename(filepath))

print(os.path.dirname(filepath))

print(os.path.split(filepath))

print(os.path.splitext(filepath))

print(os.path.isdir(filepath))

print(os.path.isfile(filepath))

print(os.path.exists(filepath))



