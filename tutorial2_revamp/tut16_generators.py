import time
import random
import memory_profiler

print('')
print("----------------------EXAMPLE 1------------------------------")
print('')

list1 = [1, 2, 3, 4, 5, 6]

list2 = [x*x for x in list1]

gen1 = (x*x for x in list1)

print(list2)

print(gen1)


print('')
print("----------------------EXAMPLE 2 (Performane check)------------------------------")
print('')


name = ['amar', 'deep', 'viki', 'kumar', 'kokki']
job = ['civil', 'mech', 'EIE','ECE','IBT']

print('Memory used before the process : {} MB'.format(memory_profiler.memory_usage()))

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {'id':i, 'name':random.choice(name), 'job':random.choice(job)}
        result.append(person)
    return result


def people_gen(num_people):
    for i in range(num_people):
        person = {'id': i, 'name': random.choice(name), 'job': random.choice(job)}
        yield person


t1 = time.clock()
chumma = people_list(1000000)
t2 = time.clock()


print('{} seconds taken for this process'.format(t2-t1))

print('Memory used after the process : {} MB'.format(memory_profiler.memory_usage()))

