
# More elegant to use the format
def hello_func(greeting,  name = 'X'):
    # print('Hello Function!')
    return '{}, {} bro!'.format(greeting, name)


# A function with a positional argument and key argument
print(hello_func('Hi',  name='Amar'))

print(hello_func('Good morning').upper())

# An example illustrating the args and kwargs
def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Maths', 'Science'] # Positional args are tuples
info = {'name':'Amar', 'age':29} # key args are dictionaries

student_info(courses, info) # Takes everything as *args
student_info(*courses, **info) # separates the args and kwargs
student_info('Math', 'Science', name='Amar', age=29) # Returns a tuple of args and a dict of kwargs


'''--------------------LEAP YEAR CALCULATOR----------------------------'''

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isleap(year):

    return year % 4 == 0 and (year % 400 == 0 or year % 100 !=0 )

def days_month(year, month):

    if not 1 <= month <= 12:
       return 'Invalid input'

    if month == 2 and isleap(year):
        return 29
    else:
        return month_days[month]

print('')
print(days_month(2017, 12)) # mentions the number of days in that month

