from __future__ import print_function
from __future__ import unicode_literals

from array import *


vals = array('i',[1,2,3,4,5,6,78])

newArr = array(vals.typecode,(a for a in vals))
#vals.reverse()
#print(vals.buffer_info())
for i in range(len(newArr)):

    print(vals[i],end =' ')
print()
print('***********************************')

for e in newArr:
    print(e , end = ' ')