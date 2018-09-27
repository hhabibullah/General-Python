from __future__ import print_function
from __future__ import unicode_literals

from array import *

arr = array('i',[])
n = int(raw_input('Enter the length of the array'))

for i in range(n):
    x = int(raw_input('Enter the next value'))
    arr.append(x)

print(arr)
k =0
val = int(raw_input('Enter the value you are looking for'))
for e in arr:
    if e == val:
        print(k)
    k +=1
# search the value by using fuction
print('***************************************************')
print('Search the value by using the function')
print(arr.index(val))