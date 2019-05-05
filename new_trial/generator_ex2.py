import time
import random

t1 = time.clock()

name = ["amar","raghu","george","bugee","ibby","sara"]

degree = ["geo","mech","image","chef","pamphlet","coder"]

# def person(mynum):
#     result = []
#     for i in range(mynum):
#         ex = {'id':i,
#               'name':random.choice(name),
#               'degree':random.choice(degree)}
#         result.append(ex)
#     return result

def person_generator(mynum):
    for i in range(mynum):
        ex = {'id':i,
              'name':random.choice(name),
              'degree':random.choice(degree)}
    yield ex

# amar_list = person(1000000)
amar_gen = person_generator(1000000)

# print(amar_list)
# print(amar_gen)

t2 = time.clock()-t1

print(repr(t2) + " seconds")