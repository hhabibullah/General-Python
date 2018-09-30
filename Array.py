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
print(Employee.num_of_emps)
emp_1 = Employee('Hamid','Syed',2500)
emp_2 = Employee('Khalid','nusrat',2500)
#Employee.raise_amount = 1.06

emp_1.raise_amount =1.8
print(emp_1.fullname())
print('******************')
print(Employee.fullname(emp_1))
print('******************')
print(emp_2.fullname())
print('*******************')
print(emp_1.sal)
print(emp_1.apply_raise())
print('to check ')
print(Employee.raise_amount)
print('*******************')
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
print('********Namespace of instance *************')
print(emp_1.__dict__)
print(emp_2.__dict__)
print('*********************')
print(Employee.__dict__)
print(emp_2.raise_amount)
print(emp_1.raise_amount)
print(Employee.raise_amount)
print('**********************')
print(Employee.num_of_emps)
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