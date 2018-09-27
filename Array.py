from __future__ import print_function
from __future__ import unicode_literals

from array import *


vals = array('u',['a','f','e'])
#vals.reverse()
#print(vals.buffer_info())
for i in range(len(vals)):

    print(vals[i],end =' ')
print()
print('***********************************')

for e in vals:
    print(e , end = ' ')