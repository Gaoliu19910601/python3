import pickle
from pickling2_classfile import Player
from pickling2_classfile import Player2

items = ['apple','HP','dell']
items2 = ['Windows','linux','archlinux']
student1 = Player(2345,"Amar",100,items)
Teacher = Player2(1000,"Einstien",400,items2)

print(student1)
print(Teacher)

with open("save2.pkl",'wb') as outputFile:
    pickle.dump(student1,outputFile,pickle.HIGHEST_PROTOCOL)
    pickle.dump(Teacher,outputFile,pickle.HIGHEST_PROTOCOL)

outputFile.close()

print("------------")

student2 = None
teacher2 = None

with open("save2.pkl",'rb') as inputFile:
    student2 = pickle.load(inputFile)
    teacher2 = pickle.load(inputFile)

print(student2)
print(teacher2)
