from __future__ import print_function
from __future__ import unicode_literals
# one way of creating an array in Numpy package
from numpy import *
arr = array([1,2,3.0,4],int)
print(arr.dtype)
print(arr)

print('***********************************************************')
print('another way of creating an array from Numpy Package')

arr = linspace(0,15,20)

print(arr)

print('***********************************************************')
print('another way of creating an array from Numpy Package')
arr = arange(1,15,2)
print(arr)
print('***********************************************************')
print('another way of creating an array from Numpy Package')

arr = logspace(1,40,5)
print('%.2f'%arr[1])

print('***********************************************************')
print('Another way of creating an array from Numpy Package')

arr = zeros(5,int)
print(arr)

print('*********************************************************')
print('Creating another type of array using Numpy package')

s = ones(5,int)
print(s)
