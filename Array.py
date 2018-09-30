class Employee:
    def __init__(self,first,last,sal):
        self.first = first
        self.last =last
        self.sal  = sal
        self.email = first +'.'+ last + '@hotmail.com'
    def fullname(self):
        return '{} {}'.format(self.first,self.last)

emp_1 = Employee('Hamid','Syed',2500)
emp_2 = Employee('Khalid','nusrat',2500)
print(emp_1.fullname())
print('******************')
print(Employee.fullname(emp_1))
print('******************')
print(emp_2.fullname())
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