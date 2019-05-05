from datetime import datetime
import os

#print(dir(os)) # prints all the functionalities in the os module

print(os.getcwd()) # Gets the current working directory

path = '/home/amardeep/shellscript'

os.chdir(path) # Changes the directory of the path

print('')
print(os.path.basename('/tmp/test.txt'))
print(os.path.dirname('/tmp/test.txt'))
print(os.path.split('/tmp/test.txt'))
print(os.path.splitext('/tmp/test.txt'))
print(os.path.exists('/tmp/test.txt'))
print(os.path.isdir('/tmp/test.txt'))
print(os.path.isfile('/tmp/test.txt'))
print(os.path.exists(path+'/demo.txt'))
print(os.path.isfile(path+'/demo.txt'))
print('')
print('')

filepath = os.path.join(os.environ.get('HOME'), 'test.txt') #Elegant way to define a path

print(filepath)

print(os.getcwd()) # To check the changed working directory

os.rename('demo.txt', 'something.txt') # renaming a file in that directory

os.removedirs('OS-DEMO2/sub-dir1') # Removes the folders in that directory

os.rmdir('OS-DIR1') # REmoves the folder in that directory

os.mkdir('OS-DIR1') # Creates the folder in that directory

os.makedirs('OS-DEMO2/sub-dir1') # Creates the folders in that directory

os.rename('something.txt', 'demo.txt') # renames a file in that directory

print(os.stat('demo.txt')) # The status report for the changed file

modified_time = os.stat('demo.txt').st_mtime # modified time

print(datetime.fromtimestamp(modified_time)) # readable format

for dirpath,  dirnames,  filenames in os.walk(path): # walks through all the folders in that path
    print('Current path: ',  dirpath)
    print('Directories: ',  dirnames)
    print('Files: ',  filenames)
    print()

print(os.listdir()) # Lists all the files and folders in that file
