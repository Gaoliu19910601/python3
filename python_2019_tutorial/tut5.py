
amar = ["mahogany",'red','blue'] # List

print(list(reversed(amar)))

print(amar+["green","blue","brown"])

print(amar*3)

amar.append("black")

print(amar)

print(amar[-2])

del(amar[-1])

print(amar)
# amar.remove("blue") # considers the direct value only
# amar.pop(2) # considers the index
# print(amar)

a = [i*i for i in [5,3,9,7]]

print(a)

print(sorted(a))

print(a[::-1])

b = (2,5,7,9,4)

print(b)

print(sorted(b))

print(b[::-1])

print(b+(4,6,5,7,5,2))

del(b)

# print(b)

name = 'amar'
print(name.replace('a','--a--',1))
print(name.upper())
print(name.find('m'))
print(name.index("r"))
print(name[::-1])
print(name*2)

age = 21

# Several ways of writing a print statement
print("Hi my name is "+ name +" and I am "+ str(age) + " years old")
print("Hi, My name is %s and I am %d years old" % (name,age))
print("Hi My name is {} and I am {} years old".format(name,age))

c = {1,2,3,4,5,'f'}

d = {4,5,6,7,8}

e = {3,4,5,'f'}

print(c&d)

print(c-d)

print(e.issubset(c))

print(c.issuperset(e))

print(d.issubset(c))

c.remove(4)

print(c)

e.clear()

print(e)

###-------- Dictionaries ---------###

person = {
    "name":"amardeep",
    "age":30,
    "job":"jobless",
    "city":"chennai"
}

print(person['age'])

print(person.items())

person.pop('age')

print(person.items())

if person.get('age'):
    print(person.get('age'))
else:
    print("Oops. Age not found for this dude")


###---------- Defining Functions--------------###

def add(a,b):
    sum = a+b
    return sum

print(add(3,5))
print(add(3,9))
print(add(8,5))

