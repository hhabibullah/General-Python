from __future__ import print_function
from __future__ import unicode_literals


def count(lst):
  even =0
  odd  =0
  for i in lst:
    if i%2==0:
      even += 1
    else:
      odd += 1
  return even,odd

lst = [1,2,3,4,5,6,7,8]
even,odd =count(lst)
print('Even is {} and odd is {}'.format(even,odd))


