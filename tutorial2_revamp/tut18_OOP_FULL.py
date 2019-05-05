

class Employee(object):

    raise_amount = 1.04    # Class variable
    num_of_employees = 0   # Class variable

    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        # self.email = '{}.{}@company.com'.format(self.firstname, self.lastname)

        Employee.num_of_employees += 1 # This is a class variable

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.firstname, self.lastname)

    @property
    def fullname(self):
        return '{} {}'.format(self.firstname, self.lastname)

    @fullname.setter
    def fullname(self, name):
        first,  last = name.split(' ')
        print('Setting a new name')
        self.firstname = first
        self.lastname = last

    @fullname.deleter
    def fullname(self):
        print('Delete name !')
        self.firstname = None
        self.lastname = None

    @property
    def apply_raise(self):
        self.salary = self.salary*float(self.raise_amount)
        return self.salary

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, var):
        firstname, lastname, salary = var.split('-')
        return cls(firstname, lastname, salary)

    @staticmethod
    def is_present(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True

    def __add__(self,  other):
        if isinstance(other, Employee):
            return self.salary + other.salary


    def __repr__(self):
        return 'Employee({}, {}, {})'.format(self.firstname, self.lastname, self.salary)

    def __str__(self):
        return '{} - {}'.format(self.fullname, self.email)

    def __len__(self):
        return len(self.fullname)



class Developer(Employee):

    raise_amount = 1.10 # Class variable

    def __init__(self, firstname, lastname, salary, prog_language):
        super().__init__(firstname, lastname, salary)
        self.prog_language = prog_language



class Manager(Employee):

    raise_amount = 2.20

    def __init__(self, firstname, lastname, salary, employees=None):
        super().__init__(firstname, lastname, salary)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def list_of_emp(self):
        for emp in self.employees:
            print('--> ',  emp.fullname)

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)



emp1 = Employee('Amardeep',  'Amavasai',  50000)
emp2 = Employee('Dilip',  'Ramani',  60000)
emp3_string = 'Kokki-Kumar-60000'
emp3 = Employee.from_string(emp3_string)

dev1 = Developer('ganesh',  'chathurthi',  50000,  'Python')
dev2 = Developer('muruga',  'vinayaga',  80000,  'Java')


print('')
print('#========================= PART 4 Decorators ==========================')
print('')

# emp1.firstname = 'Amaranda'
emp1.fullname = 'Bradley Cooper'
print(emp1.fullname)
print(emp1.email)


del emp1.fullname

print('')
print('#========================= PART 3 DUNDER ==========================')
print('')

print(emp1)
print(emp1.__repr__())
print(emp1.__str__())

print(emp1 + emp2)

print(len(emp1))



print('')
print('#========================= PART 2 SUBCLASSES ==========================')
print('')


print(dev1.email)
print(dev2.email)
print(dev1.prog_language)
print(dev2.prog_language)

print()

print(dev1.salary)
# print(dev1.raise_amount)

dev1.apply_raise
print(dev1.salary)
Developer.set_raise_amount(1.20)
dev1.apply_raise
print(dev1.salary)

print()

print(emp1.salary)
emp1.apply_raise
print(emp1.salary)
print()

# print(help(Developer)) # gives info about the inherited things as a branch tree

mgr1 = Manager('sagala', 'ragala', 100000, [emp1, emp2])

print(mgr1.email)
print(mgr1.list_of_emp())

mgr1.add_emp(emp3)
mgr1.remove_emp(emp1)
mgr1.remove_emp(emp1)

print(mgr1.list_of_emp())

print(isinstance(mgr1, Employee))
print(isinstance(emp1, Manager))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))


print('')
print('#========================= PART 1 CLASSES ==========================')
print('')


emp3 = Employee.from_string(emp3_string)

import datetime
today = datetime.date(2018, 6, 1)

print(emp3.salary)
print(emp3.is_present(today))


print(emp1.fullname) # instance method
print(emp1.email)      # instance variable


print(emp1.salary)

print(Employee.raise_amount)
print(emp1.apply_raise)

Employee.set_raise_amount(1.07)

print(Employee.raise_amount)

print(emp1.apply_raise)

print(Employee.num_of_employees)


#========================================================