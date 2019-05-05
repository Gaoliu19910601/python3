import datetime

"""Simple way of writing a class"""
#
# class Employee():
#     pass
#
# emp1 = Employee()
# emp1.name = "amardeep"
# emp1.age = 29
# emp1.job = "VIP"
# emp1.pay = 500000
#
# print(emp1.__dict__)

"""----------------------------------------"""

class Employee:

    usage_nr = 0
    # raise_amt = 1.04

    def __init__(self,fname,lname,age,job,pay):
        self.fname = fname
        self.lname = lname
        self.age = age
        self.job = job
        self.pay = pay
        self.email = fname + "." + lname + "@gmail.com"

        Employee.usage_nr +=1

    def fullname(self):
        return "{} {}".format(self.fname,self.lname)

    def raise_pay(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls,amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls,emp_str):
        fname_str, lname_str, age_str, job_str, pay_str = emp_str.split("-")
        return cls(fname_str, lname_str, age_str, job_str, pay_str)

    @staticmethod
    def isweekday(day):
        if day.weekday()==5 or day.weekday()==6:
            return False
        return True

    def __repr__(self):
        return "{}, {}, {}".format(self.fname,self.lname,self.pay)

    def __str__(self):
        return "{} - {}".format(self.fullname(),self.email)
        # pass
    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


emp1 = Employee("amardeep","amavasai",29,"VIP",500000)
emp2 = Employee("Test","User",25,"VIP2",200000)

Employee.set_raise_amt(1.05)

print(emp1.raise_amt)
print(emp2.raise_amt)
print(emp1.__str__())
print(emp1.__repr__())
print(emp1 + emp2)
print(len(emp1))

emp3_str = "John-Woo-35-director-2000000"
emp4_str = "Steve-Jobs-56-CEO-10000000"

emp3 = Employee.from_string(emp3_str)
emp4 = Employee.from_string(emp4_str)

print(emp3.email)
print(emp4.email)

mydate = datetime.date(2017,10,6)

print(mydate.weekday())

print(emp3.isweekday(mydate))

employees = [emp1,emp2,emp3,emp4]

print(employees)

# semployees = sorted(employees,key=lambda e: e.fullname)
#
# print(semployees)

# print(emp1.pay)
# emp1.raise_amt = 1.05
# emp1.raise_pay()
# print(emp1.pay)

"------------INHERITANCE--------------------------"

class Developer(Employee):
    def __init__(self,fname,lname,age,job,pay,program):
        super().__init__(fname,lname,age,job,pay)
        self.program = program

    @classmethod
    def from_string_mod(cls,emp_str):
        fname_str, lname_str, age_str, job_str, pay_str,program_str = emp_str.split("-")
        return cls(fname_str, lname_str, age_str, job_str, pay_str,program_str)


emp5_str = "Joey-sanders-34-programmer-400000-python"
emp5 = Developer.from_string_mod(emp5_str)


print(emp5.email)

class Manager(Employee):
    def __init__(self, fname, lname, age, job, pay, employee=None):
        super().__init__(fname, lname, age, job, pay)
        if employee == None:
            self.employee = []
        else:
            self.employee = employee

    def add_emp(self,emp_add):
        if emp_add not in self.employee:
            return self.employee.append(emp_add)

    def remove_emp(self,emp_rm):
        try:
            self.employee.remove(emp_rm)
        except ValueError:
            print("{} is not supervised by this manager".format(emp_rm.fullname()))

    def show_emp(self):
        for emp in self.employee:
            print("-->", emp.fullname())

mgr1 = Manager("ramana","maharishi",55,"master","NA",[emp1])

print(mgr1.email)

mgr1.show_emp()

mgr1.add_emp(emp2)
mgr1.add_emp(emp3)
mgr1.add_emp(emp4)


# mgr1.show_emp()

mgr1.remove_emp(emp2)

# mgr1.show_emp()

mgr1.remove_emp(emp5)


class hierarchy_check:

    @staticmethod
    def instancecheck(a,b):
        if isinstance(a,b)==True:
            print("Yes, {} is an instance of {}".format(a.fullname(),b.__name__))
        else:
            print("No, {} is not an instance of {}".format(a.fullname(),b.__name__))

    @staticmethod
    def subclasscheck(c,d):
        if issubclass(c,d)==True:
            print("Yes, {} is a subclass of {}".format(c.__name__,d.__name__))
        else:
            print("No, {} is not a subclass of {}".format(c.__name__,d.__name__))


# hierarchy_check.subclasscheck(Manager,Employee)

hierarchy_check.instancecheck(mgr1,Developer)

hierarchy_check.subclasscheck(Manager,Employee)

# print(issubclass(Manager,Employee))

# print(Manager.__class__.__name__)