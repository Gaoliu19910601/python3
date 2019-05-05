import os
# print(os.getcwd())  #
# print(os.name) # name of your OS
# print(os.environ) # Environmental variables
# print(os.getlogin())
# print(os.getppid()) # Gets the parent process ID
# print(os.getcwd())
# os.mkdir("test")
# os.rmdir("test")
# print(os.getcwd())
# print(os.path.join('/home/amardeep/PycharmProjects/python_2019_tutorial','edu_tut.txt'))
# print(os.path.abspath('edu_tut.txt'))
# print(os.path.split('/home/amardeep/PycharmProjects/python_2019_tutorial/edu_tut.txt'))
# print(os.path.exists('/home/amardeep/PycharmProjects/python_2019_tutorial'))

# print(os.path.isdir(os.path.abspath('test')))

for i in os.walk('/home/amardeep/PycharmProjects/python_2019_tutorial'):
    print(i)
