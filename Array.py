from __future__ import print_function
from __future__ import unicode_literals
from functools import reduce


class student:

    school ='Applied'
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    def get_m(self):
        return self.m1
    def set_m(self,value):
        self. m1=value
        return self.m1
    @classmethod
    def getschool(cls):
        return cls.school
    @staticmethod
    def info():
        print('You are best dear')

s1 = student(1,2,3)
s2 = student(3,4,5)
print('****************Schoolname************************')
print(student.getschool())
print('***************Static method*********************')
print(student.info())

print('getting the value of m',s1.get_m())
print('setting the value of m',s1.set_m(60))
print(s1.avg())
print(s2.avg())