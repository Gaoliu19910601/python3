import math
# print(dir(math))    # The directory of a module




import sys
# print(sys.argv)     # tracks the command line arguments - useful for shell scripting
# sys.exit()        # Tells the python interpreter to quit - neat trick to debug
# print(sys.prefix)   # No idea

rand_list = ['a',0,2]

for entry in rand_list:
    try:
        print("The entry is",entry)
        r = 1/int(entry)
        break
    except:
        print("Error:{} occured".format(sys.exc_info()))
        print("Next Entry")
        print()
print("The reciprocal of {} is {}".format(entry,r))




import os
# print(os.getcwd())  #
print(os.name) # name of your OS
# print(os.environ) # Environmental variables
# print(os.getlogin())
print(os.getppid()) # Gets the parent process ID
print(os.getcwd())
# os.mkdir("test")




import json
data = {'name':'amar','age':30,'Job':'designer'}
json_script = json.dumps(data)
print(data)
print(json_script)
print(type(json_script))
print(type(data))
data['name'] = 'bob'# possible since it is a dict
print(data)
try:
    json_script['name'] = 'deep'
except:
    print("Not possible since it is a string format")





import random
num = random.randrange(100) # anything between 0-100
print(num)
rum = random.randrange(0,100,5) # in steps of 5 between range 0-100
print(rum)
rint = random.randint(0,30) # any integer between range 0-30
print(rint)




import re
print(re.sub(r'[ab]','*','abcde abcdef abcedf'))
print(re.sub(r'abc','*','abcdef abcdef'))
print(re.search('ab','This is an absolute string'))
print(re.match('ab','This is an absolute string'))



