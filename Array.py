from __future__ import print_function
from __future__ import unicode_literals
# one way of creating an array in Numpy package
import numpy
print('****************Working on Functions********************************')

def update(lst):
    print(id(lst))
    lst[0]=45
    print('x',id(lst))

a =10
print(id(a))
update(a)
print('a',a)
lst = [1,2,3,4,5,6,7,8]
print(id(lst))
update(lst)
print('lst',lst)

