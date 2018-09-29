from __future__ import print_function
from __future__ import unicode_literals
from functools import reduce


class A:
    def __init__(self):
        print('Hello i am A')
    def feature1(self):
        print('this is feature1')

class B:
    def __init__(self):
      #  super().__init__()
        print('Hello i B')
    def feature2(self):
        print('this is feature2')
class C(A,B):
    def __init__(self):
        super().__init__()
        super().feature1()

        print('Hello i am c')


c1 = C()



