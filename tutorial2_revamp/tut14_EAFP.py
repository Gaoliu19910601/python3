
print('')
print('---------------Example 1-----------------------')
print('')

class duck:

    def quack(self):
        print('quack quack')

    def fly(self):
        print("flap flap")


class person:

    def quack(self):
        print('I quack like a duck')

    def fly(self):
        print('I can fly like a duck')


# def quack_and_fly(thing):
#
#     if isinstance(thing, duck):
#         thing.quack()
#         thing.fly()
#     else:
#         print('You aint a duck')

#-----------------------------------------------------------------------
# The Non-pythonic way - lots of permissions LBYL(look beyond you leap):
#-----------------------------------------------------------------------
# def quack_and_fly(thing):
#
#     if hasattr(thing, 'quack'):
#         if callable(thing.quack()):
#             thing.quack()
#
#     if hasattr(thing, 'fly'):
#         if callable(thing.fly()):
#             thing.fly()

#-------------------------------------------
# The Pythonic way - forgiveness:
#-------------------------------------------
def quack_and_fly(thing):
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as e:
        print(e)

    print()

donald = duck()
quack_and_fly(donald)

Amar = person()
quack_and_fly(Amar)
# print(Amar.quack())
# print(Amar.fly())


print('')
print('---------------Example 2-----------------------')
print('')

# dict1 = {'name':'Amar', 'age':29, 'job':'vip'}
dict1 = {'name':'Amar', 'age':29}

#-----------------------------------------------------------------------
# The Non-pythonic way - lots of permissions LBYL(look beyond you leap):
#-----------------------------------------------------------------------
if 'name' in dict1 and 'age' in dict1 and 'job' in dict1:
    print('The name is {},  aged {} and a freaking {}'.format(dict1['name'], dict1['age'], dict1['job']))
else:
    print('Missing Key detected')

#-------------------------------------------
# The Pythonic way - forgiveness:
#-------------------------------------------
try:
    print('The name is {},  aged {} and a freaking {}'.format(dict1['name'],  dict1['age'],  dict1['job']))
except KeyError as e:
    print('Missing {} key'.format(e))


print('')
print('---------------Example 3-----------------------')
print('')

li = [1, 2, 3, 4, 5, 6]

if len(li) <= 6:
    li[5]
else:
    print('The index doesnt exist')


