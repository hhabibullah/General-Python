from __future__ import print_function
from __future__ import unicode_literals
from functools import reduce


a = 9
b = 5
try:
    print(a/b)
    k = int(input('Enter a number : '))
except ZeroDivisionError as e:
    print('Hey u can not divide a no by zero  :  the real error is  :',e)
except ValueError:
    print('Invalid number')
except Exception as e:
    print('something went wrong  :  ')
finally:
    print('It will be executed in both cases whether we have error or we dont have error')
print('Bye')


