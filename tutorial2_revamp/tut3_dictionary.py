print('')
print('-----------------------DICTIONARY-------------------------------')
print('')

# dictionaries have keys and values

student = {'name':'amar', 'age':29,  'courses':{'math', 'English'}}

print(student)
print(student['courses'])
print(student['name'])
print(student.get('age'))
print('')
# For a key that is not there
print(student.get('phone'))
print(student.get('phone', 'Not Found'))

# can insert a particular key
student['phone'] = '9873646383'

print(student)
print('')
# can update the whole dictionary
student.update({'name':'guru',  'age':25, 'phone':'8876532832'})

print(student)
print('')
# Can delete a particular key and its value
del student['age']
print(student)

# Another way of deleting a key by popping it out
course = student.pop('courses')
print(course)
print(student)
print('')
# Print all the keys
print(student.keys())

# Print all the values
print(student.values())
print('')
# Print both the keys and values in a loop
for key,  value in student.items():
    print(key,  value)
