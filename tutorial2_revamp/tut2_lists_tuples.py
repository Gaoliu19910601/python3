print('')
print("-----------------------LISTS------------------------------")
print('')
# Lists are mutable operators. Also when lists a = b then a change in
# 'a' would also change the value of 'b'.

courses = ['History','Math','science', 'comp'] # creating a list

courses3 = ['History','Math','science', 'comp']# creating a list

courses3.insert(2,'Military') # Inserting a new str in index 2

courses.append('Economics') # appending a new str in courses list

courses2 = ['Art','Music'] # create a new list

# It is possible to append a list to a list (list inside a list)
courses.append(courses2)

print(courses)


# To avoid multiple lists inside a list through append
# we can use the extend function to add new values to
# existing list from another list
courses3.extend(courses2)

print(courses3)

# Removing a particular str from a list
courses.remove('comp')

# Pops the last value from a list----
popped = courses.pop()
print(popped)

print(courses)


#------------------------------------

# Sorting and reverse the order of the list
courses.reverse()
print(courses)

num = [1,5,3,6,8,2]
num2 = [2,4,6,5,4,7,8,9]

num.sort() # sorts the values in a list in increasing order
num2.sort(reverse=True) # sorts and reverses the list to get descending order
print(num)
print(num2)
# courses.extend()

# prints the list in the forward and reverse orders
print(num[0:-2:2])
print(num[::-1])

print(min(num),max(num),sum(num)) # The maximum, minimum and sum total of a list

print(courses.index('History')) # Gets the index of a value from a list

# Logical operators
print('Math' in courses)
print('Art' in courses)

# for loop to print values in a list
for items in courses:
    print(items)

#----------Prints the loop with index values-----

for index, items in enumerate(courses):
    print(index, items)

print('')

for index, items in enumerate(courses,start=1): # Changes the starting number
    print(index, items)

#--------------Join and split operations in a list----------------

course_join_str = ' -- '.join(courses)
print('')
print(course_join_str)
print('')
new_list = course_join_str.split(' -- ')
print(new_list)

print('')
print("-----------------------TUPLES------------------------------")
print('')

# Lists are mutable and Tuples are immutable which means that
# values cannot be mutated or changed but can be accessed
# in looping and other operations

tuple_1 = ('History','Math','Physics','Chemistry')
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# Throws an error when try to change a value
#tuple_1[0] = 'Art'

#print(tuple_1)
#print(tuple_2)
print('')
print("-----------------------SETS------------------------------")
print('')
# Sets does not maintain the order and keeps changing
# everytime we print its values. Also it doesnt print repetitions.
# But there are other functions that are more interesting than lists

set_1 = {'History','Math','Physics','Chemistry','Math'}

print(set_1)

set_2 = {'History','Art','Design','Physics','English'}

print(set_2)

print('')

print(set_1.intersection(set_2)) # Common between two sets
print(set_1.difference(set_2))   # difference between two sets w.r.t set1
print(set_1.union(set_2))        # The union between the 2 sets

'''--------------------------------------------------------------'''