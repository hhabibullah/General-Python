from __future__ import print_function
from __future__ import unicode_literals
# one way of creating an array in Numpy package

print('****************Working on Functions********************************')

def greet():
    print('Hello')
    print('Good morning')


def sub_add(x,y):
    c = x + y
    d = x - y
    return c,d

greet()
result,result1 = sub_add(5,7)
print(result,result1)