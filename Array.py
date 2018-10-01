class Employee:
    raise_amount = 1.04
    num_of_emps = 0
    def __init__(self,first,last,sal):
        self.first=first
        self.last =last
        self.sal  =sal
        self.email=first +'.'+ last + '@hotmail.com'
        Employee.num_of_emps += 1
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    def apply_raise(self):
        self.sal = int(self.sal*Employee.raise_amount)
        return self.sal
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount
        return cls.raise_amount

    @classmethod
    def from_string(cls,emp_str):
        first, last, sal = emp_str.split('-')
        return cls(first, last, sal)
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        else:
            return True
import datetime
my_date = datetime.date(2018,9,30)
print(Employee.is_workday(my_date))

emp_1 = Employee('Hamid','Syed',2500)
emp_2 = Employee('Khalid','nusrat',2500)
print('*************using set method for classs **************')

print(emp_1.set_raise_amount(1.08))
Employee.set_raise_amount(1.05)
print(Employee.raise_amount)

print('*******************************************************')
emp_str_1 = 'kashmir-Khan-4000'
emp_str_2 = 'Khanabad-ras-2000'
emp_str_3 = 'Hayat-gulab-1000'
#first,last,sal   =emp_str_1.split('-')
#first1,last1,sal1=emp_str_2.split('-')
#first2,last2,sal2=emp_str_3.split('-')



#new_emp_1 =Employee.fro(first,last,sal)
#new_emp_2=Employee(first1,last1,sal1)
#new_emp_3=Employee(first2,last2,sal2)
new_emp_1 =Employee.from_string(emp_str_1)
new_emp_2 =Employee.from_string(emp_str_2)
new_emp_3 =Employee.from_string(emp_str_3)

print(new_emp_1.email)

"""
print(emp_1.email)
print(emp_2.email)
emp_1.name =' Hamid\n'
emp_1.email='hamid.116@hotmail.com\n'
emp_1.sal  = 3000

emp_2.name  =' Syed_Agha\n'
emp_2.email = 'farooq.11@hotmail.com\n'
emp_2.sal   = 2500

print(emp_1.name,emp_1.email,emp_1.sal)
print(emp_2.name,emp_2.email,emp_2.sal)
print('{} {}'.format(emp_1.first,emp_1.last))
"""