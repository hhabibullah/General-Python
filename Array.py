from __future__ import print_function
from __future__ import unicode_literals
# one way of creating an array in Numpy package

from numpy import *

arr1 = array([[1,2,3,4,7,8],
         [4,5,6,7,90,80]
        ])
arr5 = array([[8,9,0,1,2,3],[11,12,13,14,15,16]])
print(arr1.ndim)
print(arr1.dtype)
print(arr1.shape)
print(arr1.size)
print('****************************************************************')
arr2 = arr1.flatten()
print(arr2)
print('*****************************************************************')
arr3 = arr2.reshape(3,4)
print(arr3)
m= matrix(arr1)
print(m)


print(m)
print(diagonal(arr1))
print(arr1.min())
print(arr1.max())

print('addition of two arrays ')

arr6 = arr1 + arr5
print(arr6)

print('Multiplication of two arrays')

arr7 = arr1 * arr5
print(arr7)
