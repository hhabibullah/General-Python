from __future__ import print_function
from __future__ import unicode_literals
from functools import reduce


class A:

    def feature1(self):
        print('this is feature1')

class B:  
    def feature2(self):
        print('this is feature2')
class C:
    def feature3(self):
        print('this is feature3')
class D(A,B,C):#inheritance concept
    def feature4(self):
        print('this is feature4')
c1 = A()
c2 = B()
c3 = C()
C4 = D()

C4.feature1()



