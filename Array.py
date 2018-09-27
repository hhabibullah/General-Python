from __future__ import print_function
from __future__ import unicode_literals

a=10
print('the outer variable address is ',id(a))
def something():
  #  global a
    a=9
    print('the local variable is ',a)
    x = globals()['a']
    print('the local variable address is ',id(x))
    globals()['a'] = 15

something()
print('the outer variable looks like',a)



