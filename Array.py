from __future__ import print_function
from __future__ import unicode_literals


def fact(x):
    f =1
    for i in range(1,x+1):
        f *=i
    return f

x = 5
result= fact(x)
print(result)
