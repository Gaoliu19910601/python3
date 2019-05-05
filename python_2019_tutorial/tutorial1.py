
'''
This is another type of commenting
'''

# This is one type of commenting

print("Hello World")
print("Happy Friday bitches !!!, woohoo", "yay")

A1 = 10
B = "hey man wassup"

print(A1,B) # Can concatenate printing

x,y,z = 10,20,30 # better to write this way rather than having multiple lines

print(x,y,z)

a = 12-5j
b = 6+4j

print(b-a)

C = (10,23,45,22,11,'amar','wtf') # Tuple - cannot do item assignment

print(C)
print('amar' in C)      # Logical operators in print statement
print('amar' not in C)  # Checking logic
print('deep' in C)      # Checking logic


D = [[12,34,56],12,11,95,(33,45,67)] # List - can do item assignment

print(D[4][2])

D[0][2] = 65
#D[1] = 32

E = {'name':"Amar",'Age':43} # Dictionary

print(E['Age'])
print('Age' in E)
print('age' in E)
print('job' not in E)

F = {23,34,45,56,67,78,89,23,34,45} # set

print(F) # would not print repeated numbers in set


g = 12
h = 13

g += h # which is the same as g = g+h

print(g) # Now g is 25

print(g>h,g<h, g and h, g or h, not g, g and False) # 'and' returns the min value whereas the 'or' returns the max values


# VERBOSE
today = "Friday"
yoga_day = "Saturday"
MMA_day = "Friday"

print(today is yoga_day,today is MMA_day)


# Conditional statements
# IF LOOP
X = 6
Y = 15
if (X>Y):
    print('X is larger than Y')
elif(X<Y):
    if (2 <= X <= 5):
        print('X is in the range between 2 and 5')
    else:
        print("X is lesser than Y")
else:
    print("X and Y are equal")

#WHILE LOOP
j = 10
a = []
while (j>=1):
    a.append(j)
    j = j-1

print(a)
print("While loop ended")


# FOR LOOP
# The factorial of several numbers
number = 10
for n in range(1,number+1):
    c = 1
    for l in range(1,n+1):
        c *= l
    print("The factorial of",n,"is",c)


for m in range(1,10):
    if m==5:
        break # to stop the loop or "continue" to not print "5"
    print(m)

for o in [1,2,3,4,5,6]:
    pass # to close a loop or define an empty body







