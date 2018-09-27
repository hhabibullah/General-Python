from __future__ import print_function
from __future__ import unicode_literals
# one way of creating an array in Numpy package
from numpy import *

arr1 = array([1,2,3,4,5])
print('************Adding 5 to each element of array***************')
arr1 = arr1 + 5
print(arr1)
arr2 = array([1,2,3,4,5])
print('***********************Adding of two arrays ****************************')
arr3 =  arr1 + arr2
print(arr3)
print('***********************Finding SINE of each element**********************')
print(sin(arr3))
print('***********************Finding COS of each element************************')
print(cos(arr3))
print('***********************Finding LOG of each element*************************')
print(log(arr3))
print('************************Finding Square root of element************************')
print(sqrt(arr3))
print('************************Finding the sum of the array **************************')
print(sum(arr3))
print('***********************Finding the min of the arr3 ********************************')
print(min(arr3))
print('***********************Finding the max of the arr3*********************************')
print(max(arr3))
print('*********************** Concatenation of two arrays *******************************************')
print(concatenate([arr1,arr2]))

print('************************Copying one array to another ***************************************')

arr5 = arr1
print(id(arr1))
print(id(arr5))


print(arr1)
print(arr5)


print('***************************How to create two different array*****************************************************************')

arr5 = arr1.view()
arr1[0]= 1000
print(arr1)
print(arr5)
print('----------------------------------------------------------------')
arr5 = arr1.copy()
arr1[0]= 3000
print(arr1)
print(arr5)

print('*****************************************************************')