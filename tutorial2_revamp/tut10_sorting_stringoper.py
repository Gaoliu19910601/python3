
print('')
print('---------------LIST SORTING-----------------------')
print('')

nums2 = [1,2,3,3,3,4,4,5,6,6,7,3,3,8,8,9,9,5,5,4,3,3,2]
nums2_sorted = sorted(nums2,reverse=True)

nums3 = [-4,-6,-8,-9,1,3,8,4,5,2,7,4,-7,-4,-9,-2]
nums3_sorted1 = sorted(nums3)
nums3_sorted2 = sorted(nums3,key=abs)
nums3_sorted3 = nums3.sort()

print(nums2_sorted) # reverse sorted list

print(nums3_sorted1) # sorting original values
print(nums3_sorted2) # sorting with absolute values
print(nums3_sorted3) # see what happens

print('')
print('---------------TUPLE SORTING-----------------------')
print('')

tuple1 = (1,4,2,7,4,7,5,8,5,3)

#tuple1.sort() # throws an error since tuple is immutable

tuple1_sorted = sorted(tuple1)

print(tuple1_sorted)

print('')
print('---------------DICTIONARY SORTING-----------------------')
print('')

name = ['ramesh','vivek','sarang','rohit','neymar']

job = ['carpenter','builder','fitter','developer','helper']


zipped = list(zip(name,job))

print(zipped)

mydict4 = {name:job for name,job in zipped if name!= 'vivek'}

print(sorted(mydict4)) # gives the sorted keys


# The advanced string operation
Dict2 = {'name':'Amar','age':27}

sentence = 'The name of this guy is {0} and his age is {1}'.format(Dict2['name'],Dict2['age'])

print(sentence)
print('')
for i in range(10):
    sentence2 = 'The value is {:03}'.format(i)
    print(sentence2)

print('')
sentence3 = 'The value of 1 MB is {:,.2f} bytes'.format(1000**2)

print(sentence3)