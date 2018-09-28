from __future__ import print_function
from __future__ import unicode_literals
from functools import reduce

def is_even(n):
    return n%2==0
nums = [1,2,3,4,5,6,7,8,9]
evens = list(filter(is_even,nums))
print(evens)

print('***************Can be done with lambda expression*********************************')

evens = list(filter(lambda n : n%2 == 0,nums))

print(evens)

print('***************Using map function ************************************************')


def update(n):
    return n*2

result = list(map(update,evens))
print(result)
print('this can be done with lambda expression as well')
result = list(map(lambda n : n*2,evens))
print(result)

print('***********************Using reduce function **************************************')

def red(a,b):
    return a +b
res = reduce(red,result)
print(res)
print('This can be done by the help of lambda expression')

res = reduce(lambda a,b:a+b,result)
print(res)