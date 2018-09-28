from __future__ import print_function
from __future__ import unicode_literals
from functools import reduce


class computer:
    def __init__(self):
        self.name = 'Hamid'
        self.age  =   29
    def compare(self,c2):
        if self.name == c2.name:
            return True
        else:
            return False


c1 = computer()
c2 = computer()
c1.name = 'Rasheeee'
c2.name = 'Afghanistan'
print('comparing two objects ')
if c1.compare(c2):
    print('Equal')
else:
    print('Not equal')
print(c1.name)
print(c2.name)