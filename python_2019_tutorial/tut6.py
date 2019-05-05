# str = input("Enter your input")
#
# print("Received input is",str)
#
# name = input("Enter your name")
#
# age = input("What's your age")
#
# print("Hi, My name is",name,"and I am ",age,"years old")

'''
r   -  read mode
rb  -  read in binary format
r+  -  both read and write (does not overwrite the file)
w   -  write (overwrites the file)
wb  -  write the file in binary format
a   -  opens file for appending
ab  -  binary version of 'a'
a+  -  opens the file for both appending and reading
ab+ -  binary version of a+
w+  -  opens file for both writing and reading
wb+ -  binary version of w+

'''

grocery = ["Tomatoes","Onion","Honey"]

enumerate_grocery = enumerate(grocery,10)

print(list(enumerate_grocery))


ans = (lambda z: z * 4)

# which is equivalent to
# def ans(z):
#     return z*4
print(ans(7))

items = [1, 2, 3, 4]

squared = [z**2 for z in items]
squared = list(map(lambda z: z ** 2, items))
cubic = list(map(lambda z: z ** 3, items))

print(squared)
print(cubic)

# which is equivalent to
# def squared(items):
#     r = []
#     for item in items:
#         r.append(item**2)
#     return r

list1 = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
print(list1)

filter_out = list(filter(lambda x: x < 0, list1))
print(filter_out)

# which is equivalent to
# def filter_out(list_func):
#     r = []
#     for item in list_func:
#         if item<0:
#             r.append(item)
#         else:
#             continue
#     return r
# print(filter_out(list1))


from functools import reduce

product = reduce(lambda x, y: x * y, [2, 3, 4, 5])
print(product)


# which is equivalent to
# def product(list_func):
#     a = 1.0
#     for i in range(0,len(list_func)):
#         a *= list_func[i]
#     return a
#
# print(product([2,3,4,5]))

def info(name, age, salary=10000):
    my_info = "Hi my name is {} and I am {} years old. My salary is {}".format(name, age, salary)
    return print(my_info)


info("amar", 24, 50000)
info("Maria", 34)


def info2(name, *names):
    print("Hi guess who is using Python. {} you dumbass".format(name))
    for name in names:
        print("We also have {}".format(name))


info2('amar', 'deep', 'ramana', 'hanuman', 'muruga')


def info3(arg1, arg2, arg3, *args, **kwargs):
    print("The first argument:", arg1)
    print("The second argument:", arg2)
    print("The third argument:", arg3)
    print("The variable argument:", args)
    print("The keyword argument:", kwargs)


info3(1, 2, 3, 4, 5, 6, 7, name="This is me bitches")


class amaran():
    def __init__(self):
        self.pub = "Public attribute"
        self._pro = "Protected attribute"
        self.__priv = "Private attribute"

    @classmethod
    def Emp_strength(cls, employee_strength):
        cls.employee_strength = employee_strength

    # def __del__(self):
    #     self._pro = None
    #     print("Protected attribute deleted")

    def public_method(self):
        print("Public method")

    def __private_method(self):
        print("Private method")


amar = amaran()
amar2 = amaran()

print(amar.pub)  # Public attribute
print(amar._pro)  # protected attribute
# print(amar.__priv) # This will not work
print(amar._amaran__priv)  # this will work for private attribute

amar.public_method()

# amar.__del__()     # protected attribute deleted
# print(amar._pro)   # None will be the value for this

amar2.Emp_strength(400)  # from the class method

print(amar2.employee_strength)

# amar.__private_method() # this will not work
amar._amaran__private_method()  # This will work

class education_teacher():
    course = "Python"

    def Setteacher(self, name):
        self.name = name


my_course1 = education_teacher()
my_course2 = education_teacher()

print(my_course1.course)

my_course1.course = "Java"

print(my_course1.course)
print(my_course2.course)

my_course1.Setteacher("Mahima")
my_course2.Setteacher("Wicked")

print(my_course1.name)
print(my_course2.name)


class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def mdy(cls, month, day, year):
        cls.month = month
        cls.day = day
        cls.year = year
        return cls(cls.day, cls.month, cls.year)

    @classmethod
    def ymd(cls, year, month, day):
        cls.year = year
        cls.month = month
        cls.day = day
        return cls(cls.day, cls.month, cls.year)


my_birthday = Date(27, 11, 1988)
print(my_birthday.year)

my_birthday2 = Date.mdy(11, 27, 1988)
print(my_birthday2.year)

my_birthday3 = Date.ymd(1988, 11, 27)
print(my_birthday3.year)


##------ Single inheritance -------------###

class base:
    def fun(self):
        print("Idhu original thambi !")


class sub(base):
    def fun(self):
        print("Idhu dubaakoor !!!")


ob = sub()

ob.fun()


##------  Multiple inheritance -------------###

class first(object):
    def __init__(self):
        super(first, self).__init__()
        print('First')


class second():
    def __init__(self):
        super(second, self).__init__()
        print("Second")


class third(second, first):
    def __init__(self):
        super(third, self).__init__()
        print("Third")


third()


### ------------ Multilevel inheritance------------####

class Animal():
    def eat(self):
        print("Eating...")


class Dog(Animal):
    def bark(self):
        print("Barking...")


class BabyDog(Dog):
    def weep(self):
        print("Weeping...")


ob3 = BabyDog()
ob3.eat()
ob3.bark()
ob3.weep()


###------------- Child class overriding the parent class---------------###


class Rectangle(object):
    def __init__(self, length, breath):
        self.length = length
        self.breath = breath

    def get_area(self):
        print('{} is the area of the rectangle'.format(self.length * self.breath))


class Square(Rectangle):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        print("{} is the area of the square".format(self.side * self.side))


v = Rectangle(4, 8)

v.get_area()

w = Square(3)

w.get_area()


###------------Polymorphism - V.V.important feature------------###

class Animal():
    def talk(self):
        pass


class Cat(Animal):
    def talk(self):
        print("Meow !!!")


class Dog(Animal):
    def talk(self):
        print("High Five bitches !!!")


ob5 = Cat()
ob5.talk()
ob6 = Dog()
ob6.talk()


###-------------- Getters and Setters------------------###

class Edu_class():
    def __init__(self, name):
        self.name = name

    def SetcourseName(self, name2):
        self.name = name2.upper()

    def GetcourseName(self):
        return self.name


deep = Edu_class("Python")

print(deep.GetcourseName())

deep.SetcourseName("Machine_Learning")

print(deep.GetcourseName())
