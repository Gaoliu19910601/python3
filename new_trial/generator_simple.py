import numpy as np
import time

t1 = time.clock()

amar = np.linspace(0,100,10)


"""Using List method"""
def simple_mod_list(mynum):
    result = []
    for i in mynum:
        result.append(i*i)
    return result


"""Using Generator mode"""
# def simple_mod_gen(mynum):
#     for i in mynum:
#         yield (i*i)


"""Or just simply"""
# amar_mod_simplegen = (x*x for x in amar)
amar_mod_simplelist = [x*x for x in amar]

amar_mod_list = simple_mod_list(amar)
# amar_mod_gen = simple_mod_gen(amar)

# print(amar_mod_list)
# print(amar_mod_gen)
# print(list(amar_mod_simplegen))

t2 = time.clock()-t1

print(repr(t2) + " seconds")
