print('')
print('---------------LIST COMPREHENSIONS-----------------------')
print('')

num = [1,2,3,4,5,6,8,9,10]


mylist = []
mylist2 = []
mylist3 = []
mylist4 = []
mylist5 = []
mylist6 = []

# These three statements give the same answer but the second is the most elegant
for n in num:
    mylist.append(n)

mylist2 = [n for n in num]

mylist3 = map(lambda n: n, num)

print(mylist)
print(mylist2)
print(list(mylist3))

# Again the three statements with a condition
for n in num:
    if n%2 == 0:
        mylist4.append(n)

mylist5 = [n for n in num if n%2 == 0]

mylist6 = filter(lambda n: n%2==0, num)

print(mylist4)
print(mylist5)
print(list(mylist6))

print('')
print('---------------DICTIONARY COMPREHENSIONS-----------------------')
print('')


mydict1 = []
mydict2 = []
mydict3 = {}

for letter in 'abcd':
    for number in range(4):
        mydict1.append((letter,number))

mydict2 = [(letter,number) for letter in 'abcd' for number in range(4)]

print(mydict1)
print(mydict2)

name = ['ramesh','vivek','sarang','rohit','neymar']

job = ['carpenter','builder','fitter','developer','helper']


zipped = list(zip(name,job))

print(zipped)

# create a dictionary

for name,job in zipped:
    if name != 'vivek':
        mydict3[name] = job

print(mydict3)

mydict4 = {name:job for name,job in zipped if name!= 'vivek'}

print(mydict4)
print(sorted(mydict4)) # gives the sorted keys

print('')
print('------------------SET COMPREHENSIONS-----------------------')
print('')

myset = set()

nums2 = [1,2,3,3,3,4,4,5,6,6,7,3,3,8,8,9,9,5,5,4,3,3,2]

for n in nums2:
    myset.add(n)

myset2 = {n for n in nums2}

print(myset)
print(myset2)

print('')
print('--------------GENERATOR COMPREHENSIONS-----------------------')
print('')

mygen = (n for n in num)

print(list(mygen))