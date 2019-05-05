import os

# newfile = open("edu_tut.txt", 'w+')
newfile = open("edu_tut.txt", 'r')

#print(newfile.mode) #gives the mode of the file currently in
#print(newfile.name) # gives the name of the current file
#print(newfile.softspace)


# for i in range(0, 20):
#     newfile.write("\n Hello, this is a python tutorial")

#for i in range(0,20):
#    print(newfile.read())

'''The seek attribute takes the first x values given in the arg
and when u read it, it prints from x to last'''
newfile.seek(100)
print(newfile.read())

'''Tell attribute gives the number of words in the file'''
print(newfile.tell())


# os.rename("edu_tut.txt","new.txt")
#
# os.remove("new.txt")