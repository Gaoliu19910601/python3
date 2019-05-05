print('')
print('-----------------BOOLEAN AND CONDITION-----------------------')
print('')


language = 'Java'

# If the language is python then it is a true condition and would print
# the first condition and so forth for the next. However if everything
# is False there would be no match
if language is 'Python':
    print('Condition was true')
elif language is 'Java':
    print('Yes, Language is Java')
else:
    print('No match')


user = 'Admin'
logged_in = False

# Use of 'or' means that one of them should be true to print the first statement
# Use of 'and' means both should be true to print the first statement
if user is 'Admin' or logged_in:
    print("He's working")
else:
    print("He's in Reeperbahn")


# Use of 'not' means the opposite of true or false but to first statement, the condition
# should always be true
if not logged_in:
    print('Please log in')
else:
    print('Welcome')


# Be always careful when using the 'is' condition instead of '=='
a = [1,2,3]
b = [1,2,3]
b2 = a

print(id(a))
print(id(b))
print(id(b2))

print(a is b) # two different objects
print(a == b) # but have same value

print(a is b2) # two same objects
print(id(a) == id(b2)) # same as 'is' condition

# False values:
# False
# None
# numeric 0
# Empty string {}, [], ''
# Everything else would give true values

condition = None

if condition:
    print('Evaluated to true')
else:
    print('Evaluated to false')

