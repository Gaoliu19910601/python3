
class Duck:
    def quack(self):
        print("quack quack!")

    def fly(self):
        print("flap flap!")

class Person:
    def quack(self):
        print("quacks like a duck")

    def fly(self):
        print("flaps like a duck")

def quack_and_fly(thing):
    try:
        thing.quack()
        thing.fly()
        thing.bark()
    except AttributeError as e:
        print(e)

d = Duck()
p = Person()

quack_and_fly(d)
# quack_and_fly(p)

"------------------------------------------------------------"

amar = [2,3,4,5,6,7,8,9]

try:
    print(amar[15])
except IndexError:
    print("Error: list does not have this index")

"-------------------------------------------------------------"

dict1 = {"name":"amardeep","age":29,"height":180,"weight":72}

try:
    print("My name is {name} aged {age}. I am currently a {job}".format(**dict1))
except KeyError as e:
    print("Error: Does not have the {} key".format(e))

"--------------------------------------------------------------"

try:
    f = open('amar.txt')
except IOError as e:
    print(e)
else:
    print(f.read())
    f.close()

"---------------------------------------------------------------"


try:
    f = open('amar.txt')
    if f.name == 'amar.txt':
        raise Exception
    # var = bad_var

except FileNotFoundError:
    print('Sorry. file not found')

except Exception:
    print("all is well")

else:
    print(f.read())
    f.close()

finally:
    print("executing perfectly...")



"----------------------------------------------------------------"