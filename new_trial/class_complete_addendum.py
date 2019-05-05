import logging

logger = logging.getLogger(__name__)

file_handler = logging.FileHandler("employee.log")

formatter = logging.Formatter('%(asctime)s:%(lineno)d:%(name)s:%(message)s')

file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

logger.setLevel(logging.INFO)


# logging.basicConfig(filename="employee.log",level=logging.INFO,\
#                     format='%(asctime)s:%(lineno)d:%(name)s:%(message)s')

class Employee:
     usage_nr = 0
     def __init__(self,first,last):
         self.first = first
         self.last = last
         # self.email = first + "." + last + "@gmail.com"
         Employee.usage_nr += 1
         logger.info("Created Employee: {} - {}".format(self.fullname,self.email))

     @property
     def email(self):
         return "{}.{}@gmail.com".format(self.first,self.last)

     @property
     def fullname(self):
         return "{} {}".format(self.first,self.last)

     @fullname.setter
     def fullname(self,name):
         first,last = name.split(" ")
         self.first = first
         self.last = last

     @fullname.deleter
     def fullname(self):
         print("Name Deleted")
         self.first = None
         self.last = None



emp1 = Employee("Amar","Ams")

# emp2 = Employee("Amitabh","Bachann")

print(emp1.first)
print(emp1.fullname)
print(emp1.email)

emp1.fullname = "amardeep amavasai"

print(emp1.first)
print(emp1.fullname)
print(emp1.email)

emp1.first = "Amith"

print(emp1.first)
print(emp1.fullname)
print(emp1.email)

del emp1.fullname

print(emp1.first)
print(emp1.last)
print(emp1.email)
print(emp1.fullname)

del emp1

try:
    print(emp1.first)
    print(emp1.last)
except NameError as e:
    print(e)

# print(Employee.usage_nr)



