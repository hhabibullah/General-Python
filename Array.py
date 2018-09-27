from __future__ import print_function

from array import *


vals =array('i',[1,2,3,4,5])
vals.reverse()
print(vals.buffer_info())
for i in range(len(vals)):

    print(vals[i],end =' ')
print()
print('***********************************')

for e in vals:
    print(e , end = ' ')